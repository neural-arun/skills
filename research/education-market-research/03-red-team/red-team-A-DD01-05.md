# Red Team A — DD-01 through DD-05
**Date:** Aug 25, 2026 · **Mandate:** kill the theses, then render honest verdicts (STRONG / WEAKENED / DEAD).
**Method:** adversarial reasoning over `02-deep-dives/DD-01..05` + raw segment files. No thesis survives unscarred; verdicts reflect what remains after the strongest attacks.

**Portfolio-level observation before the per-thesis attacks:** all five deep dives already graded themselves BUILD-CAREFULLY, and each contains its own kill-risk list. The red-team value-add below is (a) escalating kills the dives underweight, (b) testing whether the steelmen actually hold, and (c) naming the conditions that are load-bearing versus decorative.

---

## DD-01 — SPED Casework Copilot

### Attack summary

1. **Incumbent bundling is not a risk — it is the present tense.** PowerSchool Special Programs *already* markets AI-assisted document drafting to 1,200+ districts; Everway (n2y+Texthelp roll-up) owns SpedTrack + Embrace + Polaris with capital, ISO 27001, and a Responsible-AI program; Brisk/MagicSchool give away IEP drafting at $0–$100/teacher/yr. The dive's counter-position ("cross-vendor + chasing loop + provenance") is asserted, never evidenced. Incumbents can copy chasing loops in quarters; a 5-person team cannot build 25-state template coverage in years (their own math: 3–5 engineer-weeks *per state*, plus annual form churn). Worse: the chosen beachhead — mid-size districts on Embrace/SpedTrack/Frontline — is precisely Everway's consolidation territory. "Switching anxiety" cuts both ways: Everway reps will promise roadmap AI to keep those districts, stalling standalone deals.
2. **The ROI math is circular and the budget doesn't cash out.** The $125K–270K/district "value" = caseworker hours × loaded rate. But SPED staffing is service-obligation-bound: IDEA child-find and IEP-mandated services mean workload does *not* shrink with efficiency — saved hours are absorbed into more meetings, more compliance artifacts, never headcount release (union + legal reality). No district converts hours to dollars; the ROI exists only inside the vendor's spreadsheet. Meanwhile price anchors are brutal: MagicSchool at ~$100/teacher/yr sets the psychological ceiling for "AI writing help," post-ESSER austerity caps discretionary lines, and the dive's own WTP kill-test (<50% of directors accepting >$15/SPED-student/yr; ACV settling <$10K) describes a plausible landing zone once bundled-AI objections appear. At board-approval thresholds ($15–35K), the superintendent asks the fatal question: *"why aren't we using the PowerSchool AI we already pay for?"*
3. **Liability asymmetry plus an approval-gate tax that eats the savings.** Every draft must be human-read and human-approved because it is a legally operative document about a child. Reading/red-lining grounded drafts is real time — the gate consumes much of the hour-savings being sold. Residual hallucination risk in IEPs (wrong score, wrong child's goal) is category-freezing if it ever surfaces in a due-process loss; one incident anywhere invites state guidance restricting AI-drafted IEP content. Post-AllHere + post-PowerSchool-breach, districts demand staged pilots, references, and SOC 2 Type II (~15-month runway) — none of which a new shop has — and SPED eval files (psych reports) are the most sensitive records in the district, guaranteeing the longest security reviews for the least-known vendor.
4. **Delivery trap: double-entry death and services gravity.** v1 explicitly avoids incumbent integrations → drafts re-keyed into Embrace/Frontline/state portals → usage collapse (the dive's own falsification test #4). Stage-1 of the "service→product ladder" is per-district consulting at $7.5–15K; hidden HITL cost lives in garbage eval-PDF ingestion QA (faxes, cursive OT notes), per-district goal-bank conventions, and template-pack maintenance — the classic slide from software company to regional consultancy.
5. **Substitution & politics.** Teachers can and do use ChatGPT/MagicSchool free tiers for drafting; co-ops can hire a shared retired-SPED casework clerk for less than one ACV; and the revealed preference of districts for decades is to *tolerate* procedural-noncompliance findings rather than buy tooling. Internal blockers: unionized SPED staff (surveillance/blame fears), district privacy counsel (psych records DPA), superintendent at threshold, incumbent AE quoting roadmap AI.

### What survives
The pain is the best-verified in the program (SPeNSE 5 hrs/wk, 88% interference; hardest-to-staff role). IDEA Part B flow-through is a genuinely ring-fenced budget line, and the micro-purchase fast lane ($7.5–10K p-card pilots under 2 CFR 200.320) is a real, verified mechanism. The chasing/timeline layer and especially the **due-process evidence room** remain unbuilt by incumbents, sell cross-vendor, target a different wallet (superintendent/legal, risk avoidance against $10–50K-per-case legal spend — non-circular value), and survive even if drafting gets bundled free. Tight SPED-director peer networks make one lighthouse regionally contagious. UK EHCP variant has statutory clocks + deficit-funded LAs (small TAM but real mandate).

### Conditions required
- Land ≥3 lighthouse districts within 12 months — before Everway ships GA drafting+chasing.
- Lead with evidence-room/chasing, treat drafting as the free feature; never price on drafting alone.
- Confine to 1–2 states and non-PowerSchool districts until integration depth exists; accept a $10–30M ARR niche ceiling, not venture scale.
- Validate the WTP gate (>$15/SPED-student/yr acceptance) in ≤3 paid pilots before hiring beyond 5 people.
- SOC 2 Type I by month 6 funded from services revenue; keep approval gates as product principle, and budget for the edit-time tax honestly in ROI claims.
- Maintain exit optionality (Everway/PowerSchool acquirer logic) as explicit Plan B.

### VERDICT: **WEAKENED** (confidence 0.65)
Viable only as a race: own the compliance-loop/evidence layer in 1–2 states before incumbent AI bundling compresses the drafting wedge to zero. If the 12-month lighthouse race or the $15/student WTP gate fails, downgrade to DEAD-for-standalone-software.

---

## DD-02 — School Medicaid Billing Capture Agent

### Attack summary

1. **The pricing model is federally radioactive — verified, not hypothetical.** 45 CFR 75.459(a) bars contingent consultant costs from claimed pools; the CMS guide explicitly advises schools against contingency-fee contractors and warns % arrangements raise upcoding/anti-kickback risk; OIG states it is *"intentionally seeking out states to audit where there is a contingency-based contractor relationship."* So the entire self-funding, no-budget-line GTM hook — the thing that makes a CFO move — is the exact audit magnet this market punishes. The engineered hybrid needs per-state counsel and SEA tolerance that currently exists nowhere in writing. Strip the success fee and you have base-only SaaS at $15–60K against brutal multi-state configuration effort: a mediocre, services-heavy business.
2. **The retroactive-capture prize is probably illusory — and dangerous.** OIG's refund taxonomy shows legacy paper logs fail audit standards (TX: 94% of sampled RMTS moments unsupported); sub-audit-grade OCR (70–90% field accuracy on cursive/carbon logs, by the dive's own admission) applied to retroactive claims doesn't recover money, it *manufactures False Claims Act exposure* — the vendor "causes submission" of unsupported claims. That collapses the flagship wedge (thousands of dark districts' decades of paper) down to forward capture only: smaller, slower, adoption-gated.
3. **Pipe and relationship capture.** PCG/MAXIMUS own MMIS trading-partner lanes, SEA relationships, RMTS administration, and audit-survival track records; their revenue scales with administrative effort and they can bundle capture when threatened. States centralizing during the July 2026 compliance scramble (SEA-selected clearinghouses) can simply exclude new vendors. White-label fallback = commoditized upstream componentry sold at software discounts to the very firms you hoped to displace.
4. **Three independent single-memo demand killers, all live trajectories.** (a) CMS reverses or dilutes the May 2023 SBS guide — note the free-care policy has flipped direction before, and administrations change; (b) OBBBA-era Medicaid cuts shrink rolls and state capacity, degrading eligibility-file quality and district bandwidth simultaneously; (c) ED finalizes the NPRM removing the IDEA billing-consent requirement — deleting the consent-ledger module's reason to exist. Add state centralization (kill #3 above) and the policy-fragility surface is the largest in the portfolio.
5. **Adoption politics and buyer psychology.** Forward capture means unionized nurses/therapists doing uncompensated digital logging to generate district revenue — grievance bait outside pilot honeymoon. CFOs are the most audit-literate buyers in the district; after one OIG report read, "% of recovered" smells like NJ/TX. And the "biggest prize" (non-participating small districts) is non-participating for revealed-preference reasons: they never felt the pain enough to staff it. Substitution: hire a part-time biller, join the BOCES/co-op billing service, or do nothing — all cheaper than change management.

