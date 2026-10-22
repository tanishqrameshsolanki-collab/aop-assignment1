# Installation record

## What was installed
1. **`rea-agents` (npm, MIT, github.com/morluto/rea)** via `npx -y rea-agents setup`. Status `ready`, but `environment_healthy: false`. It found none of its 25 supported MCP clients in this sandbox (Hoplite is not one of them) and no analysis backends (Ghidra/IDA/JADX/Kuna). It is usable as a CLI (`npx -y rea-agents@latest analyze-javascript-application <dir> --json`), not as a registered MCP server here.
2. **`reverse-engineer-anything` skill** at `~/re-work/.agents/skills/reverse-engineer-anything/`:
   - REA's upstream skill, vendored unchanged in `references/upstream-rea/` with its LICENSE and pinned commit.
   - A new web-application workflow in `SKILL.md`, plus 5 references, 5 templates, and scripts (`environment-check`, `mirror-bundles`, `shape.py`, `evidence-validation`, `capture.js`, `nowebgl.js`, `kill-browser.sh`).

## Verify
```bash
cd ~/re-work/.agents/skills/reverse-engineer-anything
scripts/environment-check https://example.com
scripts/evidence-validation ~/re-work/realhorizons
```
Both were run in this session and passed.

## Persistence caveat
Hoplite loads skills from a connected repository's `.agents/skills/`. This sandbox has no repository attached, so the skill persists only in this thread's workspace. To make it available in every future thread, commit `.agents/skills/reverse-engineer-anything/` to a project repository. For Claude Code, copy it to `~/.claude/skills/`.
