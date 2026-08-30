# DD-02: School Medicaid Billing Capture Agent — Deep Dive

**Date:** Aug 25, 2026 · **Status:** RESEARCH COMPLETE · **Thesis under test:** An AI-agent system owning *upstream* documentation capture/QA/chasing for school-based Medicaid billing (note structuring from paper/PDF logs, consent tracking, SIS↔eligibility matching, RMTS response chasing, claim QA, remittance reconciliation, audit-readiness packets), priced on % of newly captured reimbursement. US only.

**Method note:** Primary-source verification via HSPF (Healthy Schools Campaign), the CMS May 2023 comprehensive guide PDF (184pp, downloaded and read directly), the HSC/OIG consolidated audit review PDF (42pp, downloaded), eCFR (42 CFR 455; 45 CFR 75 cited within CMS guide), PCG/MAXIMUS/Funds-For-Learning sites. Search engines (DDG, Mojeek) captcha-blocked this session; several vendor fee structures could not be fetched and are labeled UNKNOWN. Labels: VERIFIED / ESTIMATE / UNKNOWN / REPORTED.

---

## 1. Problem & scope

School districts leave federal Medicaid money unclaimed because the *upstream* half of school-based billing is pen-and-paper labor that nobody owns:

- Policy tailwind is real and recent: CMS's May 2023 guide ("Delivering Services in School-Based Settings") affirms states may let districts bill for services to **all Medicaid-enrolled students, not only IEP students** (free-care reversal applied to schools). VERIFIED: https://www.medicaid.gov/medicaid/financial-management/downloads/sbs-guide-medicaid-services-administrative-claiming.pdf ; summary at https://healthystudentspromisingfutures.org/federal-support/
- **28 states have taken steps to expand** beyond IEP-only billing as of March 2026 (up from 25 in Oct 2023). VERIFIED: https://healthystudentspromisingfutures.org/map-school-medicaid-programs/ ; https://healthystudentspromisingfutures.org/wp-content/uploads/2023/10/Status-of-School-Medicaid-Expansion_-How-and-How-Many-States-Have-Taken-Action-to-Increase-School-Health-Access-and-Funding.pdf
- CMS set a compliance expectation of roughly **July 2026** for states to align SPAs/time-study plans with the guide, funded a Technical Assistance Center, and issued **$50M in state grants** (BSCA). VERIFIED: https://healthystudentspromisingfutures.org/federal-support/
- Expansion demonstrably moves real dollars: Illinois districts drew down **+$17.8M** in year one of expanded billing; New Mexico **+10.18% (> $6.3M)** statewide; Louisiana **+35%** federal revenue since expansion; Colorado estimated ~**+$12M (~30%)**; Georgia projected **+$48.6M** from nurse claiming alone; Michigan projected **+$14M** from master's-level school psychologists alone. VERIFIED: https://healthystudentspromisingfutures.org/wp-content/uploads/2024/09/Financial-Impact-of-Expanding-School-Medicaid-Programs-September-2024.pdf

**Scope of the opportunity:** own everything between "provider delivered a service" and "clean claim leaves the district," i.e., documentation capture + QA + chasing, consent ledger, eligibility roster matching, RMTS participation, pre-submission claim QA, remittance reconciliation, and audit-packet assembly. Explicitly *not* v1 scope: replacing state MMIS submission pipes or incumbent RMTS administrators.

**In-scope pain evidence:** OIG has audited this program relentlessly — a consolidated review of **33 OIG audits (2000–2021) found $1,184,920,464 in recommended refunds**, dominated by documentation failures, not fraud intent. VERIFIED: https://healthystudentspromisingfutures.org/wp-content/uploads/2022/03/OIG-Report-Final.pdf

---

## 2. Workflow today + failure modes

Pipeline: **capture → documentation → consent/eligibility → RMTS → claims → reconciliation → audit**. Performed by therapists/nurses (logs), SPED clerks (data entry), district Medicaid coordinators or contracted billing vendors (claims), business office (reconciliation).

