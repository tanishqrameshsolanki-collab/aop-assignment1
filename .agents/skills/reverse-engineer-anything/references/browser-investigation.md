# Browser investigation

Tool: `agent-browser` (CDP CLI). Wrap each call: `AB="timeout 40 agent-browser"`.

## Recon commands
```bash
$AB set viewport 1280 800
$AB open "$TARGET_URL"; $AB wait 4000
$AB snapshot -i -c            # interactive elements with @refs
$AB screenshot <out>/reference-assets/01-landing.png
$AB eval '(()=>JSON.stringify({s:[...document.scripts].map(x=>x.src||"inline:"+x.textContent.slice(0,80)),l:[...document.querySelectorAll("link")].map(x=>x.rel+" "+x.href),g:Object.keys(window).filter(k=>/^(__|React|next|Vue|pc|THREE|Sentry|supabase|firebase|_)/i.test(k))}))()'
$AB network requests > <out>/evidence/requests.txt   # then redact (see below)
$AB tab list; $AB console; $AB errors
```

## Instrumented sessions
- `--init-script scripts/capture.js` stores `rest/v1/rpc`, `functions/v1`, and any matching fetch responses in `window.__cap`. Edit its URL regex for other backends (GraphQL `/graphql`, `/api/`).
- `--init-script scripts/nowebgl.js` makes `getContext('webgl*'|'webgpu')` return null. Use it for UI and network study when rendering stalls the browser.
- Init scripts are registered at browser launch. Run `scripts/kill-browser.sh` to change them.

## Redaction
Pipe request logs through `sed -E 's/((token|key|apikey|sig|signature|Expires|Policy|Key-Pair-Id|code)=)[^&" ]+/\1REDACTED/gi'`. Never save request headers. Delete raw response captures after reducing them with `scripts/shape.py`.

## Coverage checklist
Routes from the router table, nav items, dialogs, context menus, keyboard shortcuts (grep `case\`k\`:` / `e.key===`), empty/loading/error states, responsive (`set viewport 390 844`), save/publish/share flows, and login-gated areas (list them; ask the user to log in only if needed).
