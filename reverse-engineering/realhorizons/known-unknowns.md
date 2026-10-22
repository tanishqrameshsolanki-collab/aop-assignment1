# Known unknowns

| Area | Why unknown | How to resolve |
|---|---|---|
| Editor behaviour with rendering (hotspot placement, gizmos, splat edits, undo/redo effects) | Editor UI inventoried (authenticated-findings.md), but WebGL was disabled | GPU machine |
| Analytics dashboard, Flight Plans, splat generation, Spatial Sense, Reframe output, AI floorplan | Gated behind paid plan / trial / credits on the test account | Paid or trial account (spends credits) |
| Live rendering behaviour (FPS, LOD streaming, artifacts, WebGL vs WebGPU selection, transitions) | Software WebGL hung the 2-CPU sandbox browser | Run on a GPU machine, or a sandbox with GPU passthrough |
| Measurement rounding/precision and pick source | Types and persistence now known (distance + rectangle area, browser-only) | Interactive test on a GPU machine |
| Exact distance formula / pick source (splat depth vs collision) | Call site not traced in minified code | Test H1–H3 in measurement-analysis.md |
| Floor-plan alignment math | Representation now known: traced vector (walls/doors/openings/labels) over the splat, optional image/PDF underlay, AI generation | Rendering test |
| Splat training pipeline and model (cloud and Mac) | Server-side | Not discoverable from the client; only public docs |
| Reframe AI and Spatial Sense model providers and prompts | Server-side; only one Gemini id (session analysis) is in the client | Not discoverable without authorized backend access |
| Voxel generation method | Offline/server | — |
| `/splat-compressor`, `/splat-compare` | Not opened | Quick follow-up pass |
