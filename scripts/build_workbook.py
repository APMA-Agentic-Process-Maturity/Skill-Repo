from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

FONT = "Arial"
LEVELS = ["A1 Assistiert", "A2 Überwacht", "A3 Autonom mit Monitoring", "A4 Delegiert"]
LABEL_FORMULA = '"A0 Nicht bereit","A1 Assistiert","A2 Überwacht","A3 Autonom mit Monitoring","A4 Delegiert"'

# ---------------------------------------------------------------- content
# Single source of truth: reference/apma_model.json
import json, os
_MP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reference", "apma_model.json")
_M = json.load(open(_MP, encoding="utf-8"))
ENTERPRISE = [(d["name"], [(l["requirement"], l["evidence"]) for l in d["levels"]]) for d in _M["gate_dimensions"]]
PROCESS = [(d["name"], [(l["requirement"], l["evidence"]) for l in d["levels"]]) for d in _M["process_dimensions"]]
KO = [(k["text"], k["cap"]) for k in _M["ko_criteria"]]
VALUE = [(v["name"], v["default_weight"], v["scale"]) for v in _M["value_criteria"]]

# ---------------------------------------------------------------- styles
def f(bold=False, size=10, color="000000", italic=False):
    return Font(name=FONT, bold=bold, size=size, color=color, italic=italic)

FILL_HEAD = PatternFill("solid", fgColor="1F3864")
FILL_SUB = PatternFill("solid", fgColor="D9E1F2")
FILL_INPUT = PatternFill("solid", fgColor="FFFFCC")
FILL_RESULT = PatternFill("solid", fgColor="E2EFDA")
FILL_GREEN = PatternFill("solid", fgColor="C6EFCE")
FILL_YELLOW = PatternFill("solid", fgColor="FFEB9C")
FILL_RED = PatternFill("solid", fgColor="FFC7CE")
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)

def head(ws, row, cols, texts):
    for c, t in zip(cols, texts):
        cell = ws.cell(row=row, column=c, value=t)
        cell.font = f(bold=True, color="FFFFFF")
        cell.fill = FILL_HEAD
        cell.alignment = CENTER
        cell.border = BORDER

def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = f(bold=True, size=14)
    if sub:
        ws["A2"] = sub
        ws["A2"].font = f(italic=True, color="595959")

def status_cf(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Erfüllt"'], fill=FILL_GREEN))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Teilweise"'], fill=FILL_YELLOW))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Offen"'], fill=FILL_RED))

