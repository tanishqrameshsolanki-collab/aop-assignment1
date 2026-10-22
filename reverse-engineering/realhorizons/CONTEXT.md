# Real Horizons Spatial Studio: condensed context

A one-page summary of the investigation (2026-10-22). Detailed reports sit next to this file. Confidence labels: Verified (observed), Strongly supported (several static signals or the saved schema), Inferred, Unknown.

## What it is
studio.realhorizons.ai is a browser editor and viewer for 3D Gaussian-splat virtual tours: real-estate interiors and exteriors, parks, landmarks. Tours combine splat scenes, 360° panoramas, Google 3D maps, media galleries and floor plans.

## Stack
- **Frontend (Verified):** React SPA, react-router, Vite/Rolldown, shadcn/Radix UI, zustand-style stores (`splat3d.store`, `map.store`, `simpleEditor.store`).
- **Splat rendering (Strongly supported):** the PlayCanvas engine with the SuperSplat viewer core and editor. Format conversion uses playcanvas/splat-transform in web workers. Scenes are `.sog`, with `lod-meta.json` for streamed LOD. A WebGPU device chunk exists. Whether it is used at runtime is Unknown.
- **Maps (Strongly supported):** three.js + react-three-fiber + Spark (`SparkRenderer`, `PackedSplats`) + 3DTilesRenderer for Google Photorealistic Tiles; maplibre-gl for 2D maps; three-mesh-bvh for mesh raycasts.
- **Backend:** Supabase (Postgres, ~45 RPCs, ~25 tables, ~30 Edge Functions; Google/Apple/email auth). Files are served from `assets.realhorizons.ai` (Cloudflare R2). Billing runs on Dodo Payments. Monitoring and analytics: Sentry, Clarity, GA4, Cloudflare.
- **Splat training:** a cloud job queue (`splat_jobs`, credits) plus a local Mac app (`/desktop/login`). The training algorithm is Unknown.
- **AI:** Reframe AI, Spatial Sense annotations, Smart Hotspots, AI floor plans, AI translation and a voice/chat tour guide. All run server-side. One model id is visible in the client: `gemini-3.1-flash-lite-preview` (tour session analysis). Other providers are Unknown.

## How the editable spatial scene works
Two layers: a rarely-changing **scan asset** and a JSON **design document** for everything authored.

1. **Scan (Verified):** each scene references one splat file (`splatFile{url, format:'sogs', size}`). It provides appearance only: no objects, no collision.
2. **Design JSON (Verified):** each project row has `design` (draft, autosaved) and `published_design` (frozen snapshot plus `published_version`). Per scene it holds:
   - **Placement:** `splatTransform` and `orientation`, plus a 5-step setup (`setup.{orientation,scale,ground,orbitBounds,openingView}Confirmed`).
   - **Cameras:** `entryCamera{position,target,fov}`, opening view, orbit limits, `navigationMode` orbit/walkthrough. Viewer modes: orbit, fly, walk and third-person (keys 1–4).
   - **Hotspots:** `{type: info|navigation, position{x,y,z}, focus{position,target}, targetSceneId, customization}`, anchored in world space. Room links: `links[]{fromSceneId, hotspotId, targetSceneId, entryCamera, transitionStyle:'camera-crossfade'}`.
   - **Collision:** authored shapes per floor (`components[]{type:'blocker', preset: wall|polygon, points[{x,z}], position, rotation, size}`), plus `baseFloor.y`, a section plane and snap in metres. Optionally a voxel grid (`.voxel.json` + `.voxel.bin`). Walk mode collides with these, never with the splats.
   - **Look:** `colorAdjustments` (10 sliders and presets), HDRI/backdrop, reveal effect, audio. These are viewer settings, not baked into the asset.
   - **LOD:** `lodSettings{lodDistances[], lodRangeMin/Max}`.
3. **Floor plans (Verified UI):** vector walls, doors, openings, labels and measurements traced over the splat in three steps, with an optional image/PDF underlay or AI generation. Stored in the `floorplan_assets` table (per organisation) and tied to `floors[]`.
4. **Splat editing (Verified UI; persistence Inferred):** a SuperSplat-style editor with brush, lasso, box, polygon, flood, colour and sphere selection, move/rotate/scale/delete, and undo/redo. This is the only path that changes the scan. Saving most likely writes a new splat file.
5. **Picking (Inferred):** a depth-pick render pass (`pickDepthMode`, alpha-weighted depth, `readPixels`) gives a pixel depth that is unprojected along the camera ray to a world point. Used for hotspot and measurement placement.
6. **Measurements (Verified UI):** editor distance tool, floor-plan Measure / Set scale, and splat Scale calibration. Visitor measurements cover distance and rectangular area, use the scene scale, and are kept in the browser only.
7. **Publishing (Verified):** `publish_project_with_entitlements` copies the draft into the snapshot. The viewer reads it via `get_public_project_for_viewer` at `/tours/:id/view` (and `/embed`). The publish settings cover 10 viewer templates, 4 layouts, CTA, language/translations, visitor measurements, embed and Explore listing.

## Plans (Verified, 2026-10-22)
Free $0 (1 tour, 2 GB, watermark), Starter $12 (200 credits), Pro $39 (1,000 credits; Spatial Sense, 4K Reframe, logo), Studio $99 (3,000 credits).

## Unknown / not tested
Anything requiring rendering (the sandbox had no GPU), splat generation, AI outputs, analytics (paid), and exact picking precision. See known-unknowns.md.

## Recommended rebuild
TypeScript + React + Vite. PlayCanvas engine (MIT) for splats. A single zustand store serialised to one design JSON. A depth-pick point picker. Supabase for persistence. See implementation-plan.md and test-plan.md.

## Learned from their YouTube channel (51 videos; full notes in youtube-channel-notes.md)
- Visitor measurement modes: Distance, Floor area and Wall area, in metres or feet, on desktop and mobile. They follow the scene scale.
- Hotspots: Add Hotspot → anchor on the subject → "Use current view" saves the camera → marker Floating or Ground-anchored → content (text, links, images, audio, video/iframe embed) → layout as a screen panel or text in the scene. Smart Hotspots drafts text, icons and colours for selected anchors from context you type; you review the drafts.
- Aerial setup: "Is the scene upright?" levelling, then orbit centre and near/far view limits (double-click recentres the orbit), opening view, ambient sound.
- Camera animations: an Animations panel with keyframes, timing and FOV, a timeline with title text, and film export (up to 4K mentioned).
- Floor plans: an AI route (mark a generation area, style prompt, uses credits) or manual tracing. Shown as a live minimap in the viewer.
- Reframe AI: Template/custom prompt, strength slider, context, quality, then Create Reframe. Results can be saved or discarded as variations. Object 3D (beta) uses a brush.
- Flight Plans: Google 3D map, stacked orbits (height, radius, heading), preview playback, downloadable capture-guide PDF. A Capture Guide can overlay the route on an existing splat.
- Other: Matterport hybrid tours (Matterport opens from a hotspot), private share links with view stats and revoke, Spatial Sense (AI-detected objects), a Mac beta app (import footage, extract frames, train locally), LCC + LOD streaming, and builder tools (construction progress, unit selection with availability filters).
