# APMA Assessment: Prüfung Werkstattrechnungen

Bereich: Schaden Kfz · Owner: Teamleitung Rechnungsprüfung · Assessor: A. Stojanovic · Datum: 2026-11-04

## Ergebnis

**Agentische Reife: A2 Überwacht**

- Minimum Prozessdimensionen: 2
- Unternehmens-Gate: 2
- Wirksames K.O.-Cap: 4
- Begrenzt durch: Unternehmens-Gate G1: Führung und Risikoappetit; Unternehmens-Gate G2: KI-Governance; Unternehmens-Gate G3: Daten- und Plattformbasis; Unternehmens-Gate G4: Fähigkeiten und Betriebsmodell; Prozessdimension P1: Prozessdefinition und Stabilität; Prozessdimension P4: Ausnahmebehandlung; Prozessdimension P5: Observability und Bewertbarkeit; Prozessdimension P6: Ownership und Haftung; Prozessdimension P7: Risiko und Regulatorik; Prozessdimension P8: Mitarbeiter
- Wert-Score: 4.2
- Portfolio-Position: **Sofort starten**

## Dimensionen

| Ebene | Dimension | Stufe |
| --- | --- | --- |
| Gate | G1 Führung und Risikoappetit | 2 |
| Gate | G2 KI-Governance | 2 |
| Gate | G3 Daten- und Plattformbasis | 2 |
| Gate | G4 Fähigkeiten und Betriebsmodell | 2 |
| Gate | G5 Kultur | 3 |
| Prozess | P1 Prozessdefinition und Stabilität | 2 |
| Prozess | P2 Entscheidungsstruktur | 3 |
| Prozess | P3 Daten und Systemzugang | 3 |
| Prozess | P4 Ausnahmebehandlung | 2 |
| Prozess | P5 Observability und Bewertbarkeit | 2 |
| Prozess | P6 Ownership und Haftung | 2 |
| Prozess | P7 Risiko und Regulatorik | 2 |
| Prozess | P8 Mitarbeiter | 2 |

## Gap-Liste zur Stufe A3

Diese Zellen sind der Arbeitsplan vor der nächsten Autonomiestufe.

| Ebene | Dimension | Anforderung | Evidenz |
| --- | --- | --- | --- |
| gate | G1 Führung und Risikoappetit | Es gibt eine explizite Autonomie-Policy: welche Entscheidungstypen ohne Einzelfreigabe delegiert werden dürfen, mit Schwellenwerten (Betrag, Reichweite, Reversibilität). Der Risikoappetit für Fehlhandlungen ist quantifiziert. | Autonomie-Policy mit Schwellenwerten; Risikoappetit-Statement |
| gate | G2 KI-Governance | Das Modellrisikomanagement deckt Agenten ab: Tests vor Freigabe, Monitoring im Betrieb, Vorfallsmanagement mit Meldewegen, periodische Re-Zertifizierung. Audit-Trail ist Pflicht. Orientierung an ISO/IEC 42001. | MRM-Richtlinie mit Agentenkapitel; Vorfallsprozess; Audit-Nachweise |
| gate | G3 Daten- und Plattformbasis | Zentrale Observability für Agenten (Traces, Kosten, Qualitätsmetriken), zentrale Tool-/Policy-Registry, Sandbox für Testläufe. Daten der Kernprozesse sind strukturiert und qualitätsgesichert. | Observability-Plattform; Tool-Registry; Datenqualitätsreports |
| gate | G4 Fähigkeiten und Betriebsmodell | AgentOps-Fähigkeit: Evaluationsdesign, Versionierung von Prompts und Policies, Drift-Monitoring, Kostensteuerung. Fachbereiche verfügen über geschulte Agenten-Supervisoren. | Rollenprofile; Schulungsnachweise; Evaluations-Suites |
| process | P1 Prozessdefinition und Stabilität | Der Prozess ist standardisiert. Entscheidungsregeln und Datenobjekte sind formal beschrieben (z. B. BPMN/DMN). Änderungen laufen über ein Change-Verfahren mit Versionierung. | Versioniertes Prozess- und Entscheidungsmodell; Change-Log |
| process | P4 Ausnahmebehandlung | Ausnahmepfade sind dokumentiert und teilweise automatisiert. Eskalationen haben SLAs. Der Agent erkennt Unsicherheit (Konfidenz, fehlende Daten) und eskaliert systematisch statt zu raten. | Dokumentierte Ausnahmepfade; Eskalations-SLA; Unsicherheitsregeln |
| process | P5 Observability und Bewertbarkeit | Die Agentenleistung wird kontinuierlich gegen die Baseline gemessen. Stichprobenprüfung ist etabliert, Drift wird erkannt. Der Prozess-Owner hat ein Dashboard. | Monitoring-Dashboard; Stichprobenverfahren; Drift-Alarme |
| process | P6 Ownership und Haftung | Der Owner hat Autorität über Prozessänderungen und die unterstützenden IT-Systeme sowie Budgeteinfluss. Er kann den Agenten jederzeit stoppen; der Stop ist getestet. | Mandat; Stop-Berechtigung; Protokoll eines Stop-Tests |
| process | P7 Risiko und Regulatorik | Für Hochrisiko oder regulierte Tätigkeiten: Human-Oversight-Konzept gemäß Anforderungen, revisionssicherer Audit-Trail, Limits technisch durchgesetzt (nicht nur organisatorisch). | Oversight-Konzept; revisionssicheres Logging; technische Limits |
| process | P8 Mitarbeiter | Supervisor-Rolle etabliert: Mitarbeitende überwachen Agenten über Dashboards, prüfen Stichproben, bearbeiten Eskalationen. Zeitanteile sind neu geregelt. | Rollenprofil Supervisor; Stellenanpassung; Schulung; Befundquote der Stichprobenprüfung |

