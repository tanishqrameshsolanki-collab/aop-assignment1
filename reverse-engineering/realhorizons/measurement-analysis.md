# Measurement analysis

## Evidence
- The viewer has a measurement mode flagged on the canvas (`canvas.dataset.measurementActive === "true"`). While it is active, click-to-walk, keyboard navigation toggles, and the 3D cursor are suppressed. Strongly supported.
- The PlayCanvas splat picker has a **depth pick mode** (`uniform pickDepthMode`). Its GLSL and WGSL shaders output `gaussianColor.a * normalizedDepth` with alpha in a second channel, read back via `readPixels` (async PBO path). This yields an **alpha-weighted depth** at the clicked pixel. The pixel is unprojected with `camera.screenToWorld` along the view ray. Strongly supported for picking. That measurement uses this path is **Inferred** (same viewer core; no direct call site traced).
- Imperial conversion uses the constant `3.28084` (m to ft) in property/unit code with `lengthScale` / `lengthUnit` props. Strongly supported.
- Scale: the scene setup wizard has `setup.scaleConfirmed`, and splat generation offers a "metric scale" option. Displayed distances are therefore only physical after generation-time metric scale or a manual scale confirmation. Strongly supported (schema + marketing); the calibration UI is Unknown.
- Collision snapping uses `collision.snap{enabled, incrementM}` (metres), so the authoring unit is metres. Strongly supported.

## Hypotheses (distance computation)
| H | Description | Test that separates them |
|---|---|---|
| H1 | Euclidean distance between two depth-picked world points, √Σ(Δ²), in scene units × scale | Place points on a known-size object in a metric-scale scene and compare |
| H2 | Points snapped to collision primitives / voxels instead of splat depth | Measure across a voxel-free area; check whether picks land on floating splats |
| H3 | Horizontal-only (XZ) for floor-plan/wall lengths | Measure a vertical span |

**Resolved in the authenticated pass (Verified, UI text):** visitor measurements support **distances and rectangular areas**, use the scene's scale, and **stay in the visitor's browser** (not saved to the project). The editor has a 2-click *Measure Distance* tool. The floorplan editor has *Measure* and *Set scale*. The 3D Splat transform panel has *Scale* with a *Measure* calibration action, and scene setup has a *Scale & ground* step. Angle tools: none seen. Rounding/precision is still Unknown (needs rendering).

## Limitations
Alpha-weighted depth on splats is biased near edges and semi-transparent Gaussians (glass, foliage). Expect centimetre-to-decimetre error indoors, and worse on reflective surfaces.
