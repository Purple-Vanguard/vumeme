# PRD-00 — Bootstrap Repo + One-Command Dev Start

## Goal (one sentence)
- A new developer can run one command and see a working web page and backend health endpoint.

## In Scope
- Create stable repo skeleton: `/frontend`, `/backend`, `/prd`, `/assets`, `/scripts`
- Add README with one-command local dev start (choose one: `npm run dev` OR `docker compose up`)
- Provide backend `GET /health` returning JSON `{ "ok": true }`
- Provide frontend landing page showing “Backend: OK” by calling `/health`

## Out of Scope
- No LLM/TTS
- No `/interact` endpoint yet
- No styling polish beyond basic readability

## User Stories (1–2)
- As a developer, I want a one-command start so that I can iterate quickly without setup friction.
- As a reviewer, I want a visible health indicator so that I can verify the stack is running.

## API / Data Contract
- Endpoint: `GET /health`
- Response: `200` JSON `{ "ok": true }`

## UI Behavior
- On page load, frontend calls `/health`
- If ok: show “Backend: OK”
- If failed: show “Backend: DOWN” + error message

## Acceptance Criteria
1) Given a clean machine, when I follow README steps, then I can open the frontend URL and see “Backend: OK”.
2) Given the backend is running, when I call `GET /health`, then I receive `200` with JSON `{ "ok": true }`.

## Test Steps
1) Follow README: install deps and start dev server(s).
2) Open the frontend URL in a browser; confirm “Backend: OK”.
3) `curl http://localhost:<backend_port>/health` and confirm response.

## DoD
- [ ] Repo skeleton exists and matches README
- [ ] One-command dev start works
- [ ] Health check works
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- None required (bootstrap only)
