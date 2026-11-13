# DEC-03 Dirt and robots - Decision record

| Field | Value |
|---|---|
| Status | To confirm (partly decided) |
| Decided by | user, 2026-11-10, for the suction penalty only |
| Owner | game-designer |
| Last updated | 2026-11-12 |
| Related | Review items D5, D6, D7, G1, G12; decision DEC-09; tickets T9, T24; risk R13 |

**Summary.** Dirt no longer reduces suction. Whether mud insulates against heat and whether robots enter the vertical slice are still to confirm.

## Question
Is dirt a gameplay system or only visual, and are the surveillance and cleaner robots of the sheets in the vertical slice?

## Decision
User, 2026-11-10: removing the dirt-linked penalty is "a good idea" (frustrating, no real choice; dirt already has a cost, a dimmer core, and a benefit, stealth).

Recorded interpretation, to confirm: the dirt-linked **suction penalty** is removed; core intensity (DEC-09) and stealth stay.

## Still open
1. Is the suction penalty the only thing removed?
2. Does mud keep its heat effect (insulation, melts slowly)?
3. Are robots out of the vertical slice?

Items 2 and 3 are game-designer recommendations, not user decisions.

## Options considered

| Option | Principle | Benefits | Risks |
|---|---|---|---|
| A. Visual dirt, no robots | Dirt is only a material parameter | Minimal cost, no AI | Dirt tells nothing, against the user's pillar 1; loses "clean and dirty both have advantages" (sheet 2) |
| B. Dirt as a coating in the property system, no robots | Dust, soot and mud are substances: mud insulates, soot dims the glow; one coating at a time; clean in water (+ mass) or by turning liquid (dirt stays on the floor); a fixed sensor instead of a robot if the glow needs a use | Dirt matters through existing systems, no AI; inventive solutions (mud to cross a hot zone); cheap | Stealth stays thin; dirt on translucent jelly depends on the Substrate test (T1) |
| C. Full sheet model | Four coatings and two robot types (surveillance by glow, cleaners by dirt) | Richest; dirt and glow fully meaningful | AI, perception, navigation at x10 scale, robots to model and animate without an artist; no failure state defined (G12); against the GDD rule that the game is complete without optional parts; maximum R13 risk |

## Recommendation
B, with robots out of the vertical slice (parked, reopened after the pre-production playtest), and the suction penalty removed because it weakens the central verb. Serves pillars 1 and 2 without an AI system.

## Parameters
`CoatingType` (clean, dust, soot, mud), `Coating_HeatExchangeMultiplier`, `Coating_GlowMultiplier`, `Coating_AspirationMultiplier` (1.0, no penalty), `WaterCleanMassGain`, `LiquidCleanLeavesDecal` (yes or no). Values TODO, indicative per sheet 2.

## Playtest question
Did the player use mud or soot on purpose at least once?

## Impact
T9 (dirt prototype: visual and core intensity first, stealth and robots out until confirmed), T24 (slime material), R13.
