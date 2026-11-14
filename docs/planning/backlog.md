# Volvacslime - Backlog

| Field | Value |
|---|---|
| Status | Draft (nothing created on GitHub yet) |
| Owner | producer |
| Last updated | 2026-11-13 |
| Source of truth for | Tickets: context, acceptance criteria, owner, size, dependencies |
| Related | [Roadmap](roadmap.md), [risks](risks.md), [decision log](../design/decisions/README.md) |

**Summary.** The project is in the concept phase: tickets T2, T6, T10, T11, T20 and T28 belong to it. The other prototype tickets start in pre-production, riskiest first, and seven slime production tickets are scheduled later. Every mechanic is to prototype; prototypes are disposable and labeled. Chaos destruction is a means, not the core.

Ticket format: a heading `TNN - Title`, one table row (Owner, Size, Status, Depends on, Waits for decision), then Context and Acceptance criteria. Sizes: S (days), M (one to two weeks), L (more). Gameplay tickets get test coverage in T15.

## Concept and pre-production tickets

Concept phase (now): T2, T6, T10, T11, T20, T28. Every other ticket of this section starts after the concept gate.

### T1 - Substrate test on the slime material

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| technical-artist | M | Backlog | T2, T6 | - |

- **Context:** a translucent jelly with dirt may be costly or unstable in Substrate (R2). Slime materials are validated in Blender only.
- **Acceptance criteria:**
  - [ ] Slime material with a dirt layer tested in Unreal with Substrate on, and a classic-material fallback.
  - [ ] Frame cost measured against the T2 target.
  - [ ] Written go or no-go.

### T2 - Hardware target and budgets (Windows)

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| producer (with unreal-engineer input) | S | Backlog | - | - |

- **Context:** PC is confirmed and Windows proposed; there is no minimum spec and no budget.
- **Acceptance criteria:**
  - [ ] The bible lists the minimum spec, frame-time target, memory, texture and active-fragment budgets.
  - [ ] Provisional asset budgets per category (main character, prop, environment piece: triangles, material slots, texture resolution), validated by the user, used to compare modeling proposals.
  - [ ] Main character: the budget also covers the translucent material (number of nested shells, translucent overdraw and refraction cost at the largest size step, material slots, texture resolution), not only triangles. Review of the slime sheets, 2026-11-14: the real cost of the slime is its layered translucent shader (sheet 2: 2 to 3 nested shells, Substrate), which grows with on-screen area, up to x2.5 = 200 cm.

### T3 - Graphics config changes

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | S | Backlog | T11, T2 | - |

- **Context:** recommendations, not applied: keep Lumen; disable hardware ray tracing; keep Substrate pending T1; disable the ChaosVehicles plugin (Chaos physics and Geometry Collection stay). This touches `Config/DefaultEngine.ini` and `Volvacslime.uproject`, which also carry the editor agent setup (Python remote execution, EngineWire): keep it.
- **Acceptance criteria:**
  - [ ] Ray tracing off and ChaosVehicles disabled; the project opens and the test map runs.
  - [ ] Chaos destruction still works.
  - [ ] The change is in its own commit.

### T4 - Prototype: mass and size

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | L | Backlog | T10 | N7 (world scale, for the step values) |

- **Context:** mass is the single resource (life, hunger, capacity, size, strength). The game designer supplies the brief (T10). Prototype.
- **Acceptance criteria:**
  - [ ] Mass is continuous and drives a slight swell of the body inside the current size step; three steps (small, normal, large) decide what fits ([DEC-02](../design/decisions/DEC-02-size-model.md)).
  - [ ] Step changes use hysteresis; growth into a larger step is refused without room, with "too tight" feedback.
  - [ ] Step values, thresholds, hysteresis and swell amplitude are data parameters (values TODO until T27 and N7).
  - [ ] Belly capacity and movement are tuned by mass.
  - [ ] Minimum mass gives a soft game over at a rest point.
  - [ ] Tuning values live in a data asset; prototype code is labeled.

### T5 - Prototype: aspirate, keep, taste, digest, spit, throw

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | L | Backlog | T10, T4 | DEC-04 (details) |

- **Context:** existing `BPC_AspirationComponent`, `BPC_TargetDetectionComponent`, `BPC_Inventory` and the Aspirable channel. The GDD asks a cone, size against free belly mass, heavy objects dragged, fixed objects resisting (C17). Prototype.
- **Acceptance criteria:**
  - [ ] In the greybox cage the player can aspirate, keep, taste (properties revealed without destruction), digest (mass plus at most one bonus), spit and throw with a visible trajectory.
  - [ ] Known failure cases are listed.
  - [ ] No stuck object in 10 minutes of play.

