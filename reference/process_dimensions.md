# Prozessdimensionen: Stufentexte

Eine Zelle gilt als erfüllt, wenn die Anforderung nachweislich zutrifft und das Artefakt vorliegt. Stufe k zählt nur bei erfüllten Stufen 1 bis k-1.

## P1 Prozessdefinition und Stabilität

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Der Prozess ist benannt; Start, Ende und Hauptschritte sind beschrieben. Varianten sind nicht gezählt. | Prozessbeschreibung (mindestens Skizze) |
| A2 Überwacht | Der Prozess ist end-to-end dokumentiert (Schritte, Rollen, Systeme, Inputs/Outputs). Varianten sind erfasst; die Hauptvariante deckt den Großteil des Volumens ab. Der Prozess ändert sich selten (Richtwert: nicht öfter als quartalsweise). | Prozessmodell; Variantenliste mit Volumenanteil; Änderungshistorie |
| A3 Autonom mit Monitoring | Der Prozess ist standardisiert. Entscheidungsregeln und Datenobjekte sind formal beschrieben (z. B. BPMN/DMN). Änderungen laufen über ein Change-Verfahren mit Versionierung. | Versioniertes Prozess- und Entscheidungsmodell; Change-Log |
| A4 Delegiert | Der Prozess liegt als maschinenlesbare Spezifikation vor, die Agent und Mensch gleichermaßen nutzen. Änderungen werden vor Produktivsetzung getestet oder simuliert. | Maschinenlesbare Spezifikation; Testprotokolle für Prozessänderungen |

## P2 Entscheidungsstruktur

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Die Entscheidungspunkte im Prozess sind benannt. Für jeden ist bekannt, ob er regelbasiert, musterbasiert oder Ermessen ist. | Entscheidungsinventar |
| A2 Überwacht | Die Entscheidungskriterien sind explizit beschrieben (auch für Ermessen: Faktoren, Beispiele). Handlungen sind in reversibel/irreversibel klassifiziert. Fehlerkosten je Entscheidungstyp sind geschätzt. | Entscheidungskatalog mit Kriterien, Reversibilität und Fehlerkosten |
| A3 Autonom mit Monitoring | Für delegierte Entscheidungen gibt es Schwellenwerte (Betrag, Konfidenz, Kundentyp), oberhalb derer eskaliert wird. Die Entscheidungsqualität ist am Menschen gemessen. Ein Rückabwicklungspfad für Fehlhandlungen existiert. | Schwellenwertmatrix; Baseline der Entscheidungsqualität; Rückabwicklungsverfahren |
| A4 Delegiert | Die Entscheidungslogik wird aus Ergebnissen fortlaufend nachjustiert (unter Change-Kontrolle). Der Prozess toleriert Einzelfehler, weil Aggregatkontrollen (Stichproben, Limits) greifen. | Kontrollkonzept auf Aggregatebene; Nachweise der Nachjustierung |

## P3 Daten und Systemzugang

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Inputs liegen digital vor (auch unstrukturiert: E-Mail, PDF). Der Agent erreicht die relevanten Systeme lesend. | Datenflussdiagramm; nachgewiesener Lesezugang |
| A2 Überwacht | Zielsysteme sind per API oder stabiler Schnittstelle schreibbar. Der Agent handelt unter eigener Identität mit minimalen Rechten; jede Schreibaktion ist ihm zuordenbar. | API-Zugang; Service-Identität; Rechtekonzept |
| A3 Autonom mit Monitoring | Strukturierte Daten sind qualitätsgesichert (Vollständigkeit, Aktualität). Unstrukturierte Inputs werden mit gemessener Extraktionsgüte verarbeitet. Eine Testumgebung mit realistischen Daten existiert. | Datenqualitätsmetriken; Extraktionsgüte; Testumgebung |
| A4 Delegiert | Alle Prozessschritte sind über Schnittstellen erreichbar, keine Medienbrüche. Der Agent kann Zustand und Historie eines Falls vollständig lesen. | Schnittstellenabdeckung 100 %; Falldatenmodell |

## P4 Ausnahmebehandlung

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Es ist bekannt, dass Ausnahmen vorkommen; typische Fälle können benannt werden. | Liste typischer Ausnahmen |
| A2 Überwacht | Die Ausnahmequote ist gemessen, Ausnahmetypen sind kategorisiert. Je Kategorie ist eine Eskalationsrolle benannt. Der Agent hat eine definierte Stop-and-ask-Regel. | Ausnahmestatistik; Eskalationsmatrix; Stop-Regel |
| A3 Autonom mit Monitoring | Ausnahmepfade sind dokumentiert und teilweise automatisiert. Eskalationen haben SLAs. Der Agent erkennt Unsicherheit (Konfidenz, fehlende Daten) und eskaliert systematisch statt zu raten. | Dokumentierte Ausnahmepfade; Eskalations-SLA; Unsicherheitsregeln |
| A4 Delegiert | Ausnahmen werden analysiert und fließen in Prozess- und Agentenverbesserung zurück. Der Anteil manueller Ausnahmen sinkt messbar. | Ausnahmen-Review-Zyklus; Trendkennzahl |

