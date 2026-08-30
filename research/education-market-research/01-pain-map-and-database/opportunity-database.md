# Education Pain Map & Scored Opportunity Database

**Synthesized:** Aug 25, 2026 from six raw research streams (`00-raw-segment-research/`). Evidence labels: VERIFIED (URL-cited in raw files), ESTIMATE, UNKNOWN — carried through.

---

## PART A — EDUCATION PAIN MAP

The meta-pattern found across all segments: **a regulated document pipeline between humans, agencies, and legacy systems that nobody owns end-to-end**, executed by understaffed offices, stitched together with email + spreadsheets + PDF portals. Installed software (SIS/ERP/CRM) is systems-of-record; it deliberately stops at the human handoff. The recurring agentic loop is: *acquire messy documents → extract → check against rulebook → assemble outputs → chase humans for missing inputs → log for compliance.*

### K-12 US
| Value-chain area | Pain | Intensity / anchor evidence |
|---|---|---|
| Special education | IEP authorship & timeline compliance; due-process evidence assembly; Medicaid time-study billing | EXTREME — SPeNSE 5 hrs/wk, 88% interference [V]; loudest practitioner theme (9+ threads, attrition language); CMS expansion deadline ~Jul 2026 [V] |
| Student success | Chronic absenteeism intervention loops; MTSS documentation | HIGH — 28% chronically absent [V]; ADA funding + accountability exposure |
| Compliance | CRDC biennial census, grant management/drawdowns, state reporting | MEDIUM-HIGH — universal LEA scope, Dec 2026 cycle opening [V]; post-ESSER staff cuts |
| HR/staffing | Teacher screening/reference checks; substitute coverage; license/PD tracking | HIGH — 74% schools can't fill vacancies [V]; $1.5–3M/yr sub spend per mid-size district [E] |
| Back office | AP/invoice processing w/ grant coding; enrollment doc intake; records/FOIA fulfillment | MEDIUM — classic doc-intel ROI; FERPA 45-day clock [V] |
| Communication | Multilingual parent comms (Title VI obligation); front-office call/email triage | MEDIUM-HIGH — 5.3M EL students [V]; OCR complaint risk |

### Higher Education US
| Value-chain area | Pain | Anchor evidence |
|---|---|---|
| Financial aid | Verification doc-chase & review; PJ/SAP appeals; R2T4/reconciliation; FAFSA-surge ops | 2.35M files & 371K federal burden-hours [V, 91 FR 13825]; mass manual ISIR corrections 2024 [V] |
| Admissions/enrollment | Transcript intake & evaluation; transfer articulation (43% credit loss [V, GAO]); yield/melt chasing; stop-out re-enrollment | SCNC pool 43.1M, +2.1M/yr [V, NSC]; melt math: 1pp ≈ $500K+ at mid-size private [E] |
| Student success | Early-alert follow-through failure; advising shadow-Excel plans | Caseloads 320–1400 vs 250 standard [V-practitioner]; institutions already pay EAB/Navigate six figures |
| Registrar | Degree-audit exceptions; transcript backlogs ("team of 4 : 4,000 admits") | Practitioner-verified [V]; graduation-delay revenue risk |
| Compliance/accreditation | Self-study evidence assembly; IPEDS/Clery/SARA; SEVIS fixed-period rule (Jul 2026) [V]; VA monthly verification (Jan 2026) [V] | Sanction/existential tail risks |
| Research admin | Pre-award proposal assembly; subrecipient monitoring | $2–10K/proposal prep cost [E]; audit-magnet workflows |

