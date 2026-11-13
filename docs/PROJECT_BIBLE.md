# Volvacslime - Project bible

| Field | Value |
|---|---|
| Status | Draft |
| Owner | producer |
| Last updated | 2026-11-13 |
| Source of truth for | Phase, pitch, pillars, audience, platform, team, budgets, conventions and open project questions |
| Related | [Documentation index](README.md), [decision log](design/decisions/README.md), [GDD](design/gdd.md), [roadmap](planning/roadmap.md) |

**Summary.** Volvacslime is a solo, PC, third-person puzzle game in the concept phase: a lab slime aspirates, tastes and digests matter to change size, state and properties. The GDD v0.3 is a base, not validated design; this bible wins over every other document.

Content tags: **confirmed** (validated by the user), **proposed** (to decide), **to prototype** (accepted as a starting point, to prove; may change). Unknowns are marked `TODO(question)`.

## Phase

**Concept (confirmed, user 2026-11-13).** The goal of this phase is to know what the game is: the project is validating ideas, and no game feature is developed yet. Everything in the Unreal project today (aspiration components, Chaos stone, test slime mesh, level design test, first cage) is an idea test, not production content. Such tests are disposable and labeled as such. Exit gate and milestones: [roadmap](planning/roadmap.md).

| Done (confirmed) | Remaining in concept |
|---|---|
| GDD foundations: premise, verbs, pillars 1 to 4 | Approve the pitch, pillar 5 and the audience (all proposed) |
| Temperature model, tone, no explicit help, body signals, World Partition, size model ([decision log](design/decisions/README.md)) | Settle the open decisions: dirt and robots, duration and cuts, interface, digestion details |
| Slime art direction "Specimen", materials validated in a Blender test | Validate the living [GDD](design/gdd.md) and close the open review items (T20) |
| Slime sheets v1, a base to modify ([character spec](design/slime-character.md)) | Review the sheets against the decisions (T6) |
| Idea tests in Unreal (aspiration, Chaos stone, first cage) | Concept gate review (T28), then the user decides to move to pre-production |

Next phase, pre-production (not started): prototype mass, the six verbs, states and dirt; build the cage greybox, first version of the vertical slice ([DEC-10](design/decisions/DEC-10-cage-and-phases.md)); then model the main character from the sheets (T21 to T27).

## Pitch (proposed)

"A lab slime, abandoned after an incident, aspirates, tastes and digests the matter around it to change size, state and properties, and finds by itself how to escape, or to understand where it comes from."

Chaos destruction is a means, not the core. The core is experimentation on matter: states and temperature, mass as a resource, taste and digestion as access to lore, a sandbox without explicit help. The GDD pitch ("swallowing, mixing and throwing matter to find the exit") is superseded if the user approves (C2).

## Pillars

Any idea that serves none of the pillars is rejected or parked.

| # | Pillar | Status |
|---|---|---|
| 1 | The body is the dashboard: size, state, dirt and core glow replace the UI | confirmed (wording differs from the GDD, C4) |
| 2 | Matter responds: properties react by rules in data, not by scripts | confirmed |
| 3 | Understand by digesting: lore and progression through taste and digestion, not notes to collect | confirmed |
| 4 | Free to experiment: no explicit help, clues in the world, several solutions per obstacle | confirmed ([DEC-07](design/decisions/DEC-07-no-explicit-help.md)) |
| 5 | An abandoned place that tells a story: decayed lab, traces of the incident, wordless story | proposed |

## Audience and tone

- Tone: unsettling and poetic world, attaching but not cute creature ([DEC-05](design/decisions/DEC-05-tone.md)).
- Age: 12+ (PEGI 12 targeted), no violence or gore. Proposed.
- Players: confirmed or curious players. Proposed.
- References (proposed): Grounded (scale), Luigi's Mansion (building as puzzle, suction), Little Nightmares and Inside (small character, hostile place, no UI), Kirby (swallow and absorb, mechanics only). The GDD also lists "Moi quand je me réincarne en slime"; merging the lists is open (C14).

