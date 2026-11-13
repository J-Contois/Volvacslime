# DEC-11 World Partition - Decision record

| Field | Value |
|---|---|
| Status | Decided |
| Decided by | user, 2026-11-13 |
| Owner | game-designer (record); unreal-engineer (technical spec) |
| Last updated | 2026-11-13 |
| Related | [GDD](../gdd.md) section 10, [repository page](../../knowledge/repository-overview.md), tickets T12, T13 |

**Summary.** The game world uses World Partition, to get the most out of level generation and playability. This replaces the original GDD proposal of one persistent level with per-room sublevels.

## Question
How is the building loaded: World Partition, or one persistent level with per-room streamed sublevels as the original GDD proposed ("World Partition is useless for a closed building")?

## Decision
World Partition, "to optimize generation and playability as much as possible" (user, 2026-11-13). `Lvl_VolvacslimeMap` already uses it.

## Still open
- How rooms map to World Partition cells and data layers (for example one data layer per room or biome state).
- How saving per room change (GDD) works with World Partition streaming.
- Both go into a technical spec by the unreal-engineer.

## Options considered

| Option | Principle | Benefits | Risks |
|---|---|---|---|
| A. Persistent level and per-room sublevels (original GDD) | One sublevel per room, streamed by volumes | Simple, explicit control per room | Manual streaming setup; less engine help for large spaces |
| B. World Partition (chosen) | Grid-based automatic streaming, data layers, HLODs | Engine-managed streaming and HLODs; already set up in the project | Built for open worlds: cell size and data layers must fit small, dense rooms at x10 scale |

## Recommendation
Not applicable: decided by the user.

## Parameters
Cell size, loading range, data layers per room or state: TODO, in the technical spec.

## Playtest question
Does moving between rooms stay seamless, with no visible loading or popping?

## Impact
GDD technical direction (section 10), level documents, T13 (cage greybox), T12 (Chaos fragments and streaming).
