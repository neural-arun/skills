# DD-01 — SPED Casework Copilot (Deep Dive)

**Date:** Aug 25, 2026 · **Status:** Research complete · **Verdict:** BUILD-CAREFULLY (see §12)

**Labels:** VERIFIED = fetched/read this session or in prior session with URL · ESTIMATE = directional, reasoning given · UNKNOWN = could not establish.

**New findings this session (all VERIFIED unless noted):**
- **Everway** (formerly **n2y + Texthelp**) is a SPED roll-up that now owns **SpedTrack**, **Embrace**, and **Polaris** ("collaborative IEP solution"), with ISO/IEC 27001 certification and a "Responsible AI" program page. https://www.everway.com
- **PowerSchool Special Programs** publicly markets "**AI-assisted document drafting**" today: 1,200+ districts, 9.5M students supported, 417,297 forms completed in 2025, 25 state-specific IEP/504 models + a federal model usable in all 50 states. https://www.powerschool.com/products/student-information/special-programs/
- **Brisk Teaching** (freemium, claims 2M+ teachers / 20,000+ districts) ships an **AI IEP Goal Generator**, **IEP 504 Template Maker**, and MTSS tools. https://www.briskteaching.com/use-cases/special-education-and-english-language-learners
- **MagicSchool** includes an **IEP Generator** among its 80+ teacher tools; Plus plan priced **$8.33/user/mo billed annually** (~$100/teacher/yr); SOC 2 + FERPA/COPPA posture. https://www.magicschool.ai/pricing
- **UK:** Liquidlogic (now **System C**) sells **Education Case Management** (EHCP case management for LAs) and already embeds a **Liquidlogic AI** drafting module in social-care case management. https://www.systemc.com/local-government/education-case-management/
- Neither SpedTrack nor Embrace publishes pricing (VERIFIED absence on both sites); legacy per-student figures remain UNVERIFIED.

---

## 1. Problem & scope

