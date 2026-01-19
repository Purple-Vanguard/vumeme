# PRD-09 — Deploy a Public Mobile-Friendly Demo URL

## Goal (one sentence)
- Publish a reachable demo URL that works on mobile and supports the full MVP loop with graceful fallback.

## In Scope
- Deploy frontend + backend (same domain or separate with CORS)
- Configure API keys via environment variables
- Minimal protection:
  - basic rate limit / abuse guard
- Document deployment steps (README or DEPLOY.md)

## Out of Scope
- No billing
- No auth
- No multi-tenant

## Acceptance Criteria
1) Given the public URL, when opened on a phone, then page loads and loop video plays.
2) Given user input, then user receives overlay+subtitle quickly and audio when available; if not, fallback works.
3) Given rapid repeated requests, then requests are throttled or rejected gracefully.

## Test Steps
1) Deploy to chosen platform.
2) Open on mobile; verify playback.
3) Send 3 interactions; verify stability.
4) Hammer test (10 rapid requests); verify throttling.

## DoD
- [ ] Public URL available
- [ ] Secrets not committed
- [ ] Deployment docs exist
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- At minimum log request counts and latency; export should still work (PRD-08).
