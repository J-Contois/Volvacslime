"""Generate Notion-importable files from the repository documentation.

Usage (from anywhere):  python Scripts/export_notion.py
Owner: build-engineer. Source of truth: docs/ (see docs/README.md).

Output, generated and git-ignored (never edit by hand):
  exports/notion/pages/       every markdown document of docs/, folders kept,
                              file named after the document title  -> Notion: Import > Text & Markdown
  exports/notion/databases/   Tickets, Risks, Milestones, Decisions -> Notion: Import > CSV
"""
import csv
import pathlib
import re
import shutil

repo = pathlib.Path(__file__).resolve().parent.parent
docs = repo / "docs"
out = repo / "exports" / "notion"
pages, dbs = out / "pages", out / "databases"


def read(rel):
    """Text of a document, or "" when the project does not have it yet."""
    path = docs / rel
    return path.read_text(encoding="utf-8") if path.exists() else ""


def plain(cell):
    """Markdown cell to plain text: links to their label, no emphasis or code marks."""
    cell = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cell)
    return cell.replace("**", "").replace("`", "").strip()


def table(text, header_start):
    """Rows of the first markdown table whose header line starts with header_start ([] when absent)."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(header_start):
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                rows.append([plain(c) for c in row.strip().strip("|").split("|")])
            return rows
    if text:
        print(f"warning: table {header_start!r} not found, database skipped")
    return []


def write_csv(name, header, rows):
    if not rows:
        return
    with open(dbs / name, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"databases/{name}: {len(rows)} rows")


def title_of(path):
    """File name for Notion: the document's H1 title, cleaned of characters Windows refuses.
    Templates keep their file name, since their titles are placeholders."""
    if path.parent.name == "templates":
        return path.stem
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return re.sub(r'[<>:"/\\|?*]', "", line[2:]).strip()
    return path.stem


def parse_tickets():
    """Tickets of docs/planning/backlog.md as dicts (also used by Scripts/sync_github.py)."""
    found = []
    for block in re.split(r"\n(?=### T\d+ - )", read("planning/backlog.md"))[1:]:
        lines = block.splitlines()
        tid, name = re.match(r"### (T\d+) - (.*)", lines[0]).groups()
        row = next(l for l in lines if l.startswith("|") and not l.startswith(("| Owner", "|---")))
        owner, size, status, depends, decision = [plain(c) for c in row.strip().strip("|").split("|")]
        context = next((plain(l.split(":**", 1)[1]) for l in lines if l.startswith("- **Context:**")), "")
        criteria = [plain(l.split("]", 1)[1]) for l in lines if l.strip().startswith("- [ ]")]
        found.append({"id": tid, "title": name, "owner": owner, "size": size, "status": status, "depends": depends,
                      "decision": decision, "context": context, "criteria": criteria})
    return found


def tickets():
    rows = [[f"{t['id']} - {t['title']}", t["id"], t["owner"], t["size"], t["status"], t["depends"], t["decision"],
             t["context"], "; ".join(t["criteria"])] for t in parse_tickets()]
    write_csv("Tickets.csv", ["Name", "ID", "Owner", "Size", "Status", "Depends on", "Waits for decision",
                              "Context", "Acceptance criteria"], rows)


def main():
    if out.exists():
        shutil.rmtree(out)
    pages.mkdir(parents=True)
    dbs.mkdir(parents=True)

    for src in sorted(docs.rglob("*.md")):
        rel = src.relative_to(docs)
        dest = pages / rel.parent / f"{title_of(src)}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        print(f"pages/{dest.relative_to(pages).as_posix()}")

    tickets()
    write_csv("Risks.csv", ["Name", "ID", "Probability", "Impact", "Mitigation", "Owner"],
              [[f"{r[0]} - {r[1]}", *r[:1], *r[2:]] for r in table(read("planning/risks.md"), "| Id | Risk")])
    write_csv("Milestones.csv", ["Name", "ID", "Playable goal", "Notes"],
              [[f"{m[0]} {m[1]}", m[0], m[2], m[3]] for m in table(read("planning/roadmap.md"), "| Id | Name")])
    write_csv("Decisions.csv", ["Name", "ID", "Status", "Decided", "Current answer"],
              [[f"{d[0]} - {d[1]}", d[0], d[2], d[3], d[4]]
               for d in table(read("design/decisions/README.md"), "| Id | Topic")])


if __name__ == "__main__":
    main()
