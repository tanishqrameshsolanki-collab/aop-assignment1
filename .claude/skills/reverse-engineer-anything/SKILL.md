---
name: reverse-engineer-anything
description: Investigate a web application from its URL (public pages, an authorized session, or an optional source repo), inventory its features, infer its architecture from evidence, and plan or build an independent reconstruction. Use when asked to reverse engineer, clone, or explain how a website or web app works.
---

# Reverse Engineer Anything (web-application workflow)

Inputs: `TARGET_URL` (required), `DEPTH` (`recon` | `standard` | `deep`, default `standard`), optional `SOURCE_REPO`, optional authorized login session, optional `BUILD=yes` (implementation authorized).

For native binaries, APKs, ASAR/Electron trees, firmware, or captures, follow `references/upstream-rea/SKILL.md` (vendored from github.com/morluto/rea, MIT) and use the `rea-agents` CLI (`npx -y rea-agents@latest ...`). This file covers browser-delivered apps.

## Hard rules
- Never store, print, or commit tokens, cookies, auth headers, or session fragments. If the user pastes a URL containing `#access_token=`/`refresh_token=`, strip it, use the clean URL, and tell them to revoke the session.
- Do not bypass auth, paywalls, or rate limits; no exploitation, fuzzing, or destructive/mutating requests against production. Observe only what the browser legitimately fetches.
- Public JS bundles may be mirrored for static reading. Use source maps only if they are publicly served or explicitly authorized.
- Every claim gets a confidence label: **Verified**, **Strongly supported**, **Inferred**, or **Unknown**. Never mark a feature as working because a button exists.

## Workflow (checkpoint after each step into `<out>/checkpoint.md`)
1. **Validate**: run `scripts/environment-check`. Confirm the target is reachable and decide which areas need login. Ask the user only to authenticate. Never ask for tokens.
2. **Recon**: open the URL with `agent-browser` and take a `snapshot` (accessibility tree) and a screenshot. Collect script/link tags and window globals, and list network hosts (see `references/browser-investigation.md`).
3. **Mirror bundles**: run `scripts/mirror-bundles <entry.js URL> <dir>`. Fingerprint libraries and versions. Extract routes, API/RPC names, tables, serverless functions, and storage paths (`references/api-and-data-analysis.md`).
4. **Exercise workflows**: walk every reachable route and control. Record each feature into `templates/feature-matrix.md`. Test reload persistence where safe.
5. **Capture data shapes**: load `scripts/capture.js` as an `--init-script`, then reduce the responses with `scripts/shape.py` (keys and types only; IDs and secrets dropped).
6. **Specialist passes**: for 3D/WebGL/splats/maps, use `references/3d-spatial-systems.md`.
7. **Hypotheses**: where internals are hidden, write competing explanations and the evidence that would separate them (`references/architecture-inference.md`).
8. **Report**: fill the templates. Include a Mermaid diagram with inferred edges dashed. Write `known-unknowns.md`.
9. **Plan**: write a staged rebuild plan, one subsystem at a time, naming the real dependencies (models, renderers, services).
10. **Build/validate** (only if `BUILD=yes`): implement in a separate directory and test using `references/implementation-validation.md`.
11. Run `scripts/evidence-validation <out>` before reporting. It must pass.

## Headless-browser pitfalls (learned the hard way)
- Software WebGL (SwiftShader) on small sandboxes can saturate the GPU process and make every CDP call hang. Use a small viewport. To study the UI shell and network without rendering, add `--init-script scripts/nowebgl.js`.
- Cards that `window.open` a new tab escape init scripts. Check `agent-browser tab list`, then reopen the URL in the instrumented tab.
- Never `pkill -f chrome` from a shell whose own command line contains that word. Use `scripts/kill-browser.sh`.
- Wrap every browser command in `timeout`.
- Use `rg -o` (not `grep -E '.{0,N}...'`) on multi-MB minified bundles.

## Outputs
`<out>/` contains README, INSTALLATION, application-inventory, feature-matrix, architecture-report, rendering-analysis (if 3D), measurement-analysis (if relevant), api-inventory, data-model, implementation-plan, test-plan, known-unknowns, reference-assets/, and evidence/ (redacted). Create only documents you can populate. Mark gaps explicitly.
