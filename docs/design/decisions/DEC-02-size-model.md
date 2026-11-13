# DEC-02 Size model - Decision record

| Field | Value |
|---|---|
| Status | Decided |
| Decided by | user, 2026-11-13 |
| Owner | game-designer |
| Last updated | 2026-11-13 |
| Related | [GDD](../gdd.md) sections 3, 5 and 10, review items D3, D4, N7; tickets T4, T14, T21, T22, T26, T27 |

**Summary.** The slime's mass stays continuous and drives a slight visible swell inside the current size step; the size that decides what fits changes only at step thresholds, with hysteresis. The vertical slice uses three steps (small, normal, large); the five sheet steps remain values to tune later.

## Question
The GDD scales the slime with its mass; the sheets show five steps (x0.5 to x2.5). The user asked: continuous scaling, only two or three steps (eating changes mass by grams), "or a better way".

## Decision
Option C, the hybrid, as proposed. The user: « Je suis pour ta proposition "Hybride, 3 paliers" » (2026-11-13).

1. Mass is continuous. Grams eaten or lost always move it.
2. Mass drives a slight visible swell of the body inside the current step, so hunger and small damage stay readable ([DEC-09](DEC-09-body-signals.md): size = mass).
3. The size step decides what fits (openings, belly volume class, objects that can be pushed). It changes only when mass crosses a threshold.
4. Thresholds use hysteresis, so mass hovering around a threshold does not make the slime flip between steps.
5. Growth into a larger step is refused when there is no room: the slime stays in its current step and the player gets "too tight" feedback.
6. The vertical slice has three steps: small, normal, large. The five sheet steps (x0.5, x1, x1.5, x2, x2.5) stay values to tune later; they are not part of the slice.

Content tags: the model is confirmed; step values, thresholds, hysteresis and swell amplitude are to prototype.

## Still open
- Step values and mass thresholds, after the cage measurement (T27) and the world scale question (N7, which stays open).
- Hysteresis width and swell amplitude: to prototype.
- Which of the five sheet steps the three slice steps map to: TODO(question), after T27.

## Options considered

| Option | Principle | Benefits | Risks |
|---|---|---|---|
| A. Continuous | Scale follows mass continuously | GDD rules work as written (slow hunger and damage visible); simplest to code | Player cannot tell whether a gap fits; level design on a continuum is hard |
| B. Five steps (sheet 3) | x0.5, x1, x1.5, x2, x2.5; 0.8 s transition | Readable thresholds; easy progression gates; matches the sheets | Hunger and small damage invisible between steps; a step change in a pipe can trap the slime; 1-to-5 size range is hard for camera and physics |
| C. Hybrid (chosen) | Mass stays continuous and drives a slight visible swell inside the current step; the size that decides what fits changes only at step thresholds, with hysteresis; growth is refused without room ("too tight" feedback) | Readable gates and an always-visible resource; keeps the sheets and the GDD | Two tuning layers; limit bugs at step boundaries, to cover in QA |

## Recommendation
Not applicable: decided by the user, who chose the recommended option C with three steps for the vertical slice. It serves pillar 1 (mass always readable) and pillar 4 (predictable thresholds, so experimenting is not frustrating).

## Parameters
`SizeStepScales` (initial from sheet 3: 0.5, 1, 1.5, 2, 2.5; the slice uses three of them, TODO), `SizeStepMassThresholds` (TODO), `SizeStepHysteresis` (TODO), `SizeStepTransitionTime` (0.8 s, sheet 6), `InStepScaleVariation` (TODO).

## Playtest question
Does the player know, before trying, whether the slime will fit through an opening?

## Impact
T4 (mass and size), T14 (camera), T21 and T22 (mesh and rig), T26 (integration). QA covers the step boundaries (hysteresis, growth refused in a tight spot). Prerequisite for the values: settle the x10 world scale (N7) with the unreal-engineer and the level-designer.
