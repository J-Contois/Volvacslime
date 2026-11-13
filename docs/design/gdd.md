# Volvacslime - Game design document

| Field | Value |
|---|---|
| Status | Draft (living document) |
| Owner | game-designer (the user decides every design choice) |
| Last updated | 2026-11-13 |
| Source of truth for | The current design of the whole game, with every decided choice applied |
| Related | [Bible](../PROJECT_BIBLE.md) (pitch, pillars, scope), [decision log](decisions/README.md), [slime character](slime-character.md), [consistency review](reviews/gdd-consistency-review.md), [original GDD v0.3](../reference/GDD_source_v0.3.txt) |

**Summary.** A slime abandoned in a manor turned lab experiments on matter with six verbs to escape, or to understand where it comes from. Mass is its single resource, temperature changes its state, and digesting objects reveals the story. This document is the user's GDD v0.3 with every decided choice applied (see the decision log); everything else is still a proposal or to prototype. The project is in the concept phase.

How to read: every rule carries a tag, **confirmed** (validated by the user), **proposed** (to decide) or **to prototype** (a starting point to prove), and cites its source: a decision (DEC-NN), a review item (C, D, N, G) or a line of the original GDD (GDD l.N). Details live in the decision records and, later, the design briefs; this document summarizes and links them. It is updated in the same run as any decision or brief that changes the design.

## 1. Vision