def write_matrix(ws, dims, start_row, summary_row0):
    """Long-format detail table. Returns dict dim -> (first_row, last_row) of status cells.
    Also fills summary block starting at summary_row0 with per-dimension achieved level."""
    cols = list(range(1, 9))
    head(ws, start_row, cols, ["Dimension", "Stufe", "Anforderung (muss erfüllt sein, damit diese Autonomiestufe vertretbar ist)",
                               "Gefordertes Evidenz-Artefakt", "Status", "Nachweis / Fundstelle", "Kommentar", "Gating-Check"])
    dv = DataValidation(type="list", formula1='"Offen,Teilweise,Erfüllt"', allow_blank=False)
    ws.add_data_validation(dv)
    r = start_row + 1
    ranges = {}
    for dname, levels in dims:
        first = r
        for i, (req, art) in enumerate(levels):
            ws.cell(row=r, column=1, value=dname).font = f(bold=(i == 0))
            ws.cell(row=r, column=2, value=LEVELS[i]).font = f()
            ws.cell(row=r, column=3, value=req).font = f()
            ws.cell(row=r, column=4, value=art).font = f()
            s = ws.cell(row=r, column=5, value="Offen")
            s.font = f(color="0000FF"); s.fill = FILL_INPUT; s.alignment = CENTER
            dv.add(s)
            ws.cell(row=r, column=6).fill = FILL_INPUT
            ws.cell(row=r, column=7).fill = FILL_INPUT
            if i == 0:
                g = ws.cell(row=r, column=8, value="OK")
            else:
                g = ws.cell(row=r, column=8, value=f'=IF(AND(E{r}="Erfüllt",E{r-1}<>"Erfüllt"),"Verstoß: Vorstufe nicht erfüllt",IF(AND(E{r}="Teilweise",E{r-1}<>"Erfüllt"),"Hinweis: Vorstufe zuerst","OK"))')
            g.font = f(); g.alignment = CENTER
            for c in cols:
                ws.cell(row=r, column=c).border = BORDER
                if c in (3, 4, 6, 7):
                    ws.cell(row=r, column=c).alignment = WRAP
            ws.row_dimensions[r].height = 75
            r += 1
        ranges[dname] = (first, r - 1)
    status_cf(ws, f"E{start_row+1}:E{r-1}")
    ws.conditional_formatting.add(f"H{start_row+1}:H{r-1}", FormulaRule(formula=[f'ISNUMBER(SEARCH("Verstoß",H{start_row+1}))'], fill=FILL_RED))
    ws.conditional_formatting.add(f"H{start_row+1}:H{r-1}", FormulaRule(formula=[f'ISNUMBER(SEARCH("Hinweis",H{start_row+1}))'], fill=FILL_YELLOW))

    # summary block
    head(ws, summary_row0, [1, 2, 3], ["Dimension", "Erreichte Stufe (0-4)", "Bezeichnung"])
    sr = summary_row0 + 1
    for dname, _ in dims:
        a, b = ranges[dname]
        ws.cell(row=sr, column=1, value=dname).font = f()
        c = ws.cell(row=sr, column=2, value=f'=IF(E{a}<>"Erfüllt",0,IF(E{a+1}<>"Erfüllt",1,IF(E{a+2}<>"Erfüllt",2,IF(E{a+3}<>"Erfüllt",3,4))))')
        c.font = f(); c.alignment = CENTER
        l = ws.cell(row=sr, column=3, value=f"=CHOOSE(B{sr}+1,{LABEL_FORMULA})")
        l.font = f()
        for col in (1, 2, 3):
            ws.cell(row=sr, column=col).border = BORDER
        sr += 1
    return summary_row0 + 1, sr - 1

# ---------------------------------------------------------------- workbook
wb = Workbook()

