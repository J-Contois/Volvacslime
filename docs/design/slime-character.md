# Slime "Specimen" - Character spec

| Field | Value |
|---|---|
| Status | Approved as a base (sheets v1, validated by the user on 2026-11-10, to modify later) |
| Owner | game-designer (intent); art roles own their asset sheets |
| Last updated | 2026-11-13 |
| Source of truth for | The slime's look, sizes, states, reactions and animation base, as read from the sheets |
| Related | [Slime sheets](../reference/slime_sheets/), [consistency review](reviews/gdd-consistency-review.md) (D1 to D12), tickets T21 to T27 |

**Summary.** The six sheets fix the look and intent of the slime: a translucent layered green jelly with an emissive core, about 80 cm in engine. Mechanics shown on the sheets stay to prototype: a "Validated" label on a sheet validates the look, not the mechanic.

Sources (French): `Slime_v1_1_Identite`, `Slime_v1_2_Matiere_Salete`, `Slime_v1_3_Etats_Tailles_Reactions`, `Slime_v1_4_Bouche_Objets`, `Slime_v1_5_Animations_Deplacement`, `Slime_v1_6_Animations_Transformations`.

Tags: C = confirmed as look or intent, P = proposed, T = to prototype.

## Look

| Area | Spec | Tag |
|---|---|---|
| Identity | "Abandoned lab experiment", translucent layered green jelly, "no cute face"; name "Specimen" | C |
| Engine size and pivot | 80 x 80 x 53 cm (story size about 8 cm, world x10); pivot on the ground, centred; front = +X | C, to check against the cage (D4) |
| Budget | About 5000 triangles for the mesh | C as a target |
| Layers | Thin glossy skin, cloudy jelly with bubbles, dense dark heart, emissive core with veins; Blender Cycles render is the reference | C look; Unreal approach T (T1) |
| Eyes and mouth | Two dark spots floating in the jelly; no mouth at rest; the front face hollows into a funnel to aspirate or spit | C |
| Fixed debris | Screw, glass shard, "EXP-07" label, always present | C |
| Drips | Two small drips at the floor | C |
| Belly inventory | Kept objects float visibly in the belly; no menu | C look; T behaviour |

## Body signals

Per [DEC-09](decisions/DEC-09-body-signals.md): core colour = temperature (green normal, blue cold, orange hot, red burning), core intensity = dirt, size = mass, core rhythm and softness = cohesion. Thresholds are T.

## Dirt

Four coatings: clean, dust, soot, mud. Indicative effects from sheet 2, all to tune:

| Coating | Core glow | Heat | Surveillance | Cleaners |
|---|---|---|---|---|
| Clean | Strong | Melts fast | Very visible | Ignore |
| Dust | Slightly dull | Normal | Less visible | Slight interest |
| Soot | Very weak | Normal | Almost invisible | Attracted |
| Mud | Weak | Insulated, melts slowly | Little visible | Very attracted, leave trails |

The sheet's suction penalty is removed; the heat effect and the robots are to confirm ([DEC-03](decisions/DEC-03-dirt-and-robots.md)). Getting dirty: dust, soot, mud, cage sawdust. Cleaning: water (makes the slime grow) or turning liquid (dirt stays on the floor). Tag P.

## States and sizes

| Item | Spec | Tag |
|---|---|---|
| States | Frozen, gelatinous, hot liquid, burning; mass kept across states; auto return to gelatinous ([DEC-01](decisions/DEC-01-temperature-states.md)) | T |
| Size steps (sheet values) | x0.5 = 40 cm (tubes), x1 = 80, x1.5 = 120 (pushes medium objects), x2 = 160 (breaks weakened things), x2.5 = 200 (max force, few passages); size model decided in [DEC-02](decisions/DEC-02-size-model.md): three of these steps in the slice, the others to tune | T |
| Anti-softlock | Spit mass at will, so the slime is never stuck | P |

## Objects and digestion

| Item | Spec | Tag |
|---|---|---|
| Objects by free volume | Small: stored, floats; medium: stored, deforms the silhouette, slows; too big: cannot swallow, push or stick to it | C |
| Swallowing | Small objects go through the opening; medium ones are engulfed by the spreading jelly | C |
| Digest | The object disappears and gives mass ([DEC-04](decisions/DEC-04-digestion-output.md)) | P |
| Loop | To swallow bigger, grow; to grow, drink (or digest); spit to shrink | P |

## Reactions and animation

| Item | Spec | Tag |
|---|---|---|
| Reactions (replace the UI) | Look, taste likes, taste rejects, alert, effort, fatigue; short and stackable | C look; triggers T |
| Animation base (durations to tune) | Idle 2 s; hops 0.6 s loop; jump 1.2 s; aspirate 0.8 s; engulf 1.4 s; spit 0.7 s; digest 2 s; grow or shrink 0.8 s per step; spit mass 0.6 s; melt and reform 1 s + 0.8 s; freeze or thaw 1.2 s | C base; T durations |
| Rig | root to body_low, body_mid, body_top, eye_L, eye_R; mouth = morph target; liquid and frozen = mesh or state shader; core = material parameter | P, to confirm with the unreal-engineer and the technical-artist |

Final modelling is scheduled later (tickets T21 to T27). The slime mesh in `Content/_Volvacslime/Characters/Slime` was only a test: it is not this character (user, 2026-11-13).
