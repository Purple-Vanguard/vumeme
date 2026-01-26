#!/usr/bin/env python3
import os, sys, subprocess, json, time, re
from pathlib import Path

def sh(*args, check=True, capture=False):
    if capture:
        return subprocess.run(args, check=check, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
    subprocess.run(args, check=check)

def main():
    if len(sys.argv) != 2:
        print("Usage: apply_patch.py <patch_file>", file=sys.stderr)
        sys.exit(2)

    patch_file = sys.argv[1]
    comment_id = os.getenv("CODEX_COMMENT_ID", "").strip()
    comment_url = os.getenv("CODEX_COMMENT_URL", "").strip()
    allow_workflows = os.getenv("ALLOW_WORKFLOWS", "false").lower() == "true"

    if not comment_id:
        print("Missing CODEX_COMMENT_ID", file=sys.stderr)
        sys.exit(2)

    # Prevent duplicate apply
    log = sh("git", "log", "-n", "50", "--pretty=%B", capture=True)
    if f"codex-comment-id:{comment_id}" in log:
        print(f"Already applied codex comment {comment_id}, skipping.")
        sys.exit(0)

    patch_text = Path(patch_file).read_text(encoding="utf-8", errors="replace")
    if len(patch_text) > 500_000:
        raise SystemExit("Patch too large (>500KB). Refuse.")

    # Block workflow edits unless explicitly allowed
    touched = set()
    for m in re.finditer(r"^\+\+\+\s+b/(.+)$", patch_text, re.MULTILINE):
        touched.add(m.group(1).strip())
    for m in re.finditer(r"^---\s+a/(.+)$", patch_text, re.MULTILINE):
        touched.add(m.group(1).strip())

    if not allow_workflows:
        for p in touched:
            if p.startswith(".github/workflows/"):
                raise SystemExit("Refuse: patch touches .github/workflows/** (add label allow-github-workflows).")

    # Apply
    sh("git", "apply", "--3way", "--whitespace=fix", patch_file)

    # Trace log (in-repo, audit-friendly)
    trace_dir = Path(".codex")
    trace_dir.mkdir(exist_ok=True)
    trace_path = trace_dir / "trace.jsonl"
    entry = {
        "ts": int(time.time()),
        "codex_comment_id": comment_id,
        "codex_comment_url": comment_url,
        "touched_files": sorted(touched),
    }
    with trace_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # Commit
    sh("git", "config", "user.name", "github-actions[bot]")
    sh("git", "config", "user.email", "github-actions[bot]@users.noreply.github.com")
    sh("git", "add", "-A")
    sh("git", "commit", "-m", f"codex: apply patch\n\ncodex-comment-id:{comment_id}\ncodex-comment-url:{comment_url}\n")

if __name__ == "__main__":
    main()
