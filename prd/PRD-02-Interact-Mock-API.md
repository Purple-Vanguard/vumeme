# PRD-02 — POST /interact Mock API (Contract-First)

## Goal (one sentence)
- Frontend can call `/interact` and receive a contract-compliant mock response to drive UI state changes.

## In Scope
- Implement `POST /interact` endpoint returning the contract shape from agent.md
- Response must include:
  - `request_id`
  - `reply_text`
  - `director_tags` (validated/sanitized)
  - `segments` (at least 1)
  - `audio.type = "none"`
  - `meta.latency_ms`
- Minimal request parsing (`session_id`, `user_text`, `lang`) with basic validation
- Minimal CORS for local dev (if needed)

## Out of Scope
- No LLM/TTS
- No persistent logging (PRD-08)

## User Stories
- As a user, I want instant visible feedback so that I feel the system is responsive.
- As a developer, I want a stable API contract so that frontend can be built independently.

## API / Data Contract
- Endpoint: `POST /interact`
- Request: minimum `{ session_id, user_text }`
- Response: required fields per agent.md

## Acceptance Criteria
1) Given any user_text, when POST /interact is called, then it returns 200 with required fields and valid director_tags.
2) Given a typical request, when called, then `meta.latency_ms` is present and > 0.
3) Given malformed JSON, when called, then it returns 400 with a helpful error message.

## Test Steps
1) Start dev servers.
2) `curl -X POST /interact` with sample JSON; verify response fields.
3) Open frontend and send a message; verify UI updates (text + overlay).

## DoD
- [ ] Endpoint works and returns contract-compliant JSON
- [ ] Uses sanitizer for director_tags
- [ ] Basic error handling
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- meta.latency_ms
- meta.fallback_reason (none for mock)
