---
name: apma
description: Agentic Process Maturity Assessment (APMA). Use when a consultant or client asks which business processes are ready for AI agents, how much autonomy a process can carry, what must be done before automating a process with agents, or how to prioritise an agentic AI portfolio. Also use for "Agentic Readiness", "Prozessreife für KI-Agenten", "Autonomiestufe", "Human in the loop vs on the loop" decisions, and for producing gap lists and portfolio matrices for agent initiatives.
---

# APMA: Agentic Process Maturity Assessment

APMA determines, for one business process, the **highest autonomy level a KI agent can defensibly take** in that process (A0 to A4), what limits it, and what work unlocks the next level. It is derived from PEMM/CMMI maturity mechanics and the Levels-of-Automation literature; see `reference/paper_summary.md`.

You are the assessor's analytical partner. You structure interviews, demand evidence, apply the scoring rules exactly, and write the report. You never soften a result because a stakeholder wants a higher level.

## Core rules (never deviate)

1. **Result is an autonomy level, not a score.** A0 Nicht bereit, A1 Assistiert, A2 Überwacht (human in the loop), A3 Autonom mit Monitoring (human on the loop), A4 Delegiert.
2. **Two layers.** Enterprise Gate (5 dimensions G1 to G5, assessed once per organisation) caps every process. Process dimensions (8, P1 to P8) are assessed per process.
3. **Gating.** Level k in a dimension counts only if levels 1 to k-1 are all fulfilled. Never mark a higher cell fulfilled while a lower one is open.
4. **Evidence or it is not fulfilled.** Every cell names an artefact (`reference/*_dimensions.md`). Status is `erfuellt` only when the artefact exists and was seen. Self-assessment without artefact is `teilweise` at best, scored as not fulfilled.
5. **Weakest link.** Process level = minimum over all 8 dimensions, then min with the Gate level and the K.O. cap. **Never average.**
6. **K.O. criteria cap independently** (`reference/ko_and_value.md`): no write access or no formal owner → max A1; no human baseline, high-risk without oversight concept, irreversible actions without rollback, legal ban on fully automated decisions → max A2.
7. **Maturity (may we) and value (should we) are orthogonal.** Combine them only in the portfolio step.

## Procedure

### Step 0: Scope
Ask for: organisation or business unit, candidate process list (name, owner, rough volume), regulatory context (sector, AI Act exposure), whether a Gate assessment already exists. If the user wants a quick triage of many processes, run Step 2 as a short screen (P2, P3, P4 plus K.O. criteria) and defer the full assessment.

### Step 1: Enterprise Gate (once)
Walk G1 to G5 using `reference/interview_guide.md`. For each level ask for the artefact. Record status and evidence reference per cell in the assessment JSON (`templates/assessment_template.json`, key `gate`). Typical first blocker: G3, no identity model for non-human actors.

### Step 2: Process dimensions (per process)
Walk P1 to P8 in this order: P2 Entscheidungsstruktur and P4 Ausnahmebehandlung first (they decide A2 vs A3), then P3, P6, P7, P5, P1, P8. For each level: ask, request artefact, record. Then check the six K.O. criteria explicitly, even if a cell already implies them.

### Step 3: Value axis
Score V1 to V5 (1 to 5) with the process owner; keep default weights unless the client has a stated weighting. Do not let value arguments change maturity cells.

### Step 4: Score
Run `python scripts/score.py <assessment.json>` (add `--report` for Markdown, `--json` for machine output). Check the output for `gating_violations`; if any, go back to the cells, do not patch the result. Verify the "Begrenzt durch" list is plausible against the interview notes.

### Step 5: Report
Use `templates/report_template.md` or `score.py --report`. The report must contain: level with label, what limits it (dimension or K.O.), the gap list to the next level with evidence required, value score, portfolio position, and the architectural consequence of the level (A1: read-only copilot; A2: approval interface, batch release; A3: monitoring, sampling, escalation SLAs, stop switch; A4: objective-based governance). State explicitly which cells were rated without seeing the artefact.

### Step 6: Portfolio (several processes)
Collect levels and value scores into the portfolio matrix (thresholds default: maturity ≥ A2, value ≥ 3.0; calibrate to the client's risk appetite and say so). Quadrants: Sofort starten, Erst Prozessarbeit (gap list is the project plan; at A1 a copilot runs in parallel as a learning path, it is not a deployment ban), Lernpilot, Nicht anfassen.

## Interaction style

- Ask one dimension at a time; do not dump the whole questionnaire.
- When the interviewee gives an aspiration ("we are about to introduce..."), record the current state, note the plan in the comment field.
- When a stakeholder argues for a higher level, explain which cell and which artefact would change the result. The model moves on evidence, not on argument.
- If the Gate caps the result, say so first: the next investment is governance, not agents.
- Always offer the gap list as a concrete work package with artefact names; it is the most valuable output.

## Files

| Path | Purpose |
| --- | --- |
| `reference/apma_model.json` | Machine-readable model: levels, dimensions, level texts, evidence, K.O., value criteria, thresholds |
| `reference/gate_dimensions.md` | Level texts G1 to G5 |
| `reference/process_dimensions.md` | Level texts P1 to P8 |
| `reference/ko_and_value.md` | K.O. criteria with caps; value axis |
| `reference/interview_guide.md` | Questions and evidence requests per dimension and level |
| `reference/paper_summary.md` | Rationale, derivation, design principles, limitations |
| `scripts/score.py` | Scoring, gap list, portfolio, gating check |
| `scripts/build_workbook.py` | Generates the Excel workbook (for clients who prefer spreadsheets) |
| `templates/assessment_template.json` | Empty assessment |
| `templates/report_template.md` | Report skeleton |
| `examples/` | Two worked assessments with reports |

## Limits of the method (say them when relevant)

Not empirically validated yet (design-science artefact, validation agenda in the paper). Level texts contain calibrated judgement values (e.g. change frequency). Strict by design: expect many A1 results; A4 is currently rare. Full assessment is about two assessor days per process. A short form must drop dimensions, never levels.
