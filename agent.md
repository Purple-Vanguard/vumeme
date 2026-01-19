# agent.md — Vumeme Long-Term Memory (Project Constitution)

> Purpose: This is the project's single source of truth (SSOT) and must be read first.
> Any agent (Ralph/Codex/automation) MUST read this file before `process.txt`.

## 0) North Star & Scope Lock (Non-negotiable)

### North Star (fixed)
We are NOT building a "video platform".
We are building:
**an embeddable interactive Video Agent (Web component / iframe) for ONE vertical use case.**

**MVP single success metric**
After user input, within **2–4 seconds**, the user receives stable **visual + audio feedback** and wants to come back.

### Forbidden during MVP (No-go)
- ❌ Real-time high-quality text-to-video generation per interaction
- ❌ Creator platform / UGC pipeline / multi-tenant billing / revenue share / moderation back office
- ❌ Complex plot graphs, multi-character ensembles, long-horizon story consistency
- ❌ Native iOS/Android or desktop clients (Web only, mobile-first + iframe)
- ❌ Self-built infra (custom streaming protocol, transcoding clusters, model serving)

### Allowed change surface (MVP)
- Base layer: **one looping background video stays constant**
- Variation: **overlay layer** (subtitles, glow, symbols, rhythm) + **audio/TTS**
- Interaction output: `reply_text + director_tags` (structured)

---

## 1) Target Experience (User POV)

User types one sentence → immediately sees overlay change + first subtitle segment → shortly hears voice reply.
Any failure must degrade gracefully (no blank screens, no hard errors).

---

## 2) Core Concepts

- **Video Agent**: fixed character + fixed look (MVP: single look) + interactive feedback
- **Loop Video**: background loop (mp4/webm), always playable
- **Overlay**: Canvas or HTML/CSS layer driven by director tags
- **director_tags**: fixed enumerations; LLM cannot invent new tags
- **Fallback Ladder**: mandatory degradation path to keep demo always working

---

## 3) director_tags (Fixed Enum Dictionary)

> LLM can ONLY choose from these values. Backend MUST validate + sanitize.

```json
{
  "emotion": ["calm", "encouraging", "serious"],
  "visual_action": ["CALM_GLOW", "TEACHING_TEXT", "BLESSING_LIGHT"],
  "pace": ["slow", "normal"]
}
```

### Frontend mapping principle
LLM outputs tags only (no free parameters like colors/positions/intensity).
- `CALM_GLOW`: breathing glow + subtle particles
- `TEACHING_TEXT`: larger subtitles + emphasis
- `BLESSING_LIGHT`: edge light beams + symbol reveal

---

## 4) API Contract (`POST /interact`)

### Request (recommended)
```json
{
  "session_id": "string",
  "user_text": "string",
  "lang": "en|zh",
  "client_ts": 1730000000,
  "last_state": {
    "emotion": "calm",
    "visual_action": "CALM_GLOW",
    "pace": "slow"
  }
}
```

### Response (required fields)
```json
{
  "request_id": "string",
  "reply_text": "string",
  "director_tags": {
    "emotion": "calm",
    "visual_action": "CALM_GLOW",
    "pace": "slow"
  },
  "segments": [
    { "t": 0.0, "text": "string" }
  ],
  "audio": {
    "type": "url|base64|none",
    "value": "string",
    "duration_ms": 0
  },
  "meta": {
    "latency_ms": 0,
    "token_estimate": 0,
    "tts_char_count": 0,
    "cost_estimate_usd": 0,
    "fallback_reason": "none|invalid_tags|llm_failed|tts_failed|timeout|other"
  }
}
```

### Hard rules
- `director_tags` must be valid; unknown values are sanitized to defaults
- `reply_text` must be short (1–2 sentences, 3–8s TTS)
- `segments` can be coarse but must be usable (else show full text)
- `audio` may fail; failure must set `fallback_reason` and trigger graceful UI behavior

---

## 5) Fallback Ladder (Mandatory)

1) **LLM invalid/failed** → default copy + default tags
2) **TTS failed** → subtitles + overlay only; optionally browser SpeechSynthesis as backup
3) **Audio delayed** → render overlay + first subtitle segment first; then attach audio when ready
4) **Frontend asset failures** → pure text mode still works

Principle: the demo must always be deliverable and operable.

---

## 6) Logging & Observability (Minimum Operable)

Every interaction must record (JSONL or SQLite):
- request_id, session_id, timestamp
- user_text_length (avoid storing raw sensitive text; truncate/hash if needed)
- final director_tags (after sanitation)
- latency_ms, token_estimate, tts_char_count, cost_estimate_usd
- fallback_reason
- cache_hit (if any)

---

## 7) Repo Structure (suggested stable layout)

```
/
  agent.md
  process.txt
  /prd/
    index.md
    PRD-TEMPLATE.md
    PRD-00-...
    ...
  /frontend/
  /backend/
  /assets/
  /scripts/
```

---

## 8) Ralph/Codex Collaboration Rules (Enforced)

- One PRD = one PR = independently demoable/acceptable
- Prefer ≤ 5 files changed (or ≤ 400 net LOC) per PR; otherwise split PRD
- One dimension per round (frontend OR backend OR logging OR LLM OR TTS OR assets)
- No "opportunistic refactors" unless explicitly in PRD scope


---

## Codex Cloud Loop (GitHub, No OpenAI API Key)

### Why this exists
We run Codex via the GitHub integration (cloud tasks) to avoid using `OPENAI_API_KEY` in CI.
Codex is triggered by PR comments that mention `@codex`. Anything other than `@codex review` starts a cloud task.  

### Source of truth for the loop
- Backlog state machine: `prd/index.md`
  - Next work item is the first `[TODO]` in the MVP path: PRD-00 → PRD-06.
- Short-term log: `process.txt`
  - Used for recording what happened (Goal / shipped / acceptance / lessons / next).
  - Do not rely on humans manually editing NEXT_PRD/NEXT_MODE.

### One PRD = one PR
For every PRD implementation PR:
1) Implement ONLY the PRD “In Scope”.
2) Run the PRD Test Steps and report results in the PR description.
3) Update `prd/index.md`:
   - Mark the PRD as `[DONE]`.
4) Update `process.txt`:
   - Append one new round block with Goal / What shipped / Acceptance / Lessons / Next.
   - Optionally update machine fields, but the canonical scheduler is `prd/index.md`.

### Repair loop (bugfix inside the same PR)
- If CI fails or review requests changes:
  - Prefer fixing within the same PR (multiple commits are OK).
  - Reviewer can comment: `@codex fix only what is required to satisfy this PRD acceptance criteria and CI`.
- If fixes exceed scope/size, create a new PRD (e.g., PRD-02B Bugfix) instead of scope creep.

### Merge policy
All Codex PRs must be merged via normal review process (no direct pushes to `interactive_chain`).