### T6 - Slime sheets v1 review

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| blender-artist (asset sheet only); the user decides | S | Backlog | - | DEC-03 |

- **Context:** the six sheets in `docs/reference/slime_sheets/` are validated as a base to modify; the character spec is in `docs/design/slime-character.md`. D1, D2 (DEC-01), D7 (DEC-09) and D10 (DEC-05) are settled; only the burning dome needs a redraw (N9). Still to review: D3, D4, D5, D6, D8, D9, D11, D12.
- **Acceptance criteria:**
  - [ ] The user reviews the remaining discrepancies and confirms what is kept.
  - [ ] A short "sheets v1 review" note records the changes.
  - [ ] The asset sheet is drafted once T21 to T27 exist. No modelling here.

### T7 - Prototype: temperature and states

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | L | Backlog | T4, T10 | - |

- **Context:** four states from DEC-01: gelatinous, frozen, hot liquid, burning (mass loss); no vapor and no vent flight; only hot liquid passes grids (N1, parameter to confirm). Progressive transitions, auto return to gelatinous, per-actor temperature plus zone volumes. Prototype.
- **Acceptance criteria:**
  - [ ] Temperature zones change the slime state with a few seconds of transition.
  - [ ] Frozen breaks glass and supports weight; burning loses mass.
  - [ ] The slime never stays stuck; values live in data.

### T8 - Prototype: properties and reactions from data

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | M | Backlog | T7 | - |

- **Context:** properties (hot, cold, humid, conductive, sticky) and rules in a Data Table, for example cold + humid gives gel. Prototype.
- **Acceptance criteria:**
  - [ ] At least 3 reactions defined only in data.
  - [ ] Adding a rule needs no code change.
  - [ ] Reactions are visible in the world.

### T9 - Prototype: dirt and core glow

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| game-designer, then technical-artist and unreal-engineer | M | Backlog | T1, T10 | DEC-03 |

- **Context:** per DEC-09, core intensity depends only on dirt and core colour is temperature; per DEC-03 there is no suction penalty. Prototype dirt as visual plus core intensity first; mud heat effect, stealth and robots stay out until DEC-03 is confirmed.
- **Acceptance criteria:**
  - [ ] A short design note says what dirties, what cleans and what dirt carries.
  - [ ] A prototype shows dirt on the body, readable in play, with the core intensity indicator.
  - [ ] Checked against the T1 results.

### T10 - Design brief: mass, verbs and states

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| game-designer | M | Backlog | - | - |

- **Context:** the rules exist in the GDD but not as testable briefs; C3, C7, C9 and C10 must be settled.
- **Acceptance criteria:**
  - [ ] Brief or briefs in `docs/design/briefs/` from the design-brief template, with numbered testable rules.
  - [ ] The living GDD (`docs/design/gdd.md`) links the briefs and reflects their rules.
  - [ ] Tuning parameters: mass, thresholds, temperatures, belly capacity.
  - [ ] Edge cases listed; taste input and output defined.

### T11 - Repository conventions and Git LFS

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer with producer; the user decides | S | Backlog | - | - |

- **Context:** the pending config changes (editor agent setup) were committed on 2026-11-13; conventions are only proposed; Git LFS is unverified.
- **Acceptance criteria:**
  - [ ] Git LFS status checked.
  - [ ] Conventions and branch naming approved in the bible.

### T12 - Spike: Chaos destruction as a means

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | M | Backlog | T2 | - |

- **Context:** a `BP_Stone` test exists. Destruction is a means (reveal contents, open a path) and has a cost (noise, fragments).
- **Acceptance criteria:**
  - [ ] Frame time measured with N active fragments (N from T2).
  - [ ] Fragment lifetime limit proven.
  - [ ] Go or no-go, with a fallback (pre-fractured or fake).

### T13 - Level: the cage greybox

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| level-designer | L | Backlog | T10, T5 (started) | - |

- **Context:** the cage is the first version of the vertical slice (DEC-10); its place in the building is open (N8). Clues in the world, no explicit help (DEC-07).
- **Acceptance criteria:**
  - [ ] Level document in `docs/levels/` from the level-doc template.
  - [ ] Greybox with human-scale props, one obstacle with an evident and an inventive solution, one rest point.
  - [ ] Diegetic clues only; supports T5, T7 and T8.

### T14 - Camera prototype

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | M | Backlog | T4 | Camera question (step or continuous swell, DEC-02 follow-up) |

