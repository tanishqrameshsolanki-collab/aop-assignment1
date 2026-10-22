# Project notes for Claude Code

This repo has two unrelated parts:
- `power_calculator.c` and `algorithm.txt`: AOP Practical 52 (C). Build with `gcc power_calculator.c -o power`.
- `reverse-engineering/realhorizons/`: an investigation of Real Horizons Spatial Studio (studio.realhorizons.ai), a Gaussian-splat virtual-tour editor. It covers architecture, data model, editor behaviour and a rebuild plan.

Reusable skill: `.claude/skills/reverse-engineer-anything/` (copy of `.agents/skills/reverse-engineer-anything/` for other agents; keep both in sync).

## Real Horizons context (always loaded)
@reverse-engineering/realhorizons/CONTEXT.md

Detailed files in `reverse-engineering/realhorizons/`: feature-matrix.md, architecture-report.md, rendering-analysis.md, measurement-analysis.md, data-model.md, api-inventory.md, authenticated-findings.md, implementation-plan.md, test-plan.md, known-unknowns.md. Field paths of the published tour JSON: evidence/project-paths.txt.

## Rules
- Never commit credentials, tokens, cookies or the user's email/password.
- Real Horizons code and assets are proprietary. Use the findings as a capability reference only. Do not copy their code.
