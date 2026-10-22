# Rendering analysis

## Representation
- Tours are **3D Gaussian splats**. The published scene's `splatFile.format` is `"sogs"`, and the asset list contains `.sog` files. Verified (payload).
- Supported inputs/outputs in code: PLY, compressed PLY, SPZ, SOG (`meta.json` + `means_l/means_u/quats/scales/sh0/shn_centroids/shn_labels.webp`), `lod-meta.json` (chunked LOD), XGRIDS `.lcc`, and experimental GLB. Strongly supported (code + features page).
- Collision does **not** come from the splats. It comes from authored **primitives** (`collision.source: "primitives"`; walls/polygons as `blocker` components) and/or a **voxel grid** (`.voxel.json` metadata + `.voxel.bin`, `voxelResolution`, grid bounds, overlay toggle `v`). Strongly supported.
- Maps scenes: Google Photorealistic 3D Tiles (3DTilesRenderer) with an optional splat placed using `splatTransform{position,rotation,scale}`, rendered by Spark on three.js. Strongly supported.
- Point-cloud display mode exists (`pointCloudSettings{pointSize, opacity, colorMode:'rgb'}`). Strongly supported.

## Engine
- PlayCanvas GSplat rendering through the SuperSplat viewer core: `gsplat` assets, LOD via `lod-meta.json`, WebGL2 with a WebGPU device chunk present. Whether WebGPU is selected at runtime is Unknown.
- Sorting, SH evaluation, and shaders are the PlayCanvas engine's (open source). Real Horizons-specific shader changes are Unknown. A custom depth-pick variant exists (see measurement-analysis.md).
- Color Studio values are stored as renderer parameters in the design JSON (`colorAdjustments`). Assets are not re-baked. Strongly supported.
- Reveal animation (`revealSettings.effect: "magic"`), HDRI/sky with ground plane (`hdriSettings`), quality presets (`sceneSettings.quality`), FOV, and zoom limits. Strongly supported.

## Camera
Modes: orbit, fly, walk, and third-person (character, `openingViewCharacterPosition`, `characterOcclusionEnabled`). Orbit limits: min/max distance and polar angle, damping, auto-rotate. The entry camera is position + target + fov. Scene-to-scene transitions use `camera-crossfade`. Strongly supported (schema + key handler). Speeds and easing curves are Unknown (`cameraAnimation`, `spline` chunks exist).

## Runtime caveat
Live rendering could not be observed. Software WebGL in the 2-CPU sandbox saturated Chrome's GPU process. A machine with a GPU is needed for frame timing, memory, and visual artifact checks.
