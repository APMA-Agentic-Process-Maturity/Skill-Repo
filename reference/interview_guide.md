# APMA Interview-Leitfaden

Je Dimension: Einstiegsfrage, dann Stufenfragen aufsteigend. Nach jeder bejahten Stufe: "Zeigen Sie mir bitte [Artefakt]." Ohne Artefakt: Status `teilweise`, zählt nicht. Interviewdauer Richtwert: Gate 2 bis 3 Stunden, Prozess 3 bis 4 Stunden plus Artefaktprüfung.

Rollen: Gate mit CIO/CDO, KI-Verantwortlichem, Compliance, HR/Mitbestimmung. Prozess mit Prozess-Owner, zwei Sachbearbeitenden, IT-Verantwortlichem der Zielsysteme, Datenschutz.

## Unternehmens-Gate

### G1 Führung und Risikoappetit
- Einstieg: Wer im Haus darf entscheiden, dass ein System eine Entscheidung trifft, die bisher ein Mensch traf?
- A1: Gibt es einen benannten Sponsor und ein Budget für KI-Assistenz? → Budgetfreigabe, Sponsor-Nennung
- A2: Welches GL-Mitglied verantwortet agentische KI? Welche Handlungsklassen dürfen Agenten unter Freigabe ausführen? Wer haftet? → GL-Beschluss, Haftungszuordnung
- A3: Gibt es eine Autonomie-Policy mit Schwellenwerten (Betrag, Reichweite, Reversibilität)? Ist der Risikoappetit beziffert? → Policy-Dokument, Risikoappetit-Statement
- A4: Stehen Autonomieziele je Prozessdomäne in der Planung? → Strategie-/Planungsdokument

### G2 KI-Governance
- Einstieg: Wie kommt heute ein KI-Use-Case von der Idee in den Betrieb?
- A1: Nutzungsrichtlinie GenAI? Anlaufstelle? → Richtlinie
- A2: Use-Case-Register, Risikoeinstufung nach AI Act, DSFA-Prüfung, Oversight-Anforderungen je Klasse? → Register, Prozessbeschreibung
- A3: MRM mit Agentenkapitel, Vorfallsmanagement, Re-Zertifizierung, Audit-Trail? → MRM-Richtlinie, Vorfallsprozess, Auditnachweise
- A4: ISO/IEC 42001 oder äquivalent, Change-Kontrolle für Prompts/Tools/Policies? → Zertifikat/Audit, Change-Prozess

### G3 Daten- und Plattformbasis
- Einstieg: Unter welcher Kennung würde ein Agent heute in Ihr Kernsystem schreiben?
- A1: Freigegebene LLM-Plattform, lesender Datenzugang (Suche, RAG)? → Plattformfreigabe, Zugangskonzept
- A2: APIs für Schreibzugriff, Identitäts- und Rechtemodell für nicht-menschliche Akteure, Logging? → API-Katalog, IAM-Konzept, Logauszug
- A3: Zentrale Observability (Traces, Kosten, Qualität), Tool-/Policy-Registry, Sandbox, Datenqualitätssicherung? → Plattform-Demo, DQ-Reports
- A4: Plattform als Produkt mit SLA, Mandantentrennung, Kostenattribution, automatisierte Evaluation je Release? → SLA, Eval-Pipeline

### G4 Fähigkeiten und Betriebsmodell
- Einstieg: Wer würde einen Agenten um 3 Uhr nachts stoppen, wenn er Unsinn macht?
- A1: Prototypen, aber kein Betrieb? → Prototyp-Inventar
- A2: Team kann bauen, testen, deployen; Betrieb wie Software (Incident, Rollback)? → Betriebshandbuch
- A3: AgentOps: Evaluationsdesign, Versionierung, Drift-Monitoring, Kostensteuerung; geschulte Supervisoren im Fachbereich? → Rollenprofile, Schulungsnachweise
- A4: Fachbereiche konfigurieren selbst innerhalb Leitplanken? → Self-Service-Framework

### G5 Kultur
- Einstieg: Was ist passiert, als zuletzt ein automatisiertes System einen Fehler gemacht hat?
- A1: Offenheit für Assistenz, Skepsis gegenüber Entscheidungen? → Befragung/Interviews
- A2: Agentenfehler als Lernfall, Mitbestimmung eingebunden? → Vereinbarung mit BR, Fehlerkultur-Regelung
- A3: Kontrollabgabe bei Monitoring akzeptiert, Rollenwechsel zum Supervisor durch PE gestützt? → Rollenkonzepte, Change-Programm
- A4: Mitarbeitende schlagen Delegation vor und bewerten Agenten kritisch? → Vorschlagsquote, Reviews

## Prozessdimensionen

### P2 Entscheidungsstruktur (zuerst)
- Einstieg: Nennen Sie die drei Entscheidungen im Prozess, bei denen zwei erfahrene Kollegen unterschiedlich entscheiden würden.
- A1: Entscheidungspunkte benannt, je Typ (Regel, Muster, Ermessen)? → Entscheidungsinventar
- A2: Kriterien explizit (auch für Ermessen: Faktoren, Beispiele), Handlungen reversibel/irreversibel klassifiziert, Fehlerkosten geschätzt? → Entscheidungskatalog
- A3: Schwellenwerte für Delegation, Baseline der menschlichen Entscheidungsqualität, Rückabwicklungspfad? → Schwellenwertmatrix, Baseline, Rückabwicklungsverfahren
- A4: Nachjustierung unter Change-Kontrolle, Aggregatkontrollen? → Kontrollkonzept
- Prüffrage K.O.: Gibt es Handlungen ohne Rückabwicklungspfad? → K5

