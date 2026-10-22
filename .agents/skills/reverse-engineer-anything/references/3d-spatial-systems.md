# 3D / spatial systems checklist

## Identify the renderer (static bundle evidence)
| Signal string | Indicates |
|---|---|
| `REVISION`, `WebGLRenderer`, `@react-three/fiber` | three.js / R3F |
| `playcanvas`, `GSplat`, `gsplat`, `supersplat-viewer`, `splat-transform` | PlayCanvas engine and SuperSplat stack |
| `SparkRenderer`, `SplatMesh`, `PackedSplats`, `spark_rs` | Spark (World Labs) splats on three.js |
| `GaussianSplats3D` | mkkellogg three.js splats |
| `TilesRenderer`, `tile.googleapis.com` | 3D Tiles / Google Photorealistic Tiles |
| `maplibre-gl`, `mapbox-gl`, `cesium` | map engines |
| `MeshBVH` | three-mesh-bvh raycasting acceleration |
| `navigator.gpu`, `WebGPU` | WebGPU path (check whether it is actually selected) |

## Scene formats
`.ply` (raw 3DGS), `.splat`, `.spz` (Niantic), `.sog` / `meta.json` + `means_l/means_u/quats/scales/sh0/shn_*.webp` (PlayCanvas SOG), `lod-meta.json` (streamed LOD chunks), `.lcc` (XGRIDS), `.voxel.json` + `.voxel.bin` (collision voxels), `.glb`.

## Questions to answer
- Which representation drives appearance, picking, collision, and navigation? Splats rarely drive collision. Look for voxels, proxy primitives, or meshes.
- Camera modes and shortcuts, damping, polar and distance limits, and the entry/opening camera schema.
- Picking: a depth render pass (`pickDepth`, `readPixels`) versus CPU raycasting (BVH) versus a collider.
- Measurements: units, conversion constant (3.28084), precision, scale-calibration steps (look for `scaleConfirmed`, `metricScale`).
- Color grading: renderer uniforms versus baked assets (look at the saved settings schema).
- LOD: distance thresholds, chunk manifest, and streaming budget.

## Sandbox note
Software rendering of large splats may hang the browser. Prefer bundle and schema evidence. Test rendering only with tiny viewports or on a machine with a GPU.