**The pain (anchored in raw research):**
- SPED teachers average **5 hrs/week on paperwork**; **88% say it interferes with teaching** (federally sponsored SPeNSE study — VERIFIED: https://eric.ed.gov/?id=ED479674). Practitioner accounts put total IEP-authorship time at **3–5 hrs per annual IEP** including data-gathering (ESTIMATE, consistent with 20–28-student caseloads).
- **7.5M IDEA students** (15% of enrollment) — VERIFIED: https://nces.ed.gov/programs/coe/indicator/cgg/students-with-disabilities. SPED is the **hardest-to-fill teaching assignment** (74% of schools struggle; VERIFIED: https://nces.ed.gov/whatsnew/press_releases/10_17_2024.asp) — paperwork burden is a retention tax on the scarcest staff.
- Installed "IEP software" (PowerSchool Special Programs, Frontline, Embrace, SpedTrack, PCG EasyIEP/SEAS, state systems) = **structured form-fillers + compliance-date dashboards**. They do not read evaluation PDFs, draft defensible narratives, reconcile goals↔assessment↔services, generate PWNs, or chase teachers/parents for inputs (VERIFIED product scope from vendor sites this session; judgment from raw research §1.2).
- Consequences: procedural-noncompliance findings, compensatory education, due-process filings, parent distrust, attrition (k12-us.md problem #1/#2).

**What v1 DOES (scope):**
1. **Drafting grounded in artifacts**: present levels of performance, measurable annual goals, accommodations grid text, and **Prior Written Notice (PWN)** drafts generated strictly from ingested evaluation reports (PDF), prior IEPs, grades/SIS extracts, and logged progress data — every sentence traceable to a source span.
2. **Compliance-timeline orchestration**: initial-evaluation clock, annual-review anniversaries, triennial re-evals; escalation queues for at-risk cases.
3. **Input-chasing**: automated multi-touch requests (email/SMS) to gen-ed teachers and parents for IEP input forms and meeting availability, with response tracking.
4. **Progress-report generation** each grading period from logged goal data.
5. **Own document store** as system-of-record-lite during v1 (import/export with incumbent IEP systems; no write-back dependency).

**What v1 does NOT do:**
- No eligibility/placement recommendations (legal decision reserved to the IEP team — IDEA requires decisions by a group of qualified professionals with parent participation).
- No auto-submission of anything: every artifact passes a **human approval gate** before export/print/signature.
- No write-back into PowerSchool/Frontline/state systems (export formats only in v1).
- No due-process module in v1 (expansion path, §10).
- Not child-facing (COPPA surface minimized).

---

## 2. Workflow today (trigger → steps → failure modes)

Source: k12-us.md problems #1/#2 (cited there against NCES/ERIC/eCFR).

| Stage | Today | Failure mode |
|---|---|---|
| Trigger | Referral or calendar anniversary | Triggers live in someone's head/spreadsheet; initial-eval clocks (state deadlines, often 60 school days) missed → state monitoring findings |
| Eval planning | Permission-to-evaluate forms; consent chase | Consent chasing manual; evaluations start late |
| Assessment intake | Psych/SLP/OT reports arrive as **PDFs/scans/faxes** | Scores retyped by hand into IEP fields; transcription errors propagate into legal documents |
| Drafting | Case manager writes present levels/goals/accommodations from memory + binders | 3–5 hrs/IEP (ESTIMATE); inconsistent quality across writers; goals copied forward year-over-year |
| Input gathering | Emails/paper forms to 5–7 teachers + parents | Weeks of nudging; meetings rescheduled repeatedly; parents disengaged |
| Meeting & final doc | Meeting held; final IEP generated; minutes entered | Document quality depends on whoever typed it; PWN often written late/thin |
| Progress reporting | Each grading period, per-goal narrative updates | Bulk-produced at deadline from sparse logs; weak evidence trail |
| Annual/triennial | Repeat | Anniversary drift; triennial re-evals missed |

**Due-process tail (problem #2):** dispute → counsel reconstructs evidence ad hoc from IEP system, email, paper logs → resolution session (15-day window), mediation, hearing; outside counsel $250–$600/hr; contested cases routinely cost tens of thousands (ESTIMATE; CADRE national stats remained inaccessible this session — cadreworks.org returned 403, consistent with prior research).

---

## 3. Buyer & economic math (bottom-up)

**Unit economics for a mid-size district (5,000 students):**

| Unit | Value | Label |
|---|---|---|
| IEP students | ~750 (15% × 5,000) | ESTIMATE on 15% base (VERIFIED national share, NCES) |
| Caseworkers (SPED teachers + SLP/OT/psych) | ~38–45 | ESTIMATE (matches k12-us.md model) |
| Paperwork hrs/wk per caseworker | 5 (floor) – 8–10 incl. IEP authorship | 5 = VERIFIED (SPeNSE); 8–10 = ESTIMATE |
| Annual caseworker paperwork hours | 7,900 (floor) – ~13,000 | arithmetic |
| Copilot-addressable share (drafting + chasing + progress reports + scheduling) | ~45% | ESTIMATE |
| Realized savings (assume tool captures half of addressable) | 1,800–2,900 hrs/yr | ESTIMATE |
| Blended loaded rate ($62–72K salary + ~30% benefits ÷ 1,750 hrs) | **~$48–58/hr** | ESTIMATE (BLS blocked this session; medians widely reported) |
| **Labor value released** | **$95K–$170K/yr** | ESTIMATE anchored to VERIFIED 5 hrs/wk |
| Compliance-chasing coordinator time | ~0.5 FTE ≈ $30K | ESTIMATE |
| Retention value (1 avoided long-term SPED vacancy: subs/agencies/class-splitting) | $40K–$70K/yr | ESTIMATE |
| **Total addressable value per mid-size district** | **≈ $125K–$270K/yr** | ESTIMATE |

This brackets k12-us.md's independent estimate ($180K–$280K loaded labor equivalent) — good convergence.

**Who signs:**
- **Champion:** Director of Special Education (owns IDEA compliance + staffing pain).
- **Signatory:** superintendent/business office; board approval typically triggered between $15K–$50K depending on local policy (competitive-landscape.md §4.1, INFER-typical range).
- **Fast lane:** purchases charged to **IDEA Part B flow-through** under **2 CFR 200.320**: micro-purchases **≤$10K need no competitive quotes** (p-card eligible); grantees may self-certify up to $50K; simplified acquisition to $250K needs only informal quotes (VERIFIED regulation: https://www.ecfr.gov/current/title-2/part-200/section-200.320). A $7.5K pilot is a legitimate single-card buy.

**Budget sources:** IDEA Part B grants-to-states (federal formula aid, roughly $14–15B/yr nationally ⇒ order of $1,900/IDEA student — ESTIMATE), state SPED categorical aid, general-fund excess-cost lines. Note: federal IDEA covers only a fraction of excess cost; most SPED staffing is state/local money — meaning the buyer's budget is real but politically defended.

**TAM:**
- **US theoretical ceiling:** ~13,500 LEAs (VERIFIED count basis, k12-us.md) × $18–22K avg ACV at full deployment ≈ **$240–300M/yr** (ESTIMATE).
- **Serviceable now:** ~6,000 districts with ≥2,500 enrollment (ESTIMATE) × $20–25K ≈ **$120–150M SAM**; realistic 5-year penetration 15–20% ⇒ **$20–30M ARR** category winner outcome (ESTIMATE). Add 504/MTSS attach to expand.
- **UK:** 718,800 active EHC plans, +12.5% YoY; only 46.1% issued within statutory 20 weeks; 56.8% of annual reviews completed (ALL VERIFIED: https://explore-education-statistics.service.gov.uk/find-statistics/education-health-and-care-plans). Buyer = 153 local authorities with structurally deficit High Needs Budgets (international.md). Direct LA software TAM modest: ~£5–10M/yr (ESTIMATE); strategic value larger because Safety-Valve-style interventions fund process reform (ESTIMATE).

---

## 4. Willingness-to-pay & pricing

**Benchmarks:**
- Legacy forms suites: commonly cited **$10–$30 per SPED student/yr** (Embrace class) — carried from competitive-landscape.md §1.2, remains UNVERIFIED (no public pricing found again this session; SpedTrack/Embrace sites publish none — VERIFIED absence).
- District-level K-12 ACVs typically **$10K–$50K** mid-size, six-figure large urban (competitive-landscape.md §4.1, INFER).
- Teacher-AI anchors: **MagicSchool Plus $8.33/user/mo** (~$100/teacher/yr, VERIFIED: https://www.magicschool.ai/pricing); Brisk freemium with paid tiers. These set a low psychological anchor for "AI writing help" — our price must be justified by **workflow ownership + compliance outcomes**, not drafting alone.
- Slate's flat-tier discipline ($30K floor, no increase in 20 yrs — VERIFIED: https://www.technolutions.com/licensing) shows edu buyers accept clean fixed SKUs.

**Recommended model — hybrid:**
- **Per-SPED-student/month** platform fee: **$2.00–$3.00/SPED-student/mo** ($24–36/yr) — deliberately 2–3× legacy forms pricing because the value claim is labor release, not form storage. Includes unlimited caseworker seats.
- **Implementation/onboarding:** $5K–$15K one-time (artifact ingestion, goal-bank/narrative conventions, training) — becomes productized (§9).
- **Due-process evidence room** later as add-on module (+$5K–$15K/yr) or per-active-case pricing.

**Target ACV bands:**

| District size | Enrollment | SPED students | Target ACV |
|---|---|---|---|
| Small / rural co-op | <2,500 | <400 | $6K–$12K (often via co-op/shared-service) |
| Mid-size (beachhead) | 2,500–10,000 | 400–1,500 | **$15K–$35K** |
| Large suburban / charter network | 10,000–25,000 | 1,500–4,000 | $50K–$90K |
| Urban | >25,000 | 4,000+ | $100K–$200K+ (avoid initially) |

WTP sanity check: at $27K ACV against $125K+ identified value and a $250–400K SPED payroll, price ≈ 15–20% of quantified value — within normal edtech ROI tolerance (INFER). Kill-test for pricing in §11.

---

## 5. Competitive teardown

**Named players (status as of Aug 2026):**

| Player | What they have | Agentic gap / threat level |
|---|---|---|
| **PowerSchool Special Programs** | 1,200+ districts; 9.5M students; 25 state models + federal model; **already markets "AI-assisted document drafting"**; PowerBuddy contextual AI across suite (VERIFIED: https://www.powerschool.com/products/student-information/special-programs/) | **Highest threat.** The "incumbents won't add AI" assumption is dead. Their AI is assistant-grade inside their forms world; they don't own cross-document synthesis + chasing loops yet. Bundling power is the danger: "free with what you already pay for." |
| **Everway (ex-n2y + Texthelp)** — owns **SpedTrack, Embrace, Polaris** | Roll-up of mid-market SPED forms vendors + assistive tech; ISO 27001; Responsible-AI program (VERIFIED: https://www.everway.com) | PE-backed consolidation = capital + distribution; expect AI features bolted into SpedTrack/Embrace within 12–18 months. Also makes customers restless (acquisition fatigue) — a switching window for us. |
| **Frontline SpEd** (Excent/eSped lineage) | Market leader in NY/TX-class states; forms + compliance calendars + Medicaid modules (competitive-landscape.md §1.2) | Legacy UX complaints; slow feature velocity typical of PE roll-ups (INFER). |
| **PCG EasyIEP / SEAS, state-built systems** (MD Online IEP, SEIS-CA) | Statewide contracts; deeply form-centric | Locked at state level; slowest movers; also hardest to integrate around. |
| **Brisk Teaching** ($20M raised; 2M+ teachers claim) | AI IEP Goal Generator, IEP/504 templates, MTSS menus — browser-native, freemium (VERIFIED: https://www.briskteaching.com/use-cases/special-education-and-english-language-learners) | Occupies the "free drafting" mindshare. NOT a system of record, no compliance orchestration, no artifact-grounded drafting, no audit trail. Competes for the teacher's heart, not the director's budget. |
| **MagicSchool** ($15M A; BCV) | IEP Generator tool inside 80+ tools; $8.33/user/mo (VERIFIED) | Same as Brisk. Their enterprise tier sells district oversight, not casework execution. |
| **RethinkEd / n2y Unique Learning System** | SPED curriculum + behavior, some goal libraries | Curriculum-side; not paperwork workflows. |
| **System C / Liquidlogic (UK)** | Education Case Management for LAs (EHCPs); Liquidlogic AI already drafting-assists social workers (VERIFIED: https://www.systemc.com/local-government/education-case-management/) | UK analogue of incumbent-response risk; partner-or-avoid, don't replace head-on at entry. |

**Why forms-vendors historically didn't build agentic drafting:** (a) pre-LLM, drafting-from-documents was technically impossible — they rationally optimized forms/compliance dates; (b) their revenue is config/services-heavy (state-form maintenance treadmill eats roadmap — every state changes forms); (c) risk culture: legal-document errors create liability their buyers punish hard. This logic delayed them ~2 years; it will not stop them permanently — hence BUILD-CAREFULLY, not a land-grab.

**Incumbent-response scenario (explicit):** PowerSchool ships present-levels + PWN drafting GA inside Special Programs at no incremental license cost; Everway follows in SpedTrack/Embrace. Counter-position: we are **cross-system and cross-vendor** (works when the district uses Frontline, Embrace, or a state portal — PowerSchool AI only helps PowerSchool districts), we own the **chasing/timeline/evidence loop** (not just text-in-forms), and we produce an **audit-ready provenance log** per draft.

**Union/teacher-trust dynamics:** SPED teachers fear two things: surveillance ("AI grading my paperwork") and blame ("AI wrote my legal document"). Positioning must be **copilot-not-replacement**: drafts are always human-edited and human-approved; provenance shown; workload framed as "get your evenings back," never "reduce SPED headcount"; recruit a SPED-teacher advisory council pre-launch. Post-AllHere (LAUSD chatbot collapse; VERIFIED The74 series in competitive-landscape.md Cautionary Tales) and post-PowerSchool-breach, districts require staged pilots, references, and security review — design GTM around it instead of fighting it.

---

## 6. Technical feasibility (1–5 people)

**Integrations (v1 → later):**
1. **v1: own document store.** Import eval-report PDFs, prior IEPs (PDF/export), gradebook CSVs. Avoid state-IEP-system integration entirely until revenue justifies it. Export print-ready documents matching state templates (start with 1–2 states).
2. **SIS roster sync:** OneRoster/Clever/ClassLink for rosters + basic demographic/grade reads (standard, cheap).
3. **Email/SMS for input-chasing:** SendGrid/Twilio; parent-portal-independent (most districts lack usable parent portals for this).
4. **Later (v2+):** read/export APIs for Embrace/SpedTrack/Frontline (mostly file-export based; true API access is rare — plan for SFTP/CSV glue), state IEP portals (per-state projects), Medicaid billing handoff.

**Architecture sketch (agent-owned workflow):**
- Ingestion layer: OCR + layout-aware parsing (eval reports are tables of scores: WISC indices, CBMs, speech norms) → structured "student evidence graph."
- Grounded-drafting engine: templates-per-state + retrieval over the evidence graph; **every generated sentence carries source citation spans**; numeric fields (scores, minutes, dates) filled by deterministic extractors, not free generation.
- Workflow/orchestration: timeline state machine (referral→eval→meeting→final→progress cycles) with escalation policies; chasing agents (draft email/SMS → human click-to-send initially).
- Human-approval UI: redline diff view (AI draft vs current doc), approve/edit/reject per section; immutable audit log (who saw what, which sources, which model version) — this log doubles as the due-process asset.
- Security: tenant-isolated storage, least-privilege roles mirroring FERPA "school official" access, no training on student data, US-region hosting, zero-retention LLM endpoints (or self-hosted open-weights model by v2 for sensitive districts).

**Realistic v1 timeline (3 engineers + founder-as-GTM):**
- Wks 1–3: ingestion pipeline + evidence-graph schema; parse 200 real de-identified eval PDFs from design partners.
- Wks 4–7: grounded drafting for present levels + goals + PWN in ONE state format; redline approval UI.
- Wks 8–10: compliance calendar + chasing agent (click-to-send); progress-report generator.
- Wks 11–14: pilot hardening, audit log, DPA/security packet, 2 design partners live.
- **~14–16 weeks to paying pilot.** State #2 template pack: +3–5 weeks each thereafter.

**Hardest 3 technical risks:**
1. **Hallucination/fabrication in legally operative documents.** A wrong score, a goal copied from the wrong child, invented baseline data — catastrophic trust event. Mitigation: extraction-only numerics, mandatory citation spans, confidence gating, diff-based human sign-off, full provenance log. Residual risk never zero — this defines the category's insurance/liability architecture (see §7).
2. **State-form variation + local conventions.** 25 distinct state IEP models exist even at PowerSchool scale (VERIFIED count); districts additionally keep private goal banks/phrasing norms. Mitigation: template-config architecture, launch 1–2 states deep rather than 25 shallow.
3. **Eval-PDF quality.** Scanned faxes, multi-column psych reports, handwritten OT notes. Parsing accuracy gates everything downstream. Mitigation: human-in-loop verification screen for low-confidence extractions (also builds trust).

---

## 7. Deployment & regulatory

- **FERPA:** operate as a **"school official" with legitimate educational interest** under district control (34 CFR 99.31(a)(1)); DPAs reflecting direct-control requirements; no secondary use; parent inspection rights mean drafts/logs may become accessible records — design the audit log accordingly (VERIFIED framework: https://studentprivacy.ed.gov ; 34 CFR 99.10 45-day rule VERIFIED: https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-B/section-99.10).
- **IDEA confidentiality:** 34 CFR 300.610–.626 governs SPED records (more protective than general FERPA practice); AI is a tool — eligibility/placement determinations must remain group decisions with parental participation; PWN content elements are statutorily specified (34 CFR 300.503) — templates enforce completeness (VERIFIED regulation structure).
- **COPPA:** minimal exposure if strictly staff-facing; keep it that way (no student logins in v1).
- **State student-privacy laws:** NY Ed Law 2-D, CA SOPIPA/AB-1584-class contracting requirements, state privacy-agreement registries (SDPC) — budget admin time per state (ESTIMATE effort: 2–5 days each).
- **DPIA-style controls (borrowed from EU practice, increasingly demanded by US districts):** documented data-flow map, purpose limitation, model-version pinning, bias spot-checks on goal ambition across demographic groups (defensive vs OCR scrutiny), incident-response runbook, kill-switch per tenant.
- **Human-approval gates:** nothing leaves the system without named-human approval; approval events are signed entries in the audit log. This is simultaneously the compliance control and the political shield (§5).
- **Data residency:** US-only regions at launch; offer dedicated-tenant isolation for anxious districts; UK variant requires UK/EU hosting option + ICO-compliant DPIA (international.md).
- **Security certifications buyers will demand post-PowerSchool-breach** (breach → ransom paid → districts extorted anyway; VERIFIED The74 series): expect SOC 2 Type II within the first enterprise conversations; ISO 27001 nice-to-have (Everway leads with it — VERIFIED badge). Plan: SOC 2 Type I by month 6, Type II observation window through month 15; publish pen-test summary + trust page early. Brisk/MagicSchool both lead sales with Common Sense Privacy ratings + SOC 2 (VERIFIED on both sites) — table stakes now.

---

## 8. GTM

- **First-customer profile:** suburban/exurban district, **3,000–8,000 enrollment**, 500–1,200 IEP students, SPED department of 30–60 caseworkers, currently on Embrace/SpedTrack/Frontline (i.e., NOT PowerSchool-locked, so no bundled-AI conflict), state with moderate form complexity (e.g., KS/MO/OH/IN-class — where SpedTrack-class vendors are entrenched and Everway consolidation is creating switching anxiety), and a **Director of Special Education who personally feels timeline pain** (state monitoring letters are the best trigger). Charter networks (CMOs) are the fastest-signing alternative (single-signature $20–60K deals — competitive-landscape.md §4.3).
- **Channel:** CASE (Council of Administrators of Special Education) state divisions + national; CEC convention; state SPED directors' associations; regional ed-coop/shared-service organizations (co-ops can multiply one sale into many). SPED-director peer reference networks are unusually tight — one lighthouse converts a region.
- **Pilot design (90 days, priced $7.5K–$10K as a micro-purchase card buy against IDEA flow-through — VERIFIED mechanism, 2 CFR 200.320):**
  - Baseline (pre): measured hours per IEP cycle stage (time survey), % initial evals within state deadline (trailing 12 mo), % annual reviews on time, PWN turnaround days, teacher input-response latency.
  - Instrument (during): system telemetry (drafts accepted vs edited vs rejected, edit distance, approvals, chasing response rates).
  - Success bar to convert: ≥30% reduction in authoring/chasing hours per IEP; ≥10pt improvement in on-time annuals; ≥70% weekly active usage among caseworkers; zero procedural-integrity incidents (no unapproved external output).
- **Procurement path:** p-card pilot → paid pilot → 12-month subscription (board approval at $15–35K threshold) → **cooperative listing** (Sourcewell / OMNIA / AEPA / state BuyBoard) once 2–3 references exist (mechanism VERIFIED: competitive-landscape.md §4.1).
- **Cycle length:** pilot start 4–10 weeks from first meeting (card buy avoids committee); conversion + board approval + coop listing: 3–6 months. Expect **6–12 months first-deal-to-scaled-contract**; summer-budget timing matters.
- **ACV expectations year 1–3:** $15K–$35K mid-size core; blended ~$22K with implementation fees; land-and-expand via 504/MTSS/Medicaid modules (§10).

---

## 9. Service → product ladder

1. **Stage 1 — Implementation service (months 0–9):** "SPED paperwork modernization" engagements: ingest district artifacts, configure state templates + goal banks, train staff, run the pilot. $7.5K–$15K per district. Deliberately manual — this is discovery disguised as delivery and funds the build.
2. **Stage 2 — Productized onboarding (months 9–18):** templated state packs (template + rulebook + goal-bank adapters), self-serve ingestion wizard, standardized training videos; implementation fee shrinks to fixed $5K; gross margin climbs.
3. **Stage 3 — SaaS (month 18+):** per-SPED-student subscription, coop-listed, self-serve for small districts; services <20% of revenue; expansion modules (due-process room, Medicaid attach, MTSS) sold on top.

---

## 10. Expansion paths

- **Due-process evidence-room module (highest synergy):** timeline reconstruction, correspondence indexing, service-log gap detection, hearing-bundle assembly — sells to superintendent/legal line, risk-framed. Value $10K–$50K/yr risk-adjusted per district (k12-us.md #2). Same audit log built in §6 becomes the product.
- **Medicaid attach:** upstream documentation capture (provider notes → structured billable units, consent tracking, RMTS chasing) rides the CMS free-care expansion wave (~July 2026 SPA compliance; VERIFIED context: https://healthystudentspromisingfutures.org/federal-support/). Contingency pricing ("% of newly captured reimbursements") possible; CFO buyer unlocked.
- **MTSS attach:** intervention documentation + referral-packet assembly feeds directly into SPED eligibility files (same buyer, adjacent budget — Title I). Branching Minds/Panorama own dashboards, not assembly loops (k12-us.md #5).
- **UK EHCP variant — what actually changes:** buyer shifts district→**local authority** (153 of them) with statutory 20-week clocks, annual-review completion failure (56.8%, VERIFIED), and tribunal-bundle demand (SEND tribunal volumes VERIFIED in international.md). Technically: new schema (EHC needs assessments, multi-agency evidence packs, Section F provision specificity), UK GDPR + DPIA, UK hosting, G-Cloud/framework listing. Commercially: slower formal tenders, but Safety-Valve deficit districts have funded mandates to fix throughput; partner with System C-class incumbents (their Liquidlogic AI is social-care-first — VERIFIED) rather than rip-and-replace case management. Sequence: enter only after 15–25 US districts prove unit economics.

---

## 11. Kill risks (ranked, with falsification tests)

1. **Incumbent AI bundling (severity: HIGH).** PowerSchool already ships AI-assisted drafting; Everway has capital + three SPED platforms. If "good-enough" AI arrives bundled free inside whatever the district already pays for, standalone ACV compresses toward $0.
   *Falsification test:* within 12 months, either (a) PowerSchool/Everway ship present-levels + PWN + chasing-loop GA at no incremental price AND ≥2 of our 5 target-district opportunities cite it as a reason to stall, or (b) our win-rate analysis shows bundled-AI objections in >40% of lost deals → kill or pivot to cross-vendor/evidence-layer positioning.
2. **Trust catastrophe in a legal document (severity: HIGH).** One publicized case — AI-fabricated score or goal contributing to an adverse due-process ruling or state finding — freezes the whole category (AllHere dynamics, but worse because children + litigation).
   *Falsification test:* any confirmed incident in a customer district traced to our output passing approval gates unnoticed; or >2 industry-wide incidents (any vendor) triggering state guidance restricting AI-drafted IEP content → pause GTM, retrofit controls.
3. **WTP/budget compression (severity: MEDIUM-HIGH).** Post-ESSER austerity + free teacher-tool anchors (MagicSchool/Brisk IEP generators at $0–100/teacher) may cap what SPED directors will pay for drafting; they may see it as classroom-side, not operations.
   *Falsification test:* pilot→paid conversion <30%; or <50% of pilot directors accept >$15/SPED-student/yr; or ACVs settle <$10K mid-size → unit economics fail at 5-person scale → kill.
4. **Integration wall → double-entry death (severity: MEDIUM-HIGH).** If drafts must be re-keyed into the incumbent IEP system of record, weekly usage collapses and the labor-saving story dies.
   *Falsification test:* in pilots, caseworker weekly-active <50% by week 6 attributable to export/re-entry friction; or >25% of user time spent on import/export workarounds → invest in deeper integrations only if 2+ incumbents grant API/file pipelines; else kill.
5. **State-fragmentation treadmill (severity: MEDIUM).** Every new state = template pack + rulebook maintenance; incumbents amortize this across huge installed bases.
   *Falsification test:* marginal engineering cost to add state #3–5 exceeds ~3 engineer-weeks each on a sustained basis; or states change forms annually breaking automations faster than we rebuild → confine to 2–3 states forever (subscale outcome) → kill or narrow wedge to state-agnostic modules (chasing, evidence room).

---

## 12. Verdict: **BUILD-CAREFULLY**

The pain is the best-verified in the entire opportunity database: federally measured 5 hrs/week of paperwork per SPED teacher (88% interference), the nation's hardest-to-staff role absorbing that burden, statutory deadlines that fail measurably (and catastrophically in the UK analogue), and an installed base of form-fillers that provably doesn't synthesize documents or chase inputs. Budget authority is real, ring-fenced (IDEA flow-through + state SPED aid), and reachable through a genuine micro-purchase fast lane. That said, this is no longer virgin whitespace: PowerSchool Special Programs already advertises AI-assisted drafting to 1,200+ districts, Everway has consolidated SpedTrack/Embrace/Polaris with capital behind a responsible-AI program, and Brisk/MagicSchool have normalized "free AI IEP drafts" for teachers — so the survivable position is NOT "AI writes IEPs" but "we own the casework operating loop": artifact-grounded drafting with provenance, timeline orchestration, input-chasing, and an audit trail that survives due-process scrutiny, working across whichever IEP system the district keeps. Build with human-approval gates as a product principle rather than a disclaimer, launch in 1–2 states deep, sell the pilot as a $7.5–10K card-buy to prove hour-savings empirically, and treat the incumbent-bundling clock (risk #1) as the primary timer on the whole thesis.

**Re-scored key dimensions (vs. earlier opportunity-db scores where applicable):**
- **Pain: 9/10** (verified hours + staffing shortage + legal consequences)
- **Willingness-to-pay: 6/10** (real budget line, but free-tool anchors + post-ESSER austerity cap it; conversion data needed early)
- **Whitespace: 6/10** (downgraded: incumbent AI drafting is live; agentic workflow ownership still open)
- **Accessibility: 7/10** (SPED-director buyer + micro-purchase lane + coop channel; board threshold manageable)
- **Risk: 7/10 (high)** (liability-in-legal-documents, incumbent speed, double-entry trap)
