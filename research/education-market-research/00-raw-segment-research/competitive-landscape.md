# Competitive Landscape & Money Map — AI-Agent Opportunities in Education Operations

**Prepared:** Aug 25, 2026 · **Scope:** US primary, global secondary · **Client lens:** small AI-systems builder (LLM agents, RAG, OCR/doc intelligence, workflow automation) choosing which education OPERATIONS problem to attack.

**Labeling convention:** `[FACT]` = verified against a cited URL during this research. `[REPORTED]` = widely reported figure/event, plausible but not re-verified this session. `[INFER]` = analytical inference from domain knowledge. `[UNVERIFIED]` = specific number/date not independently checked.

---

## 1. Incumbent Software Map (by operational category)

### 1.1 Student Information Systems (SIS)

| Vendor | Position | Pricing signal | Ecosystem | Weaknesses |
|---|---|---|---|---|
| **PowerSchool** (incl. eSchoolPLUS, Naviance) | Dominant K-12 SIS; taken private by **Bain Capital** (Wikipedia's "PowerSchool" entry redirects to Bain Capital's page — evidence of PE roll-up status) | Opaque; district contracts commonly $1–$10+/student/mo `[INFER]` | Huge API/partner marketplace (Unified Classroom, OneRoster/SFTP integrations) | **Massive data breach**: disclosed Jan 2025, ransom paid, districts later extorted ([The74](https://www.the74million.org/article/powerschool-got-hacked-now-what/), [The74 May 2025](https://www.the74million.org/article/powerschool-paid-off-hackers-after-huge-breach-now-theyre-extorting-districts/)); Wisconsin district sued ([The74](https://www.the74million.org/article/wisconsin-district-sues-ed-tech-giant-powerschool-after-massive-data-breach/)); teen hacker sentenced to 4 years ([The74](https://www.the74million.org/article/powerschool-hacker-thankful-i-got-caught-sentenced-to-4-years-in-prison/)). Trust damage + migration fatigue from serial acquisitions `[INFER]` |
| **Infinite Campus** | Strong in large/suburban districts (esp. Midwest/West) | Not public; perpetual-license heritage `[INFER]` | Closed-ish ecosystem; state reporting built in | Monolithic one-vendor stack; UI/data-export rigidity; slow third-party integration `[INFER]` |
| **Skyward** | Mid-market districts, TX/IL/WI strongholds | Not public `[FACT-gap]` | Own finance + HR modules | Legacy codebase (sms 2.0 transition pain), thin partner API surface `[INFER]` |
| **Ellucian** (Banner, Colleague, Ethos) | Dominant higher-ed SIS/ERP | Not public; PE-owned (Vista/Blackstone take-private, ~$3.5B, 2021) `[REPORTED]` | Ethos middleware, large partner network, big services bench | Banner/Colleague are ledger-grade systems with decades of campus-specific customization; migrations routinely run years and millions; support quality is a chronic complaint theme `[INFER from buyer forums/G2 patterns]` |
| **Anthology** (CampusLogic, CampusNexus, Unit4 student mgmt) | #2 higher-ed suite; formed via PE roll-up (Campus Mgmt + Campus Labs → +CampusLogic 2021 → +Unit4 student systems 2023) `[REPORTED]` | Not public | Broad module map, weak coherence | Post-acquisition integration debt, layoffs, and lender-driven restructuring reported 2023–25 `[REPORTED/UNVERIFIED]`; customers describe "suite of acquired products, not a platform" `[INFER]` |

**Takeaway:** SIS is system-of-record territory — don't attack head-on. But every agentic workflow must read/write SIS data through creaky APIs; an integration/RAG layer over SIS is the wedge, not the SIS itself. `[INFER]`

### 1.2 Special Education / IEP software

| Vendor | Notes |
|---|---|
| **Frontline SpEd** (legacy Excent/eSped base) | Market leader in states like NY/TX; forms + compliance calendars + Medicaid billing modules `[FACT: product existence; INFER: market position]` |
| **Embrace Education** | Midwest stronghold; state-specific IEP forms; priced per-student (~$10–$30/sped student/yr typical) `[UNVERIFIED pricing]` |
| **spEdTrack**, **PCG EasyIEP**, **SEAS (PCG)**, **A2IA/state-built systems** | State-level contracts; deeply form-centric `[FACT: existence]` |

**Forms-management vs workflow intelligence:** These products are essentially **structured form fillers + deadline trackers + compliance audit trails**. None offer: drafting assistance grounded in evaluation data, cross-document consistency checking (eval → IEP goals → services → prior written notice), meeting-scheduling orchestration, or Medicaid time-study automation. Sped teachers report spending hours per IEP on clerical work `[INFER from persistent teacher workload complaints]`. This is arguably the single most paperwork-dense workflow in K-12 with zero agentic tooling. `[INFER]`

### 1.3 Student success / retention CRM (higher ed)

- **EAB Navigate** — dominant incumbent; 600+ campuses `[REPORTED]`; parent company EAB was taken private by EQT (~$3.7B, 2023) `[REPORTED]`. Launched **Navigate AI** assistant (2024) `[REPORTED — company marketing]`. Weaknesses: services-heavy delivery model (consultants configure playbooks), high contract values, rule-based campaign logic, slow feature velocity `[INFER]`.
- **Civitas Learning** — persistence analytics + advising workflows; raised $80M+ historically `[REPORTED]`. Predictive models aging in LLM era; UI complexity complaints `[INFER]`.
- **Element451** — AI-forward CRM ("Bolt" agents) targeting mid-market `[FACT: product exists; UNVERIFIED traction]`.
- **Mainstay** (ex-AdmitHub) — conversational texting/AI nudging; ~$12M raised (Rethink Education et al., 2021–22) `[REPORTED]`.
- **EdSights** — AI textbot for retention/melt; single-digit-M funding `[REPORTED]`.
- **Signal Vine** — rules-based two-way texting; acquired by EAB (2022) `[REPORTED]` — consolidation signal that standalone texting commoditized. `[INFER]`
- **ReUp Education** — re-enrollment/recovery coaching (services+software hybrid); ~$47M lifetime `[UNVERIFIED amount]`.

**Weakness pattern:** incumbents sell *campaigns and dashboards*, not *closed-loop case execution*. Advisors still manually chase documents, registration blocks, SAP appeals, melt calls. `[INFER]`

### 1.4 Admissions CRM + transcript/AI evaluation

- **Technolutions Slate** — de facto standard: **2,000+ colleges** use it `[FACT — technolutions.com](https://www.technolutions.com/)`. Public price sheet: admissions license tiers **$30K (<1,500 apps) → $175K (80–100K apps)**; student-success license $30K; advancement $50K–$175K; "most clients pay $50,000/year"; **no price increase in 20+ years** `[FACT — licensing page](https://www.technolutions.com/licensing)`. Massive Platinum/Gold implementation-partner bench (Huron, Carnegie, Encoura/Ruffalo Noel Levitz, Solidan, Ferrilli…) `[FACT — same page]`. Ships its own **Slate AI** `[FACT — nav item](https://www.technolutions.com/slate-ai)`.
  - Weaknesses: legendary configurability = steep learning curve; reader workflows remain manual; transcript/document intake is OCR-lite; consultant ecosystem means institutions pay again for configuration talent `[INFER]`.
- **TargetX** (Salesforce-based) — losing share to Slate; example: Illinois Central College migrated TargetX→Slate `[FACT — Technolutions case study](https://www.technolutions.com/slatest-news/a-solidan-success-story-illinois-central-college-icc)`.
- **Element451, Enrollment Rx, Liaison** — niche alternatives `[FACT: existence]`.
- Transcript/credential processing: Parchment (acquired by Instructure, 2024, ~$800M+) and National Student Clearinghouse dominate exchange `[REPORTED]`; international credential evaluation still dominated by human-services monopolies (WES, ECE) with weeks-long turnaround `[INFER]`. **No strong AI-native transcript-evaluation agent has displaced manual reading at scale** `[INFER]`.

### 1.5 Financial aid management (higher ed)

- **Anthology (ex-CampusLogic) StudentForms/Financial Aid suite** — verification, SAP appeals, cost-of-attendance; enterprise-priced `[FACT: existence; REPORTED: ~$730M CampusLogic acquisition 2021 — UNVERIFIED]`.
- **Ocelot** — financial-aid chatbot/video knowledge base (note: FinSMEs' "Ocelot" hits are an unrelated consultancy — the edtech Ocelot remains independent/small) `[FACT: search result confusion noted](https://www.finsmes.com/?s=ocelot)`.
- **VerifyMyFAID** — small fraud/verification point solution `[FACT: exists; UNVERIFIED scale]`.
- **Context that creates demand:** the 2024 FAFSA Simplification rollout meltdown delayed awards nationwide `[FACT: widely documented event]`, and community colleges battled waves of **"ghost student" enrollment fraud** (bot/fake applicants consuming aid and seats) `[REPORTED 2024–25; UNVERIFIED figures]`. Verification and identity triage remain human-heavy, spreadsheet-and-email processes at most CCs `[INFER]`.

### 1.6 Attendance / MTSS platforms + parent communication

- **ParentSquare** — consolidated category leader; **acquired Remind (Dec 2023)** `[FACT — FinSMEs](https://www.finsmes.com/2023/12/parentsquare-acquires-remind.html)`; PE-backed (Serent Capital, 2021) `[FACT — FinSMEs](https://www.finsmes.com/2021/08/parentsquare-receives-growth-investment-from-serent-capital.html)`; earlier $7M seed `[FACT — FinSMEs](https://www.finsmes.com/2020/12/parentsquare-raises-7m-in-new-funding.html)`.
- **Apptegy** (Thrillshare) — comms + websites; aggressive growth, nine-figure growth rounds `[REPORTED/UNVERIFIED]`.
- **TalkingPoints** — multilingual family engagement; VC-backed (~$40M lifetime est.) `[REPORTED — not found on TechCrunch/FinSMEs indexes; UNVERIFIED]`.
- **ClassDojo** — consumer-scale reach; profitable since ~2021 `[FACT — TC](https://techcrunch.com/2021/01/26/classdojos-second-act-comes-with-first-profits/)`; $35M round 2019 `[FACT — TC](https://techcrunch.com/2019/02/28/classdojo-an-app-to-help-teachers-and-parents-communicate-better-raises-35m/)`.
- **MTSS/attendance:** Panorama Education, Branching Minds, SchoolStatus (attendance-comms hybrid) — dashboards + intervention logging `[FACT: existence]`. Chronic absenteeism remains a top post-pandemic crisis and even measurement is contested (`[FACT — coverage](https://www.the74million.org/article/absenteeism-is-a-major-problem-so-why-cant-schools-agree-on-how-to-measure-it/)`, Aug 2026).

**Weakness:** all of these are broadcast/log tools. Nobody closes the loop: detect attendance risk → coordinate counselor/family/home-visit actions across SIS/comms systems → track outcome → escalate. That's an agentic gap. `[INFER]`

### 1.7 Substitute management / staffing + HR/recruiting

- **Frontline Absence Management (ex-Aesop)** — near-monopoly sub scheduling; rule-engine based; teachers complain about call-timing UX, subs complain about job matching `[INFER from long-standing user gripes]`.
- **Kelly Education, ESS, Swing Education** — managed staffing (people, not software); districts pay staffing premiums of 25–40% over sub pay `[INFER/INDUSTRY-KNOWLEDGE]`.
- **Frontline Recruiting & Hiring (AppliTrack)**, **PowerSchool Recruit & Hire** — applicant tracking for certificated staff; paper-like workflows, reference-check and credential-verification steps largely manual `[INFER]`.

### 1.8 School finance / procurement / AP

- **Tyler Munis** — ERP for local gov incl. schools; batch-oriented, invoice coding manual `[FACT: existence; INFER on workflow]`.
- **eFinancePLUS / BusinessPLUS (Frontline), Skyward Finance, LINQ** — district ERPs; PO/invoice workflows are forms-and-rules, grant-code tracking done in spreadsheets `[INFER]`.
- **ClassWallet** — managed teacher/classroom spend (PE-backed, $37M+ raised) `[REPORTED/UNVERIFIED]`.
- Generic AP-automation (AvidXchange, Paymerang) sells into education but ignores grant-fund coding rules and board-approval logic `[INFER]`.
- Cooperative purchasing (see §4) dominates big-ticket buying.

### 1.9 Certification / credentialing

- **Credly (Pearson)** — badge infrastructure; enterprise pricing, slow innovation `[INFER]`. **Accredible** — digital credentials for training orgs `[FACT: existence]`. **Badgr/Canvas Credentials (Instructure)** `[FACT: existence]`. Exam bodies (Pearson VUE, PSI, Prometric) own delivery stacks `[FACT: existence]`.
- Issuance is commoditized; **verification/registry ops and employer-facing validation workflows** remain fragmented `[INFER]`.

### 1.10 Corporate LMS / workforce training

- **Docebo** (public, TSX/Nasdaq), **Absorb LMS** (Welsh Carson-backed), **Workday Learning** (bundled) — mature, feature-complete `[FACT: existence/status]`.
- Content-generation AI is already swarming this space (Synthesia $180M Series C @ ~$2.1B, Jan 2024 `[REPORTED]`; Sana ~$54M, 2023 `[REPORTED]`). Crowded; differentiation must come from workflow depth (compliance mapping, skills evidence), not generation `[INFER]`.

---

## 2. AI-Native Startup Landscape 2023–2026 (education OPERATIONS focus)

### 2.1 Verified funding events

| Startup | Segment | Round | Date | Lead/investors | Wedge |
|---|---|---|---|---|---|
| **MagicSchool AI** | Teacher-facing AI assistant | $15M Series A (+~$2.4M seed prior) | Jun 27, 2024 | **Bain Capital Ventures**; Adobe Ventures, Common Sense Media; angels (Replit CEO, Clever founders) `[FACT — TC](https://techcrunch.com/2024/06/27/magicschool-thinks-ai-in-the-classroom-is-inevitable-so-its-aiming-to-help-teachers-and-students-use-it-properly/)` | Lesson planning/quizzes for teachers; freemium bottom-up, districts pay later |
| **Brisk Teaching** | Teacher-facing Chrome-extension AI agent | $5M seed (Sep 25, 2024) then **$15M Series A** (Mar 26, 2025) | 2024–25 | Seed+Series A leads incl. Bessemer-class funds `[FACT rounds — FinSMEs](https://www.finsmes.com/2025/03/brisk-teaching-raises-15m-in-series-a-funding.html)` / `[seed](https://www.finsmes.com/2024/09/brisk-teaching-raises-5m-in-seed-funding.html)` | In-browser feedback/IEP-draft assist for teachers |
| **SchoolAI** | Student/teacher AI workspace | **$25M Series A** | Apr 2, 2025 | **Insight Partners** `[FACT — FinSMEs](https://www.finsmes.com/2025/04/schoolai-raises-25m-in-series-a-funding.html)` | K-12 AI spaces + monitoring dashboards |
| **ParentSquare** | Parent comms consolidation | Acquired **Remind** | Dec 5, 2023 | PE (Serent) `[FACT — FinSMEs](https://www.finsmes.com/2023/12/parentsquare-acquires-remind.html)` | Category roll-up, not AI-native |

**Why MagicSchool/Brisk/SchoolAI are a DIFFERENT business:** they monetize **teaching productivity** (bottom-up teacher adoption, freemium, low ACVs, procurement-light). Operations buyers (SPED directors, registrars, financial-aid directors) have budget authority, compliance deadlines, and ROI math — slower sales but stickier dollars. Attacking ops ≠ competing with these funded players. `[INFER]`

### 2.2 Other named landscape players (status notes)

- **AllHere** — see §Cautionary Tales; dead. Its collapse chilled district appetite for flashy "district-wide AI assistants," especially anything sold top-down without procurement hygiene. `[FACT — The74 series below]`
- **Mainstay / EdSights / ReUp / Element451 / CollegeVine** — conversational nudging & enrollment-funnel AI (§1.3/§1.4). All pre-LLM-era architectures retrofitted with LLMs; none do deep back-office execution `[INFER]`.
- **EAB** — incumbent counterattack: Navigate AI (2024), plus consulting muscle `[REPORTED]`. Expect incumbents to bolt chat onto existing data moats rather than rebuild workflows `[INFER]`.
- **OpenAI/Google/Microsoft** — ChatGPT Edu (2025) and Gemini for Education sell institution-wide licenses; they commoditize generic Q&A and raise the floor — pure-chatbot startups are structurally squeezed `[REPORTED launches; INFER strategic effect]`.
- Agentic ops startups specifically in **credentialing/admissions/financial-aid ops**: searched, found only point solutions and services firms — **no scaled category winner surfaced** `[INFER from absence in funding/news sources this session]`.

### 2.3 Funding climate (2024–2026)

- Global EdTech VC collapsed from ~$17–20B peak (2021) to roughly **$2.5–3.5B/yr in 2024–25**; capital concentrated in AI-flavored deals (HolonIQ/Brighteye/Reach-style analyses) `[REPORTED — analyst consensus; direct fetches blocked by bot-walls this session, so treat magnitudes as approximate]`.
- Investor behavior shift: fewer, larger rounds for AI-product companies with real ARR (MagicSchool, SchoolAI, Brisk all raised A rounds 2024–25); non-AI ops software starved `[INFER from round pattern above]`.
- Implication for client: the market pays for **agentic proof-points with measurable labor savings**, not "AI-powered" wrappers. Small vendor should design for pilot→ROI-story→expansion economics. `[INFER]`

---

## 3. Why Pain Persists Despite This Stack

1. **Integration debt.** SIS (PowerSchool/IC), HR (Frontline), finance (Munis/eFinance), comms (ParentSquare) are separate silos with weak APIs; districts stitch them with SFTP jobs and CSV exports. Any multi-system workflow (attendance intervention, SPED services reconciliation, fee collection) requires human glue. `[INFER from product architecture patterns + PowerSchool breach showing centralized-but-fragile data infra]`
2. **Rule-based, not agentic, automation.** Incumbent "automation" = scheduled queries, if-this-then-that campaigns, workflow forms. Nothing plans across systems, handles exceptions, or executes follow-ups autonomously. `[INFER — consistent across reviewed product sets]`
3. **Services-heavy delivery.** Slate's own site lists 20+ paid implementation partners; EAB's model is consultants-as-a-service. Vendors profit from configuration labor, so they have little incentive to make software self-operating. `[FACT — partner lists](https://www.technolutions.com/licensing)` + `[INFER on incentives]`
4. **Change-management failure.** AllHere/LAUSD is the canonical post-mortem: bought top-down, little staff co-design, collapsed before adoption. Aftermath: FBI raids tied to the vendor, superintendent fallout — districts now demand staged pilots and references. `[FACT — The74 series](https://www.the74million.org/article/fbi-raid-of-l-a-supe-carvalhos-home-office-may-be-linked-to-defunct-ai-startup/)`, `[FACT](https://www.the74million.org/article/allhere-set-meeting-with-lausd-leaders-months-before-landing-6-2m-chatbot-deal/)`
5. **Data quality.** Duplicate student records, stale contacts, inconsistent codes across SIS/HR/finance make naive automation dangerous; agents need validation loops. `[INFER]`
6. **Procurement lock-in.** Multi-year contracts, cooperative-contract piggybacks, and RFP specs literally written by incumbents raise switching costs. `[INFER + §4 mechanics]`
7. **Security/trust reset.** PowerSchool breach (ransom paid, districts extorted afterward, lawsuits) made districts paranoid about vendors touching student PII — a barrier AND an opening for privacy-first, least-privilege agent design. `[FACT — The74 articles §1.1]`

---

## 4. How Education Buyers Buy

### 4.1 K-12 districts

- **Federal-grant purchases (Title I, IDEA, ESSER-successor funds):** 2 CFR 200.320 governs method. Micro-purchases **≤ micro-purchase threshold (FAR baseline $10K)** need **no competitive quotes** and can go on a purchase card; grantees may **self-certify thresholds up to $50K**; simplified-acquisition band (up to FAR SAT, $250K) needs only informal quotes; formal sealed bids/RFPs required above SAT. Noncompetitive allowed for single-source/emergency with justification. `[FACT — 2 CFR 200.320](https://www.ecfr.gov/current/title-2/part-200/section-200.320)`
- **Local board rules:** most districts require board approval somewhere between **$15K–$50K** (policy-set, varies wildly); below that, superintendent/CFO/purchasing director authority `[INFER — typical policy range]`.
- **Cooperative contracts bypass RFPs:** **Sourcewell** (MN-based, 50k+ member agencies), **OMNIA Partners** (absorbed U.S. Communities/National IPA), **AEPA**, state BuyBoards for K-12; **E&I Cooperative Services** for higher ed. A vendor gets awarded once via the coop's competition, then any member can piggyback — dramatically shortening sales cycles `[FACT — mechanism; Sourcewell site blocked bots, mechanism is standard public info]`.
- **Sales cycle reality:** 6–18 months for district-level deals; summer-budget timing; reference-checking culture post-AllHere `[INFER + FACT context]`.
- **Typical K-12 ACVs:** $10K–$50K mid-size district; six-figure for large urban `[INFER — industry-standard bands]`.

### 4.2 Higher education

- **Purchase authority:** directors/deans commonly hold p-cards and discretionary budgets usable below institutional bid thresholds; competitive solicitation generally triggered around **$50K–$100K** (institution-specific; some $10K for public flagships) `[INFER — typical policy bands]`.
- **Micro-purchase logic applies to federally funded units too** (same 2 CFR 200.320): a financial-aid office can legitimately buy a ≤$10K pilot on a card. `[FACT — regulation; INFER application]`
- **Enterprise deals** (EAB, Anthology, Ellucian) run $150K–$500K+/yr with 9–18 month committee cycles `[INFER]`.
- **Fast lanes:** individual colleges/schools within universities, continuing-ed divisions, community colleges (leaner admin, acute pain), graduate/admissions offices using departmental operating budgets. Slate's flat $30K tier shows how a fixed-price dept-level SKU unlocks card-level purchasing. `[INFER + FACT pricing anchor]`

### 4.3 Where a tiny vendor realistically lands first deals

1. **Community college financial-aid/registrars** — FAFSA chaos + ghost-student fraud + lean staffing = urgent, budgeted, faster committees `[INFER + REPORTED fraud wave]`.
2. **District SPED directors** — IDEA compliance deadlines create recurring fire-drills; SPED budgets are separate federal streams (IDEA funds flow through the micro-purchase rules above) `[INFER + FACT regulatory anchor]`.
3. **Charter networks / CMOs** — private governance, no elected boards, 1-signature deals at $20–60K `[INFER]`.
4. **Coop piggyback listing** once 2–3 lighthouse customers exist `[FACT mechanism]`.
5. **Avoid** starting with large urban districts (board politics, AllHere trauma) and university-central IT `[INFER]`.

---

## 5. Whitespace Analysis

### PROVEN DEMAND + NO STRONG AGENTIC PLAYER (attack)
| Category | Demand proof | Gap |
|---|---|---|
| **Special-ed compliance ops** (IEP drafting/consistency checks, PWN generation, Medicaid billing/time-study) | Federal mandate; permanent teacher shortage; every incumbent is a form-filler (§1.2) | Zero agentic entrants found `[INFER from landscape scan]` |
| **Financial-aid verification & fraud triage** (CCs especially) | FAFSA 2024 disaster; ghost-student epidemic; VerifyMyFAID tiny, Anthology suite clunky (§1.5) | Document-intake + appeals-processing agent |
| **Admissions/transcript doc intelligence** (OCR eval, international credentials, yield-melt outreach) | Manual readers at 2,000+ Slate schools; WES-style human services backlog (§1.4) | Slate owns CRM, NOT document/workflow intelligence — build ON Slate, not against it |
| **Attendance/intervention closed-loop ops** | Chronic absenteeism crisis; measurement chaos even in 2026 (`The74` link §1.6) | Comms tools broadcast; nobody orchestrates interventions across SIS+comms+home |
| **School-finance back-office** (invoice coding, grant-compliance reporting, board-approval packet assembly) | Every district runs Munis/eFinance + spreadsheets (§1.8) | Generic AP tools ignore education fund-accounting |
| **Sub/HR ops beyond matching** (credential verification, reference-check agents, absence-pattern analytics) | Frontline Absence is a 1990s rule engine (§1.7) | Staffing giants sell people, not software leverage |

### CROWDED — AVOID
- **Teacher-facing lesson/content AI** — MagicSchool ($15M), Brisk ($20M total), SchoolAI ($25M), Diffit, Twee + OpenAI/Google giving it away `[FACT funding above; INFER margin structure]`.
- **Generic district-parent chatbots / "district AI assistant"** — AllHere poisoned trust; ParentSquare+Remind consolidation owns the channel; hyperscalers bundle Q&A `[FACT + INFER]`.
- **Student tutoring/chatbot safety** — Khanmigo, state deals, hyperscalers `[REPORTED]`.
- **Digital credential issuance** — Credly/Accredible/Badgr commoditized (§1.9).
- **Corporate LMS content generation** — Synthesia/Sana-scale capital already deployed (§1.10).

### DISPLACEMENT/ACQUISITION TARGETS (incumbent weakness)
- Legacy **SpEd forms suites** (EasyIEP/Embrace/SEAS): aging UX, state-by-state maintenance treadmill, acquirable tech for a roll-up `[INFER]`.
- **Signal-Vine-style texting** already absorbed by EAB — remaining independents are next `[FACT acquisition precedent; INFER trend]`.
- **Ocelot-style FAQ chatbots** — LLMs commoditized their core; ripe for consolidation `[INFER]`.
- **Anthology's acquired-module sprawl** — customer defection risk during restructuring creates beachhead opportunities in aid/retention workflows `[REPORTED distress + INFER]`.

---

## Cautionary Tales Index

1. **AllHere (LAUSD "Ed" chatbot)** — $6.2M district deal → data-misuse probe (Jul 2024) → Chapter 11 (Sep 12, 2024) → founder charged in $10M investor-fraud scheme (Nov 20, 2024) → arrested (Dec 2024) → FBI raids linked to LAUSD leadership (Feb–Mar 2026):
   - https://www.the74million.org/article/chatbot-los-angeles-whistleblower-allhere-ai/
   - https://www.the74million.org/article/allhere-ai-los-angeles-schools-tool-bankruptcy-filing/
   - https://www.the74million.org/article/feds-charge-once-lauded-allhere-ai-founder-in-10m-scheme-to-defraud-investors/
   - https://www.the74million.org/article/allhere-ceo-arrested-for-fraud/
   - https://www.the74million.org/article/fbi-raid-of-l-a-supe-carvalhos-home-office-may-be-linked-to-defunct-ai-startup/
   - https://www.the74million.org/article/allhere-set-meeting-with-lausd-leaders-months-before-landing-6-2m-chatbot-deal/
   - https://www.the74million.org/article/the-key-investors-who-once-touted-l-a-schools-failed-6m-ai-chatbot-go-silent/
2. **PowerSchool breach aftermath** — ransom paid yet districts extorted anyway; class litigation; lesson: centralizing PII without least-privilege architecture is existential:
   - https://www.the74million.org/article/powerschool-paid-off-hackers-after-huge-breach-now-theyre-extorting-districts/
   - https://www.the74million.org/article/wisconsin-district-sues-ed-tech-giant-powerschool-after-massive-data-breach/
   - https://www.the74million.org/article/powerschool-hacker-thankful-i-got-caught-sentenced-to-4-years-in-prison/
3. **TargetX displacement** — lost Illinois Central College to Slate; cautionary tale for Salesforce-wrapper CRMs: https://www.technolutions.com/slatest-news/a-solidan-success-story-illinois-central-college-icc
4. `[REPORTED/UNVERIFIED this session]` **2U** Ch.11 (2024, OPM model broke), **Chegg** AI disruption, **Pluralsight** creditor takeover, **AltSchool/Altitude Learning** pivot failure, **inBloom** privacy collapse (classic), **HotChalk** ghost-students scandal — all worth a deeper dive before signing edu go-to-market assumptions.

## Sources

**Funding/startups**
- TechCrunch — MagicSchool $15M Series A (BCV), Jun 27 2024: https://techcrunch.com/2024/06/27/magicschool-thinks-ai-in-the-classroom-is-inevitable-so-its-aiming-to-help-teachers-and-students-use-it-properly/
- FinSMEs — Brisk Teaching $15M Series A, Mar 26 2025: https://www.finsmes.com/2025/03/brisk-teaching-raises-15m-in-series-a-funding.html ; $5M seed Sep 25 2024: https://www.finsmes.com/2024/09/brisk-teaching-raises-5m-in-seed-funding.html
- FinSMEs — SchoolAI $25M Series A (Insight Partners), Apr 2 2025: https://www.finsmes.com/2025/04/schoolai-raises-25m-in-series-a-funding.html
- FinSMEs — ParentSquare acquires Remind, Dec 5 2023: https://www.finsmes.com/2023/12/parentsquare-acquires-remind.html ; Serent investment 2021: https://www.finsmes.com/2021/08/parentsquare-receives-growth-investment-from-serent-capital.html ; $7M 2020: https://www.finsmes.com/2020/12/parentsquare-raises-7m-in-new-funding.html
- TechCrunch — ClassDojo $35M, Feb 28 2019: https://techcrunch.com/2019/02/28/classdojo-an-app-to-help-teachers-and-parents-communicate-better-raises-35m/ ; profitability Jan 26 2021: https://techcrunch.com/2021/01/26/classdojos-second-act-comes-with-first-profits/

**Incumbents/pricing/ecosystem**
- Technolutions Slate homepage (2,000+ institutions; Slate AI; partner ecosystem): https://www.technolutions.com/
- Technolutions Slate Licensing & Pricing (tier table $30K–$175K; "most clients pay $50,000"; 20+ yrs no increase): https://www.technolutions.com/licensing
- ICC TargetX→Slate case study: https://www.technolutions.com/slatest-news/a-solidan-success-story-illinois-central-college-icc
- Bain Capital page (PowerSchool redirect target — PE status): https://en.wikipedia.org/wiki/Bain_Capital

**AllHere / LAUSD saga (all The74, dates in section above):** links listed in Cautionary Tales.

**PowerSchool breach:** The74 links in Cautionary Tales.

**Procurement law/mechanics**
- 2 CFR 200.320 Procurement methods (micro-purchase ≤FAR threshold, p-cards, self-cert to $50K, SAT, formal methods, noncompetitive exceptions): https://www.ecfr.gov/current/title-2/part-200/section-200.320
- Sourcewell (cooperative purchasing; site blocks automated access): https://sourcewell-mn.gov/cooperative-purchasing
- E&I Cooperative Services: https://www.eandi.org/ · OMNIA Partners: https://www.omniapartners.com/

**Context/coverage**
- The74 chronic-absenteeism measurement piece (Aug 10, 2026): https://www.the74million.org/article/absenteeism-is-a-major-problem-so-why-cant-schools-agree-on-how-to-measure-it/
- Analyst climate estimates (HolonIQ/Brighteye/Reach) — magnitudes treated as approximate; direct fetches were bot-blocked this session.

*Items marked `[INFER]`/`[UNVERIFIED]`/`[REPORTED]` are explicitly flagged inline and should be re-verified before investor-facing use.*
