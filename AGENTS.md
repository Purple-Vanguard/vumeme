# AGENTS.md (Codex entrypoint)

You are Codex operating on this repository.

## Must-read files (in order)
1) agent.md
2) process.txt
3) prd/index.md
4) The target PRD file in prd/ (e.g., PRD-02-*.md)

## Non-negotiable rules
- One PRD = one PR. Implement ONLY the PRD “In Scope”.
- Keep changes minimal. No opportunistic refactors.
- Run the PRD Test Steps and report results.
- Update prd/index.md status for the PRD you completed.
- Append a round summary block to process.txt.
- If CI fails, fix within the same PR unless it becomes a new PRD-sized change.

## Output discipline
- Always list: files changed, commands run, and results.