- **Context:** low and close camera scaled by mass (confirmed); collision under furniture, aim mode and comfort options to prototype.
- **Acceptance criteria:**
  - [ ] Camera distance follows the size step or the continuous swell: TODO(question), open after DEC-02.
  - [ ] No clipping in the cage.
  - [ ] Aim mode shows the trajectory; shake can be reduced.

### T15 - Test plan and test passes

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| qa-engineer | M per milestone | Backlog | T5, T7, T8, T13 | - |

- **Context:** gameplay changes need QA before a milestone closes.
- **Acceptance criteria:**
  - [ ] Test plan in `docs/qa/` covering mass, the six verbs, states and reactions, dirt, camera and destruction.
  - [ ] One test pass report per milestone M2 to M4, with bugs filed.

### T16 - Build baseline (Windows)

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| build-engineer | M | Backlog | T3 | - |

- **Context:** no build pipeline is known.
- **Acceptance criteria:**
  - [ ] A packaged Windows build of the cage launches.
  - [ ] The steps are documented in `docs/knowledge/`.

### T17 - External playtest brief

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| human (producer writes the brief) | S | Backlog | T15, T16 | - |

- **Context:** the GDD gate needs 2 testers outside the project (C12), more later.
- **Acceptance criteria:**
  - [ ] External brief in `docs/planning/` with build, tasks, questionnaire (did they discover the rules without help, did digestion tell a story), number of testers and deadline.
  - [ ] Results analysed by the qa-engineer in a playtest report.

### T18 - External brief: final animation, sound and music

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| human (producer writes the brief) | S | Backlog | T6 | - |

- **Context:** the solo team lacks animation and sound; slime animations are a block-out base.
- **Acceptance criteria:**
  - [ ] One external brief per item with deliverables, formats, references (Little Nightmares, Inside tone), budget and deadline.

### T19 - Pre-production gate review

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| producer | S | Backlog | T1, T12, T15, T17 | - |

- **Context:** gate check before the vertical slice (roadmap).
- **Acceptance criteria:**
  - [ ] Checklist reported to the user: core loop fun, top risks resolved (T1, T12), plan approved, GDD contradictions settled. The user decides.

### T20 - Living GDD and open review items

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| game-designer; the user decides | S | In progress | - | - |

- **Context:** the living GDD `docs/design/gdd.md` replaces the original GDD as the current design; the original stays untouched in `docs/reference/`. First version written on 2026-11-13 with DEC-01, DEC-05, DEC-07, DEC-09 and DEC-10 applied. Open items of the consistency review (`docs/design/reviews/gdd-consistency-review.md`) remain.
- **Acceptance criteria:**
  - [ ] Each user decision recorded in a decision record and applied to the living GDD in the same run.
  - [ ] Every open review item closed by a user decision or marked as accepted risk.
  - [ ] Version and title of the original GDD confirmed by the user (C1, Q19).

### T28 - Concept gate review

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| producer | S | Backlog | T6, T20 | DEC-03, DEC-06, DEC-08 |

- **Context:** the project moved back to the concept phase on 2026-11-13 (user). The concept exit gate is in the roadmap.
- **Acceptance criteria:**
  - [ ] Checklist reported to the user: pitch, pillars and audience approved; open design decisions settled; living GDD validated; sheets reviewed.
  - [ ] The user decides whether the project moves to pre-production.

## Slime production tickets (scheduled later)

Do not start before the related decisions are settled and T6 is reviewed. No Blender modelling now. Candidate milestone: M1, after the T1 go or no-go.

### T21 - Slime base mesh (Blender)

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| blender-artist | M | Scheduled later | T6, T27 | N7, step mapping (three of five sheet steps) |

- **Context:** the mesh in `Content/_Volvacslime/Characters/Slime` is a test, not this character: model from the sheets. Dome 80 x 80 x 53 cm, pivot ground-centred, front +X, about 5000 triangles; fixed debris (screw, shard, EXP-07 label) and two floor drips as separate or baked details.
- **Acceptance criteria:**
  - [ ] Modeling proposal (single block or modular, with figures) validated by the user before modeling.
  - [ ] Mesh within 5000 triangles, correct scale and pivot in Unreal.
  - [ ] A test export imports without fixes; asset sheet with budget against actual.
  - [ ] Before the modeling proposal, these points from the 2026-11-14 sheet review are settled and recorded in the asset sheet:
    - Triangle budget scope: the 5000 triangles cover the whole model (shells, eyes, debris, drips) or each shell; the number of nested shells and material slots (estimate: 3 at most).
    - Frozen (faceted) and liquid (flat disk) states: extra meshes, or bones for the flattening plus the state shader for facets and frost (cheaper; decide before T21, not during T22).
    - Fixed debris: label baked into the texture; screw and glass shard as small separate meshes (they float in the jelly).
    - Drips: they hang below the dome base on sheet 1 while the pivot is on the ground; check they do not clip the floor.
    - Stored objects seen through the translucent shells: limit on how many are shown, and sorting and refraction check.
    - Eye reactions (narrowed, angry, closed, sheets 3 and 6) with only eye_L and eye_R bones: by bone scale or by material.
  - Estimates to validate (not measures): body 2500 to 3500 triangles, total 5000 at most, 3 material slots at most.

