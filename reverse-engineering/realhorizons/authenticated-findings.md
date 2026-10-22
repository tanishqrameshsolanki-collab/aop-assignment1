# Authenticated pass (Free plan account, 2026-10-22)

Logged in with user-supplied credentials. I clicked through onboarding, then **Build a virtual tour**, then **Try a sample tour**, which created a draft project "Explore an interior sample" (scene `blue-tokai-interior.sog`). The browser had WebGL disabled, so the 3D viewport showed "WebGL not supported". Everything below is UI and panel evidence. All entries are **Verified** (observed in the UI) unless noted. Nothing was published, generated, purchased, or saved beyond the sample's autosave. The agent browser was logged out afterwards.

## Dashboard (sidebar)
Dashboard (analytics; "Free plan does not include dashboard analytics"), Virtual Tours (`/tours`, list with type/status/views), Splat Generator (`/splat-gen`), Splat Viewer (`/splat-viewer`: PLY, compressed PLY, SPLAT, KSPLAT, SOG, SPZ, plus a hosted LOD-metadata URL), Flight Plans (`/flight-plans`, Starter+), Asset Library (`/asset-library`: Splats / Panoramas / Media / Plans, storage 0 B / 2 GB), Explore, Tutorials, Capture Guide, What's New, Credits & Billing (`/subscription`), Settings (`/settings?section=team`: profile, organization logo, members with roles, invite), Feedback, Support, Log Out. Legacy routes `/notifications` and `/units` redirect to `/dashboard` and `/tours`.

## Plans (from `/subscription`)
| Plan | Price | Credits | Tours | Storage | Notable |
|---|---|---|---|---|---|
| Free | $0 | 0 | 1 | 2 GB | Fast/Balanced splat quality, watermark |
| Starter | $12/mo | 200 (~5 generations) | 5 | 15 GB | Mac beta unlimited local processing, analytics, no watermark |
| Pro | $39/mo | 1,000 (~25) | 20 | 50 GB | Spatial Sense AI, AI Reframe up to 4K, custom logo |
| Studio | $99/mo | 3,000 (~75) | 75 | 200 GB | Full AI set, rollover cap 3,000 |

Estimates assume a 5-minute non-360 video at High quality. Splat generation on Free requires starting the 7-day Starter trial (50 credits), so it was not tested.

## Editor (`/editor/:tourId`)
**Top bar:** exit, rename tour, scene switcher (scene list with entry flag and mode), **Add** menu (Add 3D scene, 360° Panorama module, Gallery module, Map module), **Scene setup** checklist, autosave indicator ("All changes saved"), Preview & publish.

**Scene setup (5 steps):** 3D splat (file), Movement (Walkthrough), Orientation ("floor level, walls up"), Scale & ground, Opening view. Includes a "Walk me through it" guided mode.

**Viewport:** quality SD/HD; editor camera Third person / First person / Fly; controls guide (WASD move, Q/E elevate, left-drag look, scroll zoom, Shift fast).

**Tool rail (contextual groups):**
- Navigate: Select, Reset setup view.
- Create: Add Hotspot ("fly to the surface, then click once"), Add 3D Object (from the "Create Object 3D" asset library), Add Animation (Manual / Auto from hotspots), Measure Distance (2-click).
- Intelligence: Reframe AI (errored with "The 3D view is still loading" because there was no WebGL), Smart Hotspots (disabled until hotspots exist).
- Splat editor (SuperSplat-style): Undo/Redo; Brush, Lasso, Box, Polygon, Flood select, Color pick; volume Sphere select / Volume box; Move/Rotate/Scale splats; Clear, Invert, Delete; overlay Centers/Rings/Selection outline; color detail (SH bands 0–3); Save changes / Done.
- Floorplan: Select; Draw Walls / Door / Opening; Annotate Object / Label / **Measure** / **Set scale**; Undo / Redo / Delete.
- Collision: per-floor ("Create a floor first"); Draw Wall path / Blocked area; Add Floor / Wall / Blocker / Ramp; Import.

**Inspector tree:** Experience (Opening View: "Use current" / Preview; Character avatar "Leonard", "See through walls"), Animations, 3D Splat, Environment, Spatial Setup (Floorplan, Walk Collision), Hotspots.
- 3D Splat: Transform (position, rotation, Flip 180° X/Y/Z, **Scale with a "Measure" calibration action**); Reveal effect (Magic); Color presets (Default, Sunny, Cloudy, Indoor, Night, Cinema, plus Save custom); sliders for brightness, contrast, exposure, saturation, black/white point, shadows, highlights, temperature, tint; **Privacy: "Blur surroundings"** (soften neighbouring houses); Edit splat; Replace.
- Environment: backdrop None / Pure Sky / Outdoor Day / Coastal Dusk / Outdoor Snow / Rocky Night / Upload panorama; tour ambience audio with per-scene override or silence.
- Floorplan: **Create floorplan** ("trace it over the splat, guided in three steps"), **Image / PDF reference**, **Generate AI floorplan**. This confirms vector tracing over the splat, with an optional raster/PDF underlay.

## Preview & Publish (`Edit tour` / publish page)
- **Details:** title, description, default quality, Opening hold, Mobile joystick, **Visitor measurements** ("Let visitors measure distances and rectangular areas in 3D. Uses your scene's scale. Measurements stay in their browser."), CTA custom web link, viewer language, **Content translations** (AI translation uses credits).
- **Style:** 10 viewer templates (Horizon, Obsidian, Atelier, Lumen, Flux, Estate, Shore, Majlis, Meridian, …, each paired with a font), layouts Standard / Folio / Promenade / Monograph, scene strip Cards / Minimal, accent colour, branding (logo requires Pro).
- **Share:** embed code (after publish), "List on Explore".
- Publish Tour / Save Draft. A 5-step coach-mark explains Preview, CTA, Start mode, and Publish.
