# Implementation validation

Build one subsystem at a time in a separate project. For each feature:
1. Start from a fixed fixture (a known scene file and a saved JSON design).
2. Script the same interaction as the reference with Playwright or agent-browser.
3. Assert state (store JSON), not just pixels. Use pixel diff (`agent-browser diff screenshot --baseline`) for appearance only.
4. Reload and assert persistence.
5. Cover edge cases: cancel, repeat, invalid pick (sky/background), unit switching, and undo/redo.
6. Measurements: unit-test against synthetic coordinates (for example P1=(0,0,0), P2=(3,4,12) gives d=13 m = 42.65 ft).
Keep `parity-checklist.md` updated. A feature is done only when its test passes.
