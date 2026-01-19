# PRD-08 — Interaction Logging + Export (JSONL/SQLite)

## Goal (one sentence)
- Persist interaction records and export them for latency/fallback/cost analysis.

## In Scope
- Store one record per /interact call:
  - request_id, session_id, timestamp
  - user_text_length (no raw sensitive text)
  - director_tags
  - latency_ms, token_estimate, tts_char_count, cost_estimate_usd
  - fallback_reason, cache_hit
- Export:
  - `GET /logs/export.csv` OR `scripts/export_logs.py` producing CSV
- Storage: JSONL or SQLite (minimal)

## Out of Scope
- No dashboard
- No analytics pipeline

## Acceptance Criteria
1) Given 3 interactions, when exporting logs, then CSV contains 3 rows with required columns.
2) Given fallback occurs, when logged, then fallback_reason is not "none".
3) Given restart, previous logs remain available.

## Test Steps
1) Perform 3 interactions.
2) Export logs to CSV.
3) Verify columns + row count.

## DoD
- [ ] Log storage works
- [ ] Export works
- [ ] Sensitive text not stored
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- This PRD implements telemetry storage itself.
