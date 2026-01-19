# PRD-06 — TTS Integration (Minimal + Caching + Fallback)

## Goal (one sentence)
- Convert reply_text into playable audio with caching and graceful fallback.

## In Scope
- Backend TTS integration outputs:
  - `audio.type="url"` (preferred) OR `base64` (choose one)
  - `audio.duration_ms` best-effort
- Cache audio artifacts for repeated identical text
- Failure handling:
  - if TTS fails, set `audio.type="none"` and `meta.fallback_reason=tts_failed`

## Out of Scope
- No voice selection UI
- No perfect subtitle/audio sync

## Acceptance Criteria
1) Given a normal request, when /interact returns, then response includes audio and frontend plays it.
2) Given identical reply_text repeats, when requested again, then cache_hit is true and the same artifact is reused.
3) Given TTS fails, then audio.type="none" and UI still shows subtitles + overlay.

## Test Steps
1) Configure TTS key via env vars.
2) Send a message; confirm audio plays.
3) Repeat; confirm cache reuse.
4) Break TTS config; confirm fallback.

## DoD
- [ ] Audio generated and playable
- [ ] Cache implemented and observable
- [ ] Fallback works without breaking UI
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- meta.tts_char_count
- meta.fallback_reason
- cache_hit
