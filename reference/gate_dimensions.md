# Unternehmens-Gate: Stufentexte

Eine Zelle gilt als erfüllt, wenn die Anforderung nachweislich zutrifft und das Artefakt vorliegt. Stufe k zählt nur bei erfüllten Stufen 1 bis k-1.

## G1 Führung und Risikoappetit

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Die Geschäftsführung hat KI-Assistenz als Thema anerkannt und ein Pilotbudget freigegeben. Ein Sponsor ist benannt. Es gibt noch keine Position zu Autonomiegrenzen. | Benannter Sponsor; dokumentiertes Pilotbudget |
| A2 Überwacht | Ein Mitglied der Geschäftsleitung verantwortet agentische KI. Es ist entschieden, welche Handlungsklassen Agenten unter menschlicher Freigabe ausführen dürfen. Die Haftung für Agentenhandlungen ist einer Rolle zugeordnet. | Beschluss der Geschäftsleitung mit Delegationsgrenzen; Haftungszuordnung |
| A3 Autonom mit Monitoring | Es gibt eine explizite Autonomie-Policy: welche Entscheidungstypen ohne Einzelfreigabe delegiert werden dürfen, mit Schwellenwerten (Betrag, Reichweite, Reversibilität). Der Risikoappetit für Fehlhandlungen ist quantifiziert. | Autonomie-Policy mit Schwellenwerten; Risikoappetit-Statement |
| A4 Delegiert | Autonomiestufen sind Teil von Strategie und Zielplanung. Budget und Ziele werden nach Autonomiegrad geplant. Die Geschäftsleitung steuert agentische Prozesse über Ziele und Leitplanken, nicht über Einzelfreigaben. | Strategie-/Planungsdokument mit Autonomiezielen je Prozessdomäne |

## G2 KI-Governance

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Es gibt Nutzungsregeln für generative KI (zulässige Daten, freigegebene Tools). Eine Stelle ist für KI-Fragen ansprechbar. | KI-Nutzungsrichtlinie; benannte Anlaufstelle |
| A2 Überwacht | Ein Freigabeprozess für Agenten existiert: Use-Case-Registrierung, Risikoeinstufung nach EU AI Act, Datenschutzprüfung. Human-Oversight-Anforderungen sind je Risikoklasse definiert. | Use-Case-Register; Freigabeprozess; Oversight-Anforderungen je Risikoklasse |
| A3 Autonom mit Monitoring | Das Modellrisikomanagement deckt Agenten ab: Tests vor Freigabe, Monitoring im Betrieb, Vorfallsmanagement mit Meldewegen, periodische Re-Zertifizierung. Audit-Trail ist Pflicht. Orientierung an ISO/IEC 42001. | MRM-Richtlinie mit Agentenkapitel; Vorfallsprozess; Audit-Nachweise |
| A4 Delegiert | Governance ist in das Managementsystem integriert (ISO/IEC 42001 oder äquivalent) und regelt auch Änderungen an Agentenkonfiguration (Prompts, Tools, Policies) über Change-Kontrolle. | Zertifikat oder Audit; Change-Control-Prozess für Agentenkonfiguration |

## G3 Daten- und Plattformbasis

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Mitarbeitende haben Zugang zu einer freigegebenen LLM-Plattform. Unternehmensdaten sind für lesende Abfragen (Suche, RAG) erschlossen. | Plattformfreigabe; Datenzugangskonzept (lesend) |
| A2 Überwacht | Kernsysteme bieten APIs oder stabile Integrationspunkte für Schreibzugriffe. Es gibt ein Identitäts- und Rechtemodell für nicht-menschliche Akteure (Service-Identitäten, Least Privilege). Agentenhandlungen werden geloggt. | API-Katalog; IAM-Konzept für Agenten; Logging-Nachweis |
| A3 Autonom mit Monitoring | Zentrale Observability für Agenten (Traces, Kosten, Qualitätsmetriken), zentrale Tool-/Policy-Registry, Sandbox für Testläufe. Daten der Kernprozesse sind strukturiert und qualitätsgesichert. | Observability-Plattform; Tool-Registry; Datenqualitätsreports |
| A4 Delegiert | Agentenplattform als Produkt mit SLAs, Mandantentrennung, Kostenattribution je Prozess und automatisierter Evaluation vor jedem Release. | Plattform-SLA; Evaluations-Pipeline |

## G4 Fähigkeiten und Betriebsmodell

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Einzelne Personen bauen Prototypen. Es gibt keinen definierten Betrieb für Agenten. | Prototyp-Inventar |
| A2 Überwacht | Ein Team kann Agenten bauen, testen und in Produktion bringen. Der Betrieb folgt dem Software-Betriebsprozess (Deployment, Incident, Rollback). | Teamstruktur; Betriebshandbuch für Agenten |
| A3 Autonom mit Monitoring | AgentOps-Fähigkeit: Evaluationsdesign, Versionierung von Prompts und Policies, Drift-Monitoring, Kostensteuerung. Fachbereiche verfügen über geschulte Agenten-Supervisoren. | Rollenprofile; Schulungsnachweise; Evaluations-Suites |
| A4 Delegiert | Agentenentwicklung ist Kernkompetenz. Fachbereiche konfigurieren Agenten im Rahmen zentraler Leitplanken selbst. | Self-Service-Framework; Kompetenzmatrix |

## G5 Kultur

| Stufe | Anforderung | Evidenz-Artefakt |
| --- | --- | --- |
| A1 Assistiert | Offenheit gegenüber KI-Assistenz, aber Skepsis gegenüber maschinellen Entscheidungen. Fehlertoleranz ist nicht thematisiert. | Mitarbeiterbefragung oder Interviewprotokolle |
| A2 Überwacht | Fachbereiche akzeptieren, dass Agenten Handlungen vorbereiten und unter Freigabe ausführen. Agentenfehler werden als Lernfälle behandelt, nicht als Projektabbruch. Mitbestimmung ist eingebunden. | Vereinbarung mit Mitbestimmung; dokumentierte Fehlerkultur-Regelung |
| A3 Autonom mit Monitoring | Mitarbeitende geben Kontrolle an Agenten ab, wenn Monitoring vorhanden ist. Die Rollenveränderung (vom Bearbeiter zum Supervisor) ist akzeptiert und durch Personalentwicklung gestützt. | Rollenkonzepte; Change-Programm |
| A4 Delegiert | Zusammenarbeit mit Agenten ist Normalität. Mitarbeitende schlagen aktiv Delegation vor und bewerten Agentenleistung kritisch. | Vorschlagsquote; Reviews aus dem Fachbereich |
