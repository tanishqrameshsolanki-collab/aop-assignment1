#!/bin/bash
for p in $(pgrep -f 'agent-browser/browsers/chrom'); do kill -9 $p 2>/dev/null; done
pkill -9 -x agent-browser 2>/dev/null; true