### What survives
This is the only thesis whose ROI is denominated in real federal dollars rather than hours-saved (IL +$17.8M year-one, NM/LA/CO/GA/MI verified deltas) — non-circular, CFO-owned, cut-proof (found money survives a 5% budget cut; austerity increases hunger). OIG spent 20 years documenting precisely the failures the product eliminates — the auditor effectively wrote the product spec. July 2026 compliance wall + BSCA grants force SEA action now. The upstream documentation layer is genuinely unsold anywhere. Co-op/ESA channel offers multi-district distribution. Even the fallback (forward-capture QA SaaS attached to existing billers) is a viable small business.

### Conditions required
- Written SEA guidance + outside-counsel memo on vendor fee structures in Illinois BEFORE building pricing; if hybrid-with-exclusion fails legal review in 2 of top-3 states, kill the success component and re-underwrite base-only economics honestly.
- Forward-capture-first product; never promise retroactive OCR magic; every claim element human-certified with provenance trail.
- One state (IL) deep; enter only open-access states; track SPA announcements quarterly.
- Hybrid fees contractually excluded from every claimed cost pool, CPA-lettered, milestone-based rather than volume-based.
- Cash runway sized for 2-quarter claims lag; white-label economics accepted as Plan B without despair.

### VERDICT: **WEAKENED** (confidence 0.70 — strongest thesis of the five)
Real money, auditor-endorsed problem, urgent clock. But the pricing engine it was sold on is federally disfavored, the retroactive prize is largely a liability trap, and policy reversal risk is concentrated. Survives only in the narrower "neutral upstream plumbing, hybrid-priced, one-state-deep" form.

