# DEC-04 Digestion output - Decision record

| Field | Value |
|---|---|
| Status | Agreed in principle |
| Decided by | user, 2026-11-10 (principle only) |
| Owner | game-designer |
| Last updated | 2026-11-12 |
| Related | Review items D9, N6, G11; tickets T5, T10, T25 |

**Summary.** Digesting always gives mass, plus at most one bonus defined in data. The vertical slice uses one to three memory fragments.

## Question
What does digesting an object give? The GDD lists five outputs in four places; the sheet gives "+ mass" and leaves the rest "depending on gameplay".

## Decision
Agreement in principle (user, 2026-11-10): mass always, plus at most one data-defined bonus; vertical slice limited to 1 to 3 memory fragments. The user will review the details later.

## Still open
- Fragment format (cheap presentation, linked to open question Q18).
- Toxic objects and their mass loss.
- N6: does aspirating, or only digesting, give an object's property?

## Options considered

| Option | Principle | Benefits | Risks |
|---|---|---|---|
| A. Mass only (sheet 4) | The object disappears, + mass | Simplest; animation exists (sheet 6) | Pillar 3 disappears; keeping versus digesting is no longer a choice |
| B. Typed output per object | Each object has its output: mass (organic), temporary property (materials), memory fragment (story objects), toxic (mass loss) | Serves pillars 1, 2 and 3; fully data-driven; digesting costs the tool | Much content; fragment presentation (scene, voice) is costly without art or sound |
| C. Mass always, plus at most one bonus | Every digestion gives mass; an object may carry one bonus: temporary property or fragment. Slice: mass and 1 to 3 fragments; properties and mutations parked | Keeps the animation and the sheet loop; proves pillar 3 with little content; extensible without code | If digestion always gives mass, players digest everything: toxic objects and irreversibility are needed; fragment format TODO |

## Recommendation
C, the smallest option that still proves pillar 3. Proposed corollary for N6: aspirating and keeping an object does not give its property (it stays a tool that can be spat); digesting is the only way to gain from it; tasting reveals without destroying.

## Parameters
`DigestDuration` (2 s, sheet 6), `DigestMassGain` (per object, TODO), `DigestBonus` (per object: none, fragment, property), `ToxicMassLoss` (TODO), `DigestCancelable` (no, per GDD).

## Playtest question
After the session, can the player tell one story element learned by digesting? Did they hesitate before digesting a useful object?

## Impact
T5 (verbs prototype), T10 (design brief), T25 (digest animation stays valid: mass is always given).
