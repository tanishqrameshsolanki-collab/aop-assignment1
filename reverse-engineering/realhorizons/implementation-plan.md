# Implementation plan (independent rebuild)

Recommended stack, chosen from the evidence: **TypeScript + React + Vite**. Use the **PlayCanvas engine (MIT) with its GSplat/SOG/LOD support** for splat scenes, the same open-source base Real Horizons builds on, which avoids re-implementing sorting and SH. Use **three.js + Spark + 3DTilesRenderer** only if Google-tiles maps are needed. Use zustand for editor state and Supabase (Postgres + Auth + Storage/R2) for persistence. Use `@playcanvas/splat-transform` for conversion. Do not copy Real Horizons code or assets. The design JSON is a reference for capabilities only.

| Stage | Deliverable | Key dependencies | Done when |
|---|---|---|---|
| A. Viewer | Load PLY/SPZ/SOG, orbit/fly/walk, entry camera, orbit limits, damping | playcanvas, splat-transform | Fixture scene renders; camera-state JSON round-trips |
| B. Spatial picking | Depth-pick at a pixel → world point; 3D cursor; measurements (P2P, polyline, height, area) with m/ft | custom pick pass (alpha-weighted depth) | Synthetic tests (see test-plan) pass; visual pick error < 2% on calibration scene |
| C. Scene setup | Ground/orientation/scale calibration (two-point known length), orbit bounds, opening view | B | Scale factor persisted; measured length matches the known length |
| D. Authoring | Hotspots (info/nav), portals between scenes with crossfade, saved views, undo/redo (command stack), draft autosave | zustand, Supabase | Reload persistence and undo/redo tests pass |
| E. Walk mode | Collision primitives (walls/polygons) editor + capsule collision; optional voxel grid from splat density | B, D | Cannot walk through walls in tests |
| F. Look | Color grading uniforms (10 sliders), HDRI/sky, reveal effect, quality presets | PlayCanvas shader chunks | Slider values persist and match reference screenshots |
| G. Floor plans | Image/vector floor plan, 2-point alignment to scene, minimap sync, floors | Konva or SVG | Clicking the minimap moves the camera to the aligned position |
| H. Delivery | Publish = immutable versioned snapshot; public viewer route; iframe embed; basic analytics (views, sessions, CTA clicks) | Supabase RLS | Draft edits do not change the published view |
| I. Scale | Streamed LOD (`lod-meta.json`), memory budget, mobile | splat-transform LOD output | Large-scene FPS target met on mid-range mobile |
| J. AI (optional) | Scene annotations / hotspot text via an authorized LLM API; reframe via an image model | external model APIs | Outputs editable and anchored to hotspot positions |

Not reproducible from the client alone: **splat training** (needs a 3DGS training pipeline, e.g. gsplat/Nerfstudio or Brush, plus GPU workers), **Reframe AI** (image-generation model), and **collision-voxel generation** (needs offline processing).
