# API and data analysis

## Mirror bundles
`scripts/mirror-bundles https://host/assets/index-XXXX.js ./bundles` follows static and dynamic imports breadth-first. 404s for bare names (`index.js`, wasm wrappers) are normal false positives.

## Extract surfaces (ripgrep over the bundle directory)
```bash
rg -oN --no-filename 'path:\s*`[^`]{1,60}`' . | sort -u                 # react-router routes
rg -oN --no-filename '\.rpc\(`[a-z_0-9]+`' . | sort -u                  # Supabase RPC
rg -oN --no-filename '\.from\(`[a-z_0-9]+`\)' . | sort -u               # Supabase tables
rg -oN --no-filename 'functions\.invoke\(`[a-z0-9_-]+`|/functions/v1/[a-z0-9_-]+' . | sort -u
rg -oN --no-filename 'https://[a-z0-9.-]+\.[a-z]{2,}/' . | sort | uniq -c | sort -rn | head -40
rg -oN --no-filename 'model:`[^`]+`' .                                  # AI model ids, when embedded
```
Adapt for Firebase (`collection(`), GraphQL (`gql\``), and REST (`/api/`).

## Response shapes
After capture, reduce with `python3 scripts/shape.py capture.json > shape.json`. It outputs keys, types, and asset extensions only. A table name is not proof of access. Never query endpoints directly beyond what the app itself sends during normal use.