## Platform

- PC only (confirmed), Windows as the single target (proposed). No console. Solo, 3D, Unreal Engine 5.8.
- Graphics recommendations, not applied (ticket T3): keep Lumen, disable hardware ray tracing, keep Substrate pending the slime material test (T1), disable the ChaosVehicles plugin (Chaos physics and Geometry Collection stay).

## Team, schedule and budgets

| Topic | Value |
|---|---|
| Team | One person, Blueprint and C++; missing 2D and 3D art, animation, sound (GDD). Academic "fil rouge" project. Who makes final art and sound: TODO(question) Q5 |
| Deadlines | TODO(question) Q6. The GDD sets no durations |
| Budgets | Frame time, memory, triangles, texture size, build size: TODO(question) Q7 (ticket T2) |
| Duration | Proposal 3 to 4 hours ([DEC-06](design/decisions/DEC-06-duration-and-cuts.md)) |

## Documentation

- The repository is the source of truth; the map, ownership and writing rules are in the [documentation index](README.md).
- The current design of the whole game is the living [GDD](design/gdd.md), kept up to date by the game-designer with every decision; the original GDD stays in `docs/reference/`.
- Notion is a copy the user imports by hand from `exports/notion/`, built by `Scripts/export_notion.py`. Agents never write to Notion (user, 2026-11-12; closes Q9).
- Everything in the repository is in English, except the user material in `docs/reference/` (user, 2026-11-12).

## Conventions (proposed, not yet approved)

- All project content under `Content/_Volvacslime/`; numbered core folder `00_Core`. Numbering of other folders: TODO(question) Q8.
- Prefixes in use: `BP_` Blueprint actor, `BPC_` Blueprint component, `BPI_` Blueprint interface, `IA_` input action, `IMC_` input mapping context, `Lvl_` level.
- Prefixes to add: `M_` and `MI_` materials, `SM_` static meshes, `T_` textures, `WBP_` widgets, `ABP_` animation Blueprints, `DT_` data tables, `DA_` data assets.
- Folders by function: `Components`, `Interfaces`, `Blueprints/<Category>`, `Level`. Folders owned by other studio roles (Maps, Materials, VFX): rename `Level` or map it to `Maps`? TODO(question).
- Commits: `type(scope): subject`, as in the history. Branches: the studio suggests `feature/<issue>-<slug>`; the current branch `feature-chaosBuilding` differs. TODO(question).
- The repository state is described in [the repository page](knowledge/repository-overview.md).

## Open questions

Design questions are tracked as decisions in the [decision log](design/decisions/README.md); review items (C, D, N, G) in the [consistency review](design/reviews/gdd-consistency-review.md). Project questions:

| # | Question | Status |
|---|---|---|
| Q5 | Team and roles: who is human, which agents are used, who makes final art, animation and sound? | Open |
| Q6 | Deadlines: school milestones, jury, final delivery | Open |
| Q7 | Budgets and minimum hardware | Open (T2) |
| Q8 | Art direction conventions and naming: "Specimen" look rules, folder and asset naming | Open |
| Q10 | Git LFS for `.uasset`, `.umap`, `.blend` and textures? (the GDD requires versioning from day one) | Open (T11) |
| Q11 | Uncommitted changes in `Config/DefaultEngine.ini`, `Config/DefaultGame.ini` and `Volvacslime.uproject`: what are they, and who commits them? | Open (T11) |
| Q17 | "Build": assembly by sticking and freezing, or base customization? | Open (DEC-06) |
| Q18 | Does the slime speak, make sounds or stay mute; does the creator appear on screen? | Open (G9) |
| Q19 | Title "Volvacslime" confirmed? GDD version number and revision history to fix | Open (C1) |

Closed here: Q9 (see Documentation), Q21 (the slime mesh in `Characters/Slime` is a test, see Phase). Moved to the decision log: Q12 (DEC-05), Q13 (DEC-06), Q14 (DEC-07), Q15 (DEC-08), Q16 (DEC-09), Q20 (DEC-10).
