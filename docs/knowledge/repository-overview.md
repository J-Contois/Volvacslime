# Repository - Knowledge page

| Field | Value |
|---|---|
| Status | Draft |
| Owner | technical-writer |
| Last updated | 2026-11-13 |
| Last verified | 2026-11-13, against commit 4815bcc on branch `feature-chaosBuilding` (file listing of `Content/_Volvacslime`, not opened in the editor) |
| Source of truth for | What the repository contains today |

**Summary.** A Blueprint-heavy Unreal Engine 5.8 project on World Partition. Everything in `Content/_Volvacslime` today is a test made while validating ideas, not production content (user, 2026-11-13): aspiration components, a Chaos stone, a test slime mesh, a lab material kit and a level design test. The C++ module is the empty default.

## Overview

- Engine: Unreal Engine 5.8 (`EngineAssociation` in `Volvacslime.uproject`; the GDD says 5.8.2), Windows.
- Branch in use: `feature-chaosBuilding`; main branch: `main`.
- `Source/Volvacslime`: empty default module (`Volvacslime.Build.cs`, `Volvacslime.cpp`, `Volvacslime.h`).
- Rendering config as found: DX12 and SM6, Lumen, virtual shadow maps, ray tracing, Substrate. The ChaosVehicles plugin is enabled. Recommended changes are in ticket T3, not applied.
- Uncommitted user changes: `Config/DefaultEngine.ini`, `Config/DefaultGame.ini`, `Volvacslime.uproject` (do not edit, see T11).

## Content layout (`Content/_Volvacslime`)

| Folder | Content |
|---|---|
| `00_Core/Blueprints` | `BP_VolvacslimeCharacter`, `BP_VolvacslimeGameMode`, `BP_VolvacslimePlayerController` |
| `00_Core/Input` | `IMC_Volvacslime`; actions `IA_Aspirate`, `Interaction/IA_Interact`, `Movement/IA_Jump`, `IA_Move`, `IA_MouseLook` |
| `Components` | `BPC_AspirationComponent`, `BPC_Inventory`, `BPC_TargetDetectionComponent` |
| `Interfaces` | `BPI_Interactable`, `BPI_Utils` |
| `Data` | `S_InteractableData` (structure) |
| `Blueprints/Destruction` | `BP_Stone` |
| `Blueprints/Interactable` | `BP_PhysicsObject_Base` |
| `Mesh/GeometryCollections` | `GC_Stone` (Chaos fracture of the stone) |
| `Materials/Physics` | Physical materials `PM_Dirt`, `PM_Stone`, `PM_Wood` |
| `Characters/Slime` | Test only, not the main character of the sheets: skeletal mesh `slime` and `slime1`, `slime_Skeleton`, `slime_PhysicsAsset`, `slime_Anim`, textures `slime_albedo`, `slime_opacity`, `slime_roughness` |
| `Characters/Mannequins` | Epic Manny and Quinn template: meshes, control rigs, materials, unarmed, pistol and rifle animations, `ABP_Unarmed` |
| `Level` | `Lvl_VolvacslimeMap`, on World Partition ([DEC-11](../design/decisions/DEC-11-world-partition.md)) with an HLOD asset |
| `Level/LevelDesign/Materials` | 72 material instances `MI_Lab_*` (floors, walls, cage plastic, frost, goo, glass, hazard...) for the greybox |
| `Level/_GENERATED` | 3 generated `Box_*` assets |
| `Prototypes/UI`, `Mesh/Statics` | Empty |

## Recent work (git history)

Level design test, Chaos material destruction test, aspiration feature, Aspirable collision channel.

## Repository tools

| Path | Purpose | Owner |
|---|---|---|
| `Scripts/export_notion.py` | Builds the Notion import files in `exports/notion/` from `docs/` | build-engineer |
| `Scripts/check_docs.py` | Checks `docs/` against the writing rules (read-only); must report 0 problems | build-engineer |
| `Scripts/sync_github.py` | Mirrors backlog tickets to GitHub issues, one way; dry run by default, `--apply` only with the user's approval once `gh` is installed and `docs/` is pushed | build-engineer |
| `docs/` | Project documentation, see [the index](../README.md) | per folder |

## Known limits

- Test assets do not follow the proposed prefixes (for example `slime`, `slime_albedo`); the naming convention is not approved yet (bible, Conventions).
- Room layout on World Partition (cells, data layers) is not specified yet ([DEC-11](../design/decisions/DEC-11-world-partition.md)).
- The listing was taken from the file system; assets were not opened in the editor.