### P4 Ausnahmebehandlung (zweitens)
- Einstieg: Wie viel Prozent der Fälle laufen nicht nach Standard? Woher wissen Sie das?
- A1: Typische Ausnahmen benennbar? → Liste
- A2: Quote gemessen, Typen kategorisiert, Eskalationsrolle je Typ, Stop-and-ask-Regel definiert? → Statistik, Eskalationsmatrix, Stop-Regel
- A3: Pfade dokumentiert, SLAs, Unsicherheitserkennung statt Raten? → Pfade, SLA, Regeln
- A4: Review-Zyklus, sinkender manueller Anteil? → Trendkennzahl

### P3 Daten und Systemzugang
- Einstieg: Welche Systeme muss der Agent lesen, in welche schreiben, und gibt es dafür eine API?
- A1: Inputs digital, Lesezugang? → Datenflussdiagramm
- A2: Schreibzugang per API, eigene Identität, minimale Rechte, Zuordenbarkeit? → API-Zugang, Service-Identität
- A3: DQ gesichert, Extraktionsgüte gemessen, Testumgebung mit realistischen Daten? → Metriken, Testumgebung
- A4: Keine Medienbrüche, vollständiger Fallzustand lesbar? → Schnittstellenabdeckung
- Prüffrage K.O.: Kein Schreibzugang möglich? → K1

### P6 Ownership und Haftung
- Einstieg: Wer unterschreibt, wenn der Agent einen Kunden falsch behandelt hat?
- A1: informeller Kümmerer → Benennung
- A2: formaler Owner, RACI für Agentenhandlungen, Freigeber benannt? → Rollenbeschreibung, RACI
- A3: Autorität über Prozess und IT, Budgeteinfluss, Stop-Berechtigung getestet? → Mandat, Stop-Test-Protokoll
- A4: steuert über Ziele, Mitglied der Agenten-Governance? → Zielvereinbarung
- Prüffrage K.O.: Kein formaler Owner? → K2

### P7 Risiko und Regulatorik
- Einstieg: Fällt der Prozess unter Anhang III der KI-Verordnung? Trifft er Entscheidungen mit Rechtswirkung für Personen?
- A1: Kurzcheck Datenschutz, regulierte Tätigkeit? → Kurzcheck
- A2: AI-Act-Einstufung, DSFA, Blast Radius, Freigabe Compliance und DS? → Dokumente
- A3: Oversight-Konzept, revisionssicherer Audit-Trail, technisch durchgesetzte Limits? → Konzept, Logging, Limits
- A4: laufende Konformitätsprüfung, Audits, Nachweise abrufbar? → Berichte
- Prüffragen K.O.: Hochrisiko ohne Oversight-Konzept? → K4. Vollautomatisierte Entscheidung mit Rechtswirkung ohne Art.-22-Ausnahme? → K6

### P5 Observability und Bewertbarkeit
- Einstieg: Wie gut sind Ihre Menschen in diesem Prozess, in Zahlen?
- A1: Mengen- und Durchlaufzeitkennzahlen? → Kennzahlenblatt
- A2: Outcome-Kennzahlen als menschliche Baseline, jede Agentenhandlung geloggt? → Baseline-Messung
- A3: kontinuierlicher Vergleich, Stichproben, Drift-Erkennung, Owner-Dashboard? → Dashboard
- A4: automatisierte Evaluation vor jeder Änderung? → Eval-Suite
- Prüffrage K.O.: Keine Baseline? → K3

### P1 Prozessdefinition und Stabilität
- Einstieg: Wann wurde der Prozess zuletzt geändert, und wie oft im letzten Jahr?
- A1: benannt, Hauptschritte beschrieben → Skizze
- A2: End-to-end dokumentiert, Varianten mit Volumenanteil, Änderung seltener als quartalsweise → Modell, Variantenliste, Historie
- A3: standardisiert, Regeln formal (BPMN/DMN), Change-Verfahren mit Versionierung → versioniertes Modell
- A4: maschinenlesbare Spezifikation, Änderungen vorab getestet → Spezifikation, Testprotokolle

### P8 Mitarbeitende
- Einstieg: Wer würde den Agenten überwachen, und wie viel seiner Zeit?
- A1: kennen Prozess, nutzen Assistenz punktuell → Nutzungsnachweis
- A2: können Vorschläge bewerten und korrigieren, Freigaberegeln bekannt, Rollenwechsel kommuniziert → Schulung, Richtlinie
- A3: Supervisor-Rolle mit Dashboard, Stichproben, Eskalationen, Zeitanteile geregelt → Rollenprofil, Stellenanpassung
- A4: konfigurieren und verbessern selbst → Nachweise

## Wertachse (mit Owner)
- V1 Volumen/Frequenz, V2 FTE-Bindung, V3 Durchlaufzeit-Hebel, V4 Fehler- und Nacharbeitskosten, V5 Priorität im Fachbereich. Je 1 bis 5. Zahlen erfragen, nicht Eindrücke.

## Häufige Fehler des Assessors
- Aspiration als Zustand werten.
- Zelle "erfüllt" ohne Artefakt.
- Höhere Stufe bei offener Vorstufe (Gating-Verstoß).
- Mittelwert bilden, "im Schnitt A2,5".
- K.O.-Kriterien überspringen, weil die Zellen es schon abdecken.
- Wertargumente in Reifezellen einfließen lassen.
