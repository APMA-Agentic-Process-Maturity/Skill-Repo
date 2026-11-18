# APMA: Kurzfassung der Methodik (für den Agenten)

Quelle: Stojanovic, A. und Mitwirkende, Sopra Steria Next Germany (2026). Agentic Process Maturity Assessment (APMA): Ein Reifegradmodell zur Bestimmung vertretbarer Autonomiestufen für KI-Agenten in Geschäftsprozessen. Working Paper, Version 1.0.

## Kernidee
Agentische Reife eines Prozesses = höchste Autonomiestufe, auf der ein Agent dort vertretbar handeln kann. Vertretbar: die Organisation kann die Delegation verantworten, überwachen, rückgängig machen und begründen. Das Ergebnis erzwingt eine Architekturentscheidung (A2 = Freigabe-Interface, A3 = Monitoring).

## Herkunft
- PEMM (Hammer 2007): zwei Ebenen, vier Stufen je Dimension, Stufentexte, Weakest Link, Unternehmensreife begrenzt Prozessreife.
- CMMI / BPMM (OMG 2008): staged Gating, Evidenzpflicht.
- Reifegradmodell-Design (Becker et al. 2009; Pöppelbuß/Röglinger 2011; Röglinger et al. 2012): Vorgehen, präskriptiver Anspruch (Gap-Liste).
- Levels of Automation (Sheridan/Verplank 1978; Parasuraman et al. 2000; SAE J3016; Feng et al. 2025): Ergebnisskala. APMA dreht die Kausalität: Stufe folgt aus Prozess und Organisation, nicht aus Entwicklerwahl.
- Governance (EU AI Act Art. 14; DSGVO Art. 22; ISO/IEC 42001; NIST AI RMF): harte Randbedingungen als K.O.-Kriterien.

## Adressierte Defizite bestehender Ansätze
D1 falscher Gegenstand (Prozessorientierung statt Agenteneignung) · D2 falsche Einheit (Organisation statt Prozess) · D3 Mittelwert statt Minimum · D4 kein handlungsleitender Output · D5 Autonomie als Designwahl statt Funktion der Reife · D6 Dürfen und Sollen vermischt · D7 keine Evidenzpflicht. Plus Bainbridge (1983): Aufsicht muss als Rolle, Qualifikation und Zeitanteil real vorgehalten werden.

## Verwandte Arbeit (bei Einwänden "das gibt es doch schon" verwenden)
Schmidt, Alt und Zimmermann (HICSS 2026, https://hdl.handle.net/10125/111878) haben unabhängig von und zeitgleich mit APMA ein prozessorientiertes Agentic-AI-Readiness-Framework vorgelegt: fünf Prozessperspektiven (Aktivität, Entscheidung, Datenoperation, Kontrollfluss, Ressourcen), Stakeholder-Scores 0 bis 5, Konzept der Process Debt (dokumentierter vs. gelebter Prozess), praktische Readiness = Potenzial minus Process Debt, Fallstudie an einer deutschen Hochschule (9 Prozesse, 40 Beteiligte). APMA baut nicht darauf auf; das Paper wurde dem Autor erst nach Abschluss des Modells bekannt. Sprachregelung: Zwei unabhängige Arbeiten wählen den Prozess als Einheit, das stützt die Grundannahme. Unterschiede: APMA liefert eine Autonomiestufe statt eines Profils, aggregiert über das Minimum statt kompensatorisch, hat ein Unternehmens-Gate, verlangt Evidenz je Zelle statt Stakeholder-Einschätzung und operationalisiert Regulatorik als K.O.-Kriterien. Schmidt et al. haben eine Fallstudienvalidierung, APMA noch nicht. Process Debt entspricht in APMA einer nicht erfüllten P1-Zelle, nicht einem Abzug.

## Designprinzipien
DP1 Autonomie als Ergebnis · DP2 Prozess als Einheit, Unternehmen als Gate · DP3 Weakest Link · DP4 Gating und Evidenz · DP5 harte Grenzen · DP6 Orthogonalität von Reife und Wert.

## Formalisierung
l(d) = max{k : s(d,j)=1 für alle j ≤ k} · L_G = min_g l(g) · L_K = min(4, min_{c: x(c)=1} κ(c)) · A(P) = min(min_d l(d), L_G, L_K) · Gap(P) = {(d, A+1) : s(d, A+1) = 0} ∪ {c ∈ K : x(c)=1, κ(c)=A} (K.O.-Anteil nötig, sonst leere Gap-Liste bei reinem K.O.-Cap).

## Praxisfolgen
1. Erste Investition ist meist Governance (Identitäten, Baseline, Oversight), nicht Agenten.
2. Beste Kandidaten sind Massenprozesse mit expliziten Regeln, billigen Fehlern, APIs; nicht die sichtbaren Kernprozesse.
3. Autonomie wird stufenweise verdient; Gap-Liste = Projektplan; Assessment wiederholen.

## Limitationen (immer nennen, wenn gefragt oder relevant)
Keine empirische Validierung; Setzungen in Stufentexten und Caps; streng (viele A1, A4 selten); ca. 2 Assessortage je Prozess; Stufenanforderungen verschieben sich, wenn Agenten Unsicherheit besser erkennen.
