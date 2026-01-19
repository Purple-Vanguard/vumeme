# PRD-03 — Frontend Demo v0: Loop Video + Overlay State Machine (3 Visual Actions)

## Goal (one sentence)
- Provide immediate visual feedback using a looping video plus a clearly different overlay for each visual_action.

## In Scope
- Frontend page with:
  - Looping background video (local asset placeholder OK)
  - Overlay layer (Canvas or HTML/CSS)
  - Input + send button
  - Display `reply_text`
- Overlay state machine driven by `director_tags.visual_action`:
  - CALM_GLOW
  - TEACHING_TEXT
  - BLESSING_LIGHT
- Integrate with backend `/interact` (mock OK)

## Out of Scope
- No audio playback yet
- No timed subtitle segments yet (PRD-04)

## Acceptance Criteria
1) Given visual_action=CALM_GLOW, when rendered, then overlay shows a calm glow/breathing effect.
2) Given visual_action=TEACHING_TEXT, when rendered, then overlay emphasizes text (larger area or highlight).
3) Given visual_action=BLESSING_LIGHT, when rendered, then overlay shows beam/symbol effect.
4) Given user clicks send, then user sees a visible overlay change within ~1 second (local dev).

## Test Steps
1) Start backend + frontend.
2) Send messages and force each visual_action (e.g., temporary toggle or mock response).
3) Confirm each overlay state is clearly distinct.

## DoD
- [ ] Loop video plays continuously
- [ ] Overlay states implemented and distinct
- [ ] Hooked to `/interact`
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- (Optional) frontend `time_to_first_visual_ms` via console log
