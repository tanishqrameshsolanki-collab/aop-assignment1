# Test plan

| ID | Feature | Fixture | Steps | Expected | Persistence | Status |
|---|---|---|---|---|---|---|
| T1 | Load SOG/PLY/SPZ | 3 small public-domain splats | open each | renders; no console errors | — | not built |
| T2 | Camera modes | fixture | keys 1–4, f, r | mode changes; `r` restores entryCamera within 1e-3 | entryCamera JSON round-trip | not built |
| T3 | Orbit limits | min/max distance 2/10 | wheel past limits | distance clamped | reload keeps limits | not built |
| T4 | Distance math | synthetic P1=(0,0,0), P2=(3,4,12) | compute | 13.000 m / 42.651 ft (×3.28084) | — | not built |
| T5 | Depth pick | plane at z=−5 rendered as dense splats | click centre | world point z ≈ −5 ± 0.05 | — | not built |
| T6 | Scale calibration | known 1 m bar | 2-point calibrate | later measurement of bar = 1.00 m ± 1% | factor saved | not built |
| T7 | Hotspot CRUD + undo | fixture | add, move, delete, undo ×3 | state equals initial | reload | not built |
| T8 | Portal | 2 scenes | click nav hotspot | target scene + entryCamera; crossfade | — | not built |
| T9 | Collision | wall primitive | walk into wall | camera stops at wall − radius | — | not built |
| T10 | Publish snapshot | project v1 | publish, edit draft | public view unchanged until republish | version++ | not built |
| T11 | Reference parity | Real Horizons public tour on a GPU machine | same camera path | visual comparison (manual) | — | blocked (no GPU here) |
