# K-12 US Operational Pain Research

Research date: Aug 2026. Method: primary-source web research (NCES/IES, US ED, eCFR, CMS-via-HSPF, Attendance Works, AEI, ERIC). Search engines (DDG/Bing/Mojeek) partially blocked; some claims that could not be independently fetched are explicitly labeled ESTIMATE or UNKNOWN with reasoning. No AI-vendor marketing sources used.

Context numbers used throughout (all VERIFIED):
- ~13,500 public school districts; ~49M public K-12 students. Typical mid-size district modeled below: 5,000 students, ~300 teachers, ~$60–70M budget.
- IDEA: 7.5M students ages 3–21 served under IDEA in 2022–23 = 15% of public school enrollment; all-time high. https://nces.ed.gov/programs/coe/indicator/cgg/students-with-disabilities
- English learners: 5.3M students (10.6%) fall 2021; 76.4% Spanish home language; 832K ELs also have disabilities (15.8% of ELs). https://nces.ed.gov/programs/coe/indicator/cgf/english-learners
- Chronic absenteeism: ~15% pre-pandemic → 31% in 2021-22 → 28% in 2022-23 nationally. https://www.ed.gov/teaching-and-administration/supporting-students/chronic-absenteeism ; https://www.returntolearntracker.net/
- Hiring crisis: 74% of public schools reported difficulty filling ≥1 teaching vacancy with a fully certified teacher entering 2024-25; average school had 6 teaching vacancies and filled only 79% with fully certified teachers; special education was the hardest-to-fill subject at elementary/middle (74% of schools); 69% had difficulty filling non-teaching vacancies (transportation staff filled at just 60%). https://nces.ed.gov/whatsnew/press_releases/10_17_2024.asp
- ESSER: $190B total federal pandemic aid ($13.2B + $54.3B + $122B), fully obligated as of Sept 30, 2024 → districts now face post-ESSER fiscal cliff while compliance/reporting muscle remains. https://en.wikipedia.org/wiki/Elementary_and_Secondary_School_Emergency_Relief_Fund
- FERPA: schools must fulfill record-inspection requests within 45 days (34 CFR 99.10). https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-B/section-99.10
- CRDC: OCR collects civil rights data from EVERY public school district receiving federal financial assistance, biennially, via long LEA- and school-level forms; next collection (2025-26) mandatory for all LEAs with submission opening Dec 2026. https://www.ed.gov/laws-and-policy/civil-rights-laws/civil-rights-data-collection-crdc
- SPED paperwork: federally funded SPeNSE study found SPED teachers average 5 hrs/week on paperwork; 88% said paperwork interferes with teaching to a moderate/great extent. https://eric.ed.gov/?id=ED479674
- School Medicaid: CMS May 2023 comprehensive guide affirmed districts can bill Medicaid for services to ALL Medicaid-enrolled students (not only IEP); 25 states have expanded; strict documentation/medical-necessity requirements remain; OIG has audited these programs repeatedly (HSC reviewed 33 OIG audits). https://healthystudentspromisingfutures.org/federal-support/ ; https://healthystudentspromisingfutures.org/resources/office-of-the-inspector-general-school-medicaid-reports-review/

---

## Executive Summary — ranked pains (pain × budget × agent-fit)

| Rank | Problem | Why it ranks | Est. annual value per mid-size district (5k students) |
|---|---|---|---|
| 1 | School Medicaid billing & time-study compliance | Direct federal revenue left unclaimed due to documentation burden; buyer = business office; pure document-intelligence workflow; OIG audit risk creates urgency | $50K–$500K+ recovered revenue + $50K–150K labor (ESTIMATE) |
| 2 | IEP paperwork & compliance-timeline management (SPED) | Largest verified staff-time sink in education; staffing-shortage-amplified; due-process legal risk; every district buys | $100K–$250K labor equivalent + retention value (ESTIMATE anchored to verified 5 hrs/wk) |
| 3 | Chronic absenteeism intervention workflows | 28% of students chronically absent (VERIFIED); state funding + accountability tied to it; highly repetitive outreach/documentation loop; agent-shaped | $100K–$400K ADA revenue + hundreds of staff hours (ESTIMATE) |
| 4 | Federal/state compliance reporting (CRDC, grant mgmt, report cards) | Deadline-driven census reporting from fragmented systems; error = federal enforcement; boring/PDF/spreadsheet-heavy; few incumbents solve data assembly | $30K–$120K per cycle per district (ESTIMATE) |
| 5 | Substitute teacher sourcing & absence coverage | Daily operational fire drill; fill rates well below demand amid teacher shortage; vendor markups; dispatch/logistics is agent-shaped | $200K–$500K spend optimization potential (ESTIMATE) |
| 6 | Multilingual parent communication & front-office triage | Federal civil-rights obligation (Title VI) toward 5.3M EL families (VERIFIED count); translation vendors slow/expensive; call/email volume unmanaged | $30K–$150K + civil-rights risk reduction (ESTIMATE) |
| 7 | Teacher recruitment screening & reference checks | Verified shortage (74% of schools struggle); months-long manual screening/reference processes worsen it; HR buyer exists | Time-to-fill reduction; $50K–$150K/yr efficiency (ESTIMATE) |
| 8 | Student records / transcript / public-records requests | FERPA 45-day clock (VERIFIED); high-volume clerical retrieval+redaction work scattered across schools; litigation-driven records requests rising | $20K–$80K labor + legal-risk reduction (ESTIMATE) |
| 9 | Procurement / P.O.s / invoice processing (business office AP) | Classic document-heavy AP pain; grant-funded purchases add coding complexity; CFO buyer; proven automation ROI category outside edu | $40K–$120K processing cost (ESTIMATE) |
| 10 | MTSS/RTI intervention documentation & monitoring | Prerequisite evidence for SPED referral (legal defensibility); spreadsheet-driven; consumes gen-ed + interventionist time | $30K–$100K labor (ESTIMATE) |
| 11 | Certification/license & PD-hours tracking | Lapse = employee can't legally work → classroom coverage crisis; manual checks across 50 state portals | $10K–$40K + risk avoidance (ESTIMATE) |
| 12 | Enrollment/registration paperwork intake | Seasonal surge of paper forms keyed into SIS; errors propagate to all downstream state reporting | $15K–$60K labor (ESTIMATE) |
| 13 | Constructed-response scoring volume (state + local benchmarks) | Massive hand-scoring spend sits with STATE agencies (different buyer); local benchmark scoring burns unpaid teacher time | State-level contracts ($Ms); district-side smaller (ESTIMATE) |
| 14 | SPED due process/dispute preparation | Low frequency but catastrophic cost/risk per case; strong ASSISTANT play attached to problem #2 | Risk-adjusted $10K–$50K/yr (ESTIMATE) |

