# Feature matrix

Confidence key: **Verified** (observed at runtime), **Strongly supported** (multiple static signals and/or the saved schema), **Inferred**, **Unknown**. "Schema" = fields present in the published design JSON of a public tour.

| Feature | Location | Preconditions | User action | Observed / evidenced result | State & persistence | Evidence | Confidence |
|---|---|---|---|---|---|---|---|
| Public gallery | `/explore` | none | browse, click card | Cards → new tab `/tours/:id/view` | view counts server-side | screenshot 01, RPC log | Verified |
| Published viewer load | `/tours/:id/view` | published | open | Fetches branding, project design, starts analytics session | `published_version` (10 here) pinned | tour-requests.txt | Verified |
| Analytics session | viewer | published | open | `tour-analytics` edge fn returns session id/token, attention protocol `viewport-stencil-3x3-v1` | server | tour-capture-shape.json | Verified |
| Branding / watermark / white-label | viewer | org plan | — | `watermark_required`, `custom_branding_enabled`, `white_label_enabled` flags | server | RPC shape | Verified (flags); UI effect Unknown |
| Multi-scene splat tour | viewer | ≥1 scene | navigate | `spatialTour.scenes[]` + `links[]` (`transitionStyle: camera-crossfade`) | published JSON | schema | Strongly supported |
| Camera modes orbit/fly/walk/third-person | viewer | — | keys 1–4 | Mode switch | `navigationMode`, `movement.mode`, `allowThirdPerson` | code + schema | Strongly supported |
| Orbit limits & damping | editor→viewer | — | — | `viewerSettings.{min,max}Distance, {min,max}PolarAngle, enableDamping, dampingFactor, autoRotate(Speed)` | schema | schema | Strongly supported |
| Entry / opening view | editor | — | set view | `entryCamera{position,target,fov}`, `openingViewCameraState`, `openingViewThumbnailUrl`, `setup.openingViewConfirmed` | schema | schema | Strongly supported |
| Scene setup wizard | editor | upload | confirm steps | `setup.{groundConfirmed, orientationConfirmed, scaleConfirmed, orbitBoundsConfirmed, openingViewConfirmed}` | schema | schema | Strongly supported (UI Unknown) |
| Hotspots (info / navigation) | editor | scene | place | `hotspots[]{type: info\|navigation, position{x,y,z}, focus{position,target}, targetSceneId, targetSceneType:'3d', title, description, icon, thumbnailUrl, customization{markerStyle: billboard\|mapMarker, shape, color, size, showTextBox…}}` | world-space anchor | schema | Strongly supported |
| Portals / scene links | editor | ≥2 scenes | link | `links[]{fromSceneId, hotspotId, targetSceneId, targetHotspotId, entryCamera, transitionStyle}` | schema | schema | Strongly supported |
| Collision authoring | editor | walk mode | draw walls/polygons | `collision{source:'primitives', components[]{type:'blocker', preset: wall\|polygon, points[{x,z}], position, rotation, size, floorId, locked, visible, wallPath*}, baseFloor.y, sectionPlane{axis,offset,flip}, snap{enabled,incrementM}}` | schema | schema + code | Strongly supported |
| Collision voxels | viewer | generated | `v` overlay | `.voxel.json` + `.voxel.bin`, `voxelResolution`, grid bounds | asset | code | Strongly supported |
| Streaming LOD | viewer | LOD asset | — | `lod-meta.json`; `lodSettings{isLodFormat, lodDistances[], lodRangeMin/Max, lodBaseDistance, lodMultiplier, colorizeLod}` | schema | code + schema | Strongly supported |
| Color Studio | editor | — | sliders | `colorAdjustments{exposure, brightness, contrast, saturation, temperature, tint, highlights, shadows, whitePoint, blackPoint}` (also per-map-splat) | renderer params in JSON, not baked | schema | Strongly supported |
| Environment / HDRI | editor | — | presets | `hdriSource, hdriUrl, hdriSettings{mode, scale, groundPlaneHeight, bottomColor…}`, `skybox_templates` table | schema | schema | Strongly supported |
| Reveal animation | viewer | — | — | `revealSettings{enabled, effect:'magic'}` | schema | schema | Strongly supported |
| Interior/exterior mode | editor | — | — | `sceneSettings.splatType: interior\|exterior`, `cameraHeight`, `cameraCollisionDepth` | schema | schema | Strongly supported |
| Adaptive label limit | viewer | — | — | `sceneSettings.enableAdaptiveLabelLimit / adaptiveLabelLimitValue` | schema | schema | Strongly supported |
| Measurements | viewer + editor | visitor toggle in publish settings | 2 clicks / rectangle | Distance and rectangular area, uses scene scale; editor Measure Distance; floorplan Measure / Set scale | visitor measurements stay in the browser | UI text + code | Verified (types, persistence); pick method Inferred |
| Splat editor | editor › 3D Splat › Edit splat | — | brush/lasso/box/polygon/flood/color/sphere/volume select, move/rotate/scale, delete | SuperSplat-style tools, SH detail 0–3 | Save changes | UI | Verified (UI) |
| Privacy blur | 3D Splat inspector | — | toggle | "Blur surroundings" softens neighbouring houses | design JSON | UI | Verified (UI) |
| Viewer templates & layouts | Publish › Style | — | pick | 10 templates, 4 layouts, scene strip, accent, logo (Pro) | draft | UI | Verified (UI) |
| Floor plans | editor › Spatial Setup | — | Create (trace over splat, 3 steps) / Image-PDF reference / Generate AI | walls, doors, openings, objects, labels, measure, set scale, undo/redo | `floorplan_assets` (per org) | UI + code | Verified (UI) |
| Property / units overlay | `/properties`, `/units` | real-estate entitlement | — | unit rows with `lengthScale/lengthUnit`, plot developments | DB | code | Inferred |
| Maps (Google 3D tiles) | viewer | maps module | — | Google Photorealistic 3D Tiles via `get-google-tiles-root`, optional splat placed on map (`mapSplatFile`, `splatTransform`) rendered with Spark | schema | code | Strongly supported |
| 360 panorama tours | viewer | panorama module | — | `panorama.settings{transitionEffect, hotspotScale, showCompass…}` | schema | schema | Strongly supported |
| Media gallery | viewer | module | — | `mediaGallery{categoryTree, displaySettings}` | schema | schema | Strongly supported |
| Reframe AI | editor | AI credits | generate | Stored as `scenes[].sprites[].reframe{camera{navigationMode}, variants[], display.mode:'thumbnail'}` | schema | schema | Strongly supported (generation backend Unknown) |
| Spatial Sense annotations | editor | job | run | `get-spatial-sense-annotations {job_id}`, `promote-spatial-sense-narration`, `pendingAnnotationJobId` | job based | code | Strongly supported |
| Tour AI guide (voice/chat) | viewer | entitlement | talk | `tour_ai_*` tables, audio worklets, analyzer `tour-ai-gateway`, model string `gemini-3.1-flash-lite-preview` for session analysis | DB | code | Strongly supported (one model id seen; others Unknown) |
| Studio assistant chat | app | auth | chat | `/functions/v1/studio-assistant-chat` | — | code | Strongly supported |
| Splat generation jobs | app | credits | upload → generate | `request-splat-upload`, `create_splat_job_with_billing`, `quote_splat_job_client`, queue position/depth, cancel | DB `splat_jobs` | code | Strongly supported |
| Downloads/convert | app | asset | download | In-browser worker converts to SOG/SPZ/PLY/compressed PLY/GLB (splat-transform, WebGPU-capable) | client | code + features page | Strongly supported |
| Publish snapshots | editor | entitlement | publish | `publish_project_with_entitlements`; viewer reads `published_design` vs `design` | DB | code + schema | Strongly supported |
| Share-access tokens | viewer | private tour | open | `tour-share-access` edge fn | — | code | Inferred |
| Billing | app | — | checkout | Dodo Payments edge fns, credit balance/transactions | DB | code | Strongly supported |
