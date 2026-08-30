# DD-04 — Stop-Out Re-Enrollment Engine (O22)

**Deep dive:** Aug 25, 2026 · Feeds red-team wave (`03-red-team/`). Evidence labels: **VERIFIED** (fetched this session, URL inline), **ESTIMATE** (reasoned from verified anchors), **UNKNOWN**, and **VENDOR-CLAIM** (vendor marketing number — treat as upper bound).

**Opportunity under test:** AI-agent system that mines an institution's historical stop-out database, identifies recoverable students (momentum credits, funding eligibility), runs personalized multi-channel outreach, parses prior transcripts to compute a degree gap ("you're X courses away"), clears bursar-hold triage/payment plans, and drives readmit paperwork to completion. Revenue-share or per-enrolled-student pricing.

---

## 1. Problem & scope

The macro pool is the best-verified fact in this entire research program: **43.1M Americans have some college but no credential**; **37.6M are working-age (<65)** and grew 2.2% YoY; **2.1M newly stopped out Jan 2022–Jul 2023** vs only ~1M re-enrollments/yr; first-year-back credential rate just **4.7%**. Community colleges are simultaneously the main source of stop-out and the main destination for returners; primarily-online institutions capture a disproportionate share of re-enrollees ([NSC SCNC 2025](https://nscresearchcenter.org/some-college-no-credential/), **VERIFIED**).

Two NSC findings define the product wedge (**VERIFIED**):

1. **"Potential Completers"** (≥2 years full-time-equivalent enrollment before stopping out) are markedly more likely to re-enroll, persevere into year two, and complete — i.e., the addressable cohort can be *scored* from transcript data.
2. **~1 in 4 SCNC credential earners completes WITHOUT re-enrolling**, likely via administrative-barrier removal or credit-based award. Paperwork removal alone manufactures degrees. This is the single strongest evidence that an agentic paperwork-clearing engine has value independent of persuasion.

Demand-side pressure is structural: WICHE's 11th edition projects US high-school graduates **peak in 2025 then decline ~13% through 2041**, with 38 states declining vs 2023 ([WICHE Knocking at the College Door](https://www.wiche.edu/knocking/), **VERIFIED**). Every enrollment VP now faces a shrinking traditional funnel; stop-out recovery is the largest non-traditional pool they already "own."

States have moved from talk to procurement: New Jersey built "the nation's first statewide re-enrollment marketplace" with ReUp (840K residents targeted); Illinois launched a statewide initiative across 19 public institutions covering 200K+ residents (Oct 2025); Minnesota (Mar 2025) and Massachusetts (Jan 2026) followed; ReUp cites Inc. 5000 listing two consecutive years driven by this state-policy shift ([reupeducation.com press](https://reupeducation.com/category/press/), **VERIFIED as vendor-reported events**).

**In scope:** cohort identification/scoring → contact-data remediation → compliant multi-channel outreach → transcript-gap computation → hold/payment-plan triage → readmit application completion → term-1 persistence monitoring.
**Out of scope (adjacent):** brand-new adult acquisition (marketing problem, not records problem), summer melt of admitted students (= DD-05), reverse-transfer degree conferral automation (expansion path §10).

## 2. Workflow today + failure modes

Today's campaign, reconstructed from practitioner patterns in raw research (P8/P16) and vendor positioning (**ESTIMATE** where not cited):

1. Registrar/IR exports "stopped-out with momentum" lists (60+ credits, GPA ≥2.0, left within N years).
2. Enrollment/retention staff (often <2 FTE, frequently zero dedicated) load them into Slate/Navigate or spreadsheets.
3. Mass email + letter + occasional call blitz around term start.
4. Interested students hit: stale contact info, holds (bursar/library/parking debts from years ago), readmit application requirements, FAFSA renewal, transcript requests to third institutions, placement prerequisites.
5. Staff hand-resolve each item across SIS + bursar + aid office; most students quietly die mid-funnel ("re-melt").

**Failure modes:**

- **Stale contacts:** phone/email collected 3–15 years ago; consent decay means autodialed texts/calls to old numbers are legally radioactive (§7). Institutions systematically overestimate how many former students they can actually reach (**ESTIMATE** — no published deliverability benchmark found this session: precise rate **UNKNOWN**).
- **Hold mazes:** a $180 unpaid balance from 2017 blocks re-enrollment; resolving it requires bursar negotiation, possibly payment-plan setup, sometimes financial-aid retroactivity questions. Each case is bespoke; staff default is "tell student to call the bursar," which kills conversion (**ESTIMATE**, consistent with P8 raw file).
- **Transcript archaeology:** returning adults attended 2–4 other institutions since stopping out; credits must be requested, parsed (paper/fax/legacy formats), articulated against current catalog rules before anyone can honestly say "you're X courses away." DegreeSight documents the pain: it claims 99% OCR accuracy and 90% evaluation-time savings on exactly this workflow, and reports that **48% of transfer-inquiry students walk away when credits can't be answered quickly** ([degreesight.com](https://degreesight.com/), **VERIFIED** as vendor claims). For stop-outs the archaeology is worse — records are older and scattered.
- **No closed loop:** EAB Navigate360 — installed at 850+ institutions serving 10M students — sells campaigns, alerts, and dashboards plus a "Strategic Leader" consultant; execution of document-chasing still falls to campus staff ([eab.com Navigate360](https://www.eab.com/products/navigate/), **VERIFIED**). The software generates the list; humans do the labor. That labor doesn't exist at scale, so campaigns run shallow.

## 3. Buyer & economic math

**Buyer:** VP Enrollment Management (owns revenue target) at CCs/regional publics; state higher-ed agencies/systems as second buyer (NJ/IL/MN/MA precedents, **VERIFIED** vendor-reported); CFO co-signs anything touching bursar holds. During the demographic cliff this moves from "nice retention project" to "the enrollment plan": traditional HS pipelines shrink ~13% by 2041 (**VERIFIED**, [WICHE](https://www.wiche.edu/knocking/)) while the SCNC pool grows 2.2%/yr (**VERIFIED**, [NSC](https://nscresearchcenter.org/some-college-no-credential/)).

**Database size assumptions (per institution class)** — **ESTIMATE**, anchored to the raw-file heuristic that a 15K-student university carries 30–60K historical stop-outs:

| Institution class | Current headcount | Historical stop-out DB | Plausibly recoverable (momentum ≥ some credits, <10 yrs out, in-state) |
|---|---|---|---|
| Large urban/rural CC | 10–25K | 40–100K | 5–15K |
| Regional public | 8–20K | 25–60K | 4–10K |
| Online/adult-serving university (TESU/WGU-class) | n/a | 50K+ | large, self-selected |

Momentum filter matters: NSC shows Potential Completers return and persist at higher rates (**VERIFIED**), so scoring the DB is itself a deliverable.

**Recovery-rate assumptions — honesty required.** Verified anchors:
- NJ statewide: **13.5K+ re-enrolled from an 840K-resident pool ≈ 1.6% of total pool** engaged-to-enrolled ([reupeducation.com](https://reupeducation.com/), VENDOR-CLAIM; denominator includes never-contacted residents, so true contacted-cohort conversion is far higher — **UNKNOWN**).
- UTSA: **714 re-enrolled / $5.8M tuition recovered ≈ $8.1K revenue per recovered student** (VENDOR-CLAIM, arithmetic ours; implies roughly one year of net tuition each at a large public).
- Illinois 4 legacy partners over 3 years: **2,300 re-enrolled, 265 completed (~11.5% completion among re-enrollees** — well above NSC's 4.7% national first-year rate, suggesting coaching selects/moves completers; VENDOR-CLAIM).
- ReUp aggregate: 3M+ learners reached, **60K re-enrolled since 2023**, $425M "tuition recaptured" (VENDOR-CLAIM; note $425M/60K ≈ $7.1K/recovered learner, consistent with UTSA arithmetic).

Working planning numbers for OUR model: **0.5–2% of a scored-and-contacted database enrolls in year one** (bottom half = cold internal CRM campaigns; top = well-run coached programs). **MARKETING-RISK label on all vendor rates**: denominators undisclosed, organic walk-in returns not netted out, no published control groups found this session (**UNKNOWN** — this is the biggest evidentiary hole in the category).

**Revenue per recovered student by segment** (first-year net tuition; **ESTIMATE**, consistent with raw-file P8 bands):
- Community college: $4–7K
- Regional public: $9–13K
- Private/online adult program: $15–25K+
Multi-year value if the student persists ≥2 terms ≈ 1.5–2.5× first-year net (**ESTIMATE**).

**VP Enrollment math during the cliff (illustrative regional public, ESTIMATE):** DB of 40K stop-outs; 18K score as momentum candidates; 12K reachable via at least one TCPA-safe channel (contactability assumption — see kill risk #1); 1.5% of contacted enroll ≈ 180 students × $11K ≈ **$2.0M new net tuition/yr** against a program cost of maybe $150–250K. Even at half those rates the ROI is >3:1. Compare CAC for a fresh traditional recruit ($2–5K marketing/search spend per enrolled, industry-standard band **ESTIMATE**) — recovery CAC of $800–1,400/student (cost ÷ enrolled at above volumes) is an order of magnitude cheaper *if* contactability and attribution hold.

**TAM (bottom-up, ESTIMATE):** ~1M SCNC re-enrollments/yr nationally ([NSC](https://nscresearchcenter.org/some-college-no-credential/), VERIFIED volume). At a vendor take of $500–1,500 per recovered enrollee, theoretical national fee pool ≈ **$0.5–1.5B/yr**. Serviceable near-term (CCs + regionals in attainment-active states running paid programs, mirroring the NJ/IL/MA/MN pattern): realistically **$50–200M/yr** within five years. State contracts add lumpy upside (single statewide deals plausibly $0.5–3M/yr each, **ESTIMATE** — contract values not public, **UNKNOWN**).

## 4. Pricing

Three shapes observed/inferable:

1. **Per-recovered-enrollee revshare (performance pricing).** Benchmark logic: recovered student is worth $4–25K first-year net to the institution; ReUp-style pricing is not public (**UNKNOWN** — no price sheet found; their model is bundled services+tech). Reasonable market band: **$500–1,500 flat per verified re-enrollee, or 8–15% of first-year net tuition** (**ESTIMATE**, anchored to the $7–8K/recovered-student institutional yield documented above and standard performance-marketing economics).
2. **Platform fee.** Comparable anchors: Slate student-success license $30K; "most clients pay $50,000/yr" ([technolutions.com/licensing](https://www.technolutions.com/licensing), **VERIFIED**, carried from competitive-landscape file); EAB enterprise contracts commonly six figures (**REPORTED** in raw files). A stop-out module priced $60–120K/yr fits existing budget lines.
3. **Hybrid (recommended): modest base ($30–60K, covers data wrangling + compliance ops) + success fee per enrolled.**

**Why performance pricing aligns but has margin implications:** it converts a skeptical buyer instantly (they only pay on realized tuition) and neutralizes the "we already send emails" objection. But delivery costs are front-loaded (decades of data cleanup, consent-safe channel setup, integration) while revenue is back-loaded, contingent, and contested by attribution disputes (§11 risk 3). A pure revshare vendor with 1–5 person capacity will starve between pilot and payout unless the base fee covers cost of goods. ReUp's own evolution is instructive: it sells an all-in-one bundle (outreach + intelligence + tech + human coaches) rather than pure success fees ([whats-included](https://reupeducation.com/whats-included/), **VERIFIED**) — services-heavy contracts smooth cash flow and hide unit economics from buyers.

**Target deal shapes:**
- **CC:** $25–50K base + $400–700/enrolled; annual value $40–90K; p-card/micro-purchase territory for pilots (2 CFR 200.320 mechanics per raw competitive-landscape file).
- **Regional public:** $50–80K base + $750–1,200/enrolled, targeting $100–200K total at plan.
- **Online/private university:** heavier revshare (10–12% of first-year net) — these buyers already think in per-enrolled marketing dollars, and their per-student revenue supports it.

## 5. Competitive teardown

| Player | What they do here | Why the gap persists |
|---|---|---|
| **ReUp Education** | The direct incumbent: outreach + "Intelligence" + tech (Vantage dashboard, Meridian learner portal) + human Success Coaches; 140+ partners, 33 states; state-level lockups NJ/IL/MN/MA ([site](https://reupeducation.com/), **VERIFIED**). Funding ~$47M lifetime carried from raw files as UNVERIFIED (**UNKNOWN** this session). | Services-heavy: coaches are the product; software is enablement. They win statewide deals but per-institution coverage of 4,000 Title IV schools is thin, and their unit model prices like consulting. An AI-native entrant undercuts on marginal cost of outreach + paperwork execution, not on coaching warmth. |
| **EAB Navigate360** | 850+ campuses, 10M students; campaigns/two-way SMS/alerts; markets an ROI calculator explicitly including "re-enrollment" as a lever; claims 2–12% retention lifts; embedded AI assistants (staff drafting, student Q&A) ([eab.com](https://www.eab.com/products/navigate/), **VERIFIED** incl. their own claims). | System of record for advising, not a worker. Stop-out outreach inside Navigate is rule-based campaigns executed by understaffed offices. Retaliation risk high if we sell INTO their install base (raw files flagged early-alerts as EAB home turf) — but EAB bundles broadly and ships features slowly. |
| **EdSights / Mainstay texting bots** | AI/text nudging for retention & melt; small funding rounds (**REPORTED** raw files). | Channel-only: they text, they don't reconcile transcripts, negotiate holds, or finish paperwork. Commodity risk (Signal Vine absorbed by EAB precedent, raw files). |
| **DegreeSight** | Transcript OCR (DocSight, 99% claim), InBound self-service credit answers, Insight prospective degree audits; syncs Banner/Colleague/PeopleSoft/Slate/Salesforce; SOC 2/HECVAT; ROI guarantee; 100+ institutions ([degreesight.com](https://degreesight.com/), **VERIFIED**). | Solves the *transcript-gap* slice prospectively for transfer recruitment — not the outreach/chase/hold/readmit loop for stopped-out populations. Natural partner or partial competitor; also proof-of-feasibility that our hardest parsing subproblem is commercially solved. |
| **Internal CRM campaigns (Slate/Salesforce)** | Free-ish, already owned. | No labor behind them; no degree-gap computation; no hold triage; no compliance discipline on aged contacts. |

**Why the gap persists (mechanism, not hand-waving):** recovery requires *bespoke reconciliation* — every student presents a different tangle of stale identity, multi-institution credits, ancient balances, changed programs — plus *labor* (calling, negotiating, form-wrangling) that registrars don't have. Incumbents monetize either analytics (EAB/Civitas) or humans (ReUp); nobody productized the reconciliation itself. LLM document intelligence changes that equation for the first time — this is the same "chase, verify, reconcile, resolve" hole identified across the whole pain map (raw files §cross-cutting 3).

**Incumbent-response risk:** moderate-high from EAB (AI feature velocity + distribution), low-moderate from ReUp (their economics depend on selling humans; automating themselves cannibalizes revenue). EdSights/Mainstay could bolt on gap-computation via partnerships faster than building.

## 6. Technical feasibility (1–5 people)

- **Legacy-data wrangling (hard, the real product).** Decades-old records in Banner/Colleague/PeopleSoft/Datatel-era schemas: duplicate identities, dead addresses, retired course codes, catalog-year drift. Extract via Ethos/API/SFTP nightly dumps; build an identity-resolution layer (fuzzy match on name+DOB+last-4 across alumni/CRM/SIS); score momentum using NSC's Potential Completer definition (≥2 yrs FTE) (**VERIFIED** definition source) plus local GPA/credit rules. Expect 30–50% of engineering time on data quality in year one (**ESTIMATE**).
- **Contact-data enrichment & legality (hardest non-obvious constraint).** Waterfall: institution-owned email → USPS NCOA mail → consent-gated SMS. Skip-data/people-search enrichment of former students is legally permissible for address history but *texting/calling a number harvested years ago* collides with TCPA (§7). Practical v1: mail + email + human-dialed calls from institution's own staff line; treat SMS as opt-in-permitted only. Carrier 10DLC/A2P registration needed even for school-branded texting; expect 2–4 weeks and nonzero rejection friction (**ESTIMATE**).
- **Transcript parsing for gap computation (medium; proven feasible).** DegreeSight's existence and claimed 99% OCR accuracy prove the pipeline works commercially (**VERIFIED** claim). Our edge cases are older paper/fax transcripts and defunct institutions; LLM extraction handles format variance well. The genuinely hard part is mapping extracted courses onto *current* catalog + equivalency tables to produce a defensible "X courses away" statement — wrong promises destroy trust and create liability. v1: compute conservative ranges ("roughly 2–3 semesters") pending registrar confirmation; auto-draft the audit exception memo, human registrar approves (pattern matches O24/DD-06 core).
- **Payment-plan/bursar integration (messy but bounded).** Holds live in SIS finance tables; payment plans run through Nelnet Campus Commerce/TouchNet/E-Cashier. Realistic v1: read ledger balance, classify hold type, generate triage recommendation + pre-negotiated plan options per bursar policy, route to bursar queue for one-click execution. Writing directly into finance systems is a phase-3 fantasy — nobody lets a startup post payments to their ERP (**ESTIMATE**).
- **v1 scope (buildable by 3 engineers + 1 GTM in ~4–6 months, ESTIMATE):** SIS extract pipeline → momentum scorer → contact-hygiene + mail/email sequences with human-call escalation → transcript-upload intake + gap estimate → readmit-application checklist tracker with automated chase. Defer: SMS automation, payment-plan write-back, FAFSA-renewal agent.
- **Hardest three technical risks:** (1) contactability/identity resolution yield on 10+-year-old records — unbounded until measured on real databases; (2) degree-gap correctness across catalog versions and defunct-course equivalencies — trust-critical, registrar-dependent; (3) per-campus workflow variance (readmit policies differ across 100s of institutions) — config sprawl that eats the software-margin story unless heavily templated.

## 7. Regulatory/deployment

- **TCPA/FCC — the central legal design constraint.** 47 CFR 64.1200 (**VERIFIED**, [ecfr.gov](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200)): autodialed/artificial-voice calls to wireless require prior express consent; telemarketing calls require prior express **written** consent; consumers may revoke by any reasonable means ("STOP" or any words a reasonable person reads as revocation) honored within 10 business days; calls restricted to 8am–9pm local. Aged student numbers carry decayed or ambiguous consent; class-action litigators target exactly this. Design consequences: no ATDS-pattern dialing on enriched numbers; human-initiated calls; informational (non-telemarketing) framing helps but does not eliminate exposure; FCC has separately signaled that AI-generated voice in robocalls is unlawful without consent (**REPORTED** — Feb 2024 FCC declaratory ruling, widely covered, not refetched this session). Mail and institution-originated email remain the safe backbone.
- **FERPA.** Former-student records stay protected; disclosure to our platform rides the "school official with legitimate educational interest" exception with direct-control contracting (standard ed-tech posture; EAB publicly states FERPA compliance, [trust.eab.com referenced from eab.com](https://www.eab.com/products/navigate/), **VERIFIED** as vendor statement). Enrichment must not involve the institution disclosing PII to us for purposes beyond the contracted educational function. Privacy of decades-old records: minimize retention, encrypt, least-privilege — PowerSchool breach aftermath (raw files) made higher-ed IT paranoid; HECVAT + SOC 2 are table stakes for procurement (DegreeSight advertises exactly this stack, **VERIFIED**).
- **GLBA** touches bursar/financial data flows (safeguards-rule obligations for the institution; we inherit contractual equivalents).
- **AI-outreach disclosure norms:** no federal statute mandates bot disclosure in education outreach, but FTC deception standards + growing state AI-disclosure laws push toward "AI assistant from [College] admissions team" transparency; also plain pragmatics — discovered deception torches the fragile trust a returning adult needs to re-enroll (**ESTIMATE/judgment**).
- **Deployment reality:** institution-hosted SIS access via read-only service accounts; vendor security review (HECVAT) adds 2–8 weeks to any deal (**ESTIMATE**).

## 8. GTM

**First customer:** a community college (or 3–5 college district) sitting on a 40K+ stop-out database, inside a state with active attainment politics and fresh re-engagement money — Illinois, Minnesota, Massachusetts, New Jersey pattern (**VERIFIED** state activity via ReUp releases). Rationale: CCs are both the biggest stop-out source and destination ([NSC](https://nscresearchcenter.org/some-college-no-credential/)), have leaner procurement than universities, feel the cliff through state funding formulas, and can buy pilots on p-cards below formal bid thresholds (competitive-landscape §4.2). Avoid starting where ReUp already holds the statewide contract head-on; enter adjacent states or non-covered systems.

**Who signs:** VP Enrollment Management / AVP Student Success as champion; VP Student Affairs or Dean of Students as co-sponsor (holds/holds-clearing live there); registrar consulted early (transcripts); CIO/security review gatekeeper.

**Pilot design (pre-contractual, this is the whole game given attribution risk §11):**
- Randomized matched cohorts: treatment vs holdout from the SAME scored list, minimum 3,000 contacted per arm.
- Primary metric: **enrolled-per-1K-contacted** (not clicks/replies); secondary: term-1 persistence of returners, hold-clearance cycle time, readmit-application completion rate.
- Duration: one full recruitment cycle (4–6 months) + one term persistence readout.
- Success bar agreed in writing: e.g., treatment beats holdout by ≥3 enrolled/1K-contacted and ≥1.0pp persistence lift → convert to hybrid deal (§4).
- Instrument the internal SLA: median days from "student says yes" to registered — quantifies the re-melt leak and arms the expansion case.

**Procurement path:** pilot under micro-purchase/simplified thresholds (2 CFR 200.320 mechanics per raw file) → 12-month subscription via normal PO → E&I cooperative piggyback once 2–3 lighthouse references exist (mechanism per competitive-landscape §4). State/system deals run on legislative budget cycles: 9–18 months, RFP-driven, incumbency advantages — enter year two, not day one.

**Cycle length:** institutional pilot 3–6 months to signature (fast lane exists below $50K); full deployment decision 6–12 months; state contracts 12–24 months (**ESTIMATE**, consistent with raw-file buying-behavior bands).

## 9. Service→product ladder

The honest ladder here starts agency-shaped because the scarce input (cleaned data + compliant channels) is produced once and reused:

1. **Stage 1 — Done-for-you campaign (agency):** we run everything for 1–3 flagship customers: cohort scoring report, contact remediation, creative, sequences, weekly human-call escalation to their staff, results dashboard. Price $40–75K per cycle. Purpose: measure contactability + recovery on REAL databases (kill-risk falsification §11) while getting paid to learn.
2. **Stage 2 — Co-delivered playbooks:** customer staff own calls/counseling using our sequences, scripts, hold-triage SOPs, and readmit tracker; we own data + software + gap computation. Base + success fee. This mirrors what ReUp charges a premium for, at software margins on our side.
3. **Stage 3 — Platform:** self-serve campaign builder over their SIS, transcript-gap engine with registrar approval queue, hold-triage routing, persistence monitoring; Slate/Navigate integrations as distribution. Move toward $60–120K platform fees + optional success fees.

Anti-pattern warning: do NOT hire a big human calling floor (ReUp already owns that cost structure and scale advantage). The differentiation is software-executed reconciliation with humans only at judgment moments.

## 10. Expansion paths

- **Summer melt (DD-05 adjacency):** identical chase/checklist/document engine pointed at deposited-but-not-arrived freshmen instead of stop-outs; bigger per-unit dollars at privates; shares the orchestration core. Sell both to the same VP Enrollment.
- **Veterans stop-outs:** SCNC population overlaps GI-Bill beneficiaries with interrupted entitlement (Rudisill re-reviews, monthly verification per raw file P11); veterans offices are chronically understaffed; per-student revenue high ($15–40K). Same engine + VA-form wrappers.
- **Credential-completion grants / reverse transfer:** NSC's finding that ~1 in 4 SCNC credential earners complete *without re-enrolling* via administrative barrier removal (**VERIFIED**) implies a pure-paperwork SKU: mine near-completers, assemble audit-exception packets, drive degree conferral. Revenue via state completion-grant funding (states pay per completer) and institutional performance-funding metrics; also the least legally fraught product (no solicitation of people, just record processing). Historically, Lumina-funded reverse-transfer initiatives proved conferral-at-scale works, though precise totals were not re-verified this session (**UNKNOWN**).
- **State marketplace plays:** replicate the NJ/IL model in uncovered states as the software-first alternative; one state win compounds (system-wide data access, reference monopoly).
- **UK/international adult learners:** UK Lifelong Learning Entitlement (2027) and credit-accumulation frameworks create a returning-adult paperwork wave; Open University-class institutions and FE colleges have analogous stop-out records. Longer shot: different regulatory regime, weaker per-student revenue (**ESTIMATE**; flagged UNKNOWN detail level).
- **Employer/workforce partnerships:** states increasingly frame re-engagement as workforce policy (IL release explicitly ties 2031 jobs-needs to credentials, **VERIFIED** vendor-reported) — WIOA/state workforce boards as payer #3.

## 11. Kill risks (top 5) + falsification tests

1. **Contactability collapse.** If only 20–30% of the scored database is reachable through any TCPA-safe channel, unit economics fail silently — everything else was modeled on 50–70%. *Test BEFORE building:* take two random stop-out cohorts at a design-partner (one recent ≤3 yrs, one old 5–10 yrs), run NCOA + email validation + permissioned phone-status checks; measure % with valid postal + email + consent-clean phone. Kill threshold: <40% single-channel reachable.
2. **Easy wins already exhausted.** States (NJ/IL/MN/MA) and ReUp/EAB campaigns may have skimmed the most recoverable layer at flagship targets; remaining pools could be low-intent residue. *Test:* mystery-shop 10 target institutions — ask what re-engagement outreach ran in the last 36 months, at what volume, with what results; request their last campaign's enrolled-per-1K. If recent internal campaigns already hit ≥8–10 enrolled/1K-contacted, our lift thesis weakens materially.
3. **Attribution war on performance pricing.** Returning adults also walk in organically (NSC counts ~1M re-enrollments/yr nationally regardless of vendors, **VERIFIED**); finance officers will contest invoices. *Test:* pre-sell holdout methodology in the pilot contract; if a design partner refuses a holdout, that refusal IS the signal — walk.
4. **Services-heavy margin trap.** If converting one enrollee requires >15–20 human-hours (coaching, chasing, negotiating), we've rebuilt ReUp with worse scale. *Test during stage 1:* instrument hours-per-enrolled by task; software-addressable share must exceed ~70% by stage 2 or pivot to DD-05/other opportunities.
5. **Re-melt / institutional capacity bottleneck.** Student says yes, then registrar/bursar takes 6 weeks and the enrollment dies — vendor blamed for "results not showing up." *Test:* in stage-1 pilots, track stage-conversion from verbal-yes → applied → registered → census-day-enrolled; if internal SLA losses exceed ~30% of yeses, the product must include institution-workflow pressure tooling (or the deal shape must pay on census-verified enrollment only).

## 12. Verdict

### BUILD-CAREFULLY

Honest paragraph: The demand side is as close to verified as this research program gets — a 43.1M-person pool growing yearly, a demographic cliff that turns re-engagement from virtue into survival, state legislatures actively funding it, and NSC's own data proving paperwork removal alone confers credentials. But skepticism demands three admissions. First, ReUp Education is not a sleeping incumbent: it signed four states in ~18 months, claims 60K re-enrollments since 2023 and Inc. 5000 growth two years running, and its human-coach model demonstrably works — an entrant's wedge is software-cost disruption, not discovery of a hidden market. Second, the category's headline numbers (1.6% pool conversion, $8.1K/student yields) are all VENDOR-CLAIMs with undisclosed denominators and zero published control groups; our entire economic model rests on contactability assumptions that are UNKNOWN until tested on real databases — hence the falsification tests are sequenced before code, not after. Third, the compliance surface (TCPA on aged consents, FERPA on decades-old records, GLBA on bursar data) is manageable but punishes naivety with statutory damages, and one sloppy-texting lawsuit would poison the reference chain this GTM depends on. Build the agency-stage first to get paid while measuring the two unknowns (reachability, true incremental lift), keep humans at judgment points, and expand along the transcript-core family (DD-06) where the technical moat actually lives. This scores below the raw database's optimistic 114 once competition and implementation difficulty are re-priced — still comfortably above the build/no-build line for a disciplined 3–5 person team that refuses pure-revshare deals.

**Re-scored dimensions (vs original O22 row: 8·7·9·9·9·8·7·7·7·6·7·6·6·8 = Σ114):**

| Dim | Old | New | Rationale |
|---|---|---|---|
| P1 pain severity | 8 | 8 | unchanged — cliff-verified |
| P2 frequency | 7 | 7 | unchanged |
| P3 economic cost | 9 | 9 | unchanged — net-tuition lever intact |
| P4 buyer WTP | 9 | 8 | states fund it, but budget scrutiny up in cliff era |
| P5 agent suitability | 9 | 9 | unchanged |
| P6 automation potential | 8 | 8 | unchanged |
| P7 competition whitespace | 7 | **5** | ReUp scaling fast; EAB AI-shipping; EdSights adjacent |
| P8 differentiation | 7 | 7 | reconciliation-depth moat still real |
| P9 ease reaching buyers | 7 | 7 | clear named buyers; conference/coop channels |
| P10 implementation ease | 6 | **5** | legacy data + compliance engineering heavier than scored |
| P11 regulatory safety | 7 | 6 | TCPA statutory-damages tail on aged contacts |
| P12 data access ease | 6 | **5** | consent-decayed, quality-poor records; FERPA gating |
| P13 global scalability | 6 | 6 | UK/intl possible, unproven |
| P14 recurring revenue | 8 | 7 | revshare contingent + attribution disputes |
| **Σ** | **114** | **100** | still BUILD tier, no longer top-3 of database |

---
**Key sources:** [NSC SCNC 2025](https://nscresearchcenter.org/some-college-no-credential/) · [WICHE Knocking 11th ed.](https://www.wiche.edu/knocking/) · [ReUp site + press](https://reupeducation.com/category/press/) (incl. [Illinois initiative](https://reupeducation.com/2025/10/08/illinois-re-enrollment-initiative/)) · [EAB Navigate360](https://www.eab.com/products/navigate/) · [DegreeSight](https://degreesight.com/) · [47 CFR 64.1200](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200) · [Technolutions licensing](https://www.technolutions.com/licensing) · raw files `00-raw-segment-research/higher-ed-us.md` (P7/P8), `00-raw-segment-research/competitive-landscape.md` (§1.3, §4).
