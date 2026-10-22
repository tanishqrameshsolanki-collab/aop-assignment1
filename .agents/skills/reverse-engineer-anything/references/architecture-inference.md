# Architecture inference

- Separate **library evidence** (the bundle contains PlayCanvas) from **usage evidence** (this route renders with it at runtime).
- Chunk names emitted by Vite/Rolldown (`SplatViewer-xxxx.js`, `map.store-xxxx.js`) reveal module and component names. Treat them as Strongly supported, not Verified.
- Saved-document schemas (published JSON) are the best data-model evidence. Field names such as `setup.scaleConfirmed` reveal workflows.
- For every hidden internal, write two or more hypotheses and name the observation that would separate them.
- The Mermaid diagram uses solid edges for verified relationships and dashed (`-.->`) for inferred ones.
- Confidence levels: Verified (observed at runtime or in authorized source), Strongly supported (several independent static signals), Inferred, Unknown.