# ---- Methode
ws = wb.active
ws.title = "Methode"
title(ws, "Agentic Process Maturity Assessment (APMA)", "Methode zur Ermittlung der Reife von Prozessen für die Integration agentischer KI")
lines = [
 ("Grundidee", True),
 ("Der Reifegrad eines Prozesses ist keine abstrakte Zahl, sondern die maximal vertretbare Autonomiestufe für einen Agenten in diesem Prozess. Das Assessment beantwortet zwei Fragen: Was darf man (Reife) und was soll man (Wert).", False),
 ("", False),
 ("Autonomiestufen", True),
 ("A0 Nicht bereit: Der Prozess ist nicht agentenfähig. Erst Prozessarbeit.", False),
 ("A1 Assistiert: Der Agent recherchiert, bereitet vor und schlägt vor. Der Mensch führt jede Handlung selbst aus (Copilot).", False),
 ("A2 Überwacht: Der Agent führt aus, der Mensch gibt einzelne Handlungen oder Batches frei (Human in the Loop).", False),
 ("A3 Autonom mit Monitoring: Der Agent führt aus, der Mensch wird nur bei Ausnahmen und über Stichproben einbezogen (Human on the Loop).", False),
 ("A4 Delegiert: Der Agent betreibt und verbessert den Prozess innerhalb definierter Leitplanken. Der Mensch steuert über Ziele und Budgets.", False),
 ("", False),
 ("Aufbau", True),
 ("Ebene 1, Unternehmens-Gate (Tab 'Unternehmens-Gate'): 5 Dimensionen x 4 Stufen. Kein Prozess kann über dem Unternehmenslevel liegen. Einmal pro Unternehmen oder Geschäftsbereich ausfüllen.", False),
 ("Ebene 2, Prozess-Assessment (Tab 'Prozess-Assessment'): 8 Dimensionen x 4 Stufen, K.O.-Kriterien und Wertachse. Pro Prozess den Tab kopieren (Rechtsklick auf den Tab, 'Verschieben oder kopieren', Kopie erstellen).", False),
 ("Portfolio (Tab 'Portfolio'): Reife und Wert aller bewerteten Prozesse in einer 2x2-Matrix mit Handlungsempfehlung.", False),
 ("", False),
 ("Scoring-Regeln", True),
 ("1. Jede Zelle (Dimension x Stufe) enthält prüfbare Anforderungen und ein gefordertes Evidenz-Artefakt. Status 'Erfüllt' nur mit vorliegendem Artefakt; Fundstelle in Spalte 'Nachweis' eintragen.", False),
 ("2. Gating innerhalb einer Dimension: Stufe n zählt nur, wenn alle Stufen unter n 'Erfüllt' sind. Die Spalte 'Gating-Check' markiert Verstöße rot. Die erreichte Stufe einer Dimension ist die höchste lückenlos erfüllte Stufe.", False),
 ("3. Weakest Link: Die Reifestufe eines Prozesses ist das Minimum über alle 8 Dimensionen, nicht der Durchschnitt. Ein Agent scheitert am schwächsten Glied.", False),
 ("4. Unternehmens-Gate: Die Prozess-Reifestufe wird zusätzlich durch das Unternehmenslevel gedeckelt (Minimum der 5 Unternehmensdimensionen).", False),
 ("5. K.O.-Kriterien deckeln unabhängig vom Rest. Trifft ein Kriterium zu, gilt das zugehörige Cap.", False),
 ("6. Ergebnis = MIN(Minimum Prozessdimensionen; Unternehmenslevel; wirksame K.O.-Caps).", False),
 ("7. Gap-Liste: Alle Zellen der nächsthöheren Stufe, die nicht 'Erfüllt' sind, bilden den Arbeitsplan vor der Automatisierung. Filter in Spalte 'Status' auf 'Offen' und 'Teilweise'.", False),
 ("", False),
 ("Wertachse und Portfolio", True),
 ("Reife sagt, ob man darf. Wert sagt, ob man soll. 5 Wertkriterien (1-5, gewichtbar) ergeben einen Wert-Score. Reife und Wert ergeben die Portfolio-Position: Sofort starten / Erst Prozessarbeit / Lernpilot / Nicht anfassen. Schwellenwerte im Tab 'Portfolio' anpassbar.", False),
 ("", False),
 ("Legende", True),
 ("Gelbe Zellen = Eingabefelder (Dropdowns oder Freitext). Grüne Zellen = berechnete Ergebnisse. Formeln nicht überschreiben.", False),
 ("", False),
 ("Herkunft und Abgrenzung", True),
 ("Mechanik (zwei Ebenen, vier Stufen je Dimension, Weakest-Link-Logik, Evidenzpflicht) angelehnt an M. Hammer, 'The Process Audit', Harvard Business Review, April 2007 (PEMM). Inhaltlich vollständig auf Agenteneignung umgebaut: PEMM misst Prozessorientierung, nicht Automatisierbarkeit. Regulatorische Bezüge: EU AI Act (insb. Art. 14 menschliche Aufsicht), DSGVO Art. 22, ISO/IEC 42001.", False),
 ("Richtwerte in den Stufentexten (z. B. Änderungsfrequenz 'nicht öfter als quartalsweise') sind Erfahrungswerte des Methodenautors, keine Normvorgaben, und sollten je Branche kalibriert werden.", False),
]
r = 4
for text, bold in lines:
    c = ws.cell(row=r, column=1, value=text)
    c.font = f(bold=bold, size=11 if bold else 10)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
ws.column_dimensions["A"].width = 150
for rr in range(4, r):
    if ws.cell(row=rr, column=1).value and len(str(ws.cell(row=rr, column=1).value)) > 150:
        ws.row_dimensions[rr].height = 45

# ---- Unternehmens-Gate
ws = wb.create_sheet("Unternehmens-Gate")
title(ws, "Ebene 1: Unternehmens-Gate", "Einmal pro Unternehmen/Geschäftsbereich. Das Unternehmenslevel deckelt jede Prozessbewertung.")
ws["A4"] = "Unternehmen / Bereich"; ws["A4"].font = f(bold=True)
ws["B4"].fill = FILL_INPUT; ws["B4"].font = f(color="0000FF")
ws["A5"] = "Assessment-Datum"; ws["A5"].font = f(bold=True)
ws["B5"].fill = FILL_INPUT; ws["B5"].font = f(color="0000FF"); ws["B5"].number_format = "DD.MM.YYYY"
s0, s1 = write_matrix(ws, ENTERPRISE, start_row=17, summary_row0=7)
ws.cell(row=s1 + 1, column=1, value="UNTERNEHMENSLEVEL (Minimum)").font = f(bold=True)
c = ws.cell(row=s1 + 1, column=2, value=f"=MIN(B{s0}:B{s1})"); c.font = f(bold=True); c.fill = FILL_RESULT; c.alignment = CENTER
l = ws.cell(row=s1 + 1, column=3, value=f"=CHOOSE(B{s1+1}+1,{LABEL_FORMULA})"); l.font = f(bold=True); l.fill = FILL_RESULT
for col in (1, 2, 3):
    ws.cell(row=s1 + 1, column=col).border = BORDER
