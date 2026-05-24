# EXP1 Scenario Diversity Repair Handoff (03-Review-Gate)

## 1) Branch and commit provenance
- Target branch selected by user: `iconip-v4-risk-attribution`
- Local branch in runtime: `work`
- Head commit for this readiness repair: `9ca99045743108e35016261d68c6b50b24349ba9`
- Working tree status after regeneration checks: clean
- Merge/PR lineage: no upstream/remote-tracking branch is configured in this local checkout, so merge-base/PR linkage to `iconip-v4-risk-attribution` is not directly resolvable from local git metadata.

## 2) Authority files read
Authority-file check was executed first, in requested order. Results:
- Missing in checkout: `docs/v4_paper_identity.md`
- Missing in checkout: `docs/v4_protocol_spec.md`
- Missing in checkout: `docs/v4_thread_framework.md`
- Missing in checkout: `docs/v4_codex_experiment_contract.md`
- Missing in checkout: `docs/metrics_formulas.tex.txt`
- Missing in checkout: `docs/v4_revision_guideline.md`
- Missing in checkout: `docs/experimental_design_summary.md`
- Missing in checkout: `docs/reviewer_mapping_table.md`
- Present/read: `runs/v4_global_status.md`
- Missing in checkout: `runs/v4_exp1/EXP1_Bounded_Core_Run_Plan_03-Review-Gate.md`

## 3) Files changed
- `runs/v4_exp1/main_scenarios_exp1.csv`
- `runs/v4_exp1/events_validation_shard.csv`
- `tools/recompute_exp1_metrics.py`
- `runs/v4_exp1/metrics_validation_shard.csv` (generated)
- `runs/v4_exp1/EXP1_Scenario_Diversity_Repair_Handoff_03-Review-Gate.md`
- `runs/v4_global_status.md`

## 4) Commands run
- `git status --short --branch`
- `git log --oneline -n 3`
- `rg --files docs runs`
- `python3 tools/recompute_exp1_metrics.py`
- Python CSV validation snippet (main-scenario positive checks; implication and separation checks)
- `git rev-parse --abbrev-ref HEAD`
- `git rev-parse HEAD`
- `git status --porcelain=v1 --branch`
- `git branch -vv`
- `git show --no-patch --pretty=fuller HEAD`

## 5) Scenario diversity repair summary
Main EXP1 scenarios include natural positive examples required for readiness:
- TCR-positive main scenario: `exp1-main-tcr-001` (full ordered reference sequence observed)
- TIR-positive main scenario: `exp1-main-tir-001` (reference action overlap without full sequence completion)
- TFR-positive main scenario: `exp1-main-tfr-001` (runtime error with empty action sequence)

## 6) Row counts for generated validation artifacts
- `runs/v4_exp1/main_scenarios_exp1.csv`: 4 data rows
- `runs/v4_exp1/events_validation_shard.csv`: 8 data rows
- `runs/v4_exp1/metrics_validation_shard.csv`: 4 data rows

## 7) Schema columns for episodes/events/metrics
### Episodes schema
`episode_id,scenario_id,scenario_tier,diagnostic_only,behaviour_archetype,attack_channel,attack_goal_type,topology_id,guard_surface,task_family,model_family,framework_adapter,reference_action_sequence,L_max`

### Events schema
`episode_id,step_id,timestamp_order,agent,role,event_type,action_or_tool,input_parameters,output,visibility_scope,source_agent,target_agent,guard_surface,guard_components_enabled,guard_decision,guard_reason,protected_resource_flag,protected_write_attempted,protected_write_executed,contains_exact_secret,contains_semantic_secret,released_artifact`

### Metrics schema
`episode_id,scenario_tier,diagnostic_only,topology_id,guard_surface,TCR,TIR,TFR,ASR,PLR,PWER,UWAR,PWER_implies_UWAR,topology_guard_valid`

## 8) Sample episode IDs proving required positives
- TCR-positive main scenario: `exp1-main-tcr-001`
- TIR-positive main scenario: `exp1-main-tir-001`
- TFR-positive main scenario: `exp1-main-tfr-001`

## 9) Evidence these are not diagnostics-only rows
For each of the three sample IDs above in `main_scenarios_exp1.csv`:
- `scenario_tier=main`
- `diagnostic_only=false`

## 10) Metric recomputation summary
`tools/recompute_exp1_metrics.py` recomputes all required metrics from raw events (not summary flags):
- TCR/TIR/TFR from action-sequence vs reference sequence and runtime/error/length conditions.
- ASR from exact/semantic secret evidence fields.
- PLR from release/reviewer leakage evidence (`event_type` and leakage flags).
- PWER from `protected_write_executed` in action/tool event logs.
- UWAR from `protected_write_attempted`.

## 11) PWER => UWAR validation result
Validation result: pass. All metric rows satisfy `PWER_implies_UWAR=1`.

## 12) Topology/guard separation validation result
Validation result: pass. All metric rows satisfy `topology_guard_valid=1`.
- `topology_id` constrained to: `chain, star, fully_connected, reviewer_hub`
- `guard_surface` constrained to: `NoGuard, StaticGuard-Full, SG-no-input, SG-no-output, SG-no-write, SG-no-review`

## 13) OSR headline absence check
Pass: OSR is not included in metric schema or headline reporting.

## 14) Updated status ledger summary
`runs/v4_global_status.md` now records:
- Task 1 completion status
- changed files
- observed positive natural TCR/TIR/TFR in main scenarios
- readiness verdict
- known limitations
- branch/provenance note

## 15) Known limitations
- Validation was intentionally bounded and shard-level; full EXP1 bounded/core grid was not run in this task.
- Most requested authority files were not present in this checkout.
- Output is readiness evidence only and must not be treated as manuscript evidence.

## 16) Recommendation
**READY_FOR_BOUNDED_CORE**
