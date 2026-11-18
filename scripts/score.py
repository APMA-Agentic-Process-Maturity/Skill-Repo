#!/usr/bin/env python3
"""APMA scoring: assessment JSON in, maturity level, gap list and portfolio position out.

Usage:
    python scripts/score.py assessment.json            # human-readable summary
    python scripts/score.py assessment.json --json     # machine-readable result
    python scripts/score.py assessment.json --report   # Markdown report

Rules implemented (see paper, section 6.6):
    l(d)   = highest level k such that levels 1..k are all "erfuellt" (gating)
    L_G    = min over gate dimensions
    L_K    = min cap over KO criteria that apply (4 if none)
    A(P)   = min( min_d l(d), L_G, L_K )
    Gap(P) = all cells at level A(P)+1 that are not "erfuellt"
"""
import json, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = json.load(open(os.path.join(HERE, "..", "reference", "apma_model.json"), encoding="utf-8"))
LABELS = {l["level"]: l["label"] for l in MODEL["autonomy_levels"]}
OK = {"erfuellt", "erfüllt", "ok", "yes", "true", "1"}


def _ok(cell):
    if isinstance(cell, dict):
        return str(cell.get("status", "")).strip().lower() in OK
    return str(cell).strip().lower() in OK


def level_of(dim_cells):
    """Gating: highest k with all 1..k fulfilled."""
    k = 0
    while k < 4 and _ok(dim_cells.get(str(k + 1), {})):
        k += 1
    return k


def gating_violations(dim_id, dim_cells):
    v = []
    for k in range(2, 5):
        if _ok(dim_cells.get(str(k), {})) and not _ok(dim_cells.get(str(k - 1), {})):
            v.append(f"{dim_id}: Stufe {k} erfüllt, Stufe {k-1} nicht (Gating-Verstoß)")
    return v


def score(a):
    gate = a.get("gate", {})
    proc = a.get("process_dimensions", {})
    ko = a.get("ko", {})
    val = a.get("value", {})
    th = a.get("thresholds", MODEL["portfolio_thresholds"])

    gate_levels = {d["id"]: level_of(gate.get(d["id"], {})) for d in MODEL["gate_dimensions"]}
    proc_levels = {d["id"]: level_of(proc.get(d["id"], {})) for d in MODEL["process_dimensions"]}
    L_G = min(gate_levels.values())
    min_D = min(proc_levels.values())

    ko_hits = [k for k in MODEL["ko_criteria"] if ko.get(k["id"]) in (True, "true", "ja", "Ja", 1)]
    L_K = min([k["cap"] for k in ko_hits], default=4)

    A = min(min_D, L_G, L_K)

    # what limits
    limited_by = []
    if L_K == A and ko_hits:
        limited_by += [f"K.O. {k['id']}: {k['text']} (Cap A{k['cap']})" for k in ko_hits if k["cap"] == A]
    if L_G == A:
        limited_by += [f"Unternehmens-Gate {g}: {next(d['name'] for d in MODEL['gate_dimensions'] if d['id']==g)}" for g, lv in gate_levels.items() if lv == A]
    if min_D == A:
        limited_by += [f"Prozessdimension {p}: {next(d['name'] for d in MODEL['process_dimensions'] if d['id']==p)}" for p, lv in proc_levels.items() if lv == A]

    # gap list to next level
    nxt = A + 1
    gap = []
    if nxt <= 4:
        for d in MODEL["gate_dimensions"]:
            if not _ok(gate.get(d["id"], {}).get(str(nxt), {})):
                lv = d["levels"][nxt - 1]
                gap.append({"scope": "gate", "dimension": d["id"], "name": d["name"], "level": nxt, "requirement": lv["requirement"], "evidence": lv["evidence"]})
        for d in MODEL["process_dimensions"]:
            if not _ok(proc.get(d["id"], {}).get(str(nxt), {})):
                lv = d["levels"][nxt - 1]
                gap.append({"scope": "process", "dimension": d["id"], "name": d["name"], "level": nxt, "requirement": lv["requirement"], "evidence": lv["evidence"]})
        for k in ko_hits:
            if k["cap"] < nxt:
                gap.append({"scope": "ko", "dimension": k["id"], "name": k["text"], "level": nxt, "requirement": "K.O.-Kriterium beseitigen", "evidence": ""})

    # value
    ws, ss = 0.0, 0.0
    complete = True
    for v in MODEL["value_criteria"]:
        cell = val.get(v["id"], {})
        w = float(cell.get("weight", v["default_weight"]))
        s = cell.get("score")
        if s is None:
            complete = False
            continue
        ws += w
        ss += w * float(s)
    value_score = round(ss / ws, 2) if complete and ws > 0 else None

    portfolio = None
    if value_score is not None:
        hi_m = A >= th.get("maturity", 2)
        hi_v = value_score >= th.get("value", 3.0)
        portfolio = {(True, True): "Sofort starten", (False, True): "Erst Prozessarbeit", (True, False): "Lernpilot", (False, False): "Nicht anfassen"}[(hi_m, hi_v)]

    violations = []
    for d in MODEL["gate_dimensions"]:
        violations += gating_violations(d["id"], gate.get(d["id"], {}))
    for d in MODEL["process_dimensions"]:
        violations += gating_violations(d["id"], proc.get(d["id"], {}))

    return {
        "process": a.get("process", {}),
        "gate_levels": gate_levels, "L_G": L_G,
        "process_levels": proc_levels, "min_D": min_D,
        "ko_hits": [k["id"] for k in ko_hits], "L_K": L_K,
        "maturity": A, "maturity_label": LABELS[A],
        "limited_by": limited_by,
        "gap": gap, "next_level": nxt if nxt <= 4 else None,
        "value_score": value_score, "portfolio": portfolio,
        "gating_violations": violations,
    }