---

## DD-03 — Aid Verification & Appeals Pipeline (CCs first)

### Attack summary

1. **The payer is actively demolishing the workflow, on a stated timetable.** FA-DDX pre-verifies FTI-imported items ("considered verified"); ED's April 2026 real-time fraud screening moves identity checks into the FAFSA itself, explicitly framed as "relieving institutions of the most burdensome aspects"; SSA wage-data matching is the obvious next deletion; the No Aid for Ghost Students Act passed the House to codify centralization. Every award year the addressable population shrinks. The "build for the residue" defense (203/206/212 codes, non-filers, conflicts) targets a shrinking, moving surface with no moat: the moment a residue item is productized, FSA automates it. You are building on land the government is rezoning, with the zoning maps published quarterly.
2. **Buyer poverty and budget fragility.** CC aid offices are the leanest buyers in the portfolio: hourly non-exempt staff, overtime as the coping mechanism, no fat ACVs (dive scores Budget 3/5, Regulatory durability 2–3/5). Pell-heavy CCs face enrollment-driven fiscal crisis; discretionary office tooling freezes first. A 5% institutional cut lands directly on the $18–24K license. ED's own PRA fiction (9.5 min/response) proves the burden is politically invisible — meaning there is no external forcing function to fund relief.
3. **Incumbent endgame is bundling, and fear consolidates TO the incumbent.** Ellucian absorbed StudentVerification with 260+ customers; ERP consolidators bundle verification into six-figure Banner/Colleague renewals at zero marginal price. Post-Anthology-chapter-11, contract-fearful customers consolidate toward Ellucian for safety — the switching window closes from both sides. The dive's own falsification #2 (≥3 losses to "free with our renewal" out of 10 encounters = wedge broken) is a coin-flip outcome.
4. **The services phase is the real business — which tells you the software isn't.** Phase-0 done-for-you processing at $25–40/file funds development and harvests the corpus, but US labor at that price point doesn't scale profitably, and the labeled-corpus "moat" evaporates exactly when FSA deletes the document categories it covers. FTI handling under IRC 6103(l)(13) imposes enterprise-grade safeguarding obligations on a tiny vendor; CC CIOs post-breach will hesitate handing IRS-derived data to a 3-person company, and one security-review cycle can outlast a FAFSA cycle.
5. **Substitution is entrenched and cheap.** Student workers/temp processors at $15–18/hr during peaks; NASFAA Excel trackers; the existing Anthology/Ellucian suite; or simply absorbing the pain — offices have done so forever. Who blocks internally: CIO/security (FTI + GLBA questionnaires), VP finance (budget), the Ellucian AE at renewal time, and federal policymakers by shrinking scope.

