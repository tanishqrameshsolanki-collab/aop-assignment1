# Real Horizons Spatial Studio: investigation

Target: https://studio.realhorizons.ai/ (public surfaces only). Date: 2026-10-22. Produced with the `reverse-engineer-anything` skill (`../.agents/skills/reverse-engineer-anything`).

**Scope actually covered**
- Public `/explore` gallery: DOM, network, screenshot.
- Public published tour `/tours/ed72e7f2-…/view` ("The Villa Tour"): network and the full published design JSON returned by the viewer's own RPC call, reduced to a schema.
- Static analysis of all 314 public JS chunks (29 MB), mirrored from `/assets/`.
- Public product pages: realhorizons.ai/features and /spatial-studio.

**Authenticated pass:** a Free-plan account (dashboard, editor UI, publish settings, plans); see `authenticated-findings.md`.

**Not covered:** live 3D rendering (software WebGL hung the sandbox browser), and AI feature execution. See `known-unknowns.md`.

| File | Contents |
|---|---|
| application-inventory.md | Routes, shell, shortcuts |
| feature-matrix.md | Features with confidence |
| architecture-report.md | Stack and Mermaid diagram |
| rendering-analysis.md | Splat engine, formats, LOD, collision |
| measurement-analysis.md | Picking, units, calibration |
| api-inventory.md | RPCs, tables, edge functions (redacted) |
| data-model.md | Entities and published design schema |
| implementation-plan.md | Staged rebuild |
| test-plan.md | Parity tests |
| CONTEXT.md | One-page summary (loaded by CLAUDE.md) |
| known-unknowns.md | Open questions |
| authenticated-findings.md | Logged-in dashboard, editor, publish, plans |
| evidence/ | Redacted request logs, schema paths, DOM dump |
| reference-assets/ | Screenshots |
| ../.cache/realhorizons-bundles/ | Mirrored public JS (local reference only, kept outside deliverables; contains the public anon key; do not redistribute) |
