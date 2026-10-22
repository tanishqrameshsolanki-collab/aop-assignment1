# reverse-engineer-anything

A reusable, target-agnostic skill for investigating web applications. Native binary analysis comes from the vendored REA skill.

Invoke it by asking your agent: *"Use the reverse-engineer-anything skill on https://example.com, depth standard, output to ./investigations/example."*

- `SKILL.md`: workflow and rules (agents load this).
- `references/`: playbooks (browser, 3D/spatial, API/data, inference, validation). `references/upstream-rea/` is the MIT-licensed skill from github.com/morluto/rea (pinned commit in `UPSTREAM_COMMIT`).
- `scripts/`: `environment-check [url]`, `mirror-bundles`, `shape.py`, `evidence-validation`, browser init scripts (`capture.js`, `nowebgl.js`), `kill-browser.sh`.
- `templates/`: report skeletons.

Install: copy this directory to `<repo>/.agents/skills/` (Codex, Hoplite, and other AGENTS.md-style agents) or `~/.claude/skills/` (Claude Code). The format is a plain SKILL.md with YAML front matter.