def summary(r):
    p = r["process"]
    out = [f"APMA Ergebnis: {p.get('name','(Prozess)')}",
           f"  Autonomiestufe:      {r['maturity_label']}",
           f"  min Prozessdim.:     {r['min_D']}   Gate: {r['L_G']}   K.O.-Cap: {r['L_K']}",
           f"  Begrenzt durch:      " + ("; ".join(r["limited_by"]) or "-"),
           f"  Wert-Score:          {r['value_score'] if r['value_score'] is not None else 'fehlt'}",
           f"  Portfolio:           {r['portfolio'] or 'Wert-Score fehlt'}"]
    if r["gating_violations"]:
        out.append("  Gating-Verstöße:     " + "; ".join(r["gating_violations"]))
    if r["gap"]:
        out.append(f"  Gap-Liste zu A{r['next_level']} ({len(r['gap'])} Zellen):")
        for g in r["gap"]:
            out.append(f"    - [{g['dimension']}] {g['name']}: {g['requirement'][:110]}{'...' if len(g['requirement'])>110 else ''}")
    return "\n".join(out)


def report(r):
    p = r["process"]
    md = [f"# APMA Assessment: {p.get('name','')}", "",
          f"Bereich: {p.get('domain','')} · Owner: {p.get('owner','')} · Assessor: {p.get('assessor','')} · Datum: {p.get('date','')}", "",
          "## Ergebnis", "",
          f"**Agentische Reife: {r['maturity_label']}**", "",
          f"- Minimum Prozessdimensionen: {r['min_D']}", f"- Unternehmens-Gate: {r['L_G']}", f"- Wirksames K.O.-Cap: {r['L_K']}",
          f"- Begrenzt durch: {'; '.join(r['limited_by']) or '-'}",
          f"- Wert-Score: {r['value_score'] if r['value_score'] is not None else 'fehlt'}",
          f"- Portfolio-Position: **{r['portfolio'] or 'Wert-Score fehlt'}**", "",
          "## Dimensionen", "", "| Ebene | Dimension | Stufe |", "| --- | --- | --- |"]
    for d in MODEL["gate_dimensions"]:
        md.append(f"| Gate | {d['id']} {d['name']} | {r['gate_levels'][d['id']]} |")
    for d in MODEL["process_dimensions"]:
        md.append(f"| Prozess | {d['id']} {d['name']} | {r['process_levels'][d['id']]} |")
    if r["ko_hits"]:
        md += ["", "## Wirksame K.O.-Kriterien", ""] + [f"- {k}" for k in r["ko_hits"]]
    if r["gating_violations"]:
        md += ["", "## Gating-Verstöße (bitte korrigieren)", ""] + [f"- {v}" for v in r["gating_violations"]]
    if r["gap"]:
        md += ["", f"## Gap-Liste zur Stufe A{r['next_level']}", "", "Diese Zellen sind der Arbeitsplan vor der nächsten Autonomiestufe.", "",
               "| Ebene | Dimension | Anforderung | Evidenz |", "| --- | --- | --- | --- |"]
        for g in r["gap"]:
            md.append(f"| {g['scope']} | {g['dimension']} {g['name']} | {g['requirement']} | {g['evidence']} |")
    return "\n".join(md) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("assessment")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()
    a = json.load(open(args.assessment, encoding="utf-8"))
    r = score(a)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    elif args.report:
        print(report(r))
    else:
        print(summary(r))
