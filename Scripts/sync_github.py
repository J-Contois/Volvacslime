"""Mirror the backlog tickets to GitHub issues (one way: docs/planning/backlog.md stays the source of truth).

Usage (from anywhere):
  python Scripts/sync_github.py                 dry run: prints what would be created or updated, changes nothing
  python Scripts/sync_github.py --apply [--project <number>] [--owner <login>]
Owner: build-engineer. --apply needs the GitHub CLI (gh auth login, with the project scope for --project)
and the user's explicit approval: it creates labels and issues on GitHub. Prerequisite: docs/ committed and
pushed, so the issue links resolve.

Each ticket becomes the issue titled "TNN - <title>", found again by that prefix on later runs (no duplicates).
The body holds the context, the acceptance criteria and a link to the backlog section; labels give the role,
the size and the status. Tickets marked Done are closed. Edit tickets in backlog.md, never on GitHub.
"""
import argparse
import json
import pathlib
import shutil
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from export_notion import parse_tickets  # noqa: E402

ROLE_LABELS = {"game-designer": "role:design", "level-designer": "role:level", "unreal-engineer": "role:unreal",
               "build-engineer": "role:build", "blender-artist": "role:art", "technical-artist": "role:techart",
               "qa-engineer": "role:qa", "technical-writer": "role:docs", "marketing-writer": "role:marketing",
               "producer": "role:production", "human": "owner:human", "idea-scout": "role:design"}


def labels_for(ticket):
    roles = {label for name, label in ROLE_LABELS.items() if name in ticket["owner"]}
    labels = sorted(roles) + [f"size:{ticket['size'].split()[0]}"] if ticket["size"] else sorted(roles)
    status = ticket["status"].lower().replace(" ", "-")
    labels.append(f"status:{status}")
    if ticket["decision"] not in ("", "-"):
        labels.append("blocked")
    return labels


def body_for(ticket, repo_url, branch):
    link = f"{repo_url}/blob/{branch}/docs/planning/backlog.md" if repo_url else "docs/planning/backlog.md"
    criteria = "\n".join(f"- [ ] {c}" for c in ticket["criteria"]) or "- [ ] TODO(question)"
    return (f"Mirrored from [the backlog]({link}), the source of truth. Edit the ticket there, not here.\n\n"
            f"| Owner | Size | Status | Depends on | Waits for decision |\n|---|---|---|---|---|\n"
            f"| {ticket['owner']} | {ticket['size']} | {ticket['status']} | {ticket['depends']} | {ticket['decision']} |\n\n"
            f"**Context.** {ticket['context']}\n\n**Acceptance criteria**\n{criteria}\n")


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=True).stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="create or update issues on GitHub (asks nothing: get approval first)")
    parser.add_argument("--project", type=int, help="GitHub Projects number to add the issues to")
    parser.add_argument("--owner", default="@me", help="project owner for --project")
    args = parser.parse_args()

    repo_url, branch = "", "main"
    try:
        remote = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True, check=True).stdout.strip()
        repo_url = remote.removesuffix(".git").replace("git@github.com:", "https://github.com/")
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    tickets = parse_tickets()
    if not args.apply:
        print(f"Dry run: {len(tickets)} tickets would be mirrored to {repo_url or 'the origin repository'}.")
        for t in tickets:
            action = "close" if t["status"].lower() == "done" else "create or update"
            print(f"  {action:16} {t['id']:4} {t['title'][:55]:55} [{', '.join(labels_for(t))}]")
        print("Nothing was changed. Run with --apply after the user approves (needs gh and docs/ pushed).")
        return 0

    if not shutil.which("gh"):
        sys.exit("gh is not installed: winget install GitHub.cli, then gh auth login.")
    existing = {i["title"].split(" - ", 1)[0]: i for i in json.loads(gh("issue", "list", "--state", "all", "--limit", "500",
                                                                         "--json", "number,title,state"))}
    for label in sorted({l for t in tickets for l in labels_for(t)}):
        gh("label", "create", label, "--force")
    for t in tickets:
        title, body, labels = f"{t['id']} - {t['title']}", body_for(t, repo_url, branch), labels_for(t)
        issue = existing.get(t["id"])
        if issue:
            gh("issue", "edit", str(issue["number"]), "--title", title, "--body", body, *sum((["--add-label", l] for l in labels), []))
            number = issue["number"]
            print(f"updated #{number} {title}")
        else:
            url = gh("issue", "create", "--title", title, "--body", body, *sum((["--label", l] for l in labels), [])).strip()
            number = int(url.rsplit("/", 1)[-1])
            print(f"created #{number} {title}")
        if t["status"].lower() == "done":
            gh("issue", "close", str(number))
        if args.project:
            gh("project", "item-add", str(args.project), "--owner", args.owner, "--url", f"{repo_url}/issues/{number}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