ENT_LEVEL_CELL = f"'Unternehmens-Gate'!$B${s1+1}"
ws.cell(row=15, column=1, value="Detailbewertung").font = f(bold=True, size=12)
for col, w in zip("ABCDEFGH", [28, 24, 70, 40, 12, 32, 32, 26]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "A18"

# ---- Prozess-Assessment
ws = wb.create_sheet("Prozess-Assessment")
title(ws, "Ebene 2: Prozess-Assessment", "Pro Prozess diesen Tab kopieren. Ergebnis = maximal vertretbare Autonomiestufe.")
for i, lab in enumerate(["Prozessname", "Bereich / Domäne", "Prozess-Owner", "Assessment-Datum", "Assessor"]):
    ws.cell(row=4 + i, column=1, value=lab).font = f(bold=True)
    c = ws.cell(row=4 + i, column=2); c.fill = FILL_INPUT; c.font = f(color="0000FF")
ws["B7"].number_format = "DD.MM.YYYY"

# Summary of dimensions at rows 11..19 ; detail from row 52
ws.cell(row=10, column=1, value="Dimensionen").font = f(bold=True, size=12)
s0, s1 = write_matrix(ws, PROCESS, start_row=52, summary_row0=11)
ws.cell(row=50, column=1, value="Detailbewertung").font = f(bold=True, size=12)
MIN_DIM = f"MIN(B{s0}:B{s1})"

# K.O. block rows 22..29
ws.cell(row=21, column=1, value="K.O.-Kriterien (deckeln unabhängig vom Rest)").font = f(bold=True, size=12)
head(ws, 22, [1, 2, 3, 4], ["Kriterium", "Trifft zu?", "Cap (max. Stufe)", "Wirksames Cap"])
dvjn = DataValidation(type="list", formula1='"Nein,Ja"', allow_blank=False)
ws.add_data_validation(dvjn)
kr = 23
for text, cap in KO:
    ws.cell(row=kr, column=1, value=text).font = f()
    ws.cell(row=kr, column=1).alignment = WRAP
    a = ws.cell(row=kr, column=2, value="Nein"); a.fill = FILL_INPUT; a.font = f(color="0000FF"); a.alignment = CENTER
    dvjn.add(a)
    cc = ws.cell(row=kr, column=3, value=cap); cc.alignment = CENTER; cc.font = f()
    w = ws.cell(row=kr, column=4, value=f'=IF(B{kr}="Ja",C{kr},4)'); w.alignment = CENTER; w.font = f()
    for col in (1, 2, 3, 4):
        ws.cell(row=kr, column=col).border = BORDER
    ws.row_dimensions[kr].height = 30
    kr += 1
KO_FIRST, KO_LAST = 23, kr - 1
ws.conditional_formatting.add(f"B{KO_FIRST}:B{KO_LAST}", CellIsRule(operator="equal", formula=['"Ja"'], fill=FILL_RED))

# Wert block rows 32..38
ws.cell(row=31, column=1, value="Wertachse (soll man?)").font = f(bold=True, size=12)
head(ws, 32, [1, 2, 3, 4], ["Kriterium", "Gewicht", "Score (1-5)", "Skala"])
dv15 = DataValidation(type="whole", operator="between", formula1="1", formula2="5")
ws.add_data_validation(dv15)
vr = 33
for text, wgt, scale in VALUE:
    ws.cell(row=vr, column=1, value=text).font = f()
    g = ws.cell(row=vr, column=2, value=wgt); g.fill = FILL_INPUT; g.font = f(color="0000FF"); g.alignment = CENTER
    s = ws.cell(row=vr, column=3); s.fill = FILL_INPUT; s.font = f(color="0000FF"); s.alignment = CENTER
    dv15.add(s)
    ws.cell(row=vr, column=4, value=scale).font = f(italic=True, color="595959")
    for col in (1, 2, 3, 4):
        ws.cell(row=vr, column=col).border = BORDER
    vr += 1
V_FIRST, V_LAST = 33, vr - 1
ws.cell(row=vr, column=1, value="WERT-SCORE (gewichteter Mittelwert)").font = f(bold=True)
c = ws.cell(row=vr, column=3, value=f'=IF(COUNT(C{V_FIRST}:C{V_LAST})<{len(VALUE)},"",SUMPRODUCT(B{V_FIRST}:B{V_LAST},C{V_FIRST}:C{V_LAST})/SUM(B{V_FIRST}:B{V_LAST}))')
c.font = f(bold=True); c.fill = FILL_RESULT; c.alignment = CENTER; c.number_format = "0.0"
WERT_CELL = f"C{vr}"
for col in (1, 2, 3):
    ws.cell(row=vr, column=col).border = BORDER

# Result block rows 41..47
ws.cell(row=40, column=1, value="ERGEBNIS").font = f(bold=True, size=12)
res = [
 ("Minimum Prozessdimensionen", f"={MIN_DIM}"),
 ("Unternehmenslevel (Gate)", f"={ENT_LEVEL_CELL}"),
 ("Wirksames K.O.-Cap", f"=MIN(D{KO_FIRST}:D{KO_LAST})"),
 ("AGENTIC-MATURITY-STUFE", f"=MIN(B41:B43)"),
 ("Bezeichnung", f"=CHOOSE(B44+1,{LABEL_FORMULA})"),
 ("Begrenzt durch", f'=IF(B43=B44,"K.O.-Kriterium",IF(B42=B44,"Unternehmens-Gate","Prozessdimension: "&INDEX(A{s0}:A{s1},MATCH(B41,B{s0}:B{s1},0))))'),
 ("Wert-Score", f"={WERT_CELL}"),
 ("Portfolio-Empfehlung", f'=IF({WERT_CELL}="","Wert-Score fehlt",IF(AND(B44>=Portfolio!$B$3,{WERT_CELL}>=Portfolio!$B$4),"Sofort starten",IF(AND(B44<Portfolio!$B$3,{WERT_CELL}>=Portfolio!$B$4),"Erst Prozessarbeit",IF(AND(B44>=Portfolio!$B$3,{WERT_CELL}<Portfolio!$B$4),"Lernpilot","Nicht anfassen"))))'),
]
for i, (lab, frm) in enumerate(res):
    rr = 41 + i
    a = ws.cell(row=rr, column=1, value=lab); a.font = f(bold=lab.isupper())
    b = ws.cell(row=rr, column=2, value=frm); b.font = f(bold=lab.isupper()); b.fill = FILL_RESULT; b.alignment = CENTER
    if lab == "Wert-Score":
        b.number_format = "0.0"
    for col in (1, 2):
        ws.cell(row=rr, column=col).border = BORDER
ws.merge_cells("B46:D46"); ws.merge_cells("B48:D48")
ws["B46"].alignment = Alignment(horizontal="left", vertical="center")
ws["B48"].alignment = Alignment(horizontal="left", vertical="center")

for col, w in zip("ABCDEFGH", [34, 24, 70, 40, 12, 32, 32, 26]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "A53"

# ---- Portfolio
ws = wb.create_sheet("Portfolio")
title(ws, "Portfolio: Reife x Wert", "Ergebnisse aller Prozess-Assessments eintragen. Schwellenwerte anpassbar.")
ws["A3"] = "Schwelle Reife (Stufe ab der 'reif' gilt)"; ws["A3"].font = f(bold=True)
ws["B3"] = 2; ws["B3"].fill = FILL_INPUT; ws["B3"].font = f(color="0000FF"); ws["B3"].alignment = CENTER
ws["A4"] = "Schwelle Wert-Score (ab dem 'hoher Wert' gilt)"; ws["A4"].font = f(bold=True)
ws["B4"] = 3; ws["B4"].fill = FILL_INPUT; ws["B4"].font = f(color="0000FF"); ws["B4"].alignment = CENTER
ws["C3"] = "Standard: A2. Annahme des Methodenautors, nicht normativ."; ws["C3"].font = f(italic=True, color="595959")
ws["C4"] = "Standard: 3,0 auf Skala 1-5."; ws["C4"].font = f(italic=True, color="595959")

head(ws, 7, [1, 2, 3, 4, 5, 6, 7], ["Prozess", "Bereich", "Reifestufe (0-4)", "Bezeichnung", "Wert-Score (1-5)", "Quadrant", "Empfehlung"])
REC = {
 "Sofort starten": "Pilot auf der erreichten Autonomiestufe starten; Gap-Liste zur nächsten Stufe parallel abarbeiten.",
 "Erst Prozessarbeit": "Gap-Liste ist der Projektplan: fehlende Stufenanforderungen schließen, dann erneut bewerten.",
 "Lernpilot": "Pilot zum Fähigkeitsaufbau ohne Business-Case-Druck; Erkenntnisse auf wertvolle Prozesse übertragen.",
 "Nicht anfassen": "Keine Agenteninvestition; ggf. konventionelle Prozessverbesserung.",
}
dv04 = DataValidation(type="whole", operator="between", formula1="0", formula2="4")
ws.add_data_validation(dv04)
dvw = DataValidation(type="decimal", operator="between", formula1="1", formula2="5")
ws.add_data_validation(dvw)
example = ("Beispiel: Rechnungsprüfung Eingang", "Finance", 2, 3.8)
for i in range(20):
    rr = 8 + i
    for col in (1, 2, 3, 5):
        c = ws.cell(row=rr, column=col); c.fill = FILL_INPUT; c.font = f(color="0000FF")
    ws.cell(row=rr, column=3).alignment = CENTER
    ws.cell(row=rr, column=5).alignment = CENTER
    ws.cell(row=rr, column=5).number_format = "0.0"
    dv04.add(ws.cell(row=rr, column=3)); dvw.add(ws.cell(row=rr, column=5))
    if i == 0:
        ws.cell(row=rr, column=1, value=example[0]); ws.cell(row=rr, column=2, value=example[1])
        ws.cell(row=rr, column=3, value=example[2]); ws.cell(row=rr, column=5, value=example[3])
    d = ws.cell(row=rr, column=4, value=f'=IF(C{rr}="","",CHOOSE(C{rr}+1,{LABEL_FORMULA}))'); d.font = f()
    q = ws.cell(row=rr, column=6, value=f'=IF(OR(C{rr}="",E{rr}=""),"",IF(AND(C{rr}>=$B$3,E{rr}>=$B$4),"Sofort starten",IF(AND(C{rr}<$B$3,E{rr}>=$B$4),"Erst Prozessarbeit",IF(AND(C{rr}>=$B$3,E{rr}<$B$4),"Lernpilot","Nicht anfassen"))))')
    q.font = f(); q.alignment = CENTER
    e = ws.cell(row=rr, column=7, value=(f'=IF(F{rr}="","",IF(F{rr}="Sofort starten","{REC["Sofort starten"]}",'
                                         f'IF(F{rr}="Erst Prozessarbeit","{REC["Erst Prozessarbeit"]}",'
                                         f'IF(F{rr}="Lernpilot","{REC["Lernpilot"]}","{REC["Nicht anfassen"]}"))))'))
    e.font = f(); e.alignment = WRAP
    for col in range(1, 8):
        ws.cell(row=rr, column=col).border = BORDER
rng = "F8:F27"
ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Sofort starten"'], fill=FILL_GREEN))
ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Erst Prozessarbeit"'], fill=FILL_YELLOW))
ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Lernpilot"'], fill=FILL_SUB))
ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Nicht anfassen"'], fill=FILL_RED))
ws.cell(row=29, column=1, value="Zeile 8 ist ein Beispiel mit fiktiven Werten; überschreiben oder löschen. Quadrantenlogik: Reife >= Schwelle und Wert >= Schwelle = Sofort starten; Reife < Schwelle und Wert hoch = Erst Prozessarbeit; Reife hoch und Wert niedrig = Lernpilot; sonst Nicht anfassen.").font = f(italic=True, color="595959")
for col, w in zip("ABCDEFG", [36, 18, 16, 26, 16, 20, 70]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "A8"

for sheet in wb.worksheets:
    sheet.sheet_view.showGridLines = False

wb.save("Agentic_Maturity_Assessment.xlsx")
print("saved")
