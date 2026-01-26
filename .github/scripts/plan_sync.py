#!/usr/bin/env python3
import os
import yaml
import requests

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["REPO"]
OWNER, NAME = REPO.split("/", 1)
API = "https://api.github.com"

def gh(method, path, **kwargs):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    url = f"{API}{path}"
    r = requests.request(method, url, headers=headers, **kwargs)
    if r.status_code >= 400:
        raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text}")
    return r.json() if r.text else None

def ensure_label(name, color="8250df", description=""):
    labels = gh("GET", f"/repos/{OWNER}/{NAME}/labels", params={"per_page": 100})
    if any(l["name"] == name for l in labels):
        return
    gh("POST", f"/repos/{OWNER}/{NAME}/labels", json={"name": name, "color": color, "description": description})

def find_pr_by_branch(branch):
    prs = gh("GET", f"/repos/{OWNER}/{NAME}/pulls", params={"state": "open", "per_page": 100})
    for pr in prs:
        if pr["head"]["ref"] == branch:
            return pr
    return None

def create_branch_if_missing(branch, base="main"):
    try:
        gh("GET", f"/repos/{OWNER}/{NAME}/git/ref/heads/{branch}")
        return
    except Exception:
        pass
    base_ref = gh("GET", f"/repos/{OWNER}/{NAME}/git/ref/heads/{base}")
    sha = base_ref["object"]["sha"]
    gh("POST", f"/repos/{OWNER}/{NAME}/git/refs", json={"ref": f"refs/heads/{branch}", "sha": sha})

def create_pr(title, branch, body):
    return gh("POST", f"/repos/{OWNER}/{NAME}/pulls", json={
        "title": title,
        "head": branch,
        "base": "main",
        "body": body,
        "draft": True,
    })

def add_labels(issue_number, labels):
    gh("POST", f"/repos/{OWNER}/{NAME}/issues/{issue_number}/labels", json={"labels": labels})

def post_comment(issue_number, body):
    gh("POST", f"/repos/{OWNER}/{NAME}/issues/{issue_number}/comments", json={"body": body})

def main():
    with open("docs/plan.yaml", "r", encoding="utf-8") as f:
        plan = yaml.safe_load(f)

    ensure_label("codex:autopilot", "0e8a16", "Allow auto-apply Codex diff comments")
    ensure_label("codex:ready", "1d76db", "Ready for Codex kickoff")
    ensure_label("codex:blocked", "b60205", "Blocked by dependencies")
    ensure_label("allow-github-workflows", "fbca04", "Permit patching workflow files")

    tasks = plan.get("tasks", [])
    prd_path = plan.get("prd", "docs/PRD.md")

    for t in tasks:
        tid = t["id"]
        title = t["title"]
        branch = t["branch"]
        deps = t.get("depends_on", [])
        autopilot = bool(t.get("autopilot", False))

        create_branch_if_missing(branch)

        pr = find_pr_by_branch(branch)
        if not pr:
            body = f"""### Task {tid}: {title}

PRD: `{prd_path}`

Dependencies: {", ".join(deps) if deps else "None"}

### How to run
- CI is defined in `/.github/scripts/ci.sh`

### Codex instructions
Please keep changes minimal and output a single unified diff in ```diff``` block.
"""
            pr = create_pr(f"[{tid}] {title}", branch, body)

        labels = ["codex:autopilot" if autopilot else "codex:ready"]
        add_labels(pr["number"], labels)

        kickoff = f"""@codex Implement **{tid}: {title}** according to `{prd_path}`.

**Output requirements**
1) Reply with ONE unified diff inside a single ```diff``` block.
2) Keep changes scoped to this PR.
3) If tests are needed, update `/.github/scripts/ci.sh` accordingly (do not touch workflows unless allowed).
"""
        post_comment(pr["number"], kickoff)

if __name__ == "__main__":
    main()
