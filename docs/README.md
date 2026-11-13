# Volvacslime documentation - Index

| Field | Value |
|---|---|
| Status | Approved |
| Owner | technical-writer |
| Last updated | 2026-11-13 |
| Source of truth for | Where each document lives, who owns it, and how documents are written |

**Summary.** The repository is the source of truth for every technical document. Notion receives a copy that the user imports by hand from `exports/notion/`. Each folder has one owner role; other roles ask the owner (through the studio lead) instead of editing.

## Start here

1. [`PROJECT_BIBLE.md`](PROJECT_BIBLE.md): phase, pitch, pillars, scope, budgets, conventions, open questions. It wins over every other document.
2. [`design/gdd.md`](design/gdd.md): the current design of the whole game.
3. [`design/decisions/README.md`](design/decisions/README.md): every design decision and its status.
4. [`planning/backlog.md`](planning/backlog.md): what is being built next.

## Map

| Path | Owner | Document types | Template |
|---|---|---|---|
| `PROJECT_BIBLE.md` | producer | Project bible | (single file) |
| `reference/` | user (read-only for agents) | User material kept as received: GDD source, its markdown conversion, slime sheets | none |
| `design/gdd.md` | game-designer | Living game design document: the original GDD with every decided choice applied, plus the glossary; updated in the same run as any decision or brief change | [gdd](templates/gdd.md) |
| `design/slime-character.md` | game-designer | Character spec from the slime sheets | (single file) |
| `design/briefs/` | game-designer | Design briefs, one per feature | [design-brief](templates/design-brief.md) |
| `design/decisions/` | game-designer records, the user decides | Decision records `DEC-NN-<topic>.md` and the decision log | [decision-record](templates/decision-record.md) |
| `design/reviews/` | game-designer | Consistency reviews of design sources | [review-report](templates/review-report.md) |
| `specs/` | unreal-engineer | Technical specs `<feature>-technical-spec.md` | [technical-spec](templates/technical-spec.md) |
| `levels/` | level-designer | Level documents | [level-doc](templates/level-doc.md) |
| `assets/` | blender-artist | Asset sheets for meshes and exports | [asset-sheet](templates/asset-sheet.md) |
| `techart/` | technical-artist | Asset sheets for materials, VFX, lighting; rendering cost reports | [asset-sheet](templates/asset-sheet.md) |
| `qa/` | qa-engineer | Test plans, bug reports, test pass and playtest reports | [test-plan](templates/test-plan.md), [bug-report](templates/bug-report.md), [test-pass-report](templates/test-pass-report.md), [playtest-report](templates/playtest-report.md) |
| `ideas/` | idea-scout | Idea batches and the user's decisions | [idea-batch](templates/idea-batch.md) |
| `planning/` | producer | `roadmap.md`, `backlog.md`, `risks.md`, external briefs | [external-brief](templates/external-brief.md) |
| `knowledge/` | technical-writer (build-engineer for build docs) | Architecture, onboarding, repository overview, changelog | [knowledge-page](templates/knowledge-page.md) |
| `release/` | build-engineer | Release checklists | [release-checklist](templates/release-checklist.md) |
| `audio/` | audio-designer | Audio specs, mixing notes, briefs for composers and sound designers | [external-brief](templates/external-brief.md) |
| `marketing/` | marketing-writer | Store copy, devlogs, press kit | none yet |
| `README.md` | technical-writer | This index: map, ownership, writing rules | (single file) |
| `templates/` | technical-writer | One template per document type | - |

Folders that do not exist yet are created with their first document.

## Writing rules

1. **English only.** Exception: `reference/`, kept in the user's language.
2. **One fact, one place.** Write a fact in the document that owns it; elsewhere, link to it. The bible links to decisions instead of repeating them.
3. **Start from the template.** Every document opens with the title `<Subject> - <Document type>`, the header table (Status, Owner, Last updated, Source of truth for, Related) and a two or three sentence summary.
4. **Current state, not history.** Update the document in place. Git keeps the history; no "Update YYYY-MM-DD" paragraphs.
5. **Short cells.** One sentence per table cell. Reasoning goes in a section under the table.
6. **Short documents.** A brief, a spec or a decision fits on about two pages. Split by feature rather than growing one file.
7. **Mark unknowns** as `TODO(question)` and never guess. Mark prototype work as prototype.
8. **Stable ids.** Decisions `DEC-NN`, tickets `TNN`, risks `RNN`, milestones `MN`, review items `CNN` (contradictions), `DNN` (sheet discrepancies), `NNN` (other discrepancies), `GNN` (gaps). Never renumber; retire an id with status Superseded.
9. **File names** are lowercase kebab-case. Exceptions: `README.md`, `PROJECT_BIBLE.md`, `DEC-NN-<topic>.md`.
10. **Living documents.** A change to a decision record or a design brief updates the living GDD (`design/gdd.md`) in the same change, in studio and in normal sessions alike. A code change that alters a documented system updates its technical spec and knowledge page.
11. **Modeling proposal.** Every asset sheet starts from a proposal (single block or modular, with figures) that the user decides; nobody models before the choice (`templates/asset-sheet.md`).
12. **Check before you finish.** Run `python Scripts/check_docs.py` after changing `docs/`; it checks titles, headers, summaries, status values, file names, links, ids, the decision log and the language, and must report 0 problems.

## Status values

| Document kind | Values |
|---|---|
| Documents | Draft, In review, Approved, Implemented, Deprecated |
| Decisions | Open, To confirm, Agreed in principle, Decided, Superseded |
| Tickets | Backlog, Ready (acceptance criteria, owner, dependencies done, no waiting decision: the studio's sprint mode runs only these), In progress, Blocked, Done, Scheduled later |
| Ideas | Proposed, Accepted, Rejected, Parked |
| Content tags (bible and design docs) | confirmed, proposed, to prototype |

## Notion import

Notion is a read-only copy for the user. Agents never write to Notion in this project (`.claude/studio/notion.json` sets `"mode": "export"`).

```bash
python Scripts/export_notion.py
```

The script (owner: build-engineer) writes `exports/notion/` (git-ignored, never edited by hand):

- `pages/`: every document of `docs/`, folders kept. In Notion: Import > Text & Markdown.
- `databases/`: `Tickets.csv`, `Risks.csv`, `Milestones.csv`, `Decisions.csv`. In Notion: Import > CSV, then set the Owner, Size and Status columns to the Select type.

Edit the documents here, run the script, then import again.

## GitHub issues (prepared, not active)

`python Scripts/sync_github.py` shows how the backlog tickets would be mirrored to GitHub issues (one way: `planning/backlog.md` stays the source). Nothing is created until the user approves `--apply`, which needs the GitHub CLI and `docs/` pushed to GitHub.
