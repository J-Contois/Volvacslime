"""Check the project documentation against the writing rules of docs/README.md.

Usage (from anywhere):  python Scripts/check_docs.py
Owner: build-engineer. Read-only: it never changes a file. Exit code 0 when every check passes.

Checks every markdown document of docs/ (templates and reference material excluded):
  - title "# <Subject> - <Document type>", header table with Status, Owner and Last updated, a Summary;
  - status value allowed for the document kind;
  - file name in lowercase kebab-case (README.md, PROJECT_BIBLE.md and DEC-NN-<topic>.md excepted);
  - relative links point to existing files;
  - ticket (TNN) and decision (DEC-NN) ids exist; every decision record is in the decision log with the same status;
  - English only (no French accented letters outside quoted text).
"""
import pathlib
import re
import sys

repo = pathlib.Path(__file__).resolve().parent.parent
docs = repo / "docs"
SKIP = {"templates", "reference"}
DOC_STATUS = {"Draft", "In review", "Approved", "Implemented", "Deprecated"}
DECISION_STATUS = {"Open", "To confirm", "Agreed in principle", "Decided", "Superseded"}
NAME = re.compile(r"^([a-z0-9]+(-[a-z0-9.]+)*\.md|README\.md|PROJECT_BIBLE\.md|DEC-\d\d-[a-z0-9-]+\.md)$")
FRENCH = re.compile(r"[éèêëàâçùûôîï]")
QUOTED = re.compile(r'"[^"\n]*"|«[^»\n]*»')

problems = []


def problem(path, message):
    problems.append(f"{path.relative_to(repo).as_posix()}: {message}")


def field(lines, name):
    for line in lines[:12]:
        if line.startswith(f"| {name} |"):
            return line.split("|")[2].strip()
    return None


def documents():
    for path in sorted(docs.rglob("*.md")):
        if not SKIP & set(path.relative_to(docs).parts[:-1]):
            yield path


def main():
    backlog = docs / "planning" / "backlog.md"
    tickets = set(re.findall(r"^### (T\d+) - ", backlog.read_text(encoding="utf-8"), re.M)) if backlog.exists() else set()
    decisions = {p.name[:6]: p for p in (docs / "design" / "decisions").glob("DEC-*.md")}
    count = 0
    for path in documents():
        count += 1
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not NAME.match(path.name):
            problem(path, "file name is not lowercase kebab-case")
        if not lines or not lines[0].startswith("# ") or " - " not in lines[0]:
            problem(path, 'first line must be "# <Subject> - <Document type>"')
        for name in ("Status", "Owner", "Last updated"):
            if field(lines, name) is None:
                problem(path, f"header table has no {name} row")
        status = field(lines, "Status") or ""
        allowed = DECISION_STATUS if path.name.startswith("DEC-") else DOC_STATUS
        if status and not any(status.startswith(s) for s in allowed):
            problem(path, f"status '{status}' is not one of {sorted(allowed)}")
        if not any(line.startswith("**Summary.**") for line in lines[:16]):
            problem(path, "no **Summary.** line under the header")
        if FRENCH.search(QUOTED.sub("", text)):  # quotes and titles may keep their language
            problem(path, "contains French accented letters (documents are in English)")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#")[0]
            if target and not target.startswith(("http:", "https:", "mailto:")) and not (path.parent / target).resolve().exists():
                problem(path, f"broken link: {target}")
        for tid in set(re.findall(r"\bT\d{1,2}\b", text)) - tickets:
            if tickets:
                problem(path, f"unknown ticket id {tid}")
        for did in set(re.findall(r"\bDEC-\d\d\b", text)) - set(decisions):
            problem(path, f"unknown decision id {did}")

    log = docs / "design" / "decisions" / "README.md"
    if log.exists():
        log_text = log.read_text(encoding="utf-8")
        for did, path in decisions.items():
            row = next((l for l in log_text.splitlines() if f"({path.name})" in l), None)
            if row is None:
                problem(log, f"{did} is missing from the decision log")
                continue
            record_status = field(path.read_text(encoding="utf-8").splitlines(), "Status") or ""
            log_status = row.split("|")[3].strip()
            if not record_status.startswith(log_status):
                problem(log, f"{did} status '{log_status}' differs from the record ('{record_status}')")

    for line in problems:
        print(line)
    print(f"{count} documents checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
