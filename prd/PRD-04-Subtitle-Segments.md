# PRD-04 — Subtitle Renderer v0 (Timed Segments)

## Goal (one sentence)
- Render subtitles using `segments` with timing so the text changes during playback.

## In Scope
- Subtitle component:
  - If `segments` exists: display text according to `t` offsets (seconds)
  - If missing/empty: display full `reply_text`
- Simple timer driven by request start time (no perfect A/V sync required yet)

## Out of Scope
- No phoneme-level sync
- No typography/animation polish beyond readability

## Acceptance Criteria
1) Given segments with two entries (t=0.0, t=2.0), when rendered, then subtitle switches around 2 seconds.
2) Given no segments, when rendered, then reply_text shows as a single subtitle block.

## Test Steps
1) Ensure `/interact` returns segments (mock can be edited for testing).
2) Send a message; observe subtitle timing.
3) Confirm fallback behavior when segments absent.

## DoD
- [ ] Segments timing works
- [ ] Fallback to reply_text works
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- None required