### T22 - Slime rig and skinning

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| blender-artist | M | Scheduled later | T21 | N7, step mapping (three of five sheet steps) |

- **Context:** root to body_low, body_mid, body_top, eye_L, eye_R; squash and stretch by bones; three size steps (DEC-02) by scale or per-step proportions, plus a slight in-step swell.
- **Acceptance criteria:**
  - [ ] Modeling proposal for the rig and its parts validated by the user before work starts.
  - [ ] The rig deforms without tears in every pose of sheets 5 and 6.
  - [ ] Skeleton naming in the asset sheet; test pose export.

### T23 - Mouth morph target

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| blender-artist | S | Scheduled later | T21 | - |

- **Context:** no mouth at rest; the front face hollows into a funnel with ripples (aspirate, spit). Morph target "opening" driven by animation.
- **Acceptance criteria:**
  - [ ] Modeling proposal validated by the user before work starts.
  - [ ] Morph target imported in Unreal, value 0 to 1 driven from animation.
  - [ ] No artifacts at the angle used by the aspiration cone.

### T24 - Slime material: nested shells and dirt (Substrate)

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| technical-artist | L | Scheduled later | T1, T2, T21 | DEC-03 |

- **Context:** reproduce the Blender Cycles reference (skin, cloudy jelly, dense heart, emissive core) with 2 or 3 nested shells plus thickness absorption; core colour = temperature and intensity = dirt (DEC-09); four coatings; classic-material fallback. Extends T1.
- **Acceptance criteria:**
  - [ ] Material instance with parameters for core colour and intensity, coating, frozen and liquid states.
  - [ ] Frame cost measured against T2; readable in the cage lighting; result recorded in T1.

### T25 - Slime animation set (block-out)

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| blender-artist (block-out); human for final | L | Scheduled later | T22, T23 | DEC-04 (details) |

- **Context:** durations from the character spec (idle, hops, jump, aspirate, engulf, spit, digest, grow and shrink, spit mass, melt and reform, freeze and thaw) and the six reactions; indicative, tuned in game. No vapor animation. The digest animation stays valid since mass is always given.
- **Acceptance criteria:**
  - [ ] Block-out animations imported and playable from a test Animation Blueprint; durations in data.
  - [ ] Final hand-keyed animation, if wanted, goes through T18.

### T26 - Slime state and reaction integration in Unreal

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| unreal-engineer | L | Scheduled later | T24, T25, T7, T4 | N7, step mapping (three of five sheet steps) |

- **Context:** Animation Blueprint, state shader or mesh swap for liquid and frozen, core as a material parameter, reactions layered on other animations, size steps, belly objects displayed. Cohesion shown by core rhythm and softness (DEC-09).
- **Acceptance criteria:**
  - [ ] Test map where temperature, size step and a reaction can be triggered by debug commands.
  - [ ] No UI used; matches the T7 state model; covered by the T15 test plan.

### T27 - Cage and scale check for the slime

| Owner | Size | Status | Depends on | Waits for decision |
|---|---|---|---|---|
| level-designer | S | Scheduled later | T13 | - |

- **Context:** D4 and N7: 80 cm engine size, steps x0.5 to x2.5 (three kept for the slice, DEC-02; this check feeds their values), against the cage, doors, tubes and grids.
- **Acceptance criteria:**
  - [ ] Written check with the measured cage dimensions against each size step and narrow passage.
  - [ ] Recommendation reported to the user; no asset change.

## GitHub setup (to create after approval)

- **Labels:** `role:design`, `role:level`, `role:unreal`, `role:build`, `role:art`, `role:techart`, `role:qa`, `role:docs`, `role:marketing`, `owner:human`, `idea`, `bug`, `severity:blocker`, `severity:major`, `severity:minor`, `size:S`, `size:M`, `size:L`, `prio:1`, `prio:2`, `prio:3`, `blocked`, `needs-design`.
- **Milestones:** `M0 Foundations lock`, `M1 Slime and mass`, `M2 Aspirate keep taste digest`, `M3 States and reactions`, `M4 Cage vertical slice and playtest` (dates TODO).
- Existing issues, milestones and PRs were not read: duplicates not checked.
