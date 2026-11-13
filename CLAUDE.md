# Volvacslime

Unreal Engine 5.8 third-person puzzle game (a lab slime that aspirates, tastes and digests matter), student project at Gaming Campus 2026-2027. Blender for art, versioned on GitHub. Gameplay is in Blueprints today; the C++ module `Source/Volvacslime` is the empty default.

## Source of truth

Read `docs/PROJECT_BIBLE.md` before any work. It holds the phase (concept), pillars, scope, decisions and open questions. If it conflicts with anything else, the bible wins. If it is missing or incomplete for the task, say so and stop instead of guessing.

- The user's GDD (`docs/reference/GDD_source_v0.3.txt`) and slime sheets (`docs/reference/slime_sheets/`) are in French and are a base, not validated design: follow the status legend of the bible (confirmed, proposed, to prototype).
- The current design is the living GDD `docs/design/gdd.md`; design decisions and their status are in `docs/design/decisions/README.md`. Never treat a decision that is not "Decided" as settled.

## Documentation

Technical documents live in the repository; `docs/README.md` gives the folder of each document type, its owner, its template (`docs/templates/`) and the writing rules. Notion is a copy the user imports by hand from `exports/notion/` (`python Scripts/export_notion.py`): never write to Notion.

## How we work

- The user validates every idea, every phase change and every sensitive action.
- The user writes in French: answer in French. Everything written to the repository (code, comments, docs, commits, issues, PRs) is in English.
- Concept phase: work in Unreal is idea testing only; tests and prototypes are disposable and labeled as such.

## Hard rules

- Never delete or overwrite assets, push, merge, create issues or PRs without explicit approval.
- `Config/DefaultEngine.ini`, `Config/DefaultGame.ini` and `Volvacslime.uproject` carry uncommitted changes of the user: do not modify them unless asked.
- Never commit `Binaries/`, `Intermediate/`, `Saved/` or `DerivedDataCache/`.
- Only one agent drives the Unreal editor at a time.
- Never put secrets in documents or commits.