| Stage | What happens today | Documented failure modes (source) |
|---|---|---|
| Capture | Providers hand-write therapy/service logs on paper or free-text in IEP systems after the fact | No service-provision documentation available; notes missing required elements; notes show different service than billed (individual vs group) — OIG findings across AZ, CT, FL, IL, MA, MD, ME, NJ, NY, OR, RI, TX, WI (OIG review, pp.8–9). VERIFIED |
| Documentation | Clerk transcribes units into billing spreadsheet/vendor portal | Texas: **94% of sampled RMTS moments unsupported by documentation**; two TX LEAs had **72% and 97% of weekend claims unsubstantiated** (OIG review pp.9–10). VERIFIED |
| Consent | One-time signed parental consent required before first Medicaid billing of IDEA services (34 CFR 300.154(d)(2)(iv)); tracked on paper/spreadsheet | Consents missing/expired → entire student months unbillable; expansion cohorts (non-IEP students) add notice-tracking burden. VERIFIED rule: CMS guide p.34. ED proposed removing the consent requirement (May 18, 2023 NPRM) — monitor. VERIFIED same page |
| Eligibility | Monthly roster match of SIS students vs state Medicaid enrollment files (file layouts vary by state) | Mismatched names/DOBs silently drop eligible students; provider enrollment lapses void claims (OIG provider-requirements findings, p.12). VERIFIED pattern |
| RMTS | Sampled staff must answer random-moment surveys quarterly; coordinators chase responses and code them | Wrong schedules, missed moments, mis-coding by contractors (13 states); non-response mishandling; standardized work schedules invalidating universes (OIG pp.14–15). VERIFIED |
| Claims | Vendor/spreadsheet converts documented units into claims; submitted via state portal/MMIS or through SEA clearinghouse | Units billed > plan-of-care units; durations exceeding prescriptions; double-billing; services above cost (9 states, OIG p.11). VERIFIED |
| Reconciliation | Remittances reconciled against claims in spreadsheets; interim payments vs annual cost settlement | Interim payments not reconciled; LEAs skip cost reports (minor findings, OIG pp.16–17). VERIFIED |
| Audit | State pulls district records years later; OIG reviews 100% of reimbursable-coded moments and largest LEAs | Records not retained (3 yrs from final expenditure report per 42 CFR 433.32; OIG takeaway: 5 yrs from final cost settlement); attendance records can't corroborate service dates (billed on absences/holidays/weekends — 9 states). VERIFIED |

The meta-failure: **every downstream actor optimizes their slice; nobody owns the upstream loop** — exactly where the OIG says refunds originate. Notably, the OIG's own learning takeaways recommend things like *"Consider possible integrations with LEAs' Student Information Systems (SIS) and Medicaid billing systems"* and *"consider using a RMTS system that automatically codes responses"* (OIG review pp.10, 15) — i.e., the auditor is asking for this product. VERIFIED.

---

## 3. Buyer & economic math

### Buyer logic
- **Economic buyer = CFO/assistant superintendent of business/finance**: this is a revenue line, not a cost line. Post-ESSER cliff (all $190B obligated Sept 30, 2024 — VERIFIED per raw research file) makes found federal money uniquely attractive.
- **Co-buyer = Director of Special Education** (owns provider compliance) and, in expansion states, **school nursing/mental-health leads** (new billable provider classes).
- CFO psychology: silent losses don't create budget lines today, so any credible recovery story is net-new money. But CFOs are also the most audit-literate buyer in the district — they know what OIG findings do to a general fund, which cuts both ways: it sells risk-reduction AND raises scrutiny of anything that smells like contingency billing (see §4).

### Bottom-up recovery math (all arithmetic ESTIMATE unless noted)