## P5 Observability und Bewertbarkeit

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Grundlegende Mengen- und Durchlaufzeitkennzahlen existieren. | Kennzahlenblatt |
| A2 Überwacht | Outcome-Kennzahlen (Qualität, Fehler, Nacharbeit, Kundenwirkung) sind definiert und als menschliche Baseline gemessen. Jede Agentenhandlung ist geloggt und nachvollziehbar. | Baseline-Messung; Logs |
| A3 Autonom mit Monitoring | Die Agentenleistung wird kontinuierlich gegen die Baseline gemessen. Stichprobenprüfung ist etabliert, Drift wird erkannt. Der Prozess-Owner hat ein Dashboard. | Monitoring-Dashboard; Stichprobenverfahren; Drift-Alarme |
| A4 Delegiert | Automatisierte Evaluation (Testsets, Regressionstests) vor jeder Änderung. Prozesskennzahlen fließen in die strategische Steuerung. | Evaluations-Suite; Regressionsnachweise |

## P6 Ownership und Haftung

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Eine Person fühlt sich für den Prozess verantwortlich, ohne formalen Auftrag. | Benennung |
| A2 Überwacht | Formaler Prozess-Owner mit Mandat. Es ist festgelegt, wer für Agentenhandlungen die Verantwortung trägt und wer freigibt. | Rollenbeschreibung Owner; RACI für Agentenhandlungen |
| A3 Autonom mit Monitoring | Der Owner hat Autorität über Prozessänderungen und die unterstützenden IT-Systeme sowie Budgeteinfluss. Er kann den Agenten jederzeit stoppen; der Stop ist getestet. | Mandat; Stop-Berechtigung; Protokoll eines Stop-Tests |
| A4 Delegiert | Der Owner steuert den Prozess über Ziele und Leitplanken für den Agenten und ist Teil der Agenten-Governance des Unternehmens. | Zielvereinbarung Prozess/Agent; Gremienmitgliedschaft |

## P7 Risiko und Regulatorik

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Grobe Einschätzung liegt vor: Datenschutzrelevanz, regulierte Tätigkeit ja/nein. | Kurzcheck |
| A2 Überwacht | AI-Act-Einstufung durchgeführt; Datenschutz-Folgenabschätzung falls erforderlich. Der Blast Radius einer Fehlhandlung ist beschrieben (Betrag, Kundenzahl, Reputation). Freigabe durch Compliance und Datenschutz liegt vor. | AI-Act-Einstufung; DSFA; Risikobewertung; Freigabe |
| A3 Autonom mit Monitoring | Für Hochrisiko oder regulierte Tätigkeiten: Human-Oversight-Konzept gemäß Anforderungen, revisionssicherer Audit-Trail, Limits technisch durchgesetzt (nicht nur organisatorisch). | Oversight-Konzept; revisionssicheres Logging; technische Limits |
| A4 Delegiert | Laufende Konformitätsprüfung, periodische Audits, Nachweise für Aufsicht kurzfristig verfügbar. | Audit-Berichte; Konformitätsdossier |

## P8 Mitarbeitende

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Mitarbeitende kennen den Prozess und nutzen KI-Assistenz punktuell. | Nutzungsnachweis |
| A2 Überwacht | Mitarbeitende können Agentenvorschläge bewerten und korrigieren. Sie wissen, wann sie freigeben dürfen und wann nicht. Die Rollenveränderung ist kommuniziert. | Schulungsnachweis; Freigaberichtlinie; Quote abgelehnter oder geänderter Agentenvorschläge (liegt sie nahe null, wird durchgewunken: Automation Bias, Art. 14 Abs. 4 lit. b KI-VO) |
| A3 Autonom mit Monitoring | Supervisor-Rolle etabliert: Mitarbeitende überwachen Agenten über Dashboards, prüfen Stichproben, bearbeiten Eskalationen. Zeitanteile sind neu geregelt. | Rollenprofil Supervisor; Stellenanpassung; Schulung; Befundquote der Stichprobenprüfung |
| A4 Delegiert | Mitarbeitende konfigurieren und verbessern Agenten im Rahmen der Leitplanken selbst und schlagen Delegation weiterer Teilaufgaben vor. | Verbesserungsvorschläge; Self-Service-Nutzung |