---

## Problem Detail

### 1. Special education IEP paperwork & compliance-timeline management

**Workflow today:** Referral → evaluation planning (permission-to-evaluate forms) → assessments (psych/SLP/OT reports arrive as PDFs/scans) → IEP drafting (present levels, goals, accommodations, service minutes) → scheduling meetings around parent/teacher availability (multiple reschedules) → meeting held → final IEP document generated → service minutes entered into scheduling systems → progress reports each grading period → annual review → triennial re-evaluation. Performed by case-managing SPED teachers, school psychologists, SLPs, SPED coordinators; suffers: SPED teachers (nights/weekends), parents (delays), students (service gaps).

**Economic buyer:** Director of Special Education; ultimate budget authority = superintendent/board. IDEA Part B flow-through plus general fund covers SPED staffing.

**Volume/cost:** 7.5M IDEA students nationwide (VERIFIED, NCES). SPeNSE (federally sponsored): SPED teachers average 5 hrs/week on paperwork; 88% report interference with core duties (VERIFIED, https://eric.ed.gov/?id=ED479674). Practitioner accounts commonly describe far higher totals when including IEP writing itself (3–5 hrs per annual IEP incl. data gathering and meetings — ESTIMATE consistent with caseloads of 20–28 students). Mid-size district: ~750 IEP students, ~35–45 SPED teachers/service providers × 5+ hrs/wk × 36 wks ≈ 6,300–8,000+ hrs/yr ≈ 3–4 FTE ≈ $180K–$280K loaded labor (ESTIMATE). Plus coordinator time chasing timeline compliance (initial eval within state deadline, often 60 school days; annual review before anniversary date — states vary).

**Consequence if late/bad:** Procedural noncompliance findings in state monitoring; compensatory-education awards; due-process filings; parent distrust; SPED teacher attrition (paperwork is among most-cited reasons for leaving — practitioner consensus, ESTIMATE for magnitude).

**Current software:** PowerSchool Special Programs, Frontline IEP Direct/ExGEN, Embrace, SpedTrack, SEIS (CA), state systems (e.g., Maryland MD Online IEP). These are structured form-fillers + compliance-date dashboards. They don't draft content, don't read the psych report PDFs, don't reconcile goals vs. assessment data vs. service minutes, don't generate defensible present-levels narratives, don't chase teachers for input.

**Why still unsolved:** The bottleneck is authorship + data synthesis across documents (eval reports, work samples, grades, prior IEPs, health plans) — exactly what pre-LLM workflow tools couldn't do; vendors optimized forms/compliance dates instead. Also local variation: every district has its own goal banks/narrative conventions.

**Judgment vs deterministic:** Judgment: eligibility reasoning, goal ambition level, placement recommendations, parent conversation. Deterministic/repetitive: extracting scores from eval PDFs into present levels; assembling goal-progress data; generating compliant boilerplate sections; timeline monitoring; meeting-scheduling loops; input-chasing emails; progress-report generation from logged data.

**Documents/portals:** Evaluation reports (PDF), medical reports, prior IEPs, 504 plans, gradebooks/SIS exports, state IEP systems, parent-portal consents, meeting notices.

**Agent fit:** WORKFLOW-AUTOMATION trending AGENT-OWNED. Agent can own: trigger (calendar/timeline event) → gather artifacts → draft → route for human edit/approval → schedule → file → monitor progress-report cadence → escalate at-risk timelines. Humans must approve educational content (legal requirement; also politically necessary with unions).

**Value/district:** Cutting paperwork 30–50% ≈ $60K–$140K/yr labor equivalent + measurable effect on vacancy fill/retention in a market where SPED is the hardest position to staff (VERIFIED difficulty, NCES). National TAM: ~90K schools; SPED software spend already exists and can be displaced/augmented.

---

### 2. SPED due process & dispute readiness

**Workflow:** Parent disputes identification/services/placement → informal resolution meetings → state complaint or due-process complaint filed → district counsel gathers evidence: all IEP versions, meeting notes, progress data, service logs, correspondence → resolution session (15-day window under IDEA) → mediation → hearing. Performed by SPED directors + outside counsel ($250–$600/hr).

**Buyer:** Superintendent/board via legal line + SPED director.

**Volume/cost:** National filing counts are tracked by CADRE (national dispute-resolution data center) — site blocked during research; historically several thousand due-process complaints filed nationally per year, concentrated in a minority of districts (ESTIMATE — verify against CADRE national data files). Cost per contested case commonly runs tens of thousands of dollars including attorney fees, expert witnesses, staff time, and possible compensatory remedies; settlements routinely include private placement tuition ($30K–$100K+/yr) (ESTIMATE from practitioner/attorney consensus; no single fetched source — label accordingly).

**Consequence:** Financial judgments, consent decrees, state monitoring escalation, reputational damage, staff demoralization.

**Current software:** None purpose-built; districts assemble evidence ad hoc from IEP systems, email, and paper logs.

**Why unsolved:** Rare-event per district (no one builds tooling for it) but common in aggregate; evidence lives in many silos.

**Judgment vs deterministic:** Judgment: strategy, settlement posture. Deterministic: evidence assembly, timeline reconstruction (who-knew-what-when), gap detection in service-delivery logs, correspondence indexing.

**Docs/portals:** IEP system audit logs, service-delivery logs, signed meeting notes, parent communications, state hearing portals.

**Agent fit:** ASSISTANT→WORKFLOW-AUTOMATION (evidence-room builder, timeline reconstructor, gap flagger). Sell as module onto #1.

**Value/district:** Risk-adjusted savings $10K–$50K/yr; higher for urban districts with frequent disputes.

---

### 3. School-based Medicaid billing (related services + expansion beyond IEP)

**Workflow:** Identify Medicaid-enrolled students → obtain parental consent (one-time notice under IDEA regs) → providers deliver billable services (speech, OT, PT, counseling, nursing, psych) → providers document services in logs/paper notes → periodic random-moment time studies (RMTS) where sampled staff code their moment → billing vendor converts documented units to claims → claims submitted through state Medicaid portal → remittances reconciled → quarterly/annual cost reports; PLUS administrative claiming (MAC) based on RMTS. Performed by SPED secretaries, nurses/therapists, Medicaid billing clerks, contracted billing vendors; suffers everyone in the chain.

**Buyer:** Business office/CFO owns the revenue line; SPED director co-owns provider compliance.

**Volume/cost:** Policy landscape transformed: CMS's May 2023 guide affirms billing for ALL Medicaid-enrolled students (free-care reversal), 25 states expanded so far, CMS expects SPA compliance by ~July 2026, and BSCA funded a technical assistance center + $50M in state grants to push participation (ALL VERIFIED: https://healthystudentspromisingfutures.org/federal-support/). Documentation requirements (medical necessity, service notes, provider enrollment) are explicit federal requirements (VERIFIED same source). OIG audits are routine — HSC consolidated 33 OIG audits showing recurring findings on documentation quality (VERIFIED: https://healthystudentspromisingfutures.org/resources/office-of-the-inspector-general-school-medicaid-reports-review/). District reimbursement ranges widely; large urban districts recover millions/yr; many small/rural districts claim nothing because paperwork exceeds capacity (ESTIMATE — national total not fetchable this pass; CMS financial data would resolve). Mid-size district realistic recovery upside: $100K–$800K/yr depending on state expansion status (ESTIMATE).

**Consequence if bad:** Money simply never claimed (silent loss); recoupments after OIG audits for poor documentation; provider enrollment lapses voiding claims; expansion opportunity missed entirely in non-participating districts.

**Current software:** Billing intermediaries (Public Consulting Group, MAXIMUS-type RMTS vendors, district co-ops like MDE Collaborative), spreadsheets + paper therapy logs upstream. Upstream capture (what actually happened in the classroom/therapy room) remains pen-and-paper in most districts — the weakest link.

**Why unsolved:** Billing vendors optimize claims submission (downstream); nobody owns upstream structured documentation from providers, consent tracking, eligibility matching between SIS and state Medicaid files, and RMTS response chasing. Expansion multiplies the workload (more students/providers eligible), making manual processes worse exactly when money got bigger.

**Judgment vs deterministic:** Judgment: medical necessity framing, complex third-party liability. Deterministic: consent tracking, eligibility roster matches, note→structured-claim extraction, unit math, deadline/RMTS chasing, reconciliation, audit-readiness packets.

**Docs/portals:** Paper therapy logs, IEP service pages, state Medicaid provider portals, RMTS notifications (email), remittance advices (PDF/EDI), parental-consent forms.

**Agent fit:** AGENT-OWNED for the documentation-capture/QA/chasing loop; WORKFLOW-AUTOMATION for claim QA. Contingency-fee pricing models exist in adjacent markets (e.g., E-rate) — natural here ("% of newly captured reimbursements").

**Value/district:** See Volume above; this is the highest direct-dollar ROI item on this list and the clearest "agent owns trigger→investigation→action→verification→escalation" loop.

---

### 4. Chronic absenteeism intervention workflows & attendance reporting

**Workflow:** Daily attendance taken in classrooms → SIS aggregates → weekly lists of at-risk students (approaching 5%/10% thresholds) → clerk/principal sends form letters (state-mandated truancy letters at defined thresholds) → calls home → attendance team meetings → student success plans / attendance contracts → coordination with counselors/social workers/community resources → SARB/court referrals (state-dependent) → everything logged for state chronic-absence reporting (ESSA requires public reporting; many states use it in accountability) → year-end reconciliation. Performed by attendance clerks, APs, counselors, family liaisons; suffers principals (accountability) and clerks (labor).

**Buyer:** Superintendent/board (ADA-linked state funding in ~half the states; accountability ratings everywhere); site budgets for interventions.

**Volume/cost:** 28% of US students chronically absent in 2022-23 (VERIFIED, ed.gov); 14.7M students in 2020-21, nearly double pre-pandemic (VERIFIED, Attendance Works: https://www.attendanceworks.org/chronic-absence/the-problem/). A 5,000-student district therefore manages ~1,400 chronically absent students/yr, each requiring tiered touchpoints (ESTIMATE on touchpoint counts; framework VERIFIED via Attendance Works 3-tier model). Staff time: easily 0.5–2 FTE across sites plus principal attention (ESTIMATE). In ADA-funded states each 1-point attendance gain ≈ $60K–$150K/yr revenue for a 5K district (ESTIMATE: ~$10K/student-year funding × fraction attributable).

**Consequence:** Lost ADA revenue, accountability-rating damage, truancy court involvement for families, dropout risk; GAO and ED both flag attendance data quality issues (data-quality caution noted on ED's own dashboard page, VERIFIED: https://eddataexpress.ed.gov/dashboard/chronic-absenteeism/2022-2023).

**Current software:** SIS attendance modules (PowerSchool, Infinite Campus, Skyward), attendance-letter mail-merge tools, some point solutions (SchoolStatus, EveryDay Labs-style nudge vendors). Nudge vendors cover letters/SMS but not investigation (why is this kid absent?), cross-system root-cause synthesis (transport? health? discipline? mobility?), or documented intervention plans aligned to state formats.

**Why unsolved:** The hard part is per-student investigation + multilingual outreach + documentation that survives audit + coordination between school/agency actors. That's an agentic workflow, not a dashboard. Also staffing: clerks cut post-ESSER.

**Judgment vs deterministic:** Judgment: root-cause conversations, sensitive family situations, court referrals. Deterministic: threshold triggers, letter/SMS generation in home language, meeting scheduling, success-plan document assembly, logging, state report extracts, duplicate-record cleanup feeding accurate rates.

**Docs/portals:** SIS attendance tables, state truancy-letter templates, SARB/SART forms, health records, transportation data, McKinney-Vento flags, state longitudinal data system submissions.

**Agent fit:** AGENT-OWNED (trigger → investigate across SIS/transport/health/discipline → personalized multilingual outreach → schedule meetings → maintain plan docs → escalate to human for home visit/court step → verify outcomes → produce compliance reports).

---

### 5. MTSS/RTI intervention documentation & monitoring

**Workflow:** Universal screening 3×/yr (scores land in assessment platform) → identify at-risk students → Tier 2/3 intervention assignment → weekly-biweekly progress monitoring (often paper/graphed by hand) → data-team meetings with notes → fidelity checklists → parent notification letters → adjustment decisions → (if insufficient) SPED referral packet assembly. Performed by classroom teachers + interventionists + coaches/APs.

**Buyer:** Curriculum/instruction leadership; Title I funds pay for many interventions/staff.

**Volume/cost:** Nearly universal adoption of MTSS frameworks across states (state guidance documents mandate documentation tiers — qualitative). Per school: 50–150 students in Tier 2/3 with weekly data points; data teams meet monthly; documentation largely spreadsheets + Google Docs (practitioner consensus, ESTIMATE). Teacher time: 1–3 hrs/wk per teacher involved (ESTIMATE).

**Consequence:** Weak Tier-1/Tier-2 documentation undermines SPED eligibility determinations (states require documented intervention history before evaluation approval in most cases) → either wrongful placements or denied evaluations (litigation exposure); intervention time wasted without fidelity data.

**Current software:** Branching Minds, EduClimber/Illuminate, Panorama, Google Sheets reality. Screening platforms store scores; they don't chase teachers for missing probes, don't auto-graph/summarize for team meetings, don't assemble referral packets from disparate artifacts.

**Why unsolved:** Fragmented data (assessment platform + gradebook + behavior log + attendance), heavy narrative documentation, no admin bandwidth to enforce process.

**Judgment vs deterministic:** Judgment: intervention selection, team decisions about movement between tiers, eligibility discussion. Deterministic: probe collection chasing, chart generation, meeting-note templating, parent letters, referral-packet assembly, fidelity-log completeness checks.

**Docs/portals:** Assessment platform exports, progress-monitoring graphs, meeting agendas/notes, parent consent/notification letters, state MTSS manuals, SPED-referral forms.

**Agent fit:** WORKFLOW-AUTOMATION (strong): continuous data collection nudges, meeting-prep packs, referral assembly. Natural attach to #1 (same buyers overlap heavily).

---

### 6. Multilingual parent communication & front-office triage

**Workflow:** District must communicate with limited-English-proficient (LEP) parents meaningfully (Title VI obligation; ED OCR guidance) — report cards, IEP invitations, disciplinary notices, emergency messages, enrollment forms → requests routed to district translator (if any) or external agency (days of turnaround, $0.10–$0.25+/word ESTIMATE industry pricing) or machine-translated ad hoc by bilingual secretary (quality/liability risk) → phone calls handled by whoever speaks the language or not at all → interpretation arranged for meetings (24–72hr advance booking norm). Front office simultaneously fields high call/email volume (absences, bus questions, records, registration) with chronic clerical understaffing.

**Buyer:** EL director (Title III funds), Communications office, site budgets for interpretation.

**Volume/cost:** 5.3M EL students; 76% Spanish but 400+ languages represented (VERIFIED NCES). A 5K district with 15% EL density serves ~750 EL families; written comms requiring translation run into thousands of pages/yr across district+sites (ESTIMATE); professional translation spend $20K–$150K/yr at scale (ESTIMATE); phone interpretation minutes additional. Front-office volume: dozens of contacts/site/day (UNKNOWN precisely; practitioner consensus).

**Consequence:** OCR complaints/enforcement for failure to serve LEP parents; parents uninformed about IEP/discipline/health events (drives #2/#4 problems); bilingual secretaries as single points of failure.

**Current software:** ParentSquare/Remind/ClassDojo (messaging w/ basic MT), LanguageLine/Propio (phone interpretation), translation agencies (documents). Messaging tools translate outbound templates poorly for nuance/legal text and do nothing for inbound comprehension/triage or document translation workflows with review.

**Why unsolved:** Pre-LLM MT was inadequate for legally consequential text (IEP notices, discipline), so districts defaulted to expensive/slow agencies; inbound phone/email triage had zero automation; no system connects "which families need which message in which language by when."

**Judgment vs deterministic:** Judgment: legally sensitive phrasing review, culturally specific situations. Deterministic: translating standardized notices/notices-with-deadlines, formatting/translating attachments, answering routine FAQ calls/emails in-language, routing complex ones, maintaining glossaries, logging communication for compliance evidence.

**Docs/portals:** District notification templates, SIS contact/language fields, IEP meeting notices, handbooks, registration packets, phone systems.

**Agent fit:** WORKFLOW-AUTOMATION → AGENT-OWNED (voice/text agents handling routine inbound in-language with human escalation; document-translation pipeline with terminology memory and review gates). Communication-compliance log becomes audit asset.

---

### 7. Teacher recruitment: applicant screening & reference checking

**Workflow:** Posting on district ATS/job boards → applications flood in (hundreds for elementary, handful for SPED/math) → HR generalists screen resumes against certification/endorsement requirements → phone screens → reference checks (manual phone calls to prior supervisors, 3+ per finalist) → credential verification (license lookup on state portal) → background/fingerprint clearance → offer → board approval. Principals complain time-to-hire is months; best candidates take other offers first.

**Buyer:** Chief HR officer / superintendent; board approves hires.

**Volume/cost:** 74% of schools struggled to fill teaching vacancies entering 2024-25; average school had 6 vacancies; only 79% filled with fully certified teachers; SPED hardest (VERIFIED NCES SPP: https://nces.ed.gov/whatsnew/press_releases/10_17_2024.asp). District HR processes hundreds–thousands of applications/yr; reference-check calls alone consume hundreds of staff-hrs/yr; cost-per-hire $3K–$8K fully loaded (ESTIMATE). Unfilled positions convert to sub spend (#8) and larger class sizes.

**Consequence:** Unfilled SPED/ESL classes taught by uncertified long-term subs; emergency-certified teachers; slower pipelines compound shortage (candidates accept other districts within days).

**Current software:** Frontline Recruiting & Hiring (AppliTrack), PowerSchool Talent, Tallo/K12JobSpot boards, state license lookup portals. ATS stores applicants; does not rank fit vs. endorsement codes, doesn't conduct references, doesn't parse out-of-state licenses/transcripts.

**Why unsolved:** Screening/reference steps are phone-and-PDF work embedded in statute/collective agreements; HR departments are thin (post-ESSER cuts); ATS vendors compete on posting distribution, not judgment-work automation.

**Judgment vs deterministic:** Judgment: culture fit interviews, portfolio review, equity considerations in selection. Deterministic: resume→structured profile extraction, certification/endorsement match against state licensure data, out-of-state transcript parsing, reference-check orchestration (AI voice or structured async forms), background-status tracking, offer-letter/board-agenda doc generation.

**Docs/portals:** Applicant PDFs, transcripts, state educator-license lookup portals, fingerprint/background vendor portals, board agenda systems.

**Agent fit:** WORKFLOW-AUTOMATION (screening/ranking/reference orchestration with human final decision). High-frequency, low-glamour — classic ugly-problem profile.

---

### 8. Substitute teacher management & absence coverage

**Workflow:** Teacher enters absence (night before/5am) → automated system calls/texts qualified subs → subs decline/ignore → secretary/AP manually phones list at 6:30am → unfilled absences covered by specials teachers, counselors, APs, or class-splitting → daily fill-rate report to HR → payroll reconciles timesheets → long-term absences (FMLA/parental) need weeks of continuity planning. Performed by site secretaries/APs + district substitute coordinators.

**Buyer:** Site budgets pay sub costs; HR owns program; some regions outsourced to Kelly Education/ESS (vendor takes markup, typically 25–35%, ESTIMATE industry norms).

**Volume/cost:** ~300 teachers × 7–9 absences/yr ≈ 2,100–2,700 absence-days/yr in a 5K district (ESTIMATE). Sub daily cost $110–$220 + vendor markup (ESTIMATE; widely variable by region). Annual sub spend $1.5M–$3M for such a district (ESTIMATE). Fill rates: districts routinely operate below full fill; national averages commonly cited in the 60–80% range with wide variation (ESTIMATE — could not fetch a clean national survey this pass; EdWeek Research Center surveys are the canonical source to verify). NCES confirms broader staffing strain: schools averaged 6 teaching vacancies filling at 79% (VERIFIED), which mechanically raises absence pressure.

**Consequence:** Instructional loss (unfilled day ≈ 25 students losing a day), internal staff burnout (counselors covering classes instead of caseloads), compounding of #7 (teachers cite lack of support), overtime costs.

**Current software:** Frontline Absence Management (Aesop), Red Rover, Kelly/ESS proprietary systems. These automate the *call-out sequence* but not proactive supply management: recruiting/credentialing subs, predicting absence spikes (PD days, flu season), matching subs to classrooms by subject/history, negotiating long-term coverage, or integrating with payroll quickly.

**Why unsolved:** Supply-side problem more than dispatch-software problem; incumbent vendors monetize volume, not fill-rate; districts lack recruiting engine for subs (it IS a recruiting funnel — see #7).

**Judgment vs deterministic:** Judgment: which classes can merge safely, long-term placement choices. Deterministic: absence prediction, targeted sub matching/ranking, automated multi-channel outreach with fallback trees, credential-expiry monitoring, timesheet reconciliation, coverage-plan proposals for known upcoming absences (PD days).

**Docs/portals:** Absence management system, sub credential files, payroll system, PD calendar, state sub-permit portals.

**Agent fit:** AGENT-OWNED for dispatch/coverage-planning loop (trigger → predict/match → multi-channel action → verify filled → escalate to human at 5pm prior day → document). Competitive incumbents mean differentiation must come from fill-rate outcomes + recruiting integration.

---

### 9. Certification/license tracking & professional-development compliance

**Workflow:** HR (or a designated cert specialist, or nobody) tracks expiration dates of teaching/admin/sub licenses, endorsements, CPR/first-aid, bus-driver certs, coaching stipend requirements → renewal requires state portal transactions + PD-hour documentation (e.g., states require 60–180 clock hours per renewal cycle) → staff upload certificates as random PDFs → verification against state license lookup → lapse discovery often happens at payroll/licensure audit or mid-year → emergency remediation. Also drives assignments-outside-certification reporting to states (a compliance metric).

**Buyer:** HR chief; Title II-A funds pay for PD.

**Volume/cost:** Every district; ~300 certificated staff × renewal cycles + ~200 paraprofessionals/sub credentials (mid-size district). Hours: 0.25–1 FTE spread across HR + site clerks (ESTIMATE). PD-hour auditing at renewal surges.

**Consequence:** An expired license = employee cannot legally perform duties → immediate classroom coverage crisis, payroll complications, state findings; unqualified-assignment flags hurt accreditation/accountability metrics.

**Current software:** Frontline/AppliTrack modules, state licensure portals (lookup-only), spreadsheets. No system reads uploaded PD certificates and reconciles hours automatically, monitors multiple state portals, or alerts employees with renewal instructions.

**Why unsolved:** Cross-jurisdictional mess (50 state portal formats), low salience until it breaks, HR understaffed.

**Judgment vs deterministic:** Judgment: equivalency decisions for unusual PD/out-of-state credentials. Deterministic: expiry monitoring, certificate OCR→hour extraction→ledger update, portal lookups, employee reminders, assignment-vs-endorsement audits, board-report generation.

**Docs/portals:** Uploaded certificate PDFs, state license lookups, university transcripts, district PD calendars, payroll.

**Agent fit:** WORKFLOW-AUTOMATION (high certainty, modest ACV). Good wedge product; bundles into #7.

---

### 10. Assessment: constructed-response scoring & paper data entry

**Workflow (state level):** Spring summative testing → student constructed responses (essays, math explanations) captured → vendor trains seasonal hand-scoring workforce → responses scored against rubrics (double-scored samples, adjudication) → score files returned → state publishes results months later. **Workflow (district level):** interim/benchmark tests and common assessments frequently include open-response items scored by teachers after school or entered from paper answer sheets by clerks.

**Buyer:** STATE education agency (assessment contracts worth tens of $Ms annually per state — e.g., statewide testing programs typically run $15–$60M/yr in large states; hand scoring is a major contract line) (ESTIMATE — contract values vary; verify per-state RFPs). District side: curriculum directors buying benchmark platforms.

**Volume/cost:** Tens of millions of constructed responses nationally per year across summative + interim programs (ESTIMATE). Industry hand-scoring unit economics commonly quoted at roughly $0.30–$2.00 per response depending on rubric complexity (ESTIMATE — anchor by requesting 2-3 state scoring RFP/contract line items; e.g., Texas STAAR redesign added extended constructed responses beginning 2022-23, materially expanding volume — public knowledge, not re-verified this pass).

**Consequence:** Score delays push results past instructional-use windows; seasonal scorer quality variability; teacher unpaid evening scoring erodes morale; paper entry errors corrupt data used for accountability.

**Current software:** Cambium/ETS/Pearson/WestEd/NCS Pearson scoring platforms (state), NWEA MAP/Illuminate/I-ready (interim). AI-assisted scoring exists at states but adoption is conservative (validity defensibility, litigation risk, union/political sensitivity).

**Why unsolved:** It's not unsolved technically — it's a trust/regulatory problem. States require human-in-loop validity evidence; vendors move slowly; procurement cycles are 5–10 years.

**Judgment vs deterministic:** Judgment: holistic rubric edges, adjudication. Deterministic: first-pass scoring with confidence thresholds, double-scoring only uncertain items (cost halving), rubric calibration materials, paper-sheet OCR.

**Docs/portals:** Scoring platforms, item banks, state assessment portals.

**Agent fit:** ASSISTANT→WORKFLOW-AUTOMATION (confidence-routed hybrid scoring). Buyer is SEA not district — longer sales motion, much bigger contracts. For district-side, bundle benchmark open-response scoring into MTSS/assessment products.

---

### 11. Federal/state compliance reporting: grant management & CRDC

**Workflow (grants):** Accept formula grants (Title I-A/II-A/III-A/IDEA, state programs) → write/submit applications & amendments → maintain budgets by object code → approve expenditures against grant rules (allowability, supplement-not-supplant) → collect documentation from sites → monthly/quarterly drawdowns via state grants portal → period-of-performance closeouts → single-audit support. Performed by federal-programs directors + business-office grant specialists.

**Workflow (CRDC):** Every other winter/spring, every LEA must respond: LEA form + per-school form covering enrollment by race/sex/EL/disability, discipline events, restraint/seclusion, harassment allegations, course access, teacher experience, school finance — assembled from SIS/behavior/discipline/HR systems that don't agree → weeks of spreadsheet reconciliation → submit via CRDC portal → resubmit after validation errors. Next cycle opens Dec 2026 for 2025-26 (VERIFIED: https://www.ed.gov/laws-and-policy/civil-rights-laws/civil-rights-data-collection-crdc).

**Buyer:** Superintendent (compliance owner); federal-programs director + CFO execute. Post-ESSER, grant-compliance staff were cut while obligations persist.

**Volume/cost:** Typical mid-size district manages 8–15 active grants (ESTIMATE); grant management ≈ 0.5–2 FTE + superintendent cabinet attention (ESTIMATE). CRDC: 100–400 staff-hrs per district per cycle (ESTIMATE; scale VERIFIED — universal LEA scope, two long forms). ESSER demonstrated the stakes: $190B flowed through these exact administrative muscles with significant fraud/error findings (VERIFIED totals: Wikipedia ESSER article citing oversight reports).

**Consequence:** Drawdown disallowances (repay federal $), single-audit findings, OCR enforcement triggered by CRDC disparities, late/failed submissions (public record), post-ESSER cliff mismanagement.

**Current software:** State grants-management portals (clunky, per-state), EMAT/Title-specific tools, Excel glue; CRDC has its own portal + PDF survey forms (VERIFIED existence of forms). Nothing assembles the underlying data across systems or drafts allowability reviews.

**Why unsolved:** Each grant small-ish; vendors sell ERP (Tyler/Blackbaud/Skyward finance) that records expenditures but doesn't reason about allowability, prepare narratives, or reconcile across SIS/discipline systems for collections like CRDC.

**Judgment vs deterministic:** Judgment: allowability edge cases, supplement-not-supplant determinations. Deterministic: expenditure-document extraction/coding checks, drawdown prep, deadline tracking, cross-system reconciliation for CRDC elements, anomaly flagging before submission (e.g., suspension counts inconsistent with discipline incidents), narrative drafting.

**Docs/portals:** Grant award notices (PDF), state GME portals, invoice/receipt PDFs, SIS/DIS extracts, CRDC portal + forms PDFs, board reports.

**Agent fit:** WORKFLOW-AUTOMATION → AGENT-OWNED (continuous reconciliation agent with submission-day pack + pre-validation). CRDC timing (Dec 2026) creates a dated forcing function for GTM.

---

### 12. Student records requests, transfers, transcripts (+ public records/FOIA)

**Workflow:** Student moves → new school faxes/emails records request → old school registrar pulls cumulative folder (paper vault + digital SIS) → copies immunizations/transcripts/discipline/IEP → mails/scans → repeat thousands of times yearly; families request copies (FERPA: comply within 45 days — VERIFIED 34 CFR 99.10); colleges/employers order transcripts (increasingly via Parchment/National Student Clearinghouse, which exist specifically to offload this administrative burden — VERIFIED positioning: https://www.studentclearinghouse.org/); attorneys/litigants/journalists file public-records (FOIA/state-equivalent) requests spanning emails and databases → general counsel coordinates searches and redactions under statutory deadlines. Performed by registrars, counseling clerks, central records offices, counsel.

**Buyer:** Central office (student services) + legal; per-site clerks absorb labor. Transcript fees offset little.

**Volume/cost:** Mobility ~10%/yr of enrollment nationally (ESTIMATE from historical NCES mobility rates — verify current figure) → 500 transfer-in record requests/yr for 5K district, plus equal outgoing, plus family requests, plus records-retention purges (state schedules require documented destruction). Records staff 1–3 FTE (ESTIMATE). Public-records requests: rising volume in high-profile districts (litigation/press-driven; UNKNOWN precise trend — qualitative).

**Consequence:** Missing records delay enrollment/special-ed services (child sits without IEP services after move — legally fraught), FERPA/statutory deadlines breached, redaction mistakes leak PII (breach liability), records-loss during storage purges.

**Current software:** Parchment/Clearinghouse handle outbound transcript ordering for participating districts; SIS holds digital records; paper vaults persist; FOIA handled by email + counsel. No agent reads a records request, locates artifacts across SIS+paper scans+email, applies redaction rules, and produces a logged response package.

**Why unsolved:** Long-tail formats (decades of paper), privacy stakes, per-district rarity of dedicated tooling; vendors solved the easy slice (transcript e-commerce) not the retrieval/redaction slice.

**Judgment vs deterministic:** Judgment: discretionary disclosures, subpoena nuances. Deterministic: request intake/classification, artifact location, standard redactions (directory vs. confidential fields), assembly, delivery tracking, retention-schedule enforcement, FOIA log maintenance.

**Docs/portals:** Cumulative folders, SIS transcript modules, state records-retention schedules, public-records portals, fax/email inboxes.

**Agent fit:** AGENT-OWNED for intake→retrieve→redact→assemble→log with human sign-off gate on disclosures. Redaction accuracy is the trust bar.

---

### 13. Back-office finance: procurement, P.O.s, invoice processing

**Workflow:** Site staff want goods → paper/PDF requisition → budget check → P.O. issued (finance system) → vendor ships → paper invoice arrives (mail/PDF) → AP clerk keys it → three-way match (P.O./receipt/invoice) → discrepancies chased by email → coding (fund/object/grant!) → approval routing → check/ACH run → W-9/vendor onboarding, 1099s. Purchasing cards create parallel statement-reconciliation drudgery. Bid/RFP processes add document heft.

**Buyer:** CFO/business manager (this IS the buyer's own pain — strongest economic-buyer alignment of any item here).

**Volume/cost:** Mid-size district: 15K–40K invoices/yr (ESTIMATE scaled from budget/typical ratios); manual processing cost commonly benchmarked at $8–$18/invoice all-in vs $2–$4 automated (industry benchmarks — ESTIMATE, verify against APQC/Ardent Partners data) → district AP cost $200K–$500K/yr (ESTIMATE). Duplicate/erroneous payments and missed early-pay discounts are silent losses.

**Consequence:** Late payments strain vendor relations; grant-coded miscoding causes disallowances (links to #11); fraud exposure; audit findings; CFO time diverted.

**Current software:** Tyler Munis, Skyward, Blackbaud, Escape, PowerFinance + AP-automation point tools (less penetration than private sector). Finance ERPs record transactions; they don't ingest messy PDF invoices, match against receipts, or chase approvals intelligently.

**Why unsolved:** Education lags AP automation adoption generally; procurement rules/local controls make districts cautious; thin IT staff for integrations.

**Judgment vs deterministic:** Judgment: unusual purchases, bid-threshold strategy. Deterministic: invoice OCR→header/line extraction, PO/receipt matching, tolerance checks, grant/object coding suggestions, approval routing/chasing, duplicate detection, p-card statement reconciliation, vendor-doc onboarding (W-9 OCR).

**Docs/portals:** Invoice PDFs/mail, P.O. system, receiving docs, state cooperative contracts, W-9s, 1099 filings.

**Agent fit:** WORKFLOW-AUTOMATION → AGENT-OWNED (touchless processing for matched invoices; exception queue for humans). Well-understood ROI math makes this the easiest pilot to price; competition from horizontal AP vendors means vertical wedge (grant coding + public-sector approval chains) matters.

---

### 14. Enrollment / registration paperwork processing

**Workflow:** Family enrolls (year-round, summer surge) → gathers birth certificate, immunization records, proof of residency, custody orders, prior transcripts (often photos/faxes) → submits online portal or paper packet → registrar/clerk reviews for completeness → chases missing docs → keys data into SIS → uploads documents → language-placement screening flagged (HLS) → free/reduced-meal application data → athletic/health forms → data feeds state student-record system (SSIDs). Charter networks add lottery/waitlist administration; choice/open-enrollment adds inter-district transfer paperwork.

**Buyer:** Central student services; site clerks execute.

**Volume/cost:** 5K district: ~600–900 new enrollments/yr + annual re-registration updates for all (ESTIMATE). Registration season = overtime for clerical staff; incomplete-submission churn dominates effort (practitioner consensus, ESTIMATE).

**Consequence:** Data errors propagate into ALL downstream state reporting (funding counts, #11 CRDC, #4 attendance), immunization noncompliance risks (exclusion laws), delayed start for transient/homeless students (McKinney-Vento immediate-enrollment obligations).

**Current software:** PowerSchool/Infinite Campus online registration modules (forms-based), Scribbles, Docufide-era tools. Portals collect what families type; they don't validate uploaded documents (blurry immunization card? residency utility bill name mismatch?) or reconcile against prior-school records automatically.

**Why unsolved:** Document heterogeneity + verification judgment; SIS vendors treat registration as form-builder, not document-intelligence problem.

**Judgment vs deterministic:** Judgment: residency edge cases, custody disputes. Deterministic: document classification/validation (OCR immunization dates → state format), completeness chasing, SIS field population, duplicate-student detection, HLS routing, SSID submission prep.

**Docs/portals:** Registration packets (PDF/paper), immunization cards, residency docs, state student-ID systems, meal-application systems.

**Agent fit:** WORKFLOW-AUTOMATION (doc-intake validation + auto-keying with human exception queue). Moderate standalone value; high leverage as data-quality foundation for #4, #10, #11.

---

## Cross-cutting observations

1. **The meta-pattern:** every top pain = *document intelligence + chasing humans + deadline compliance + fragile handoffs between SIS/HR/finance/state portals*. This is precisely LLM-agent territory; the installed base (IEP systems, SIS, ATS, ERPs) deliberately stops at structured forms.
2. **Budget-holder map:** direct-revenue problems (Medicaid #3, ADA/attendance #4) have self-funding ROI and CFO/SPED-director buyers — fastest sales motion. Compliance problems (CRDC/grants #11, due process #2) sell on risk to superintendents. Labor problems (#1, #8, #9, #13, #14) sell on hours saved but need union-sensitive framing (reduce nights/weekends, not headcount).
3. **Staffing-shortage amplification:** NCES hiring data (VERIFIED) shows the people who do this paperwork are the scarcest staff; every hour recovered from SPED teachers/registrars/AP clerks converts directly into coverage for unfilled positions.
4. **Timing hooks:** CMS school-Medicaid expansion compliance (~July 2026), Dec 2026 CRDC opening, post-ESSER austerity forcing labor productivity, persistent 28% chronic absenteeism.
5. **Verification gaps to close in diligence:** CADRE national due-process volumes (site blocked), national school-Medicaid reimbursement totals (CMS-64/financial data), substitute fill-rate national survey (EdWeek Research Center), state assessment hand-scoring RFP line items, APQC-style invoice-cost benchmarks applied to districts.

---

## Sources

Verified primary:
- NCES Condition of Education – Students With Disabilities (7.5M IDEA students; 15%): https://nces.ed.gov/programs/coe/indicator/cgg/students-with-disabilities
- NCES Condition of Education – English Learners (5.3M; 10.6%; home languages; ELs w/ disabilities): https://nces.ed.gov/programs/coe/indicator/cgf/english-learners
- NCES School Pulse Panel press release Oct 17, 2024 (vacancies, fill rates, hardest subjects): https://nces.ed.gov/whatsnew/press_releases/10_17_2024.asp
- NCES SPP press-release index: https://nces.ed.gov/surveys/spp/pressreleases.asp
- US ED chronic absenteeism page (31% → 28%): https://www.ed.gov/teaching-and-administration/supporting-students/chronic-absenteeism
- ED Data Express chronic-absenteeism dashboard (data-caution note): https://eddataexpress.ed.gov/dashboard/chronic-absenteeism/2022-2023
- AEI Return to Learn Tracker (~15% pre-pandemic baseline): https://www.returntolearntracker.net/
- Attendance Works – The Problem (14.7M students; doubling): https://www.attendanceworks.org/chronic-absence/the-problem/ and 2022-23 state analysis: https://www.attendanceworks.org/chronic-absence-remained-a-significant-challenge-in-2022-23/
- ERIC ED479674 – SPeNSE Paperwork Substudy (5 hrs/wk; 88% interference): https://eric.ed.gov/?id=ED479674
- Healthy Students Promising Futures – Federal Guidance (CMS 2023 guide; free care; 25 states; July 2026 compliance): https://healthystudentspromisingfutures.org/federal-support/
- HSPF – OIG audit consolidation (33 audits): https://healthystudentspromisingfutures.org/resources/office-of-the-inspector-general-school-medicaid-reports-review/
- HSPF – BSCA impact report page: https://healthystudentspromisingfutures.org/resources/how-the-bsca-helped-expand-school-medicaid-and-student-health-services/
- US ED – Civil Rights Data Collection page (universal LEA scope; forms; Dec 2026 opening): https://www.ed.gov/laws-and-policy/civil-rights-laws/civil-rights-data-collection-crdc
- eCFR 34 CFR 99.10 (FERPA 45-day rule): https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-B/section-99.10
- Wikipedia ESSER ($190B breakdown; oversight context): https://en.wikipedia.org/wiki/Elementary_and_Secondary_School_Emergency_Relief_Fund
- National Student Clearinghouse (transcript/verification burden-offloading positioning): https://www.studentclearinghouse.org/
- NCES School Pulse Panel overview/data index: https://nces.ed.gov/surveys/spp/results.asp
- Mississippi DOE chronic-absence definition example (ADA vs chronic absence): https://www.mdek12.org/publicreporting/wp-content/uploads/sites/33/2024/01/chronic_absenteeism_2023-final_9.25.2023_230p.pdf
- AEI/ERIC – Lingering Absence in Public Schools: https://files.eric.ed.gov/fulltext/ED673951.pdf

Blocked/unavailable during research (recommended follow-ups):
- CADRE national IDEA dispute-resolution statistics (cadreworks.org returned 403)
- NCSL teacher-shortage summaries (403)
- EdWeek Research Center substitute-teacher surveys (paywall/search-block)
- State assessment hand-scoring contract line items (need RFP pulls, e.g., TEA/Georgia DOE procurement)
- OCR CRDC portal detail (ocrdata.ed.gov is JS-only)
