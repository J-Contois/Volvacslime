# GDD v0.3 and slime sheets v1 - Consistency review

| Field | Value |
|---|---|
| Status | In review |
| Owner | game-designer (the user decides each item) |
| Last updated | 2026-11-13 |
| Source of truth for | Contradictions (C), sheet discrepancies (D), other discrepancies (N) and gaps (G) between the GDD, the slime sheets and the user's answers |
| Related | [GDD source](../../reference/GDD_source_v0.3.txt), [slime sheets](../../reference/slime_sheets/), [decision log](../decisions/README.md), ticket T20 |

**Summary.** The GDD v0.3, the six slime sheets and the user's answers of 2026-11-10 disagree on 17 points (C), the sheets add 12 discrepancies (D) and 11 more were found on verification (N); 13 topics are missing (G). Items are closed only by a user decision, recorded in the decision log.

References: "GDD l.N" is a line of `GDD_source_v0.3.txt`; "P1" to "P6" are sheets 1 to 6. Verdicts on D items: **Confirmed** (exists as described), **Nuanced** (exists but described imprecisely), **Partly wrong** (the description contradicts the source).

## Contradictions (C)

Between the GDD and the user's answers, or inside the GDD.

| Id | Topic | Detail | Suggested handling | Status |
|---|---|---|---|---|
| C1 | GDD version | Cover says 0.1, history stops at 0.2, file is named v0.3 | User fixes version and history | Open (Q19) |
| C2 | Pitch | GDD: swallow, mix, throw to find the exit; user: aspirate, taste, digest, escape or understand origins | Adopt the user pitch and update the GDD | Open (T20) |
| C3 | Verbs | GDD names 3 base verbs but its tables add Digest, Keep and Taste | Unify as aspirate, keep, taste, digest, spit, throw; decide which are core | Open (T10) |
| C4 | Pillar 1 wording | GDD "the body is the resource"; user "the body is the dashboard" (size, state, dirt, core glow) | Keep the user wording | Open |
| C5 | Pillar 4 and world clues | Clues versus "no hints" | Clues in the world, no explicit help | Closed by DEC-07 |
| C6 | "No UI" versus GDD UI | GDD has a belly wheel, reticle gauge, recipe notebook and archive | Decide which are allowed or diegetic | Covered by DEC-08 |
| C7 | One resource versus several | "One number replaces four gauges", yet cohesion is a second resource | Keep or merge cohesion in prototype | Open (T4) |
| C8 | Chaos role | GDD gives Chaos a central role; user says it is only a means | Keep Chaos as a means; no "destroy" in the pitch | Open |
| C9 | Hunger versus no pressure | Mass drops "to push forward", yet exploration is not punished and there is no countdown | Tune in prototype; decide if hunger stays | Open (T4) |
| C10 | Frozen state | Frozen is slow and rigid, puzzles rely on freezing, and auto-return may fight them | Prototype state timing | Open (T7) |
| C11 | Phases | GDD roadmap: 5 phases, 4 gates; studio: 7 phases; only the first GDD phase is detailed | Map GDD phases to studio phases | Partly covered by DEC-10 |
| C12 | Playtest size | GDD gate: 2 outside testers; earlier backlog assumed 5+ | 2 for the first gate, more later | Open (proposed) |
| C13 | Team | GDD: one person without art, animation, sound; user: slime art and materials validated in Blender | Confirm who made the art and who makes the rest | Open (Q5) |
| C14 | References | GDD and user references differ (Grounded, Little Nightmares, Inside added) | Merge the list | Open |
| C15 | Tone | Cute or unsettling | Unsettling and poetic, attaching not cute | Closed by DEC-05 |
| C16 | Scope | Seven biomes, mutations, build, split, four endings, save, combat for a solo academic project | Cage-first slice and a cut list | Covered by DEC-06, DEC-10 |
| C17 | Existing implementation | Repo aspiration uses a collision channel; GDD asks cone detection, belly volume by mass, six verbs | Review in the aspiration prototype | Open (T5) |

## Sheet discrepancies (D)

