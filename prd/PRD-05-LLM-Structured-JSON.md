# PRD-05 — LLM Integration (Structured JSON Output Only + Fallback)

## Goal (one sentence)
- Replace mock text generation with an LLM that outputs only `reply_text`, `director_tags`, and optional `segments`.

## In Scope
- Backend integrates an LLM provider (external API)
- Prompt enforces strict JSON output and fixed enums
- Validate + sanitize LLM output:
  - parse JSON
  - schema validate
  - sanitize director_tags
- Fallback response on errors:
  - default safe `reply_text`
  - default tags
  - `meta.fallback_reason=llm_failed`

## Out of Scope
- No TTS (PRD-06)
- No long-term memory system

## Acceptance Criteria
1) Given a normal request, when /interact runs, then it returns valid JSON with sanitized director_tags and short reply_text.
2) Given invalid JSON/timeout, when /interact runs, then it returns a valid fallback response with fallback_reason=llm_failed.
3) Given unknown tags from LLM, when sanitized, then response contains only allowed tag values.

## Test Steps
1) Configure API key via env vars.
2) Call `/interact` with sample input; verify response constraints.
3) Simulate LLM failure; verify fallback.

## DoD
- [ ] LLM output parsing + validation
- [ ] Sanitization + fallback implemented
- [ ] Secrets via env vars only
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- meta.latency_ms
- meta.token_estimate (best-effort)
- meta.fallback_reason
