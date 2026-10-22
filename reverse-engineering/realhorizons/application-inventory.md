# Application inventory

## Shell
- React SPA with react-router (`__reactRouterVersion` global), served by Cloudflare. Vite/Rolldown chunks (`rolldown-runtime-*.js`). **Verified**
- Public sidebar: Explore Tours, Splat Viewer ("Open local splats"), Capture Guide, Tutorials, Create Account, Log In; CTAs "Start Free" and "Sign In". **Verified** (accessibility snapshot)
- Explore cards carry a type badge (SPLAT / MAPS), title, description, view count, and author. A click opens `/tours/:id/view` in a **new tab**. **Verified**

## Routes (from the router table in `App-*.js` / `index-*.js`; Strongly supported)
| Route | Auth | Purpose |
|---|---|---|
| `/explore` | public | Featured gallery (`get_featured_explore_projects`). Verified at runtime |
| `/tours/:tourId/view` | public if published | Published viewer (`get_public_project_for_viewer`). Verified |
| `/tours/:tourId/embed` | public | Iframe embed surface (an inline script special-cases `/tours/*/(view\|embed)`) |
| `/splat-viewer` | public | Local splat file viewer (linked from the features page) |
| `/splat-compressor` | ? | Format conversion, "Powered by playcanvas/splat-transform" |
| `/splat-compare` | ? | Side-by-side splat comparison |
| `/splat-gen/reference/:captureId/:setting` | ? | Splat-generation reference scenes |
| `${editor}/:tourId` | auth | Tour editor |
| `/properties/:propertyId`, `/units` | auth | Real-estate property workspace and unit inventory |
| `/org/:orgId`, `/user-management`, `/user/:userId` | auth | Organisation and users |
| `/share/analytics` | token link | Shared analytics (`analytics-share-access`) |
| `/flight-preview` | ? | Drone flight plans (`flight_plans`, `get_shared_flight_plan`) |
| `/notifications`, `/onboarding` | auth | Feed and onboarding |
| `/login`, `/signup`, `/forgot-password`, `/reset-password`, `/desktop/login` | public | Auth (Supabase; Google OAuth observed by the user). `/desktop/login` + `desktop-auth-code` points to a desktop (Mac training) app |
| `/privacy`, `/terms` | public | Legal |

## Viewer keyboard shortcuts (from `splat-viewer-core`; Strongly supported)
`1` orbit · `2` fly · `3` walk · `4` third-person · `f` frame · `r` reset · `h` help · `v` voxel-collision overlay · `g` toggle "gaming" controls in walk/third-person · WASD auto-enables gaming controls in walk mode. All are suppressed while `canvas.dataset.measurementActive === "true"`.

## Not inspected
Everything behind login (dashboard, editor panels, publish/analytics UI, AI tools).
