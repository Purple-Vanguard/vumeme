# PRD-01 — director_tags Enums + Schema Validation + Sanitization (Backend)

## Goal (one sentence)
- Ensure `director_tags` are strictly validated against fixed enums and unknown values are sanitized to defaults.

## In Scope
- Define the enum dictionary:
  - emotion: calm | encouraging | serious
  - visual_action: CALM_GLOW | TEACHING_TEXT | BLESSING_LIGHT
  - pace: slow | normal
- Implement backend schema validation for `director_tags`
- Implement `sanitize_director_tags(input)`:
  - Unknown/missing fields → defaults
  - Always returns a complete valid `director_tags` object
- Add unit tests for validation/sanitization

## Out of Scope
- No LLM integration
- No frontend changes (unless strictly required to run tests)

## User Stories
- As the system, I want to enforce tag validity so that the UI remains controllable and consistent.
- As a developer, I want sanitizer defaults so that failures degrade gracefully.

## Acceptance Criteria
1) Given invalid tags, when sanitized, then output contains only allowed enum values and all required keys.
2) Given missing fields, when sanitized, then defaults are applied without error.
3) Given valid tags, when validated, then validation passes.

## Test Steps
1) Run unit tests: `npm test` or `pytest` (depending on stack).
2) Confirm test cases cover invalid/missing/valid tags.

## DoD
- [ ] Enum dictionary exists in a single central module
- [ ] Sanitizer exists and is used by response builders
- [ ] Unit tests pass
- [ ] Updated `prd/index.md` status
- [ ] Updated `process.txt`

## Telemetry
- Record `fallback_reason=invalid_tags` when sanitization changes values (if on runtime paths)