### Education Businesses (fastest-moving buyers)
| Segment | Pain | Anchor evidence |
|---|---|---|
| Certification bodies | Application adjudication vs 100-page handbooks; CE/recert audits; credential verification phones; accommodations files | TruMerit 14-week primary-doc delay [V]; LSAC 85K applicants/yr scale [V] |
| Study abroad/recruitment | Application factory (portal re-keying × dozens of universities); visa-file refusal prevention | Adventus 60K students/yr + outsourced admissions arms prove paid demand [V]; 47% of Canadian refusals = money paperwork [V, ApplyBoard/ICEF] |
| Tutoring vendors | District-contract ops: attendance→invoice→progress-report pipeline; disputes | NSSA codifies mandatory artifacts [V]; disputed-invoice leakage 2–5% [E] |
| Career colleges/bootcamps | Multi-jurisdiction filing stack (BPPE SPFS Dec 1, accreditors, SARA); placement-rate verification & marketing-compliance | BloomTech: $75K fine + CFPB order [V] — existential precedent |
| Test-prep/training cos | Essay scoring ops; localization update propagation; compliance-training audit evidence | AP 2M+ human-scored exams as market proof [V] |

### International
| Region | Loudest pain |
|---|---|
| UK | **SEND/EHCP crisis**: 718.8K plans (+12.5% YoY), only 46% within 20-week limit, annual reviews only 56.8% completed [V, DfE]; MAT back-office centralisation; university finance squeeze |
| Australia | RTO/VET compliance evidence packs (~4,000 RTOs); CRICOS obligations post-visa tightening |
| Canada | Post-permit-cap retention desperation; PAL/LOA document handling; 997,820 intl students end-2024 [V] |
| EU | Erasmus+ administration (€26bn programme); AI Act makes education high-risk — conformity is a moat for early movers |
| Gulf | Private-school parent ops (KHDA-accessible); ministry-scale tenders partner-only |
| India | NAAC overhaul post-corruption scandal (CBI arrests Feb 2025 [V]) — "provably untainted" accreditation-evidence wedge across ~45K HEIs |

---

## PART B — OPPORTUNITY DATABASE (52 problems)

Scoring: each dimension 1–10, oriented so **higher = better** (competition=whitespace; complexity=ease of implementation; regulatory risk=low risk; data access=easy access). Total = sum/140. Scores are judgment calls anchored to raw-file evidence; totals are a sorting aid, NOT the decision — see finalist rationale.

Legend: P1 pain severity · P2 frequency · P3 economic cost · P4 buyer WTP · P5 agent suitability · P6 automation potential · P7 competition whitespace · P8 differentiation potential · P9 ease reaching buyers · P10 implementation ease · P11 regulatory safety · P12 data access ease · P13 global scalability · P14 recurring-revenue potential