| Id | Topic | Verdict | Finding | References | Status |
|---|---|---|---|---|---|
| D1 | Temperature states | Confirmed | GDD: liquid, frozen, vapor; sheets: frozen, gelatinous, liquid (first hot threshold), burning (second threshold) | GDD l.163, l.234-249; P1, P3 | Closed by DEC-01 |
| D2 | Vapor versus burning | Nuanced | The gap is vapor versus burning, not frozen versus mass loss: GDD and sheets agree on mass loss; the sheets just omit floating. Merged into D1 | GDD l.246-249; P3 | Closed by DEC-01 |
| D3 | Size steps | Nuanced | The GDD never says "continuous", but its rules assume it (slow mass loss, visible shrinking, object versus free belly mass); with steps, slow loss is invisible | GDD l.210, l.221, l.224, l.258, l.463, l.497; P3, P6 | Closed by DEC-02 (hybrid: continuous mass with a visible swell, 3 steps in the slice; step values to prototype) |
| D4 | Engine size and world scale | Nuanced | Per P1 the world is built at x10, so 200 cm in engine is 20 cm "story size", still small. The real question is technical: x10 affects gravity and jumps, Chaos masses, Character Movement, shadow distances and Lumen, and human-scale assets (Mannequin). Cage not measured yet. DEC-02 does not settle this: it needs the measurement and the scale choice before size step values can be set | GDD l.104, l.367; P1 | Open (T27, N7; prerequisite of the DEC-02 step values) |
| D5 | Dirt | Confirmed, corrected | Absent from the GDD. The sheets give four coatings (clean, dust, soot, mud) with unordered effects, not four levels of one gauge, so the "hidden gauge" argument is weak. Real tensions: one more system, a penalty on the central verb, half the effects need robots | GDD l.185; P2 | Covered by DEC-03 |
| D6 | Robots | Nuanced | Cleaner robots are not in the GDD, which keeps enemies optional. The sheet lists threats but does not make them core or part of the slice. The GDD already has an implicit detection channel, noise; no detector is defined (G12) | GDD l.231, l.274, l.403, l.506, l.512-515; P2 | Covered by DEC-03 |
| D7 | Core glow | Confirmed, completed | The glow carries five pieces of information, not four: temperature (hue), dirt and stealth (intensity), digestion (flash) and cohesion (slow pulse). No conflict with the GDD on temperature | GDD l.291-292; P1, P2, P3, P6 | Closed by DEC-09 |
| D8 | Drinking grows the slime | Partly wrong | The earlier claim that the GDD gives no mass source is wrong: "certain liquids" restore mass, so drinking fits the GDD. Still true: washing has a side effect (growth). New point: if water gives mass, the flooded basement becomes an unlimited source that cancels hunger (C9) | GDD l.118, l.160, l.224, l.285, l.348; P2, P4 | Open |
| D9 | Digest gives mass | Confirmed, nuanced | The GDD is inconsistent with itself (five outputs in four places), and l.201 says aspirating gives the property (N6). The sheet does not exclude other outputs | GDD l.157, l.187, l.201, l.267, l.297, l.315, l.406; P4, P6 | Covered by DEC-04 |
| D10 | "No cute face" versus eyes | Nuanced | Not a GDD conflict (the GDD leaves tone open) but a tension inside P1: glossy eyes versus "not cute". The eyes are functional: the reactions depend on them | GDD l.519; P1, P3, P6 | Closed by DEC-05 |
| D11 | Reactions versus "no UI" | Confirmed, stronger | Two direct contradictions: the selection wheel against "no menu", the reticle cohesion gauge against "no gauge". Notebook and archive are not covered by the sheets | GDD l.289, l.295, l.313, l.425; P1, P2 | Covered by DEC-08 |
| D12 | Cohesion | Nuanced | Cohesion exists in the GDD; the contradiction is inside the GDD (pillar 1 reads endurance on mass, yet cohesion is a separate resource). The real gap with the sheets is how it is read (on the body, 3 levels, versus a gauge) | GDD l.154, l.185, l.288-289; P3 | Reading closed by DEC-09; existence open (C7) |

## Other discrepancies found on verification (N)

| Id | Topic | Finding | References | Status |
|---|---|---|---|---|
| N1 | Grid passing | GDD: the normal state passes under doors and through grids; sheets: only hot liquid passes grids. Squeezing becomes a heat puzzle, which changes level design | GDD l.240, l.386-387; P3, P6 | Open parameter of DEC-01 |
| N2 | Taste output | GDD: tasting reveals properties; sheets: binary like or reject, which does not say whether an object is conductive or sticky (pillar 2) | GDD l.157; P3, P6 | Open (G4) |
| N3 | Body reading collisions | "Dull" and "flat" have five possible causes (hunger, zero cohesion, low cohesion, liquid, dust); two signals cannot carry five pieces of information | GDD l.286, l.288; P2, P3 | Partly closed by DEC-09 |
| N4 | "Look" reaction | An explicit clue, in tension with "no hints" | P3, P6 | Open rule in DEC-07 |
| N5 | Spit mass | New verb and anti-softlock absent from the GDD, close to "split"; could be one verb | GDD l.163, l.377, l.383-385; P3, P6 | Open (C3, DEC-06) |
| N6 | Property from aspirating or digesting | GDD contradicts itself: aspirating gives the property (l.201) versus digesting gives it (l.297) | GDD l.201, l.297 | Open in DEC-04 |
| N7 | x10 world scale | Technical choice with physics effects, to make before building the cage | P1 | Open (D4); prerequisite of the DEC-02 step values |
| N8 | Cage placement | The cage is not in the GDD, which starts in the hall and offices | GDD l.328-332; P2 | Open in DEC-10 |
| N9 | Burning drawn as a dome | Hotter than liquid yet drawn as a dome; no liquid-to-burning animation | P3, P6 | Open parameter of DEC-01 |
| N10 | Colour accessibility | Green (normal) versus red (burning) core is a classic colour-blind confusion pair; redundancy by shape and effects is needed | P1; GDD l.195 | Open (G7) |
| N11 | Size x2 breaks weakened things | A new way to break, by size; compatible, to account for in level design (with DEC-02, only if a slice step reaches x2) | GDD l.244, l.262; P3 | For information |

## Gaps (G)

| Id | Missing topic | Status |
|---|---|---|
| G1 | Dirt rules: what dirties, how to clean, gameplay effect | Partly covered by DEC-03 |
| G2 | Core glow meaning | Closed by DEC-09 |
| G3 | Mouth, sizes, expressions, animations | Covered by the sheets; numbers, thresholds, durations and taste outputs remain |
| G4 | Taste: input, duration, risk, output format | Open |
| G5 | Numbers: mass, thresholds, temperatures, belly capacity | Open (T10) |
| G6 | Controls and input scheme (keyboard and mouse, gamepad on PC) | Open |
| G7 | Audio, music, localization, accessibility | Open |
| G8 | Duration target | Covered by DEC-06 |
| G9 | Slime communication and creator appearance | Open (Q18) |
| G10 | Technical budgets and hardware spec | Open (Q7, T2) |
| G11 | Ending conditions and an authored fragment list | Open |
| G12 | Threats and failure states outside minimum mass | Open |
| G13 | Link between "understand where it comes from" and a concrete structure | Open |