### What survives
Verification is statutorily rooted (34 CFR 668 Subpart E — Congress created it; full elimination needs statute, historically unlikely). Fraud shocks put real dollar figures and federal legislation on record, creating genuine urgency budgets. The incumbent is uniquely wounded (Chapter 11 aftermath) — a rare, time-boxed switching window. Flat Slate-style SKUs fit CC card-level purchasing perfectly. Crucially, the **chasing/appeals modules (PJ/SAP, R2T4, multilingual family chase) are independent of verification-population size and arguably grow** as federal automation generates false positives needing human resolution. International-document review and professional-school appeals offer expansion without federal exposure.

### Conditions required
- Company-level strategy: chasing/appeals must carry the P&L; verification parsing treated as a 3–5 year wasting asset to be harvested, not a foundation.
- Quarterly tracking of EA/award-year notices with pre-committed kill trigger (>50% V1-item reduction → stop software investment).
- ≥3 paid $10K pilots in the first cycle or reassess the segment (dive's own test).
- FTI/GLBA compliance posture funded from day one; expect security review to be the long pole.
- Exit or expand (appeals/R2T4/intl docs/state grants) before the verification wedge decays past viability.

### VERDICT: **WEAKENED** (confidence 0.60)
Viable only as a timed harvest race with module diversification away from the federally-shrinking core. If Ellucian bundles aggressively while FSA keeps deleting items, both timers expire together → DEAD.

---

## DD-04 — Stop-Out Re-Enrollment Engine

### Attack summary

1. **Every economic number rests on unmeasured quantities and unaudited vendor claims.** Contactability on 5–10-year-old records is UNKNOWN (NCOA decay compounds 15–20%/yr; email churn worse; consent status ambiguous). Category conversion rates are VENDOR-CLAIMs with undisclosed denominators: NJ engaged 840K residents → 13.5K re-enrolled (~1.6% — mostly inert pool); ReUp's $425M/60K is unaudited; the dive found **zero published control groups in the entire category**. If safe-channel reachability lands <40% (plausible), unit economics fail silently — and everything else was modeled assuming 50–70%. The load-bearing experiment has not been run.
2. **The attribution war is structural, not tactical.** NSC counts ~1M re-enrollments/yr occurring nationally regardless of any vendor — organic walk-ins contaminate every performance invoice, and finance officers know it. Holdout designs need ~3,000/arm cohorts most CCs cannot spare; a partner who refuses a holdout is a walk-away signal, but refusing to buy without one is equally rational. Deal shapes get squeezed between unprovable revshare and uncompetitive platform fees. This is why ReUp sells humans-and-bundles instead of clean performance pricing — the incumbent's opacity is a survival adaptation, not laziness.
3. **Segment mismatch plus incumbent lockups.** Biggest databases (CCs) carry the lowest net tuition ($4–7K) and the thinnest staff absorption — internal SLA losses >30% of yeses (re-melt) get blamed on the vendor. Richest buyers (online/privates) have smaller DBs and running programs. Meanwhile ReUp signed four statewide contracts in ~18 months (NJ/IL/MN/MA) with coach+tech bundles: whole states foreclosed, reference monopoly forming. EAB Navigate360 sits on 850+ campuses shipping AI assistants and can bundle stop-out campaigns into renewals at will. EdSights/Mainstay own the texting channel. The entrant's unique claim — productized reconciliation — is real but narrow.
4. **TCPA tail on aged consents is a general-counsel veto waiting to happen.** Numbers collected 3–15 years ago carry decayed/ambiguous consent; FCC has ruled AI voice in robocalls unlawful without consent; class-action litigators specialize in exactly this fact pattern. Institutional GCs reviewing a proposal to auto-contact decade-old former students will likely restrict to mail + institution-originated email + human-dialed calls → conversion drops → the economics worsen precisely where they were thinnest. One lawsuit poisons the reference chain this GTM lives on.
5. **Data access paradox and delivery drag.** The product requires registrar/bursar exports of decades-old, duplicate-ridden records across SIS/alumni/CRM systems at institutions with the *thinnest* IT governance; identity-resolution yield on 10+-year-old records is unbounded until measured; the dive budgets 30–50% of year-one engineering on data quality — consulting-shaped delivery again. Substitution: run free-ish Slate/Salesforce campaigns (shallow but politically safe), hire ReUp (state-funded, proven), or do nothing — the pool has sat inert for a decade, which evidences both opportunity AND institutional indifference.

### What survives
Demand-side macro is the best-verified in the program: 43.1M SCNC growing 2.2%/yr, WICHE −13% traditional funnel through 2041, state attainment money actively procuring (NJ/IL/MN/MA). NSC's finding that ~1-in-4 SCNC credential earners complete *without re-enrolling* proves paperwork removal alone manufactures outcomes — making the adjacent **reverse-transfer/conferral SKU** real, legally clean, and grant-funded. Demographic cliff converts recovery from virtue project to enrollment plan; VP Enrollment budgets rise under existential pressure. The agency-stage design gets paid while measuring the two unknowns.

### Conditions required
- Run the contactability test on two real cohorts BEFORE building anything; kill threshold <40% single-channel reachable (dive's own test — enforce it).
- Mystery-shop 10 targets: if recent internal campaigns already hit ≥8–10 enrolled/1K, lift thesis dies.
- Never sign pure revshare; hybrid only; payment on census-verified enrollment; pre-contracted holdout methodology.
- Avoid ReUp-lockup states; GC-approved contact protocol (mail/email/human-call backbone, opt-in-only SMS).
- Instrument hours-per-enrolled (<15–20) before stage 2, else pivot to reverse-transfer/DD-05 surfaces.

### VERDICT: **WEAKENED** (confidence 0.55)
Gated on cheap-but-unrun experiments. Pass contactability + incrementality and this becomes the strongest demand story in the portfolio; fail either and it is DEAD outright, not pivoted. Asymmetric bet — size commitments accordingly.

---

## DD-05 — Yield/Melt Completion Orchestrator

### Attack summary

1. **Single-point platform failure with no channel protection.** The entire wedge sits ON TOP of Slate — with NO formal ISV marketplace (partners are consultants only), institution-sponsored API keys Technolutions can throttle or revoke, and a visible native-AI roadmap (Identity Verification, Dashboards, Reader shipped; Rules and Voice coming) from a vendor with a demonstrated habit of building adjacencies in-house (video interviewing, payments). One Summit keynote demoing a completion agent erases the thesis overnight. Even absent Slate-native, EdSights (290+ campuses, managed model, funding) can bolt on document intake in a quarter. Distribution dependence on the company most capable of absorbing your product is the portfolio's sharpest platform risk.
2. **The effect size likely cannot clear proof — and proof is the sale.** Text4College's scaled result was +1.7pp, not significant (null in 3 of 4 states), after Castleman/Page's +7pp in careful hands; melt is substantially affordability, which an execution agent cannot fix; backfill haircut removes 30–50% of gross value; power math (700–800/arm for 3pp detection) exceeds what target classes can spare for holdouts. Net: year-1 sales must close on process metrics alone, in a post-AllHere market that demands outcome evidence from unknown vendors. Selling unverifiable ROI to paranoid buyers is the worst cell in the trust matrix.
3. **Seasonality breaks the business model.** Fourteen weeks of work, nine idle months; renewals must be re-won annually against freshly unprovable results; the always-on conversion hope (≥40%) is unevidenced, and year-round completion walks onto EAB Navigate's home turf against six-figure incumbency. A seasonal SKU priced under bid thresholds wins pilots everywhere and builds ARR nowhere.
4. **Every component is contested by a better-positioned specialist.** Transcripts: NSC/Parchment status checks + DegreeSight OCR (99%-claim incumbent). Immunizations: MedProctor, hundreds of colleges, dedicated budget line. Texting/comms: EdSights/Mainstay with published engagement stats and GSU Pounce heritage. Checklist state: Slate itself owns application checklists and events. The residual unique surface — cross-system checklist truth — depends on gated integrations (StarRez account-gated APIs, health portals, SIS holds) that a 3-person team cannot obtain inside a May–August window. What remains sellable in season one is final-transcript chasing: a feature, not a company.
5. **Substitution is legitimate, cheap, and partially already deployed.** Privates already run melt lists/waitlists (backfill); student caller teams cost $12–15K/summer; EdSights rents the managed-campaign position today with evidence; Slate campaigns + orientation events are owned. And the do-nothing default is historically normal: depositor melt of 8–12% has been tolerated for decades because part of it is affordability theater the school cannot fix anyway. Internal blockers: IT/security (API keys touching minors' data post-breach), health center (immunization data), registrar, and the client's Technolutions CSM whispering "wait for our AI."

### What survives
Cleanest buyer math in the set: one retained student pays for the season twice over; VP Enrollment personally owns the melt number; flat sub-$50K seasonal SKU matches card-level purchasing and the Feb–Apr signing window perfectly. Transcript vertical is genuinely buildable in 6–8 weeks. Managed-service year one generates cash and integration learnings. Acquisition optionality is real (Technolutions, Encoura/RNL, EAB all plausible buyers of a proven melt-execution asset). Grad-program and international variants carry higher net-per-student with denser documents.

### Conditions required
- Sell two consecutive seasons; require ≥40% always-on conversion or consciously run it as a cash-generating feature business with acquisition as the exit — not a venture-scale company.
- Pre-negotiate written client-sponsored Slate key access AND informal Technolutions comfort before signing customers; monitor Slate AI roadmap quarterly with a pre-committed pivot trigger.
- Transcript-vertical depth first; immunization only behind MedProctor-class partnership/OEM framing.
- Pre-registered pilot design with stratified mini-holdouts; code every detected barrier — if >60% affordability and escalations don't convert, kill per the dive's own test.
- Keep customer concentration low and data hygiene pristine: one spam-complaint cluster or TCPA slip kills the campus channel permanently.

### VERDICT: **WEAKENED** (confidence 0.50 — lowest in the portfolio; borderline)
DEAD as a standalone durable SaaS company the day Slate demos a native completion agent or EdSights adds doc intake — both plausible inside 24 months. Alive only as a fast, cash-positive, acquisition-shaped feature business bridging to always-on completion. Do not underwrite venture returns here.

---

## Cross-cutting findings

1. **THE single most important weakness — the procurement fast lane creates a pilot mill, and nobody has evidenced the renewal wall crossing.** All five theses lean on the same crutch: micro-purchase/p-card pilots under 2 CFR 200.320 ($10K, self-certifiable to $50K). That lane reliably produces pilots everywhere and protects nothing at renewal, because conversion to full-price subscription crosses board/procurement thresholds where the killer objection is always available: *"the incumbent we already pay (PowerSchool / Everway / Ellucian / EAB / Slate / EdSights) will bundle this free."* Pilot-to-paid conversion rates are the one number absent from all five deep dives' otherwise rigorous economics — every TAM, ACV, and ARR figure downstream of it is arithmetic on an assumption.
2. **Four of five ROIs are denominated in labor-hours or contested attribution; only DD-02's is real cash — and it carries the heaviest pricing-legality burden.** Hours×rate value never cashes out in unionized, service-obligated institutions (DD-01, DD-03); revshare value is contestable by construction (DD-04, DD-05). The portfolio systematically overrates buyers' ability to convert efficiency into budget.
3. **Synchronized cold-start problem:** every thesis needs a tiny unknown vendor to receive maximally sensitive records (psych reports, IRS-derived FTI, Medicaid beneficiary data, decades-old student records, minors' health docs) immediately after the PowerSchool breach reset trust norms — while SOC 2 Type II takes 12–18 months and HECVAT/DPA cycles add weeks per deal. Year one is compliance theater across the whole portfolio while incumbent and regulatory clocks run.
4. **Regulatory demand-kill vectors point WITH the political wind, not against it:** FSA centralization (DD-03), CMS reversal potential + OBBBA Medicaid cuts (DD-02), state AI-in-legal-documents guidance (DD-01), TCPA/AI-disclosure tightening (DD-04/05). The dives treat these as "monitorable"; monitoring is not hedging, and several vectors have active momentum in the demand-killing direction.
5. **All five service ladders start as consultancies.** Stage 1 of every ladder is humans doing the workflow per customer. That is honest discovery-as-delivery, but it means the true unit economics of the "agent" are unknowable until stage 2 — by which point, in every thesis, an incumbent bundling clock (12–36 months) has nearly expired. The portfolio's implicit bet is that small teams can outrun PE-backed incumbents on feature velocity while manually servicing design partners. History mostly prices that bet against.
