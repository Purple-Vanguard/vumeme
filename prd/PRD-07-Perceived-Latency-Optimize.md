# PRD-07 — Perceived Latency Optimization (Visuals First, Audio Later)

## Goal (one sentence)
- Ensure meaningful UI feedback within ~1s even if audio generation is slow.

## In Scope (choose one)
- A) Single response: frontend renders overlay + first subtitle immediately, audio can start later.
- B) Two-phase minimal: early text+tags response, audio becomes available shortly after (polling/second endpoint).

## Out of Scope
- No streaming protocols, no queues, no complex infra

## Acceptance Criteria
1) Given a request, when user clicks send, then overlay changes and first subtitle appears within 1 second (local dev).
2) Given audio is delayed, when it arrives, then it starts without resetting visuals.
3) Given audio never arrives, then the experience still completes with subtitles + overlay.

## Test Steps
1) Add artificial TTS delay (2–3s).
2) Send a message; confirm quick visuals.
3) Confirm audio begins later without UI disruption.

## DoD
- [ ] Perceived latency improvement implemented
- [ ] No heavy infra introduced
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- frontend `time_to_first_visual_ms` (console log acceptable)
