#!/usr/bin/env python3
"""Reduce captured JSON (window.__cap dump or any JSON) to keys/types; drops values, keeps URL extensions."""
import json,sys
def load(p):
    v=json.load(open(p))
    while isinstance(v,str): v=json.loads(v)
    return v
def shape(v,d=0):
    if isinstance(v,dict): return {k:shape(x,d+1) for k,x in v.items()} if d<8 else '{...}'
    if isinstance(v,list): return [shape(v[0],d+1),f'len={len(v)}'] if v else []
    if isinstance(v,str):
        if v.startswith('http'): return 'url(.'+v.split('?')[0].rsplit('.',1)[-1][:8]+')'
        return 'str'
    return type(v).__name__
v=load(sys.argv[1])
if isinstance(v,list) and v and isinstance(v[0],dict) and 'res' in v[0]:
    out={}
    for c in v:
        try: r=json.loads(c['res'])
        except Exception: r='non-json'
        out[c['u'].rstrip('/').split('/')[-1]]=shape(r)
    v=out
else: v=shape(v)
print(json.dumps(v,indent=1))