Pitch and pillars: see the [bible](../PROJECT_BIBLE.md#pitch-proposed). Tone: unsettling and poetic world, attaching but not cute creature ([DEC-05](decisions/DEC-05-tone.md)).

### Premise (confirmed)
After a catastrophe and the immediate abandonment by its creator, a slime is alone in a human-scale building. Doors, handles and furniture are huge for it. The slime is an unregistered prototype: it was not on the evacuation list, and its creator left without it.

### The catastrophe (proposed)
The basement pumping and cooling system failed. The building locked itself (confinement protocol) and the staff evacuated in a hurry. The place is a lab installed in an old manor: converted domestic rooms mixed with technical installations (pumps, boiler room, server room).

### Consequences in the world (proposed)
Every element of the set comes from the catastrophe. The water level is a world state the player can change; it never rises by itself and there is no global countdown.

| What the player sees | Why |
|---|---|
| Locked doors | The confinement protocol cuts access until it is lifted |
| A flooded basement | Pumps stopped and groundwater filled it; valves and pumps change a zone's water level both ways |
| Zones too hot | Machines (boiler room, servers) heat without cooling |
| Zones too cold | A cooling circuit stayed on or broke |
| Electric currents, conductive water | Damaged cables in a flooded basement |
| Emergency lights, dripping, a fading hum | Backup power, pumps stopped |

### Player goal (confirmed)
Explore the building; every object the slime swallows is at once a tool, a clue and a memory. The end goal is to escape, or to understand where the slime comes from.

## 2. Core gameplay

### Verbs (to prototype)

| Verb | Behaviour | Design rules |
|---|---|---|
| Aspirate | Hold to pull objects from a cone in front of the slime; absorbed if smaller than the free belly mass | Size and weight limit what can be aspirated; a too-heavy object can be pulled or dragged; a fixed object resists |
| Keep | Store an object in the belly; kept objects float, visible through the body | Belly capacity depends on mass |
| Taste | Reveal an object's properties without destroying it | Output format open: the sheets show a binary like or reject (N2, G4) |
| Digest | Destroy a kept object for mass plus at most one bonus ([DEC-04](decisions/DEC-04-digestion-output.md)) | Takes time, cannot be cancelled, some objects are toxic |
| Spit | Release a kept object in a jet with adjustable force; it keeps its properties | Damage by mass, speed and material (glass, metal, ice) |
| Throw | Launch an object with a visible trajectory, slower but more precise than spitting | Reach switches, break windows, draw attention |

Aspirate, spit and throw must be precise, fast and satisfying before any other system (GDD l.252). Which verbs are "core" is open (C3). Spitting mass at will as an anti-softlock is proposed by the sheets and may merge with "split" (N5).

### Core systems (to prototype)

| System | Principle |
|---|---|
| Mass and cohesion | Mass is the single resource: life, size, belly capacity and strength. Cohesion is effort energy, spent by acting and recovered at rest (keeping it as a second resource is open, C7) |
| Keep, taste, digest | Keep stores, taste reveals, digest destroys for mass plus at most one bonus ([DEC-04](decisions/DEC-04-digestion-output.md)) |
| Objects and substances | Solids are aspirated, thrown and placed; liquids and powders are stored in reserve, spat and mixed |
| States of matter | Four states by temperature: frozen, gelatinous (normal), hot liquid, burning; automatic return to gelatinous ([DEC-01](decisions/DEC-01-temperature-states.md)) |
| Reactions between properties | Each object carries properties; rules stored in data make them react, for example cold + humid gives gel |

### Physics and chaos (confirmed as a means)
Chaos physics gives objects weight, bounce, breakage and stacking. Destruction is a means, never the goal (C8):
- breaking an object reveals its contents or makes it usable (a broken window opens a path, a crate gives its contents);
- a heavy object can weigh down a switch, or serve as a bridge or barricade;
- some fragile objects are the only way to carry a liquid or a dangerous product;
- destroying too much has a cost (noise, collapse, lost resources), so chaos stays a choice (costs to prototype).

### Readability (confirmed)
The player reads an object's material by eye (shiny metal, translucent ice, wood, paper) and can guess what will happen before trying.

## 3. Camera and controls

Low and close camera that adapts to the slime's mass (confirmed): the player must see the body shrink, grow, freeze or spread. Rules, all to prototype:
- **Distance by mass:** the bigger the slime, the further the camera and the wider the field of view (size model: [DEC-02](decisions/DEC-02-size-model.md); whether the camera follows the step or the swell is TODO(question), T14).
- **Collision:** the camera moves in under furniture, in a duct or a keyhole, then goes very close (almost first person) in tiny passages.
- **Aim mode:** a held input moves the camera over the shoulder with a reticle, for precise aspiration or throws, and shows the trajectory. The reticle appears only in aim mode (proposed, [DEC-08](decisions/DEC-08-interface-elements.md)).
- **Comfort:** slight camera lag, adjustable impact shake, option to reduce it.

Controls: input actions exist for aspirate, interact, jump, move and look ([repository](../knowledge/repository-overview.md)). The full scheme (keyboard and mouse, gamepad on PC) is open (G6).

## 4. Game loops

Three nested loops, each fun on its own (to prototype).

**30 seconds, try something**
1. Spot an interesting object (readable: shiny metal, ice cube, puddle, glue).
2. Aspirate it. Whether aspirating already gives its property, or only digesting does, is open (N6; proposal in [DEC-04](decisions/DEC-04-digestion-output.md): only digesting).
3. Use it: spit, throw, drop, or combine it with another property in the belly.
4. Watch the world react (breaks, conducts, freezes, sticks, burns) and draw a conclusion.

**One room, 5 to 15 minutes**
1. Arrive and spot the obstacle (locked door, cut circuit, passage too narrow).
2. Search for resources and learn the local rules (temperature, danger).
3. Experiment until one solution works; every room has several, one evident and one inventive.
4. Reward: a new zone or shortcut, a rare property, a memory fragment.

**A session, several hours**
1. Survive: mass drops slowly (hunger, damage), which pushes forward without punishing exploration (tension with "no pressure" to tune, C9).
2. Return to a rest point to save, digest and rebuild.
3. Open new biomes with properties brought from previous ones.
4. Assemble the lore and choose an ending.

## 5. Character

Look, sizes, animations and rig: see the [character spec](slime-character.md).

### Mass (to prototype)

| Role | Effect of mass | Trade-off |
|---|---|---|
| Life | Damage removes mass; the slime visibly shrinks | Small: fragile but goes everywhere |
| Hunger | Mass drops slowly; organic matter and some liquids restore it, toxic matter reduces it | Eating pushes exploration, not waiting |
| Inventory | Belly capacity depends on mass | Big: stores more but no longer fits small passages |
| Size and strength | More mass, more force to move objects | Heavier: slower and louder |

At minimum mass only a small drop remains, which rebuilds at a rest point: a soft game over without loss of progress. Whether drinking water is a mass source, and the unlimited water of the flooded basement, are open (D8).

### Size model (decided, [DEC-02](decisions/DEC-02-size-model.md); step values to prototype)
Mass is continuous; the body size follows it in two layers:
- **Swell:** mass drives a slight visible swell of the body inside the current step, so hunger and small damage stay readable.
- **Steps:** the size that decides what fits (openings, belly volume class, objects pushed) changes only when mass crosses a threshold, with hysteresis so the slime does not flip between steps near a threshold.
- **No room, no growth:** a step increase is refused when there is no space; the slime stays in its current step and the player gets "too tight" feedback.
- **Slice:** three steps (small, normal, large). The five sheet steps (x0.5 to x2.5, [character spec](slime-character.md)) stay values to tune later.

Step values, thresholds, hysteresis and swell amplitude are to prototype after the cage measurement (T27) and the x10 world scale question (N7).

### States (decided, [DEC-01](decisions/DEC-01-temperature-states.md); behaviour to prototype)

| State | Condition | Abilities | Weaknesses |
|---|---|---|---|
| Frozen | Fridge, cold room, ice | Hard: breaks glass, serves as a projectile, supports weight | Slow, cannot squeeze through |
| Gelatinous (normal) | Ambient temperature | Base state; objects visible in the belly | Does not pass grids (N1, to confirm) |
| Hot liquid | First hot threshold | Puddle, passes grids and under doors | Fragile |
| Burning | Second hot threshold | None: a danger state | Evaporates and loses mass |

The transition is progressive over a few seconds and the player can trigger it on purpose: freeze to break a window, then heat up to pass under a door. The slime returns to gelatinous by itself so it never stays stuck. Thresholds and times: parameters in [DEC-01](decisions/DEC-01-temperature-states.md).

### Body signals (decided, [DEC-09](decisions/DEC-09-body-signals.md))
No gauge on screen: the body is the dashboard. Core colour = temperature, core intensity = dirt, size = mass, core rhythm and jelly softness = cohesion.

### Dirt (partly decided, [DEC-03](decisions/DEC-03-dirt-and-robots.md))
A coating on the body (clean, dust, soot, mud) that dims the core. Dirt does not reduce suction. Mud's heat insulation and stealth uses are to confirm.

## 6. Mechanics and systems

All systems plug into mass and temperature, so the player reads the slime's state without a menu.

| System | How it works | How it reads |
|---|---|---|
| Life | Falls, crushing, acid, fire and brittle frost remove mass | Body size; no health bar |
| Hunger | Mass drops slowly; organic matter and some liquids restore it; toxic matter reduces it | Body size ([DEC-09](decisions/DEC-09-body-signals.md) drops the GDD's "duller and flatter") |
| Cohesion | Jumping, long aspiration and strong throws spend it; at zero the slime spreads, slows and jumps little; it comes back at rest | Core rhythm and softness; no reticle gauge (proposed, [DEC-08](decisions/DEC-08-interface-elements.md)) |
| Temperature | Each zone has an ambient temperature and each object its own; the slime exchanges heat by contact and changes state at thresholds | Core colour, body shape, frost or vapour |
| Inventory | The belly is a volume limited by mass; objects float in it, visible through the body | Objects in the body; scroll to choose, no wheel by default (proposed, [DEC-08](decisions/DEC-08-interface-elements.md)) |

Per-system design briefs will be written in `docs/design/briefs/` (ticket T10) and linked here.

### Properties and crafting (proposed)
Each object carries one or more properties: hot, cold, humid, conductive, sticky (user list), plus flammable, magnetic, acid, heavy, fragile (GDD). Crafting combines two objects or properties in the belly. The rule matters, not the catalogue: recipes are discovered by experiment and recorded in a notebook (pause menu, proposed in [DEC-08](decisions/DEC-08-interface-elements.md)).

| Combination | Result | Use |
|---|---|---|
| Water + salt | Conductive liquid | Close a circuit, power a socket |
| Glue + paper | Sticky pad | Fix an object to a ceiling or a wall |
| Ice + metal | Cold, hard projectile | Break a window or a lock |
| Alcohol + spark | Flammable substance (danger) | Burn an obstacle, at the risk of losing mass |

Whether digesting gives a temporary property is part of [DEC-04](decisions/DEC-04-digestion-output.md) (parked for the vertical slice).

### Mutations (proposed, cut candidate)
Permanent abilities gained by digesting a rare object (a magnet gives magnetism, a spring a super jump, a suction cup ceiling grip). Each mutation takes belly space, so the player chooses which to keep. Second in the proposed cut order ([DEC-06](decisions/DEC-06-duration-and-cuts.md)).

### Build (proposed, cut candidate)
Building by assembly: stick and freeze objects into stairs, bridges, crate towers or dams, with no build menu. First in the proposed cut order: sticking and freezing would stay as reactions only ([DEC-06](decisions/DEC-06-duration-and-cuts.md), Q17).

### Save (proposed)
Automatic save at each room change, manual save at rest points. Saved: the player's state (mass, inventory, mutations, recipes, memories) and the key world objects; debris positions are not kept.

## 7. World and levels

The building is an abandoned manor lab where each zone is a biome with its own temperature, resources, rules and dangers, travelled metroidvania-style: shortcuts and doors that open with properties brought from elsewhere (proposed).

| Biome | Temperature | Resources | Dangers | Role in progression |
|---|---|---|---|---|
| Hall and offices (start) | Ambient | Paper, light objects, basic food | Falls, falling objects | Learn aspirate, throw, break |
| Kitchen | Hot | Food, water, alcohol, utensils | Fire, steam, oil | First food; hot states |
| Cold room | Very cold | Ice, meat, tubs | Slowing frost | Learn the frozen state |
| Greenhouse | Humid, warm | Plants, soil, water | Blocking vegetation, spores | Organic and toxic matter |
| Flooded basement | Cool | Water, rust, metal | Currents, electricity in water | Conduction, floating objects |
| Server room | Hot | Metal, cables, components | Discharges, overheating | Electricity, technical mutations |
| Creator's lab | Variable | Samples, files, memories | Security systems | Heart of the lore, access to the endings |

The proposed cut keeps 3 or 4 biomes, one state of matter each ([DEC-06](decisions/DEC-06-duration-and-cuts.md)).

**First level: the cage** ([DEC-10](decisions/DEC-10-cage-and-phases.md), decided). The cage is the first version of the vertical slice; rooms of the real building come after it. Its place in the building is open (N8).

**Level design principles (proposed)**
- **One biome, one idea:** each zone teaches one rule of matter before combining it with others.
- **Loops and shortcuts:** the hall is the hub the player often returns to; a shortcut opened by a hard room rewards the effort.
- **Human scale:** furniture, doors and handles are huge for the slime, which builds the mood and the secret paths (under doors, in ducts). The world is built at x10 in engine; its technical effects are open (D4, N7).
- **Rest zones:** one rest point per biome, visually marked, with a little food nearby.

Level documents will live in `docs/levels/` and be linked here.

## 8. Puzzles

Puzzles are systemic: the game simulates rules instead of checking one solution, and several paths lead to the same result.

**Principles**
- **One obstacle, at least two solutions:** an evident one (found in about five minutes) and an inventive one that rewards experimentation.
- **Teach before combining:** a safe room shows that a frozen object breaks glass before another room makes a passage depend on it.
- **No explicit help** ([DEC-07](decisions/DEC-07-no-explicit-help.md), decided): no tutorial text, markers, help button or highlighting; clues in the world (frost traces, burnt cables, labels, the creator's diagrams).
- **No dead end:** the player can always return to a rest point or get an emergency resource.

**Slime-specific puzzle mechanics (proposed)**

| Mechanic | Principle | Example |
|---|---|---|
| Split | Leave a piece of oneself as a weight, bait or relay | A fragment holds a switch while the body goes through the open door |
| Squeeze | Pass through locks, grids, pipes and sockets, with a camera change; grids need the hot liquid state (N1) | Go through a keyhole to work the mechanism on the other side |
| Change state | Freeze or heat to change abilities (no evaporation, [DEC-01](decisions/DEC-01-temperature-states.md)) | Freeze to break a window, heat up to slip under the door |
| Chain reaction | Combine the world's properties | Water + electricity, fire + paper, cold + glass |
| Directed chaos | Destroy smartly to open a path | Knock a shelf over to make a bridge |

**Examples by biome**
- **Kitchen:** a service door has a thermal lock; heat a metal object on the stove and spit it at the lock.
- **Cold room:** an ice bridge is missing; fill a tub with water, push it into the cold room and wait for it to freeze.
- **Flooded basement:** an electrical compartment is out of reach; a conduction chain (water + salt + cable) opens a door remotely.
- **Server room:** overheating disables an alarm; opening it noisily or switching it off with cold are two different paths.

## 9. Narrative, lore and endings

The lore goes through the core mechanic: digesting an object brings back a memory fragment. The player does not read notes; they taste the building's history (pillar 3).

**Premise of the lore (proposed).** The slime is a prototype of "memory matter", a substance that keeps what it absorbs. Its creator abandoned it after the catastrophe, either believing it lost or wanting it gone. If the slime remembers what it digests, digesting becomes an investigation.

**Memory fragments (proposed; 1 to 3 in the vertical slice, [DEC-04](decisions/DEC-04-digestion-output.md))**

| Object type | Fragment revealed |
|---|---|
| Photo, frame | A short, silent scene from the past, seen from the room |
| Badge, access card | A name, a role, access to a zone |
| Notebook, file | One sentence or diagram from the creator, never a long text |
| Recording, audio device | A few seconds of voice |
| Sample, lab subject | Information on the project and on other subjects |

Fragments are sorted by theme in an archive (the creator, the project, the catastrophe, the other subjects, the slime itself); the player rebuilds the story in any order. The archive is an off-game pause-menu screen (proposed, [DEC-08](decisions/DEC-08-interface-elements.md)). Fragment format: open in [DEC-04](decisions/DEC-04-digestion-output.md).

**Endings (proposed; the cut keeps 1 or 2, [DEC-06](decisions/DEC-06-duration-and-cuts.md))**

| Ending | Indicative condition | Idea |
|---|---|---|
| Escape | Reach the exit with few fragments | Freedom without answers |
| Stay | Stay in the building after understanding everything | Choosing one's home |
| Find the creator | Enough fragments and the creator's trail | Confrontation, forgiveness or rejection |
| Take their place | All mutations and the full archive | The slime becomes what it was made to replace |

Exact conditions are set with the story (G11). Whether the slime speaks or makes sounds, and whether the creator appears on screen, are open (Q18).

## 10. Technical direction

Summary of the GDD's proposals; technical specs in `docs/specs/` will be the source. One Unreal component per slime function and one subsystem that applies the reactions; all content (properties, recipes, mutations, fragments) defined in data, not code (proposed).

| Need | Proposed Unreal approach | Note |
|---|---|---|
| Physics and destruction | Chaos Physics; Geometry Collection for breakables | Limit active fragments and their lifetime (T12) |
| Aspiration | Cone detection, physical force toward the mouth, absorbed on arrival | Blueprint prototype first; current implementation differs (C17) |
| Slime body | Simple mesh scaled by mass first (swell inside a step, steps at thresholds, [DEC-02](decisions/DEC-02-size-model.md)); soft body by material and Niagara drips later | Slime material test (T1) |
| Movement | Character Movement Component tuned by mass | Other systems only if needed |
| Properties and reactions | Gameplay Tags, Data Assets, world subsystem; "A + B gives C" rules in a Data Table | |
| Mutations | Simple components; Gameplay Ability System only beyond about five | |
| Temperature | Per-actor value plus zone volumes | No global heat simulation |
| Input | Enhanced Input, with key remapping | |
| Save | SaveGame; key objects found by Gameplay Tags | Autosave at each room change |
| Levels | World Partition (decided, [DEC-11](decisions/DEC-11-world-partition.md)) | Cells and data layers per room: technical spec to write |

Details specific to Unreal Engine 5.8 must be checked against Epic's documentation before committing.

## 11. Scope and cut list

- **Duration:** proposed ceiling of 3 to 4 hours ([DEC-06](decisions/DEC-06-duration-and-cuts.md), to confirm).
- **Cut order** (first cut first): build system, mutations, combat and robots, endings down to 1 or 2, biomes down to 3 or 4; split merged with spit mass. Kept: verbs, mass, states, data-driven reactions, digestion into fragments.
- **Optional content:** the game must be complete without it. Combat stays minimal and property-based (freeze, stick, electrocute), never an enemy health bar. Enemies would be few and readable (security robots, pests, escaped samples); robots are proposed out of the vertical slice ([DEC-03](decisions/DEC-03-dirt-and-robots.md)).
- **Phases:** the project is in the concept phase; the first GDD phase maps to pre-production. Both gates are in the [roadmap](../planning/roadmap.md).

## 12. Open design questions

- Decisions waiting for the user: [DEC-03](decisions/DEC-03-dirt-and-robots.md) dirt and robots, [DEC-06](decisions/DEC-06-duration-and-cuts.md) duration and cuts, [DEC-08](decisions/DEC-08-interface-elements.md) interface, plus the details of [DEC-04](decisions/DEC-04-digestion-output.md) and the "Look" reaction rule of [DEC-07](decisions/DEC-07-no-explicit-help.md).
- Review items still open: see the [consistency review](reviews/gdd-consistency-review.md) (notably C3 verbs, C7 cohesion, C9 hunger, D8 water as mass, N6 property from aspirating, G4 taste, G12 threats and failure states).
- Project questions (Q5 to Q19): see the [bible](../PROJECT_BIBLE.md#open-questions).

## Glossary

| Term | Meaning |
|---|---|
| Biome | A zone of the building with its own temperature, resources, rules and dangers |
| Coating | The dirt on the slime's body: clean, dust, soot or mud |
| Cohesion | Effort energy, read from the core rhythm and the jelly softness |
| Core | The emissive heart of the slime; colour = temperature, intensity = dirt |
| Fragment | A memory revealed by digesting a story object |
| Mass | The single resource: life, hunger, belly capacity, size and strength |
| Property | A tag on an object (hot, cold, humid, conductive, sticky, ...) that reacts by data rules |
| Rest point | Where the slime saves, digests and rebuilds after a soft game over |
| Substance | A liquid or powder, stored in reserve, spat and mixed |

## Changes from the original GDD

| Change | Cause |
|---|---|
| Pitch replaced by the user's pitch (aspirate, taste, digest; escape or understand origins) | Bible, proposed (C2) |
| Six verbs (aspirate, keep, taste, digest, spit, throw) instead of three | Bible glossary, core verbs open (C3) |
| Pillar 1 reads "the body is the dashboard"; pillar 4 "free to experiment" added | Bible (C4), [DEC-07](decisions/DEC-07-no-explicit-help.md) |
| Four states (frozen, gelatinous, hot liquid, burning) instead of liquid, frozen, vapor; vapor and vent flight removed; only hot liquid passes grids | [DEC-01](decisions/DEC-01-temperature-states.md) |
| Body signals defined; hunger no longer makes the body dull | [DEC-09](decisions/DEC-09-body-signals.md) |
| Dirt added as a coating, without suction penalty | [DEC-03](decisions/DEC-03-dirt-and-robots.md) (partly decided) |
| Size follows mass in two layers: continuous swell inside a step, three size steps in the slice that decide what fits, hysteresis, growth refused without room (the GDD assumed continuous scaling; the sheets showed five steps) | [DEC-02](decisions/DEC-02-size-model.md) |
| Digestion gives mass plus at most one bonus | [DEC-04](decisions/DEC-04-digestion-output.md) (agreed in principle) |
| Tone set: unsettling and poetic, not cute | [DEC-05](decisions/DEC-05-tone.md) |
| No explicit help; clues in the world only | [DEC-07](decisions/DEC-07-no-explicit-help.md) |
| The cage is the first level and first version of the vertical slice | [DEC-10](decisions/DEC-10-cage-and-phases.md) |
| World Partition instead of one persistent level with per-room sublevels | [DEC-11](decisions/DEC-11-world-partition.md) |
| GDD open questions on tone, platform and duration answered or moved to decisions | Bible, [DEC-05](decisions/DEC-05-tone.md), [DEC-06](decisions/DEC-06-duration-and-cuts.md) |
