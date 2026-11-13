# DEC-01 Temperature states - Decision record

| Field | Value |
|---|---|
| Status | Decided |
| Decided by | user, 2026-11-10 |
| Owner | game-designer |
| Last updated | 2026-11-12 |
| Related | Review items D1, D2, N1, N9, C10; tickets T7, T20, T26 |

**Summary.** The slime has four temperature states taken from the slime sheets: frozen, gelatinous (normal), hot liquid and burning. Floating vapor is dropped.

## Question
Which temperature model does the slime follow? The GDD has three states (liquid, frozen, vapor); the sheets have four on one heat axis with two hot thresholds.

## Decision
Sheets model with four states (user, 2026-11-10):

| State | Condition | Effect |
|---|---|---|
| Frozen | Cold | Rigid, frost, blue core |
| Gelatinous | Ambient temperature (normal state) | Base dome shape |
| Hot liquid | First hot threshold | Puddle, passes grids, orange core |
| Burning | Second hot threshold | Evaporates and loses mass, red core |

Floating vapor and vent flight are dropped ("useless for a slime"). The GDD must be aligned: "gelatinous" replaces "liquid (normal)", vapor is removed.

## Still open
- Threshold values and transition times.
- Burning drawn as a dome although it is hotter than the liquid puddle (N9).
- Only hot liquid passes grids (N1): parameter to confirm in prototype.

## Options considered

| Option | Principle | Benefits | Risks |
|---|---|---|---|
| A. GDD, 3 states | Liquid (normal), frozen, vapor (floats, rises through vents, loses mass) | Faithful to the GDD; squeezing is free; vertical movement | Contradicts every sheet; a resting puddle reads badly; vapor needs flight control and volumetric rendering |
| B. Sheets, 4 states | Frozen, gelatinous, liquid (first threshold), burning (second threshold, mass loss) | Matches validated art; one axis, two thresholds; liquid becomes a puzzle ability; no flight | No vapor for vents; four materials and their transitions to produce |
| C. Sheets, burning as danger | Three playable states; burning is liquid past the second threshold, a mass-loss danger, not a movement mode | Keeps the art; fewest animations; natural failure state | Loses vertical vapor movement; needing heat to pass a grid may slow pacing |

## Recommendation
The game designer recommended C. The decision matches B without vapor flight, with burning treated as the mass-loss danger state of C.

## Parameters
`TempThreshold_Freeze`, `TempThreshold_Melt`, `TempThreshold_Burn` (TODO), `StateTransitionTime` (GDD: "a few seconds"; sheets: 1.2 s to freeze, 1 s + 0.8 s to melt and reform), `BurnMassLossPerSecond` (TODO), `AmbientReturnRate` (TODO).

## Playtest question
Without explanation, does the player understand they must heat the slime to pass a grid?

## Impact
T7 (states prototype), T26 (state integration), T20 (GDD update), C10 (frozen state timing).
