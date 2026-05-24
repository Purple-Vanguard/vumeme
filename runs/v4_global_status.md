# V4 Global Status

- Date: 2026-05-24
- Gate context: 03-Review-Gate remains **RESTRICT**.
- Evidence class: preflight/readiness only (not manuscript evidence).

## Task 1 — EXP1 scenario diversity readiness repair
- Status: **Completed (bounded validation shard only)**.
- Files changed:
  - `runs/v4_exp1/main_scenarios_exp1.csv`
  - `runs/v4_exp1/events_validation_shard.csv`
  - `runs/v4_exp1/metrics_validation_shard.csv`
  - `tools/recompute_exp1_metrics.py`
  - `runs/v4_exp1/EXP1_Scenario_Diversity_Repair_Handoff_03-Review-Gate.md`
  - `runs/v4_global_status.md`
- Positive natural main-scenario evidence observed:
  - TCR-positive: yes (`exp1-main-tcr-001`)
  - TIR-positive: yes (`exp1-main-tir-001`)
  - TFR-positive: yes (`exp1-main-tfr-001`)
- Bounded/core execution readiness: **READY_FOR_BOUNDED_CORE**.
- Known limitations:
  - This is a bounded validation shard, not full EXP1 bounded/core grid execution.
  - Requested authority files were mostly absent from this checkout.
- Branch/provenance note:
  - Target branch requested: `iconip-v4-risk-attribution`
  - Local runtime branch: `work`
  - Readiness repair commit: `9ca99045743108e35016261d68c6b50b24349ba9`
  - Upstream lineage: not resolvable locally (no remote-tracking branch metadata)