| # | Problem (segment) | Buyer | Agent level | Est. value/customer/yr | Key incumbents | P1 |P2|P3|P4|P5|P6|P7|P8|P9|P10|P11|P12|P13|P14| Σ |
|---|---|---|---|---|---|---|
| O01 | IEP paperwork & compliance copilot (K-12) | SPED Director | AGENT-OWNED | $60–140K labor equiv [E] | Frontline/Embrace (form-fillers) | 9|9|8|7|8|8|9|8|6|6|6|6|8|8| **113** |
| O02 | School Medicaid billing capture & time-study agent (K-12) | CFO/Bus Office | AGENT-OWNED | $100–800K recovered [E], self-funding | PCG/MAXIMUS (downstream only) | 8|8|9|9|9|8|9|8|7|6|5|5|6|9| **116** |
| O03 | SPED due-process evidence room (K-12) | Supt/counsel | WORKFLOW-AUTO | Risk-adj $10–50K [E] | none purpose-built | 7|3|8|6|7|7|10|7|5|6|6|5|4|6| **87** |
| O04 | Chronic absenteeism intervention loop (K-12) | Supt/principals | AGENT-OWNED | $100–400K ADA + hours [E] | EveryDay Labs/SchoolStatus (nudges only) | 8|10|8|7|9|8|7|8|7|6|7|7|7|8| **115** |
| O05 | MTSS documentation & referral packets (K-12) | C&I leaders | WORKFLOW-AUTO | $30–100K [E] | Branching Minds/Panorama | 6|9|6|6|7|7|6|7|6|7|7|7|6|7| **91** |
| O06 | Multilingual family communication agent (K-12) | EL Dir/Comms | WORKFLOW-AUTO→AGENT | $30–150K + risk [E] | ParentSquare/TalkingPoints | 7|10|6|6|8|7|5|6|7|7|7|7|8|7| **98** |
| O07 | Teacher applicant screening & reference agents (K-12) | CHRO | WORKFLOW-AUTO | $50–150K [E] | Frontline Recruit & Hire | 7|9|6|6|8|7|8|7|6|6|7|6|6|7| **97** |
| O08 | Substitute sourcing/prediction agent (K-12) | HR/site budgets | AGENT-OWNED | $200–500K spend opt. [E] | Frontline Absence/Kelly/ESS | 8|10|7|6|8|7|6|7|6|5|7|6|6|7| **98** |
| O09 | License/PD-hours tracking ledger (K-12) | HR | WORKFLOW-AUTO | $10–40K [E] | spreadsheets/state portals | 5|9|4|4|7|8|8|6|6|7|8|6|5|6| **89** |
| O10 | Constructed-response scoring ops (state/test-prep) | SEA/prep cos | WORKFLOW-AUTO | $100K–Ms contracts [E] | Cambium/ETS/Pearson | 7|6|9|5|7|7|5|6|3|5|4|7|7|8| **86** |
| O11 | Grant management + CRDC assembly (K-12) | FedProgs Dir/CFO | WORKFLOW-AUTO→AGENT | $30–120K/cycle [E] | ERP+Excel glue | 7|7|7|7|8|8|8|7|6|6|6|6|5|7| **95** |
| O12 | Records/FOIA request fulfillment agent (K-12/HE) | Student svcs/counsel | AGENT-OWNED | $20–80K + risk [E] | Parchment (outbound slice only) | 6|8|5|5|8|7|8|7|6|5|5|5|7|6| **88** |
| O13 | AP invoice processing w/ grant coding (districts) | CFO | AGENT-OWNED | $40–120K [E] | Tyler/eFinance + horizontal AP tools | 6|10|6|7|8|8|6|6|7|6|8|7|5|8| **95** |
| O14 | Enrollment registration doc validation (K-12) | Student svcs | WORKFLOW-AUTO | $15–60K [E] | SIS form modules | 5|7|4|4|7|7|7|6|6|6|7|6|6|6| **82** |
| O15 | Financial aid verification pipeline (HE) | Aid Dir (Enrol Div) | AGENT-OWNED | $140–220K labor [E] + retention | Anthology StudentForms, VerifyMyFAID | 8|9|8|8|9|8|7|7|7|6|5|6|4|8| **108** |
| O16 | PJ/SAP appeal casework (HE) | Aid Dir | WORKFLOW-AUTO | $200–600K retained [E] | none dominant | 7|7|7|7|7|6|9|7|6|6|5|5|4|7| **90** |
| O17 | R2T4 withdrawal & reconciliation ops (HE) | CFO/Aid | AGENT-OWNED | liability + tens of $Ks [E/U] | SIS modules, FastR2T4-type | 6|8|7|6|8|8|8|7|6|6|5|5|4|6| **92** |
| O18 | FAFSA-disruption surge ops (HE) | Enrol Div | WORKFLOW-AUTO | insurance-frame, episodic [E] | Slate CRM | 6|3|7|6|7|7|7|6|5|6|6|5|4|5| **80** |
| O19 | Admissions transcript intake intelligence (HE) | Admissions Dir | AGENT-OWNED | 2–4 FTE equiv [E] | Slate (CRM not docs), WES (human svc) | 7|9|7|8|9|8|7|8|7|6|7|6|6|8| **111** |
| O20 | Transfer credit articulation engine (HE) | Enrol+AcadAffairs | WORKFLOW-AUTO→AGENT | $375K+ retained [E]; GAO 43% loss [V] | TES/DegreeWorks tables | 8|8|8|7|8|7|7|8|6|5|6|5|6|7| **96** |
| O21 | Yield/melt completion orchestrator (HE) | VP Enrollment | AGENT-OWNED | $500K+/pp melt [E] | Slate checklists/EAB | 8|7|9|9|9|8|7|7|7|6|7|7|5|8| **112** |
| O22 | Stop-out re-enrollment engine (HE/CC) | VP Enrol/state | AGENT-OWNED | $600K–2.5M recovered [E]; 43.1M pool [V] | ReUp/EAB modules | 8|7|9|9|9|8|7|7|7|6|7|6|6|8| **114** |
| O23 | Early-alert case execution layer (HE) | Student Affairs | WORKFLOW-AUTO | $600K–1M retention/pp [E] | EAB Navigate/Civitas/Starfish | 7|9|8|7|8|7|5|6|6|6|7|6|5|7| **94** |
| O24 | Degree-audit exception workflow (HE) | Registrar | WORKFLOW-AUTO→AGENT | 1–3 FTE + completion rev [E] | DegreeWorks/CAPP | 6|9|6|6|7|7|7|6|5|5|7|5|4|6| **87** |
| O25 | VA SCO certification queue (HE) | Registrar/Vet office | WORKFLOW-AUTO→AGENT | $150–400K retained [E] | VA-ONCE (ancient) | 6|9|6|6|8|8|8|7|5|5|6|5|4|6| **91** |
| O26 | SEVIS/DSO compliance ops (HE) | Intl office | WORKFLOW-AUTO | $200K+ protected [E]; new Jul 2026 rule [V] | Terra Dotta | 7|8|7|7|7|7|7|6|6|5|4|5|5|7| **88** |
| O27 | Accreditation evidence locker & drafting (HE) | Provost/ALO | WORKFLOW-AUTO | $50–150K/cycle + existential [E] | Watermark/Weave (hated, clunky) | 7|4|8|8|8|7|6|7|5|5|7|5|6|7| **90** |
| O28 | IPEDS/Clery/SARA reporting assembly (HE) | IR/CFO/police | WORKFLOW-AUTO | $50–150K equiv [E] | spreadsheets/portals | 5|8|5|6|7|8|7|6|5|6|5|5|5|6| **84** |
| O29 | Research pre-award assembly & subrecipients (HE) | VP Research | WORKFLOW-AUTO | $10–20M awards upside [E] | Cayuse/Kuali | 6|8|8|7|7|7|6|6|5|5|6|5|6|7| **89** |
| O30 | CC placement + Perkins/WIOA reporting (HE) | AcadAffairs/deans | WORKFLOW-AUTO | grant continuity [E] | statewide platforms+Excel | 6|8|6|6|7|7|7|6|5|5|6|5|5|6| **85** |
| O31 | Cert-body application adjudication (Biz) | Dir Certification | AGENT-OWNED | $150–400K [E] | homegrown portals | 8|9|7|8|9|8|9|8|7|7|7|6|6|8| **115** |
| O32 | Primary-source document chase network (credential eval) (Biz) | COO evaluator/agencies | AGENT-OWNED | $500K–2M throughput [E]; 14-wk delay [V] | TruMerit's own portal attempts | 8|9|8|8|9|8|9|8|6|5|6|4|8|7| **102** |
| O33 | Item-writing/psychometric doc pipelines (Biz) | VP Exams | ASSISTANT/WF | $50–200K/cycle [E] | Word/email + item banks | 5|6|6|6|7|6|8|6|5|6|7|6|6|6| **86** |
| O34 | Candidate support + accommodations triage (Biz) | Dir Cand Services | AGENT-OWNED(t1) | $300K–1.5M large bodies [E] | Zendesk+PDF handbooks | 7|9|7|7|8|7|7|7|7|7|6|6|7|8| **100** |
| O35 | Recertification/CE audit ops (Biz) | Dir Cert Ops | AGENT-OWNED | $80–250K [E] | renewal portals+Excel | 6|9|6|7|8|8|8|7|7|7|7|6|7|8| **101** |
| O36 | Credential verification service ops (Biz) | COO body | AGENT-OWNED | $100–400K + API upsell [E] | phone/email registries | 5|10|5|7|9|9|7|7|7|8|7|6|8|7| **100** |
| O37 | Essay scoring ops for test-prep (Biz) | Ops head | WORKFLOW-AUTO | $100–350K [E] | homegrown queues | 6|8|6|6|7|7|6|6|6|6|6|6|6|7| **90** |
| O38 | Study-abroad application factory (Biz/global) | Agency founder/VP Ops | AGENT-OWNED | $50–150K agency [E]; commissions at stake [V-scale] | Adventus/ApplyBoard marketplaces | 7|10|7|8|9|8|6|7|7|5|7|5|9|7| **102** |
| O39 | Visa-file packaging & refusal prevention (Biz/global) | Agency founder/Dean Intl | AGENT-OWNED | $25–100K agency; 7-figure institutional [E]; 47% stat [V] | checklists+senior eyeballs | 8|9|7|8|9|8|9|8|7|5|7|5|8|7| **105** |
| O40 | Tutoring district-contract ops pipeline (Biz) | Vendor COO/founder | AGENT-OWNED | $60–150K/vendor [E]; leakage 2–5% [E] | LMS-lite+spreadsheets | 6|9|6|7|8|8|8|7|6|6|7|6|6|7| **98** |
| O41 | Career-college multi-jurisdiction filing factory (Biz) | Owner/COO | AGENT-OWNED | $20–70K + survival [E]; BloomTech [V] | portals+consultants | 7|8|6|8|8|8|9|8|6|6|7|6|5|7| **98** |
| O42 | Placement verification & marketing-compliance audit (Biz) | President/GC | WF→AGENT | $50–150K + existential [E/V] | spreadsheets/manual ad review | 7|7|6|7|8|7|9|8|5|6|6|6|5|6| **93** |
| O43 | Training content localization propagation (Biz) | GM Delivery/VP L&D | WORKFLOW-AUTO | $50–200K [E] | TMS/CAT glue | 6|7|6|6|7|7|6|6|6|5|8|6|7|7| **90** |
| O44 | Compliance-training audit-readiness agent (Biz) | CCO provider/client | AGENT-OWNED | $40–120K/provider [E] | LMS exports+SharePoint | 6|8|6|7|8|8|8|7|6|6|7|6|7|7| **96** |
| O45 | EdTech RFP desk + roster onboarding (Biz) | VP Sales/CX | WORKFLOW-AUTO | $150–500K (0.5–2% ARR) [E] | bid libraries+scripts | 6|8|6|8|8|7|8|7|6|6|8|6|6|6| **95** |
| O46 | UK EHCP statutory casework automation (Intl) | LA SEND teams (153 LAs) | AGENT-OWNED | LA High-Needs deficits £bn-scale [E]; 46% timeliness [V] | legacy LCS-class case systems | 9|9|9|8|8|8|8|8|6|5|6|5|5|8| **102** |
| O47 | UK MAT back-office centralisation (Intl) | MAT central teams | WORKFLOW-AUTO | consolidation savings [E] | consolidating ERPs | 6|8|6|7|7|7|6|6|6|5|7|6|5|7| **89** |
| O48 | AU RTO compliance evidence packs (Intl) | RTO owners (~4,000) | AGENT-OWNED | audit-prep cost [U], sanctions risk | consultants+spreadsheets | 7|8|6|7|8|8|8|7|7|6|6|6|5|7| **94** |
| O49 | India NAAC/NBA accreditation evidence (Intl) | HEIs (~45K, rebuilding) | WORKFLOW-AUTO | accreditation survival spend [E]; scandal [V] | consultants (discredited) | 8|4|7|7|8|7|9|8|7|5|6|6|5|6| **93** |
| O50 | Erasmus+ administration assistant (EU) | coordinators (universities/schools) | WORKFLOW-AUTO | coordinator time [U] | National Agency portals | 6|8|5|5|7|7|8|6|5|5|7|5|7|5| **86** |
| O51 | Canada post-cap yield/retention + PAL handling (Intl) | college enrolment deans | WORKFLOW-AUTO→AGENT | distressed-budget retention [E]; caps [V context] | Slate-class CRMs | 7|7|7|7|8|7|7|7|6|5|6|6|6|7| **96** |
| O52 | UAE private-school admissions/parent ops (Gulf) | school groups (GEMS/Taaleem class) | WORKFLOW-AUTO | premium ARPU [E] | bespoke/local vendors | 6|8|6|8|7|7|7|6|5|5|7|6|6|7| **91** |