**Mid-size district (5,000 students):**
- ~750 IEP students (15% IDEA density — VERIFIED NCES); child Medicaid/CHIP enrollment ~40% nationally (ESTIMATE; no clean fetch this session) → ~300 IEP∩Medicaid students receiving related services.
- ~2 sessions/wk × 30 service weeks ≈ 60 billable units/student-yr → ~18,000 addressable units from IEP services alone.
- Blended realized rates (speech/OT/PT/psych/nursing; wide state variance) plausibly $15–$50/unit → gross potential ≈ **$270K–$900K/yr**; typical current capture 20–50% → **recoverable wedge ≈ $100K–$500K/yr**. Cross-check: statewide verified deltas imply averages of ~$21K/district in IL ($17.8M/~850 districts) and ~$40K+/district in NM ($6.3M/~150 LEAs) — but these are year-one, partially-implemented expansions, heavily skewed small; mature capture in mid-size districts runs far higher (ESTIMATE anchored to VERIFIED aggregates).
- **Expansion states unlock general-ed students** (counseling, psych, nursing): pool grows ~5–6× (from ~750 IEP kids to ~2,000 Medicaid-enrolled kids), so the wedge widens further (ESTIMATE; mechanism VERIFIED via CMS guide).

**Small/rural district (<2,000 students):** absolute wedge $10K–80K/yr (ESTIMATE). Historically uneconomic for anyone to serve — fixed human effort exceeds take. This is where pure software economics change the game.

**Large urban (50,000+):** already recovers $1M–$10M+/yr (ESTIMATE; consistent with OIG methodology noting audits target the 2–3 largest LEAs by reimbursement). Upside = leakage reduction + audit defense, not zero-to-one.

### Why non-participating districts are the biggest prize
1. **Zero baseline** = every dollar is attributable net-new (perfect for performance framing, clean pilot measurement, and political cover).
2. **No incumbent to displace** — co-ops/billing intermediaries haven't bothered because the manual effort doesn't pencil.
3. **Policy clock forces the issue**: July 2026 compliance + BSCA grants mean SEAs are actively trying to onboard non-participating districts right now (VERIFIED policy context).
4. Count: of ~13,500 districts, the long tail is thousands of small districts claiming little or nothing (ESTIMATE; consistent with raw-file observation and OIG focus on large LEAs).

### National TAM (with reasoning)
- Full-maturity national school SBS spend: if expanded-state capture reached even $60–$120 per public-school student per year in participating states (derived from IL/NM/GA verified statewide figures — ESTIMATE method, not a fetched rate card), 49M students implies **$3B–$6B/yr** total federal flow-through at maturity. Current actual capture likely $1.5B–3B (UNKNOWN — CMS-64 breakout not fetchable this session).
- Newly-capturable wedge ≈ **$1.5B–3B/yr**. A vendor capturing fees at an effective 15–20% of *net-new* recovered dollars across even $500M–$1B of newly captured revenue in a decade → **$75M–$200M/yr revenue pool**; broader ops-software attach (consent, RMTS, reconciliation modules across ALL billing districts) pushes serviceable TAM toward **$300M–800M/yr** (ESTIMATE, bottom-up reasoning shown; treat as directional only).

---

## 4. Pricing design

### The contingency problem — verified, not hypothetical
This is the single most important pricing finding of this deep dive:

- **45 CFR §75.459(a)** (quoted in the CMS 2023 guide, p.72): consultant costs are allowable only when "**not contingent upon recovery of the costs from the Federal Government**." The guide continues: *"if payments to contractors by schools are contingent upon payment by Medicaid, those payments may not be considered in determining the LEA's costs to be claimed for FFP."* And: *"Advises schools not to pay school-based health services contractors on a contingency fee basis"* (guide executive summary, p.9). It further warns percentage arrangements *"may increase the risk of upcoding… could violate the anti-kickback statute, section 1128(b)."* VERIFIED: https://www.medicaid.gov/medicaid/financial-management/downloads/sbs-guide-medicaid-services-administrative-claiming.pdf
- The OIG consolidated review goes further: OMB Circular A-87 Attachment B §33 bars contingent consultant costs, **"the OIG is intentionally seeking out states to audit where there is a contingency-based contractor relationship"** (NJ audit rationale quoted verbatim), and *"Be wary of allowing a contractor to work on a contingency basis"* appears as a learning takeaway. VERIFIED: OIG review p.15 fn.1.

So pure "% of newly captured reimbursement" is not merely discouraged — **it attracts federal audits and its cost can't be folded into claimed pools**, undermining both compliance posture and the vendor's own unit economics if the district tries to fund it from claimed admin dollars.

