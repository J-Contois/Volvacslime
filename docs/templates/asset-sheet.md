# <Asset> - Asset sheet

| Field | Value |
|---|---|
| Status | Draft |
| Owner | blender-artist (meshes) or technical-artist (materials, VFX, lighting) |
| Last updated | YYYY-MM-DD |
| Source of truth for | How <asset> is built and what it costs |
| Related | Design brief, level document, tickets (TNN) |
| Source path | Art/Source/... |
| Export path | Art/Export/... |
| Unreal path | /Game/... |

**Summary.** What the asset is, where it is used, and the approach chosen (single block or modular).

## Usage

## Modeling proposal and decision

Rule: the `modeling-proposal` skill of the studio. Nobody models before the user chooses. Several assets of one family can share one proposal.

- **Proposal level:** light or full.
- **Recommendation:** single block or modular, and why.
- **Decision (user, date):** the user's words, or "not decided". The choice stays open to discussion.

**Comparison** (full proposal). Ranges, marked as estimate or measure; compared with the project budget when one exists, otherwise `TODO(question)`.

| Metric | Single block | Modular |
|---|---|---|
| Triangles (total, and per module) | | |
| Unique meshes to produce, instances in a typical use | | |
| Material slots, texture resolution | | |
| Mesh sections and estimated draw calls | | |
| Collision complexity | | |
| LODs to build | | |
| Bones, if animated | | |
| Representation in the engine | | |
| Visible repetition or seam risk | | |
| Modeling cost (effort S, M or L, parts to build) | | |
| Maintenance cost (parts to touch for a typical change) | | |

**Trade-off.** Where modular wins, where it loses, and the recommendation.

## Modules (modular choice only)

| Module | Role | Dimensions | Count in a typical use |
|---|---|---|---|

## Assembly plan (modular choice only)

How modules are placed relative to each other: grid or step size, origin convention, edges that match and how, allowed rotations, variants that hide repetition. Physical joints (hinge, screw, clip) only when parts really join that way.

## Global constraints (modular choice only)

Alignment, symmetry, tolerances, gaps, texel density across modules.

## Budget versus actual

| Metric | Budget | Estimate | Measured |
|---|---|---|---|
| Triangles | | | |
| Materials | | | |
| Texture resolution | | | |

## Collision

## LODs

## Source and license

## Unreal import notes