### Database observations
1. **Highest raw scores cluster around one shape:** statutory/compliance document pipelines with a named economic buyer and direct dollar consequences (O02, O04, O22, O31, O21, O01, O19, O39, O46).
2. **Weakest scores** are either diffuse-buyer problems (teacher workload tools), state-agency sales (assessment scoring), or episodic insurance buys (FAFSA surge ops) — real pain, poor first-business shape.
3. **Cross-cutting platform logic:** O19+O20+O32 share one transcript-intelligence core; O01+O03+O46 share a special-ed casework core with UK expansion; O41 generalizes into an international "regulatory filing factory" (AU RTO O48, IN NAAC O49). Deep dives should treat these as families.

---

## PART C — FINALIST SELECTION (Top 10 for deep dives)

Selection weighted by: verified pain × economic buyer with budget × agent ownership potential × accessibility for 1–5 person team × service-first viability × defensibility — NOT raw score alone.

| DD | Opportunity (database refs) | Why selected over higher-scoring peers |
|---|---|---|
| DD-01 | **SPED casework copilot: IEP drafting, timelines, due-process readiness** (O01+O03) | Largest verified time sink; extreme practitioner intensity; empty agentic field; UK EHCP expansion path (O46). Buyer urgency proven by districts paying to split paperwork from case management. |
| DD-02 | **School Medicaid billing capture agent** (O02) | Only opportunity that *creates* district revenue (self-funding sale); CFO buyer; CMS July-2026 expansion forcing function; contingency pricing proven elsewhere. |
| DD-03 | **Financial aid verification & appeals pipeline** (O15+O16) | Biggest verified volume in higher ed (2.35M files [V]); doc-intelligence-native; community colleges as fast, desperate first customers; ghost-student fraud tailwind. |
| DD-04 | **Stop-out re-enrollment engine** (O22) | Pure revenue lever on 43.1M-person verified pool; NSC evidence that paperwork removal alone creates degrees; demographic cliff makes it strategic for every enrollment VP. |
| DD-05 | **Yield/melt completion orchestrator** (O21) | Cleanest ROI math in the study ($500K+/percentage point); deterministic chase work; VP Enrollment owns budget and target directly. |
| DD-06 | **Transcript & transfer-credit intelligence** (O19+O20+O32) | One technical core amortized across admissions/registrar/credential-eval; GAO 43% loss + team-of-4:4,000 evidence; build-on-Slate strategy avoids CRM war. |
| DD-07 | **Chronic absenteeism closed-loop intervention** (O04) | 28% national rate [V]; funding-linked; nudge incumbents leave the investigation/documentation half unsolved; natural K-12 land-and-expand. |
| DD-08 | **Certification-body adjudication ops** (O31+O34+O35+O36) | Fastest-paying customer type in study (ops teams, no boards); handbook-rule-engine-over-documents is pure RAG/OCR sweet spot; multiple wedges (apps, CE audits, verifications). |
| DD-09 | **International student application & visa-file factory** (O38+O39) | Private buyers (agencies, institutions) already pay for throughput (Adventus APS [V]); refusal-prevention has a verified 47% hook; global by construction; fastest possible sales cycles. |
| DD-10 | **Career-college regulatory filing factory** (O41+O42) | Enumerable deadlines, existential consequences, owner-operator buyers; generalizes to AU RTO (O48) and India NAAC (O49) as the same product family. |

**Deliberately NOT deep-dived despite good scores:** O06/O08 (comms/substitute — crowded or supply-side economics dominated by staffing giants), O11/O28 (reporting assembly — strong wedge but better sold as module of others), O23 (early alerts — EAB retaliation risk on its home turf), O49 (India NAAC — big but ARPU/timing uncertain), O46 (UK EHCP — tracked inside DD-01 as expansion).

Next: Wave 3 deep dives → `02-deep-dives/`, then red-team → `03-red-team/`.