Nuance (design space, ESTIMATE as legal interpretation): the prohibition targets contingent costs flowing *into claimed cost pools*. A success fee paid strictly from **non-federal local funds**, contractually excluded from all MAC/cost-report pools, with fee tied to *net-new* receipts rather than claim volume, is a materially different posture — but it requires careful structuring and state-specific legal sign-off, and some SEA rules will simply prohibit it. Treat every contingency design as needing per-state counsel.

### Adjacent-market benchmarks
- **Medicaid RAC auditors**: statutorily paid on contingency (ACA §6411 regime; codified structure at 42 CFR 455 Subpart F — VERIFIED §§455.506/455.508 require state contracts, medical directors, certified coders; the *contingent-payment mandate* itself REPORTED from ACA §6411, not re-fetched). Contract rates commonly land ~**9–17% of overpayments** (ESTIMATE — widely cited industry range; specific state contracts not fetched this session). Precedent proves gov buyers accept % models — but RACs audit *states*, paid by states, under explicit statutory authority. Different lane than a district's vendor.
- **E-rate consultants**: adjacent federal-revenue-capture market with a $3.9B/yr cap (VERIFIED: https://www.fundsforlearning.com/). Established firms like Funds For Learning sell compliance retainers + SaaS ("E-rate Manager") rather than published contingency; industry lore includes % -of-discount fees around ~10% (UNKNOWN/ESTIMATE — fee schedules not fetchable this session). FCC disclosure rules apply to provider commissions >10% (REPORTED — not re-verified).
- Takeaway: benchmarks give CFOs comfort that % framing exists elsewhere; none of them survive contact with the school-Medicaid-specific rulebook unchanged.

### Recommended model: hybrid
1. **Base subscription** (FERPA school-official platform fee; per-billable-provider or per-student tiers, $15K–60K/yr mid-district — ESTIMATE banding consistent with landscape file ACV norms) covering capture/QA/chasing/reconciliation tooling. Paid like any SaaS from operating funds; uncontroversial.
2. **Performance component** engineered away from the A-87 trap: fixed success bonuses per milestone (first compliant claim batch; eligibility-match coverage ≥95%; audit packet certified) or a capped share of *documented net-new receipts*, paid from local funds, **contractually excluded from every claimed cost pool**, with an independent CPA letter supporting that treatment. If a state balks, collapse to base-only + ROI guarantee (fee credited back if documented new revenue < 3× fee — the guarantee does the contingency's psychological work without its regulatory body).
3. Never price on raw claim volume (upcoding optics — the anti-kickback concern is about incentives, VERIFIED in guide p.72).

### Risk of contingency framing in edu procurement
Beyond federal rules: board attorneys flag contingent-fee arrangements generally; cooperative contract vehicles often disallow them; and a CFO who has read one OIG report will associate contingency with the exact vendors who got NJ/TX audited. The "no budget line needed" advantage (§8) survives via self-funding *framing* of the hybrid, not via literal pure contingency.

### What a CFO needs to say yes
(a) pay-from-proceeds cash-flow story with a defined measurement method; (b) written position on 45 CFR 75.459 compliance; (c) audit-defense indemnity + packet guarantee; (d) human-certification of every claim; (e) referenceable district + cooperative vehicle (Sourcewell/BuyBoard-class) to skip RFP.

---

## 5. Competitive teardown

**Incumbents optimize downstream.** PCG (37+ yrs, education practice, CMS QIO-like entity renewed through 2031, holds a Texas BuyBoard MSA — VERIFIED: https://www.publicconsultinggroup.com/) and MAXIMUS (large government health outsourcer: eligibility/enrollment, clinical services — VERIFIED site sections; specific school-RMTS footprint REPORTED) monetize claim aggregation, RMTS administration, and cost reports — effort-priced services, sometimes with the very %-based arrangements OIG flagged. Regional co-ops/ESAs (NY BOCES-style service bureaus, Michigan ISDs, Ohio MSP-type state programs) bundle billing into sticky regional relationships. None own upstream capture because pre-LLM it required staffing districts couldn't buy, and their services margins depend on the paperwork existing.

**Structural gaps:**
- Consent ledger, SIS↔eligibility fuzzy matching, provider-note QA, RMTS response chasing, remittance reconciliation: sold nowhere as a productized loop (INFER from landscape scan + vendor pages; consistent with raw-file finding).
- Incumbent IEP suites (Frontline SpEd, PowerSchool Special Programs, Embrace) have service-log modules but no cross-document QA, no chasing agents, no multi-state rulebook, no audit-packet assembly (INFER, consistent with competitive-landscape.md §1.2).

**Would PCG/MAXIMUS crush this?** They *could* bundle capture, but incentives cut against it: their revenue is proportional to administrative effort, a true automation layer cannibalizes services, and their product cycles are slow relative to agentic entrants. More dangerous near-term move: **PowerSchool/Frontline shipping AI log-capture inside systems districts already run** — distribution beats depth. Counter-strategy: be neutral plumbing that makes *any* downstream biller look better (sell the upstream layer TO incumbents/co-ops as white-label — see §9), and go deepest where incumbents have no data at all: paper logs and non-participating districts.

**State-level barriers:** several states effectively centralize — SEA-selected clearinghouses/RMTS contractors or mandated state programs narrow district choice (pattern REPORTED/ESTIMATE — e.g., Ohio MSP-style arrangements; per-state confirmation needed before entry). Provider/trading-partner enrollment requirements gate who can touch the pipe at all.

**Relationship moats of incumbents:** multi-year state contracts, board-level references, coop vehicles, and audit-survival track records. A newcomer's fastest counter is the ESA/co-op channel itself: co-ops want upstream capture without building AI teams.

---

## 6. Technical feasibility (1–5 people)

**State Medicaid portal integration reality.** There is no national API. Reality per state (ESTIMATE from program structure; no API catalog fetched): (a) MMIS/X12 batch trading-partner lanes (837P/999/277CA/835) requiring per-entity enrollment, sometimes per-provider NPI rosters; (b) web portals built for humans (RPA/scrape territory — fragile, ToS-sensitive); (c) SEA-run clearinghouses where districts upload files and the SEA submits. **v1 should NOT become a trading partner anywhere** — integrate downstream via the incumbent/co-op/SEA pipe and own the files upstream (eligibility files in, structured claim-ready batches out). This sidesteps the slowest, most permissioned part of the stack.

**OCR on handwritten therapy notes — hard truth-check.** Modern vision+LLM OCR handles structured forms and legible print well, but decades-old cursive, carbon-copy log sheets, and abbreviated clinical shorthand remain genuinely unreliable; expect strong-but-not-audit-grade accuracy on messy archives (field-level 70–90% on poor scans — ESTIMATE; no benchmark fetched). The honest product answer: **don't promise magic retroactive OCR; change forward capture** (mobile/structured digital logging at point-of-service with offline mode) and use OCR as a migration bridge with confidence routing + mandatory human review below threshold. Audit standard is "readily reviewable form" support for each claim element (VERIFIED: SMM §2500.2 six minimum elements — date, recipient name, Medicaid ID, provider agency+person, nature/extent/units, place of service; plus attendance corroboration per OIG patterns).

**Consent tracking.** Simple ledger problem: ingest signed forms (scan/e-sign), key to student IDs, enforce IDEA first-billing consent logic (34 CFR 300.154(d)(2)(iv) — VERIFIED), track expansion-state notice requirements, alert on gaps. Data flows stay inside FERPA boundaries; watch the pending ED rule that would remove the IDEA consent requirement (VERIFIED NPRM existence, CMS guide p.34) — it would *shrink* this module but remove a major leakage cause.

**Eligibility matching.** States deliver monthly enrollment files in wildly different shapes (some direct LEA files, some portal lookup). Deterministic pipeline + fuzzy name/DOB matching + discrepancy queue. Privacy constraint: recipient data handling must meet 42 CFR 431.306 comparable-confidentiality standards (VERIFIED, guide p.35).

**Multi-state rulebook config.** Code sets, unit caps, licensed-provider matrices, supervision rules, RMTS calendars, submission windows — a config-as-content treadmill. Feasible for 1–3 states; do not attempt 50-state coverage with 5 people.

**Hardest three technical risks (ranked):**
1. **Claim-pipe access** — becoming an accepted submitter/trading partner per state is slow, regulated, and politically gated; mitigation = partner/white-label strategy (above).
2. **Capture reliability vs audit standard** — handwritten-note OCR + provider adoption; mitigation = forward-capture redesign + confidence-gated human review.
3. **Fragmented integration surface** — thousands of SIS configs (PowerSchool/IC/Skyward exports), paper processes, and one-off spreadsheets; mitigation = start with co-op cohorts sharing infrastructure.

**v1 single-state strategy:** pick one recently-expanded state with (a) open district-vendor choice, (b) electronic pipelines, (c) fresh money momentum. Illinois fits the evidence (2023 expansion, +$17.8M verified year-one, active provider-type additions) (candidate judgment ESTIMATE from VERIFIED facts). Michigan (projected +$14M psychologists) and NM/LA/CO are second wave. Avoid single-clearinghouse states until the white-label motion exists.

---

## 7. Regulatory & deployment

**HIPAA/FERPA dual compliance.** Clean statutory answer from the CMS guide itself: districts electronically billing health insurance *can* meet HIPAA's covered-entity definition, but the HIPAA Privacy Rule **excludes FERPA-protected education records**, so in K-12 the operative regime is FERPA (+IDEA provisions) — VERIFIED guide pp.34–36. Deployment posture: operate as a FERPA "school official" under direct district control; voluntarily sign BAAs where districts assert covered-entity status; satisfy 42 CFR 431.306 comparable-confidentiality standards for Medicaid beneficiary data; least-privilege tenancy, no training on district PHI, breach terms reflecting post-PowerSchool paranoia (context VERIFIED in competitive-landscape.md §1.1).

**Fraud/false-claims exposure — who is liable when AI drafts a claim?** The district (and individually, providers) certify claims; False Claims Act liability attaches to those who submit or cause submission of false claims (general legal framework — REPORTED, standard knowledge; counsel required). Design imperatives:
- **Human certification steps as product features, not disclaimers**: provider attests each service event (their signature, their license); billing coordinator approves each submission batch; system blocks claims failing plan-of-care/unit-cap/attendance checks rather than auto-submitting.
- Pricing must avoid volume-incentive drift (anti-kickback concern re % arrangements is explicitly about upcoding incentives — VERIFIED guide p.72 citing OIG compliance guidance).
- Immutable, time-stamped audit trail linking every claim field → source artifact (note, consent, eligibility file row, licensure evidence, attendance record) — this *is* the audit packet.

**Audit defense posture.** Build the product backwards from the OIG checklist: the consolidated review's finding taxonomy (documentation sufficiency, attendance corroboration, plan-of-care unit caps, provider qualifications incl. ASHA-cert speech requirements, RMTS schedule/coding integrity, record retention 3–5 yrs) converts directly into QA gates. Selling point to CFOs: "we make you audit-proof" is stronger than "we get you money" because refunds are episodic while audit exposure is permanent. Retention: keep everything ≥5 years from final cost settlement (OIG takeaway; 42 CFR 433.32 floor VERIFIED).

---

## 8. GTM

**Which states first** (criteria: expansion status, open vendor choice, electronic pipeline, verified momentum):
1. **Illinois** — 2023 expansion, verified +$17.8M year-one drawdown, added counselor/MFT/school-psych provider types (VERIFIED HSC brief). Candidate #1 on the evidence.
2. **Michigan** — comprehensive expansion; +$14M projected from psychologists alone (VERIFIED projection; magnitude REPORTED by HSC).
3. **Louisiana / New Mexico / Colorado** — early expanders with documented gains (VERIFIED HSC brief).
Avoid until later: states with SEA-selected centralized vendors/clearinghouses (per-state confirmation REQUIRED before entry — UNKNOWN mapping this session).

**Buyer sequence.** Lead CFO/business manager (owns revenue line; self-funding pitch lands there) with SPED director as champion for provider-side adoption; in expansion states add nursing/mental-health leads (they own newly billable provider types). For non-participating small districts, sell THROUGH ESAs/co-ops (one relationship → many districts; matches how these districts already buy back-office services — INFER, consistent with landscape file coop mechanics).

**Pilot design ($ recovered in 90 days).** Scope: 1–2 provider types (speech + nursing), forward digital capture + eligibility match + consent sweep + one full claim cycle. Success metrics: ≥90% consent coverage in cohort; ≥70% weekly provider log completion; N compliant claims submitted; $ identified vs prior-year baseline. Realistic target for mid-size district: $25K–$100K identified annualized, first receipts inside two quarters (ESTIMATE; claims lag and cost-report timing make instant cash unrealistic — say so upfront to protect trust).

**Procurement reality check.** "Contingency needs no budget line" is **partially true and needs honest handling**: a hybrid base fee still needs funding, but micro-purchase/p-card thresholds cover small pilots (2 CFR 200.320 mechanics VERIFIED in competitive-landscape.md §4.1), board thresholds typically hit around $15K–50K (typical range INFER), and self-funding framing lets the CFO book it against incremental receipts. Pure contingency would indeed dodge budget lines but is federally radioactive (§4). Cycle length: 3–9 months pilot→contract for co-op/CFO-led motions; 6–18 months standalone district deals (consistent with landscape norms).

---

## 9. Service→product ladder

1. **Managed capture bureau (months 0–12):** humans+agents run capture/QA/chasing for 3–5 districts in one state; priced hybrid (§4); goal = verified recovery stories + training data.
2. **Platform (year 2):** consent ledger, eligibility matcher, RMTS chaser, claim QA, audit packets as self-serve modules for districts already using any biller.
3. **White-label upstream layer (year 2–3):** sell the capture/QA/chasing engine TO co-ops, ESAs, and billing intermediaries (PCG-class firms included) — they keep the client, you keep the engine; converts distribution threat into channel.
4. **Full-cycle owner (year 3+):** in states where permitted, hold the submission relationship and reconcile remittances end-to-end; pricing migrates to platform+success hybrid at scale.

---

## 10. Expansion paths

- **Adjacent federal-revenue capture in the same buyer's office:** E-rate compliance/capture ops ($3.9B cap — VERIFIED cap via FFL; consultant precedent exists though fee norms UNKNOWN this session) — same CFO, similar document-chasing DNA; crowded-ish consultant market but weak productization.
- **Grant drawdown QA / CRDC assembly** (raw-file problem #11): same business office, Dec 2026 CRDC forcing function.
- **Attendance/ADA revenue workflows** (#4): ADA-linked states; same "found money" narrative.
- **Other state verticals with identical anatomy:** EMS agency documentation-for-reimbursement (PCG publishes content signaling demand — VERIFIED article exists on pcg site), Head Start/pre-K health claiming, childcare nutrition (CACFP) claims.
- **Geography:** repeat the single-state playbook across the remaining expansion states; the July 2026 compliance deadline keeps generating new entrant-friendly windows as each SEA stands up its program.

---

## 11. Kill risks (top 5) + falsification tests

1. **Contingency model banned/frustrated federally or by state.** Evidence already adverse: 45 CFR 75.459(a), CMS guide advice, OIG targeting contingency contractors (all VERIFIED). *Test:* obtain written SEA guidance + outside-counsel memo in target state on vendor fee structures BEFORE building pricing; if hybrid-with-exclusion fails legal review in 2 of top-3 target states, kill the success-fee component entirely (base-only pivot must still clear unit economics).
2. **Incumbents bundle capture free** (Frontline/PowerSchool ship AI service-log capture inside IEP/SIS suites). *Test:* roadmap signals from 10 district admins + 12-month release-notes watch; if a suite ships competent capture bundled, pivot to white-label upstream for them or exit.
3. **States centralize to single SEA vendors during July 2026 compliance** — district choice evaporates. *Test:* track SPA/TAC announcements quarterly; maintain count of states with open vendor rules; enter only open-access states.
4. **Handwriting OCR never reaches audit-grade** on legacy logs. *Test:* 500-note benchmark from a pilot district within 60 days; if field-level accuracy below agreed error tolerance even with confidence-routing+human review, restrict scope to forward-capture only (smaller but still viable wedge).
5. **Provider adoption failure / union-trust blowback** (AllHere trauma is live context — VERIFIED cautionary tale in landscape file). *Test:* pilot gates — ≥70% weekly provider completion sustained 6 weeks; else the product is a clerk-back-office tool with lower ACV (still viable, smaller).
Bonus headwind (not fatal, but shape it): OBBBA-era Medicaid cuts shrink rolls and state capacity (direction VERIFIED via HSPF Sept 2025 analysis) — actually *increases* district hunger for found money while risking eligibility-file churn; monitor enrollment-file quality.

---

## 12. Verdict: **BUILD-CAREFULLY**

Honest paragraph: This is the rare education-ops market where the buyer's ROI is denominated in federal dollars rather than vague hours-saved, where an auditor (OIG) has spent 20 years documenting precisely the failures your product eliminates ($1.18B in recommended refunds across 33 audits), and where federal policy (free-care reversal, 28 expanding states, ~July 2026 compliance, BSCA grants) is actively herding thousands of previously-dark districts into a workflow they cannot staff. That combination justifies building. But the obvious business-model shortcut — pure contingency — is the single most documented way to attract an OIG audit in this niche, and the incumbents' weakness (downstream optimization) sits next to their strength (they own the submission pipes and the state relationships). The win condition is narrower than the pitch: own the upstream documentation layer as neutral plumbing, price as hybrid with lawyer-engineered success components, prove one state deeply, and make the co-ops and eventually the incumbents distribute you. If the OCR truth-check or the pricing legal review fails, the fallback (forward-capture + QA as a modest SaaS attached to existing billers) is a decent small business, not a venture outcome — size expectations accordingly.

**Re-scored dimensions (1–5, vs raw-file segment ranking):**
| Dimension | Score | Note |
|---|---|---|
| Pain intensity / urgency | 5 | OIG-documented losses + July 2026 compliance wall (VERIFIED) |
| Budget availability & buyer alignment | 4.5 | CFO-owned revenue line; post-ESSER hunger |
| Agent-fit (judgment vs deterministic split) | 4.5 | Capture/chase/match/reconcile is deterministic-heavy; medical-necessity framing stays human |
| Competitive risk | 3 | Downstream incumbents entrenched; suite vendors loom |
| Regulatory/model risk | 2.5 | Contingency pricing federally disfavored; FCA/anti-kickback edges need engineering |
| Technical feasibility (1–5 ppl) | 3 | Forward capture fine; legacy handwriting OCR and pipe access are real constraints |
| GTM speed | 3.5 | Co-op channel + pilots fast; procurement and claims lag temper it |
| Expansion optionality | 4 | E-rate/grants/ADA/other verticals share the anatomy |

---

## Key sources
- CMS, *Delivering Services in School-Based Settings* (May 2023): https://www.medicaid.gov/medicaid/financial-management/downloads/sbs-guide-medicaid-services-administrative-claiming.pdf (contingency/45 CFR 75.459: p.72; privacy/consent: pp.34–36; documentation minimums: pp.89–92)
- HSC/OIG consolidated review (33 audits, $1.18B): https://healthystudentspromisingfutures.org/wp-content/uploads/2022/03/OIG-Report-Final.pdf
- HSPF federal guidance hub (25→28 states; July 2026; TAC/$50M grants): https://healthystudentspromisingfutures.org/federal-support/ ; expansion map (28 states, Mar 2026): https://healthystudentspromisingfutures.org/map-school-medicaid-programs/
- HSC financial impact brief (IL/NM/LA/CO/GA/MI figures): https://healthystudentspromisingfutures.org/wp-content/uploads/2024/09/Financial-Impact-of-Expanding-School-Medicaid-Programs-September-2024.pdf
- HSPF OBBBA impact analysis: https://healthystudentspromisingfutures.org/the-impact-of-federal-medicaid-cuts-on-states-and-school-districts/
- 42 CFR 455.506/455.508 (Medicaid RAC program structure): https://www.ecfr.gov/current/title-42/part-455/section-455.506
- PCG corporate site (education practice; BuyBoard MSA; QIO-like designation): https://www.publicconsultinggroup.com/
- Funds For Learning (E-rate consulting precedent): https://www.fundsforlearning.com/
- Inherited context: k12-us.md problem #3; competitive-landscape.md procurement section (2 CFR 200.320; coop vehicles)
