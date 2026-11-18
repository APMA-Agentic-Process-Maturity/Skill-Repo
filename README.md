# APMA Skill: Agentic Process Maturity Assessment

Ein Skill-Paket für KI-augmentierte Berater und Assessoren. Es befähigt einen KI-Agenten (Claude Code, Claude, vergleichbare Agenten mit Skill-Unterstützung) dazu, ein APMA-Assessment methodisch korrekt zu führen: Interviews strukturieren, Evidenz einfordern, Scoring-Regeln exakt anwenden, Gap-Liste und Portfolio-Position ableiten, Report schreiben.

APMA bestimmt für einen Geschäftsprozess die höchste vertretbare Autonomiestufe eines KI-Agenten (A0 bis A4), was sie begrenzt und was die nächste Stufe erschließt. Methodik: siehe `reference/paper_summary.md` und das zugehörige Working Paper (CITATION.cff).

## Installation

Claude Code: Ordner nach `~/.claude/skills/apma` (persönlich) oder `.claude/skills/apma` (Projekt) kopieren. Der Skill wird automatisch geladen, wenn die Anfrage zu seiner `description` passt, oder explizit mit `/apma`.

Andere Agenten: `SKILL.md` als System- oder Kontextanweisung laden, `reference/` als Wissensbasis, `scripts/score.py` als Werkzeug.

Abhängigkeiten: Python 3.9+. Für `scripts/build_workbook.py` zusätzlich `openpyxl`.

## Nutzung

```bash
# leeres Assessment anlegen
cp templates/assessment_template.json kunde_prozess_x.json
# Zellen ausfüllen (status: offen | teilweise | erfuellt; evidence: Fundstelle)
# bewerten
python scripts/score.py kunde_prozess_x.json
python scripts/score.py kunde_prozess_x.json --report > kunde_prozess_x_report.md
# optional: Excel-Workbook für den Kunden
python scripts/build_workbook.py
```

Beispiele mit erwartetem Ergebnis: `examples/` (A1 Erst Prozessarbeit; A2 Sofort starten).

## Struktur

```
SKILL.md                      Anweisungen für den Agenten: Regeln, Vorgehen, Stil
reference/apma_model.json     Modell maschinenlesbar (Single Source of Truth)
reference/gate_dimensions.md  Stufentexte G1 bis G5
reference/process_dimensions.md  Stufentexte P1 bis P8
reference/ko_and_value.md     K.O.-Kriterien, Wertachse, Schwellen
reference/interview_guide.md  Fragen und Artefakte je Zelle
reference/paper_summary.md    Herleitung, Designprinzipien, Limitationen
scripts/score.py              Scoring, Gap-Liste, Portfolio, Gating-Check
scripts/build_workbook.py     Excel-Workbook erzeugen
templates/                    Assessment-JSON, Report-Vorlage
examples/                     Zwei ausgefüllte Assessments mit Report
```

## Regeln, die der Skill durchsetzt

Autonomiestufe statt Score · Gate deckelt Prozess · Gating innerhalb jeder Dimension · Evidenz oder nicht erfüllt · Minimum, nie Mittelwert · K.O.-Kriterien deckeln unabhängig · Reife und Wert orthogonal.

## Status

Version 1.0, November 2026. Design-Science-Artefakt, empirische Validierung ausstehend (Agenda im Paper). Ein unabhängig und zeitgleich entstandenes prozessorientiertes Readiness-Framework (Schmidt, Alt, Zimmermann, HICSS 2026) ist in `reference/paper_summary.md` abgegrenzt. Stufentexte und Caps sind kalibrierbar; Änderungen am Modell bitte nur in `reference/apma_model.json` und per `scripts/build_workbook.py` nachziehen.

## Zitieren

Siehe `CITATION.cff`.

## Lizenz

CC BY 4.0 für Methodik und Texte, MIT für Skripte. Siehe `LICENSE`.
