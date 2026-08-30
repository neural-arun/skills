# DD-10 — Career-College Regulatory Filing Factory (Deep Dive)

**Date:** Aug 25, 2026 · **Status:** Research complete · **Verdict:** BUILD-CAREFULLY (see §12)

**Labels:** VERIFIED = fetched/read this session or prior session (URL given) · ESTIMATE = directional, reasoning given · UNKNOWN = could not establish.

**New findings this session (VERIFIED unless noted):**
- **BPPE filing machine confirmed live and dense:** 2025 Annual Report portal opens **Aug 1, 2026**, reports due **Dec 1, 2026**; report must include program costs, graduation rates, **post-graduation job-placement rates**; a separate **School Performance Fact Sheet (SPFS) per program, per main AND branch location**, covering two prior calendar years, submitted as link with the Annual Report; BPPE publishes every institution's filed AR + catalog + SPFS publicly (2020–2024 archive live). https://www.bppe.ca.gov/annual_report/
- **BPPE enforcement page updated Aug 24, 2026**, with monthly disciplinary PDFs every month FY2022-23 → FY2026-27, and an A–Z actions list overwhelmingly populated by **citations/fines/abatement orders against truck-driving schools, beauty colleges, phlebotomy/medical schools, language schools** — many flagged "NON-PAYMENT/NON-COMPLIANCE WITH CITATION." Repeat offenders common (e.g., 160 Driving Academy cited 2023 *and* 2025; A-1 Truck Driving School: multiple citations 2020–2025 culminating in a Decision & Order Jan 2026). https://www.bppe.ca.gov/enforcement/disciplinary_actions.shtml
- **NC-SARA: >2,400 institutions** in 49 states + DC + PR + USVI; fees **$2,200–$8,800/yr by enrollment**; mandatory institutional data reporting; professional-licensure disclosure directory; Policy Manual v26.1 effective Jul 1, 2026. https://www.nc-sara.org/fast-facts/
- **Workforce Pell has arrived:** NC-SARA published a June 2026 statement on how SARA covers Workforce-Pell-eligible programs (https://nc-sara.org/wp-content/uploads/2026/08/Workforce-Pell-Statement_June-2026.pdf, linked from homepage) — short-term vocational programs entering Title IV = a new cohort of schools acquiring federal reporting obligations for the first time.
- **Enforcement climate is politically cyclical:** ED fined Grand Canyon University **$37.7M** (2023, misrepresentation of doctoral costs) then **rescinded it May 2025** under a new administration; FTC dropped its GCU suit Aug 2025 (class action continues). https://en.wikipedia.org/wiki/Grand_Canyon_University Meanwhile **state-level enforcement (BPPE citations) continued unabated through 2026** (see above). Federal softening ≠ state softening.
- **Australia: "almost 5,000 RTOs"** (ABS-cited Wikipedia figure; current active count ~3,800–4,000 per prior-session ESTIMATE), three regulators (ASQA/VRQA/TAC), AVETMISS data submission obligations, registration + compliance audits. https://en.wikipedia.org/wiki/Registered_training_organisation
- **Could NOT verify this session:** NACCAS member counts (site unreachable), FMCSA ELDT provider registry (403), ASQA stats (timeout), Anthology Student product page (404), all consultant rate cards (none publish pricing). Labeled below.

---

## 1. Problem & scope

**The pain (anchored in raw research P11/P12):** every private career college maintains an **evidence ledger behind mandatory filings**: enrollment/completion/placement aggregates per program per location → state annual report → SPFS per program×location due Dec 1 → accreditor annual report (ABHES requires an **Annual Report + Self-Evaluation Report** — VERIFIED structure: https://www.abhes.org/resources/) → NC-SARA renewal + data submission + professional-licensure disclosures → renewal of state approval → placement-verification binders (employer attestations) → marketing claims that must match the filed numbers. The data lives scattered across SIS exports, payroll, admissions spreadsheets, and placement trackers; each filing reformats the same facts differently; 1–3 back-office people run the whole stack (raw research P11: 150–400 staff-hours/yr ≈ $15–60K internal cost, **ESTIMATE**).

**Scope recommendation: US-first, CA-wedge, with rulebook-as-config architecture from day one.**

Reasoning:
1. **Rulebook content is the moat, and it's jurisdiction-local.** The hard 80% is encoding BPPE's exact SPFS field definitions, ABHES/NACCAS report schemas, and each state's placement formula. Doing CA + 2 accreditors deeply beats doing nothing well in three countries. Multi-region later reuses the engine, not the rulebooks.
2. But **do not build a hardcoded CA tool.** Every schema (BPPE SPFS template is a public Word/PDF artifact — VERIFIED: https://www.bppe.ca.gov/schools/pfs.pdf) becomes a config object: fields, formulas (completion rate, placement rate numerator/denominator per jurisdiction), deadlines, verbatim-required statements ("All verbatim statements required for the SPFS must be included as is" — VERIFIED BPPE submission tips), output templates. This makes the eventual AU/IN expansion a rulepack-authoring exercise, not a rewrite (international.md already classifies compliance reporting as INTERNATIONALLY SCALABLE, schema local).
3. **v1 includes the two adjacent problems** (P11 + P12) because the evidence ledger is shared: placement attestations feed SPFS placement rates feed marketing claims. Marketing-compliance scanning (claims vs substantiation) rides on the same ledger at near-zero marginal cost.

**What v1 does NOT do:** no auto-submission (human approves every filing), no legal advice, no Title IV financial-aid compliance in v1 (expansion §10), no write-back into SIS.

---

## 2. Workflow today + failure modes

Annual cycle (dates VERIFIED where noted):

| Stage | Today | Failure mode |
|---|---|---|
| Data assembly (Sep–Nov) | Pull rosters/completions from SIS (Anthology/CampusVue legacy, Campus Café, spreadsheets), payroll clock-hours, placement tracker | Exports don't reconcile; hours recorded differently than the state formula expects; last-minute scramble |
| Placement verification (continuous, peaks Oct–Nov) | Staff email/call graduates & employers for attestation letters; LinkedIn sleuthing | Attestation response rates low; "qualified placement" judgment calls made inconsistently; evidence binder thin exactly where auditors look (P12) |
| SPFS generation (per program × location) | Fill public template by hand; two years of data side-by-side | Wrong year windows; branch locations forgotten; verbatim statements missing; math errors propagate to the public record |
| State Annual Report | Keyed into AR portal (BPPE: opened Aug 1, due Dec 1 — VERIFIED) | Late filing → fines/probation; inconsistencies between AR and SPFS trigger inspection flags |
| Accreditor reports (ABHES Annual Report + Self-Eval; NACCAS/ACCET equivalents) | Separate forms, same underlying data, different cuts | Numbers diverge from state filing — a classic audit finding |
| NC-SARA renewal + disclosures | Renewal form, annual data report, per-state×program licensure disclosures maintained manually | Disclosure directories go stale after program changes (SARA participation is preconditioned on good standing — VERIFIED eligibility requirements) |
| Marketing scan (episodic) | Someone checks landing pages/ads against filed numbers when someone remembers | Claim drift: website still shows last year's placement rate or an unsubstantiated "86% hired" (BloomTech's exact failure mode — VERIFIED: https://en.wikipedia.org/wiki/Bloom_Institute_of_Technology) |

**Consequence ladder:** citation + fine + abatement order (the modal BPPE outcome — dozens monthly, VERIFIED) → accusation/stipulated settlement/probation (beauty-college examples on the same page) → default decisions and surrender of approval → for the extreme case, BloomTech: $75K BPPE penalty + cease-order, CFPB order fining company $64,904 + CEO $100,000, voided ISAs, lending ban (**VERIFIED**). Approval loss = business death.

---

## 3. Buyer & economic math

**Buyer:** Owner/President (single decision-maker at single-site schools); COO/Compliance Director at groups. These are businesses with $500K–$10M tuition revenue and zero-to-two compliance staff.

**Owner-operator pain math (single-campus cosmetology school, ~150 students, 1 program × 1 location + 1 branch):**
- Internal labor: 150–400 hrs/yr across state+accreditor+SARA cycles (**ESTIMATE**, raw P11 reasoning) ≈ $9–32K at $40–60/hr loaded owner/admin time.
- Consultant spend where used: $5–25K per cycle for annual-report/SPFS prep (**ESTIMATE** — no public rate cards exist; anchored on boutique compliance consultancies billing $150–350/hr and ed-law attorneys $250–450/hr; **UNKNOWN** precise).
- Attestation chasing: 0.5–2 FTE at mid-size schools for outcomes verification alone (**ESTIMATE**, raw P12).
- Total addressable pain per school: **$15–70K/yr** (**ESTIMATE**), against a school whose approval is worth its entire revenue stream.

**Enforcement-risk quantification:**
- Modal outcome: BPPE cite-and-fine orders — recurring, monthly-documented (**VERIFIED** list). Fine magnitudes per citation are typically hundreds-to-low-thousands of dollars plus abatement (individual citation PDFs on BPPE site; magnitudes **ESTIMATE** from sampled orders — **UNKNOWN** aggregate distribution).
- Catastrophic outcomes are documented, not hypothetical: BloomTech ($75K fine + cease operation; CFPB/DFPI orders) **VERIFIED**; GCU $37.7M ED fine (later rescinded) **VERIFIED**. For a $2M-tuition school, expected-loss math doesn't matter — **loss-of-approval is uncapped**, which is why willingness-to-pay is driven by dread, not ROI arithmetic.

**Segment sizes (counts):**
| Segment | Count | Label |
|---|---|---|
| CA BPPE-approved institutions | Directory live (VERIFIED: https://www.bppe.ca.gov/search/); count not extracted this session; ~1,500–2,000 | ESTIMATE |
| NC-SARA participating institutions | **>2,400** | **VERIFIED** (https://www.nc-sara.org/fast-facts/) |
| US for-profit/Title IV institutions | ~1,500–1,800 | ESTIMATE (IPEDS-based, not fetched) |
| US cosmetology/beauty schools | NACCAS site unreachable; accredited base ~300–400, total state-licensed schools ~1,500+ | ESTIMATE/UNKNOWN |
| US CDL/trucking schools | FMCSA ELDT registry 403'd; ~3,000+ registered providers incl. districts/carriers | ESTIMATE/UNKNOWN |
| State-approved private career schools, all states (top states: CA, TX ~700–1,000, FL ~600–900) | ~6,000–10,000 | ESTIMATE |
| AU RTOs | "Almost 5,000" (ABS-cited); ~3,800–4,000 active | VERIFIED (stale) / ESTIMATE (current) |
| India HEIs / NAAC-accredited | ~45,000 HEIs; only ~8,500 colleges + 450+ universities accredited as of 2024; binary-accreditation overhaul underway | VERIFIED prior session (international.md §8) |

**TAM (order-of-magnitude, serviceable-with-software pricing):**
- **US:** 6–10K schools × blended $8–15K ACV → **$60–120M/yr** (ESTIMATE). CA-only beachhead: ~2,000 × 40% addressable × $9K ≈ **$7M**.
- **AU:** ~4,000 RTOs × A$8–10K → **A$32–40M** (ESTIMATE).
- **IN:** realistic near-term buyers (institutions pursuing/retaining NAAC grade, post-scandal binary transition) 10–20K × ₹1.5–4L → **₹300–800 crore ≈ $36–96M** (ESTIMATE).
- Combined: **~$150–250M/yr globally** — a solid vertical-SaaS market, explicitly *not* venture-unicorn scale without the multi-region rulebook engine thesis working.

---

## 4. Pricing

**Model: annual retainer per campus, not per-filing.** Filings are the visible artifact; the value is the continuously-maintained evidence ledger + attestation chase + deadline engine. Per-filing pricing would push customers to skip the continuous layer (where the defensible work happens) and re-create the seasonal-crunch dynamic we're eliminating.

**Consultant-replacement benchmark:** consultants charge $5–25K per annual cycle per campus (**ESTIMATE**, §3) for work that is largely mechanical once data is structured. Price the done-for-you retainer just under the credible consultant quote:

| Tier | Profile | Retainer |
|---|---|---|
| Micro | <100 students, 1 location, 1–2 programs | **$6K/yr** ($500/mo) |
| Small | 100–500 students, 1–2 locations | **$12K/yr** |
| Mid | 500–2,000 students, multi-program/multi-location, accredited + SARA | **$25–40K/yr** |
| Group | Multi-campus chains | $60K+/yr |

ACV targets: land at $6–12K, expand to $25–40K as attestation-chase + marketing-scan modules attach. Self-serve "platform-only" tier later at $3–6K for schools who want the ledger without the service.

**Why existential-risk framing supports premium:** the retainer is 0.3–1% of a typical school's tuition revenue; the insured asset is 100% of it. Frame pricing against (a) consultant invoice, (b) owner's December lost to spreadsheet archaeology, (c) one BPPE citation + abatement cycle with counsel — never against "software budgets," which these schools barely have. This mirrors raw research's cross-cutting finding that compliance-crunch problems sell despite small budgets *because the alternative is existential* (P11/P12 precedent: fines, revocation, CFPB-class actions, all VERIFIED).

---

## 5. Competitive teardown

**1. Compliance consultants (the main competitor).** Boutique firms and ed-law practices embedded in this world for decades. Strengths: relationships with owners and even regulator staff, judgment on gray areas, full-service. Weaknesses: seasonal surge capacity (everyone's busy Sep–Nov), expensive per hour, inconsistent quality, spreadsheet-based, gone after Dec 1 — nobody maintains the ledger continuously. They are also a **channel** (white-label our engine) before they're purely competitors.

**2. SIS vendor report modules.** Anthology Student (CampusVue lineage), Ellucian, Jenzabar, career-college specialists (Campus Café, CourseKey, Element451) ship canned regulatory reports (SAP, completion, some state extracts). Product page unreachable this session (404) — capability claims **ESTIMATE** from domain knowledge. Why they don't close the gap: their reports cover *their own database*, not payroll, employer attestations, prior filings, or ad surfaces; they have no per-jurisdiction rulebook maintenance incentive (career-college sub-segment is small for them post-Anthology consolidation); they will never do chase-work (emailing employers for attestations is not in an SIS vendor's DNA).

**3. Accreditation-evidence platforms** (Weave, SPOL-class) — sell to universities' regional-accreditation workflows; wrong buyer, wrong price point, no state-vocational rulebooks.

**Why the gap persists:** a school paying $2K/yr for software couldn't fund a $50K enterprise implementation, and pre-LLM automation the work needed humans anyway. **Small-school economics never justified software; agents collapse the cost of service** — the exact structural unlock this whole research series keeps finding.

**Consolidation risk:** moderate-low near-term. Anthology/Ellucian focus on larger institutions; CECU-adjacent service firms lack software DNA. The realistic acquirer end-state (SIS vendor bundling an agentic compliance module in 3–5 years) is an exit, not a kill — if the rulebook library is deep by then.

---

## 6. Technical feasibility (1–5 people)

**Buildable. Core components:**
1. **Rulebook-as-config.** Each jurisdiction/filing = versioned config: required fields, formulas (placement-rate numerators/denominators differ by state AND accreditor — encode both), deadlines, verbatim strings, output template mapping (BPPE's public SPFS Word template is the reference pattern — VERIFIED). Rulebook releases ship with human-readable changelogs.
2. **Messy-source extraction.** Ingest SIS CSV/Excel exports, clock-hour/payroll sheets, placement trackers (often one giant spreadsheet per campus), prior-year filings (PDF). Structured-extraction + reconciliation is standard LLM-era work; expect per-customer mapping effort of days, not weeks — this is where service-tier labor goes in year one.
3. **Attestation-chase workflows.** Agent-driven email/SMS sequences to graduates/employers, response tracking, e-sign attestation capture, auto-filing into the evidence ledger with timestamps (same primitive as P2/P8 chase loops — the research series' "most defensible wedge").
4. **Template generation.** Deterministic rendering into SPFS/AR/accreditor formats with **every number hyperlinked to its source evidence**; consistency checker across state vs accreditor cuts of the same facts.
5. **Marketing-claim scanner.** Crawl the school's public pages/ads, extract outcome claims, diff against filed numbers, flag drift.

Effort: 2 engineers + 1 ops/regulatory lead + founder-sales ≈ viable v1 in 4–6 months; 5 people covers pilot cohort of 20–40 schools through one full cycle.

**Hardest three risks:**
1. **Jurisdiction churn.** Rules change mid-cycle (BPPE issued a "Notice of New Reporting Requirements" — linked from its AR page, VERIFIED; SARA Policy Manual v26.1 effective Jul 1 2026 — VERIFIED). Missing a change silently corrupts filings. Mitigation: regulatory-change monitoring pipeline (diff portals/manuals quarterly) + conservative "confirm before render" gates. This is permanent ops cost, not a solved problem.
2. **Placement-definition judgment calls.** Whether a graduate counts as "placed" (field vs occupation, part-time, self-employment, licensure-pending) is a *policy interpretation with human accountability*. Agents propose classifications with cited evidence; a named human signs the policy call. Get this wrong and we've automated BloomTech's exact misrepresentation vector — the design must make the honest path the easy path.
3. **Small-customer support burden.** Buyers are C-grade-ops organizations; expect hand-holding, dirty data, deadline-week panic at 11pm. Mitigation: done-for-you service tier prices the hand-holding in; platform tier reserved for schools that prove operable.

---

## 7. Regulatory & deployment

- **Accuracy liability.** If a filing is wrong, the school faces the citation — and may blame the vendor. Design stance: **we are tooling + evidence infrastructure, never the filer of record.** Every package exits through a human sign-off gate (school's designated approver, e-signed), every figure carries source-evidence links, immutable audit log of who-changed-what. Errors caused by bad inputs are provably attributable. Carry **E&O/professional-liability insurance** sized to retainer book (premiums **ESTIMATE** manageable at this exposure profile; get broker quotes before scaling — UNKNOWN until quoted).
- **We deliberately do not become a "placement-rate laundering" tool.** The attestation chase must collect *true* evidence; scanner flags overclaims rather than optimizing them. Post-BloomTech, regulators and plaintiffs' counsel will probe vendors in this space; "provably substantiated" is both the ethical and the marketable position (mirrors international.md's post-NAAC-scandal "provably untainted" framing).
- **Multi-state variation management:** rulebook configs versioned per jurisdiction; customers see a diff view whenever rules change; conflicting definitions between state and accreditor formulas surfaced explicitly rather than averaged away.
- **Data handling:** FERPA-adjacent student records (graduates), employer PII; SOC 2 pathway needed before mid-market groups sign; hosting US-region.

---

## 8. GTM

**First segment: California single/multi-campus beauty & allied-health schools (cosmetology, barbering, phlebotomy, medical assisting).**
Rationale: BPPE is the densest, most enforcement-active regime in the country (monthly citations against exactly these verticals — VERIFIED), Dec 1 creates an annual forcing function, and these owners feel both the paperwork and the dread. Trucking (TX/CA) is a strong #2 (160 Driving Academy and A-1 repeat-citation patterns are VERIFIED) but operators are smaller/more chaotic. Bootcamps post-BloomTech are the highest-fear, highest-WTR-per-seat segment but the population is small and shrinking; use them as lighthouse accounts, not the beachhead.

**Who signs:** the owner. One-call close dynamics; no committee. Sell in Aug–Oct (portal opens Aug 1 — VERIFIED; panic peaks Sep–Nov), deliver through Dec 1.

**Pilot offer:** "One filing cycle, done for you": fixed fee ($6–9K), we ingest your data, run the attestation chase, produce your SPFS set + Annual Report package **submit-ready by Nov 15**, you press submit. Success metric: on-time filing + zero BPPE findings + hours reclaimed (target: owner spends <8 hrs vs 100+).

**Channels:** state associations first (California Association of Private Postsecondary Schools — CAPPS — newsletter/events; Texas Association of Proprietary Schools; Florida association equivalent), accreditor conferences (ABHES National Conference and workshops — VERIFIED events calendar exists at https://www.abhes.org/events/; NACCAS conventions; ACCET workshops), CECU annual conference. BPPE itself runs compliance workshops for schools (VERIFIED: https://www.bppe.ca.gov/enforcement/compliance_workshops.shtml) — attend, don't sponsor; that's where panicked owners congregate.

**Cycle:** annual, deadline-anchored. Land Aug–Nov, expand modules Jan–Jun (attestation chase is year-round), renew Aug. Expect brutal seasonality in cash flow — plan runway accordingly.

---

## 9. Service→product ladder

1. **Done-for-you filing service (months 0–12):** humans + agents behind the curtain, priced as consultant replacement ($6–40K/campus/yr). Purpose: learn every rulebook quirk, fund development, accumulate the evidence-ledger data model. Margin thin but positive with agents doing extraction/chase/drafting.
2. **Continuous-compliance platform (year 1–2):** the ledger, deadline engine, attestation chase, claim scanner become self-serve with assisted onboarding; service tier remains for micro/operators. Gross margin flips toward software.
3. **Multi-region rulebook engine (year 2–4):** author AU-RTO (ASQA audit-readiness + AVETMISS validation) and IN-NAAC (SSR/DVV evidence packs) rulepacks; license to local partners/consultants who keep their client relationships and white-label the engine. The engine + rulebook library — not any one filing — is the durable asset.

---

## 10. Expansion paths

- **AU RTOs** (~4,000): Standards-for-RTOs evidence packs, trainer-credential currency tracking, AVETMISS validation, marketing-accuracy scans; open procurement market, no local entity mandated (international.md §2 — VERIFIED accessibility ranking). Natural second market; English-language, agent-friendly.
- **IN NAAC** (~45K HEIs, accreditation wave pending): SSR generation + DVV verification responses with tamper-evident audit trails; post-CBI-case positioning writes itself. Low ARPU demands partner/channel motion (international.md §8).
- **Charter schools (US K-12):** charter-authorizer renewal petitions are the same shape — evidence ledger → renewal document → authorizer-specific rubric. Different buyer (school leaders + boards), same engine; meaningful adjacency once rulebook machinery matures.
- **Title IV audit-readiness:** FSA audit guide evidence packs, SAP documentation, admin-capability filings. **Catalyst: Workforce Pell** — NC-SARA's June 2026 statement confirms short-term programs are entering the framework (VERIFIED); thousands of non-Title-IV career schools will inherit federal reporting obligations for the first time and will need exactly this infrastructure. Time the expansion to that wave.
- Later/adjacent: SG SkillsFuture provider clawback-proofing (international.md §5), UK OfS/ESOS-style duties — opportunistic only.

---

## 11. Kill risks (top 5) + falsification tests

1. **Schools too cheap/disorganized to pay.** Dread-driven purchases still require solvency; many micro-schools run on margins too thin for even $6K. *Test:* 20 signed pilots at ≥$6K within two selling seasons (Aug–Dec); if close rate <20% on qualified outreach from association lists, kill or move upmarket.
2. **Consultants cheaper at their price point / relationship-locked.** Some incumbents will discount to keep accounts, and owners trust their guy. *Test:* displacement win-rate head-to-head ≥50% on schools using consultants; if consultants are routinely quoting below $5K/cycle, the benchmark collapses and pricing resets to a marginless fight.
3. **Regulatory change eliminates filings.** Deregulation is plausible: GCU's $37.7M fine was rescinded in May 2025 (VERIFIED) and federal enforcement softened; a state could gut BPPE. Counter: state enforcement continued through 2026 (VERIFIED), and diversifying across states + accreditors + AU/IN hedges single-regime repeal. *Test:* standing watch on CA budget/mandate bills and BPPE staffing; if BPPE citation volume halves YoY, re-weight GTM to other jurisdictions immediately.
4. **SIS vendors bundle agentic compliance.** Anthology-class vendor ships a compliance module for career colleges. *Test:* quarterly roadmap watch; differentiation must stay in chase-work + cross-jurisdiction rulebooks + marketing scanning (things SIS vendors structurally won't do). If an incumbent ships attestation-chasing, reassess.
5. **One accuracy incident kills the niche.** A botched SPFS or missed attestation that produces a false placement rate = reputation death in a tight-knit industry. *Test (pre-launch gate):* pilot error rate <0.5% of rendered fields, zero missed-deadline incidents, E&O bound, sign-off gate exercised on 100% of filings. Any incident → root-cause postmortem published to affected customer within a week.

(Honorable mention: seasonality crushes cash flow — model it; it's a planning risk, not a kill.)

---

## 12. Verdict: BUILD-CAREFULLY

Honest paragraph: The core facts are unusually well-evidenced for a niche this size — the filing machine is real and dated (Aug 1 / Dec 1, VERIFIED), the enforcement mill grinds monthly across exactly the verticals we'd target (VERIFIED), the catastrophic-loss precedents exist (BloomTech VERIFIED), and the competitive gap has a clean structural explanation (small-school economics never justified the software until agents collapsed cost-to-serve). But this is a **grind-it-out vertical services-business-turned-SaaS, not a rocket**: TAM tops out around $150–250M globally (ESTIMATE), ACVs are $6–40K, buyers are organizationally weak, revenue is violently seasonal, and the two hardest problems — keeping rulebooks current and making placement-classification judgment calls defensible — are permanent operating costs, not one-time builds. The 2025 federal enforcement thaw (GCU rescission, VERIFIED) is a reminder that the political substrate under demand is volatile, though state-level enforcement gives the thesis a floor. Build only with a founder or founding hire who genuinely knows this world (ex-BPPE examiner, ex-NACCAS/ACCET staffer, or veteran career-college compliance director), sell one done-for-you cycle before writing much platform code, and treat the rulebook library as the asset. If pilots clear the falsification gates in §11, the AU/IN expansion converts a decent domestic niche into something strategically interesting; if they don't, you'll know by December 1.

**Re-scored dimensions (1–10):**
| Dimension | Score | Note |
|---|---|---|
| Pain intensity | 8 | Deadline dread + existential downside, VERIFIED enforcement |
| Frequency | 6 | Annual crunch + continuous attestation layer partially compensates |
| Budget availability | 5 | Real money exists but small; consultants prove WTP |
| Buyer accessibility | 8 | Owner signs, one call, association channels |
| Competitive gap | 8 | Consultants manual, SIS modules shallow, no agentic player visible |
| Technical feasibility | 7 | Extraction/chase/templates proven pattern; churn-monitoring is ongoing tax |
| Regulatory tail-risk | 5 | Politically cyclical; multi-jurisdiction hedge required |
| Scalability | 5 | Service-heavy start; margin flips only at platform stage |
| International optionality | 7 | Engine generalizes (AU/IN), rulebooks don't — by design |
| **Weighted overall** | **~6.5/10** | BUILD-CAREFULLY |

---

## Sources

**Fetched this session:**
- BPPE Annual Reports hub (Aug 1 opening, Dec 1 due date, SPFS per program per location, two-year data window, public archive, verbatim-statement rules): https://www.bppe.ca.gov/annual_report/
- BPPE Disciplinary Actions (monthly lists FY22-23→FY26-27; A–Z case list incl. trucking/beauty/phlebotomy citations, abatements, defaults; page updated Aug 24, 2026): https://www.bppe.ca.gov/enforcement/disciplinary_actions.shtml
- BPPE Enforcement index & Approved Schools directory: https://www.bppe.ca.gov/enforcement/ · https://www.bppe.ca.gov/schools/approved_schools.shtml
- NC-SARA Fast Facts (>2,400 institutions; $2,200–$8,800 fees; data reporting; licensure directory) + homepage (Policy Manual v26.1 effective Jul 1 2026; Workforce Pell statement Jun 2026): https://www.nc-sara.org/fast-facts/ · https://www.nc-sara.org/
- ABHES resources structure (Annual Report + Self-Evaluation Report; adverse/commission actions; events): https://www.abhes.org/members/ · https://www.abhes.org/events/
- Grand Canyon University — ED $37.7M fine (2023), rescinded May 2025; FTC suit dropped Aug 2025: https://en.wikipedia.org/wiki/Grand_Canyon_University
- Registered training organisation — "almost 5,000 RTOs", ASQA/VRQA/TAC split, VQF/AVETMISS, audit types: https://en.wikipedia.org/wiki/Registered_training_organisation

**Carried from prior sessions (VERIFIED there, cited in repo):**
- BloomTech (BPPE $75K fine + cease order; CFPB Apr 2024 orders; DFPI settlement): https://en.wikipedia.org/wiki/Bloom_Institute_of_Technology (other-edu-businesses.md)
- India NAAC CBI bribery case Feb 2025; binary/MERT reform; ~45,000 HEIs / ~8,500 accredited: international.md §8 with primary links
- AU RTO compliance burden, ~3,800–4,000 active, revised standards 2025, open procurement market: international.md §2

**Not established (labeled in text):**
- NACCAS membership counts (site unreachable); FMCSA ELDT provider count (registry 403); ASQA statistics (timeout); Anthology Student module specifics (product page 404); all consultant rate cards (US/AU/IN — none publish pricing; figures are reasoned estimates)
