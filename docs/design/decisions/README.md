# Design decisions - Decision log

| Field | Value |
|---|---|
| Status | Approved |
| Owner | game-designer (records); the user decides every entry |
| Last updated | 2026-11-13 |
| Source of truth for | The list of design decisions and their status |

**Summary.** Six decisions are settled (DEC-01, DEC-02, DEC-05, DEC-07, DEC-09, DEC-11), two are settled for a first version or in principle (DEC-10, DEC-04), and three wait for the user (DEC-03, DEC-06, DEC-08).

| Id | Topic | Status | Decided | Current answer |
|---|---|---|---|---|
| [DEC-01](DEC-01-temperature-states.md) | Temperature states | Decided | 2026-11-10 | Four sheet states (frozen, gelatinous, hot liquid, burning); vapor dropped |
| [DEC-02](DEC-02-size-model.md) | Size model | Decided | 2026-11-13 | Hybrid: continuous mass with a slight swell, 3 size steps for the slice (step values to tune) |
| [DEC-03](DEC-03-dirt-and-robots.md) | Dirt and robots | To confirm | 2026-11-10 (part) | Suction penalty removed; mud heat effect and robots to confirm |
| [DEC-04](DEC-04-digestion-output.md) | Digestion output | Agreed in principle | 2026-11-10 | Mass always plus at most one bonus; 1 to 3 fragments in the slice |
| [DEC-05](DEC-05-tone.md) | Tone | Decided | 2026-11-10 | Unsettling and poetic world, attaching but not cute creature |
| [DEC-06](DEC-06-duration-and-cuts.md) | Duration and cut order | To confirm | - | Proposal: 3 to 4 h ceiling and a fixed cut order |
| [DEC-07](DEC-07-no-explicit-help.md) | No explicit help | Decided | 2026-11-10 | Clues in the world only; "Look" reaction rule to confirm |
| [DEC-08](DEC-08-interface-elements.md) | Interface elements | To confirm | - | Proposal: nothing permanent; reticle in aim mode; archive in pause menu |
| [DEC-09](DEC-09-body-signals.md) | Body signals | Decided | 2026-11-10 | Colour = temperature, intensity = dirt, size = mass, rhythm and softness = cohesion |
| [DEC-10](DEC-10-cage-and-phases.md) | Cage and phases | Decided (first version) | 2026-11-10 | The cage is the first version of the vertical slice |
| [DEC-11](DEC-11-world-partition.md) | World Partition | Decided | 2026-11-13 | The world uses World Partition; room and data layer layout in a technical spec |

## How to add a decision

Copy [the template](../../templates/decision-record.md) to `DEC-NN-<topic>.md` with the next free number, add a row above, and link the decision from the documents it affects. Only the user moves a decision to Decided.
