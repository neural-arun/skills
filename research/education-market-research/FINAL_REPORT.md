# GLOBAL EDUCATION MARKET RESEARCH — AI-AGENT OPPORTUNITIES FOR OPERATIONAL WORKFLOWS

**Final report · Aug 25, 2026**
Method: 6 discovery agents (K-12 US, HigherEd US, edu businesses, international, competitive landscape, practitioner voices) → synthesis into a 52-problem scored database → 10 parallel deep dives → 2 red-team agents attempting to kill every finalist. All numbers labeled VERIFIED / ESTIMATE / UNKNOWN; citations live in the appendix files listed at the end.

**Optimization axis (per instructions):** Pain × Economic Value × Agentic Automation Potential × Buyer Willingness to Pay × Accessibility × Defensibility × Scalability. Ideas were actively attacked, not sold.

---

## PART 1 — EXECUTIVE SUMMARY

The single structural finding: **education runs on regulated document pipelines between humans, agencies, and legacy systems that nobody owns end-to-end.** Installed software (SIS/ERP/CRM) is systems-of-record; it deliberately stops at the human handoff. The recurring agentic loop — *acquire messy documents → extract → check against rulebook → assemble outputs → chase humans for missing inputs → log for compliance* — appears in every segment and is exactly what modern LLM agents make possible and what pre-LLM vendors could not deliver.

**The 15 strongest opportunities discovered** (grouped; details in Parts 4–9 and appendices):

| # | Opportunity | Segment | Why it makes the list |
|---|---|---|---|
| 1 | School Medicaid billing capture agent | K-12 US | Only opportunity that *creates* revenue (self-funding); CFO buyer; OIG effectively wrote the spec; CMS expansion deadline ~Jul 2026 |
| 2 | Transfer-credit & transcript intelligence | HigherEd US (+intl eval) | GAO-verified 43% credit loss; team-of-4-processing-4,000 evidence; one tech core, three buyers |
| 3 | Certification-body adjudication ops | Edu businesses | No fatal flaw found under attack; weeks-long sales cycles; handbook-rulebook-over-documents is pure RAG/OCR |
| 4 | SPED casework copilot (IEP drafting/timelines/evidence) | K-12 US → UK EHCP | Largest verified time sink (5 hrs/wk, 88% interference [V]); loudest practitioner pain; universal analogue problem |
| 5 | Career-college regulatory filing factory | Edu businesses (US→AU→IN) | Owner signs in one call; existential enforcement risk; enumerable deadlines |
| 6 | Financial-aid verification & appeals pipeline | HigherEd US (CC first) | Biggest verified volume (2.35M files/yr [V]); wounded incumbent (Anthology restructuring) |
| 7 | International-student visa-file factory | Global biz | Verified hook: 47% of Canadian refusals are money-paperwork [V]; dated forcing functions (IRCC Jul 2026, UK sponsor duties) |
| 8 | Chronic-absenteeism documentation engine | K-12 US | New 2024–26 statutes convert absence into mandated document production; nudge incumbents don't do documents |
| 9 | Stop-out re-enrollment engine | HigherEd US | 43.1M-person verified pool; pure revenue lever — *conditional on passing a cheap contactability test* |
| 10 | Yield/melt completion orchestrator | HigherEd US | Cleanest ROI math ($500K+/pp) but thinnest moat — cash-business shape, not durable SaaS |
| 11 | Primary-source document chase network (credential eval) | Global health workforce | TruMerit 14-week delay [V] — chase-loops, not decisions, are the bottleneck |
| 12 | Compliance rulebook engine (multi-region) | AU RTO / IN NAAC / UK | Same engine, local rulebooks; NAAC scandal creates "provably untainted" positioning |
| 13 | District grant management + CRDC assembly | K-12 US | Dec 2026 CRDC cycle = dated forcing function; post-ESSER staff cuts |
| 14 | Tutoring-vendor district-contract ops | Edu businesses | NSSA-mandated artifacts [V]; ESSER cliff makes admin efficiency existential for vendors |
| 15 | Credential-verification phone-ops automation | Cert bodies | ~100% deterministic lookup-and-respond loop; monetized friction today |

**Honest bottom line:** after red-teaming, *no* finalist survived as a clean "build it and they pay" story. Every window is a **12–18-month race against incumbent bundling**, and the pilot→paid conversion rate is the untested assumption underneath every TAM figure. The realistic play is 2–3 opportunities run simultaneously through cheap falsification tests (each <$10K and <6 weeks), then concentrate. The recommended shortlist for that testing: **#1, #2/#11 (same core), #3, #5** — they combine non-circular ROI, private/fast buyers, and survivable niches.

---

## PART 2 — EDUCATION PAIN MAP

Full map with anchors: `01-pain-map-and-database/opportunity-database.md` (Part A). Condensed:

- **K-12:** special-ed paperwork (EXTREME, federally anchored), attendance/intervention loops, compliance reporting crunches, HR/staffing drudgery (subs, screening, licenses), back-office AP/enrollment/records, multilingual comms obligation.
- **Higher ed:** financial-aid verification & appeals, transcript/transfer processing, melt & stop-out revenue leaks, early-alert execution failure, registrar exceptions, accreditation/reporting assembly, SEVIS & VA compliance step-changes (both dated 2026).
- **Education businesses:** certification adjudication & CE audits, study-abroad application factories & visa files, tutoring district-contract ops, career-college filing stacks, test-prep scoring/localization.
- **International:** UK SEND/EHCP statutory crisis (46% timeliness [V]), AU RTO audit packs, Canada post-cap retention desperation, EU Erasmus+/AI Act dynamics, India post-scandal NAAC rebuild, Gulf private-school ops.
- **Practitioner voice layer:** loudest verified themes = SPED evenings/weekends, aid-verification document purgatory, transcript backlogs, early-alert theater ("case closed"), parent-contact chasing. Weak/absent voices flagged honestly (accreditation panic, front-office chaos) rather than force-fit.

---

## PART 3 — OPPORTUNITY DATABASE

52 problems, each with customer, economic buyer, current workflow, existing solutions, agent-level rating, estimated value, competition, accessibility, risks, and 14-dimension scores:

→ `01-pain-map-and-database/opportunity-database.md` (Part B)

Top scores: O02 Medicaid (116), O04 absenteeism (115), O22 stop-outs (114), O31 cert adjudication (115), O21 melt (112), O19 admissions transcripts (111), O15 aid verification (108), O39 visa-files (105), O32 doc-chase (102), O38 app factory (102), O46 UK EHCP (102), O01 IEP (113 pre-red-team discount).

*Note:* raw Σ scores overrate opportunities where incumbents are 1–2 releases away; red-team-adjusted rankings above supersede arithmetic.

---

## PART 4 — TOP 10 DEEP DIVES

Full files in `02-deep-dives/`. One-line status each:

| DD | File | Verdict (deep dive) | Red-team verdict | Survival condition |
|---|---|---|---|---|
| 01 | sped-casework.md | BUILD-CAREFULLY | WEAKENED 0.65 | Win the evidence/chasing layer in 1–2 states within ~12 months before suite bundling compresses drafting to $0 |
| 02 | medicaid-billing.md | BUILD-CAREFULLY | WEAKENED 0.70 (**strongest overall**) | Neutral upstream plumbing only; hybrid pricing with counsel sign-off (pure contingency is federally radioactive); one state deep (Illinois) |
| 03 | aid-verification.md | BUILD-CAREFULLY | WEAKENED 0.60 | Timed harvest while statutory residue exists; appeals/PJ module carries the long-term P&L |
| 04 | stopout-reengagement.md | BUILD-CAREFULLY | WEAKENED 0.55 | Pass a cheap contactability + contractual-holdout test before building anything substantial |
| 05 | yield-melt.md | BUILD-CAREFULLY | WEAKENED 0.50 | Run as seasonal cash business; exit/acquire shape; do not build durable-SaaS hopes on it unless Slate stalls |
| 06 | transcript-intelligence.md | BUILD-CAREFULLY | WEAKENED 0.75 (**strongest of B**) | Fast-follower niche: semantic syllabus reasoning + JST/intl formats + TES-less CCs, on a 12–18-month clock |
| 07 | absenteeism.md | BUILD-CAREFULLY | WEAKENED 0.70 | Document-engine-only add-on, one statute-deep (Iowa-class), pre-registered attribution |
| 08 | cert-adjudication.md | BUILD-CAREFULLY | WEAKENED 0.60, no fatal flaw | Prove ≤2-week config productization on 3 bodies; accept bootstrap-sized SAM (~$30–65M, realistically half that) |
| 09 | visafile-factory.md | BUILD-CAREFULLY | WEAKENED 0.65 | Sell institution-side compliance; use agencies as design partners, not the market |
| 10 | filing-factory.md | BUILD-CAREFULLY | WEAKENED 0.70 | Boutique cash business with insider DNA in one vertical; venture framing is dead |

---

## PART 5 — THE 5 "UGLY BUT VALUABLE" PROBLEMS

1. **School Medicaid time-study & documentation capture (O02/DD-02)** — paper therapy logs, consent tracking, RMTS chasing. Nobody's dream job; $100–800K/district of silent federal loss. The ugliest self-funding sale in the study.
2. **District AP with grant/fund coding (O13)** — 15–40K invoices/yr keyed by hand, miscoded grants become disallowances. CFO-aligned, well-understood ROI, horizontal-tool gap on fund accounting.
3. **Grant expenditure documentation + CRDC assembly (O11/O28)** — "every penny needs paper"; biennial cross-system reconciliation nobody owns; federal enforcement tail. Dec 2026 opening = calendar-driven demand.
4. **Tutoring-vendor contract ops: attendance→invoice→progress reports (O40)** — disputed-invoice leakage 2–5% of contract value; vendors drowning post-ESSER; deterministic pipeline.
5. **Credential-verification phone/email operations (O36)** — clerks answering employer calls at $5–15/call fully loaded; ~fully deterministic; upsellable API product.

*(Honorable mention: K-12 license/PD-hour tracking O09 — small but pure expiry-monitoring automation.)*

---

## PART 6 — THE 5 HIGHEST-UPSIDE OPPORTUNITIES

1. **SPED operations platform displacement (DD-01 + O03 + O46)** — if agentic casework lands before bundling closes the window, this displaces aging forms suites (Frontline/Embrace/EasyIEP) across ~90K US schools with a UK EHCP sequel. Largest defensible prize in the study.
2. **Transcript-intelligence rails (DD-06 + O32)** — one parsing/equivalency/chase core serving admissions, registrars, evaluators, and agencies globally; infrastructure position analogous to what Clearinghouse did for exchange, but for *understanding*.
3. **Multi-region compliance rulebook engine (DD-10 family)** — same engine, configurable rulebooks: BPPE/NACCAS/SARA today, AU RTO audits and India's rebuilt NAAC process next; NAAC scandal enables "provably untainted" positioning at national scale.
4. **Adult re-engagement network (DD-04, conditional)** — if contactability holds out, a performance-priced re-enrollment engine across CCs + states in attainment-funded programs compounds into category ownership (43.1M pool grows 2.1M/yr).
5. **Institution-side international-student compliance suite (DD-09 pivot + O26)** — visa caps/sponsor-duty regimes made retention compliance existential in CA/AU/UK simultaneously; seven-figure math per approval point.

---

## PART 7 — THE 5 FASTEST-TO-REVENUE OPPORTUNITIES

1. **Certification-body adjudication (DD-08)** — private buyers, committees of zero, $10K flat pilots, weeks-long cycles; ICE-channel distribution.
2. **Career-college filing factory (DD-10)** — owner-operator signs in one call; price under the consultant quote ($6–25K/campus/yr); fear sells immediately around BPPE Dec 1.
3. **Agency visa-file QA (DD-09)** — WhatsApp-delivered managed service at $49–149/file or $99–249/mo seats; founder-signed; ICEF conferences as channel.
4. **Medicaid capture in one expanded state (DD-02)** — Illinois-class districts; base subscription paid from new receipts; CFO sees money appear inside one quarter.
5. **CC financial-aid verification pilots (DD-03)** — p-card $10K spring-term pilots converting at July 1 fiscal year; acute fraud + FAFSA-surge memory still fresh.

---

## PART 8 — SERVICE → PRODUCT OPPORTUNITIES

The study strongly validates starting as a service in four cases — because the service *builds the proprietary data asset* (document corpora, rulebooks, accuracy baselines) that becomes the moat:

| Opportunity | Service first (months 0–6) | Productized service (6–18) | SaaS/platform (18+) |
|---|---|---|---|
| DD-10 filings | Done-for-you BPPE cycle for 3 schools | Retainer per campus, template library per vertical | Continuous-compliance ledger + multi-jurisdiction rulebook engine (AU/IN) |
| DD-02 Medicaid | Capture+QA for 2 IL districts, measured recovery | Hybrid base+% contracts via co-op channel | Multi-state eligibility/note/RMTS platform |
| DD-08 certs | Managed review overflow for 2 allied-health boards | Per-file pricing + config playbook per vertical | Handbook-config engine + audit-trail exports (switching wedge) |
| DD-09 visas | Managed application/visa-file prep per file | Seats + per-file overage for agencies | Institution-side refusal-risk API + compliance pack |
| DD-01 SPED | IEP-writing-as-a-service pilot in 1 district (union-safe framing) | Drafting + timeline module per SPED student/mo | Casework platform + due-process evidence room + UK EHCP variant |

Warning from red team: the service ladder consumes engineering time — budget ≥50% engineering capacity throughout, or the 12–18-month windows close while you consult.

---

## PART 9 — FINAL RANKING (#1–#10)

### #1 — School Medicaid billing capture agent (K-12)
- **Why this problem?** Silent federal revenue loss from upstream documentation failure; OIG's 33 audits found ~$1.18B in recommended refunds driven mostly by documentation gaps — the exact layer this system owns.
- **Why now?** CMS free-care reversal, 28 states expanded, ~Jul 2026 compliance deadline, BSCA grants; districts post-ESSER need found money, not budgets.
- **Why AI agents?** Note-structuring, consent/eligibility matching, RMTS chasing, claim QA, remittance reconciliation = trigger→action→verification loops humans can't staff.
- **Why would someone pay?** Non-circular ROI: recovered dollars exceed fees visibly; CFO buyer.
- **Why isn't it solved?** Incumbents (PCG/MAXIMUS/co-ops) monetize downstream claims, not upstream capture; upstream was pen-and-paper until OCR/LLMs matured.
- **Who first?** Illinois mid-size districts (verified +$17.8M yr-1 state drawdown delta), via co-op/ESA channel.
- **First version?** Single-state: provider-note structuring + consent tracker + eligibility matcher + claim-QA checklist; human-certified submission.
- **Charge?** $15–60K/yr base + capped success fee on net-new receipts, excluded from claimed cost pools with CPA letter (45 CFR 75.459 workaround designed with counsel).
- **Build difficulty?** Medium-high: HIPAA+FERPA, BAAs, handwritten-note OCR limits, one-state focus mandatory.
- **Sell difficulty?** Low-medium: self-funding pitch, but procurement rules and incumbent relationships slow expansion beyond state one.
- **Large company potential?** Moderate — national plumbing position if multi-state succeeds; otherwise solid $3–10M ARR business.
- **International?** No (US-specific), but pattern transfers conceptually to other claimable-revenue niches.
- **Biggest failure mode?** Regulatory reversal (CMS/OBBBA-style policy shift) or accidental FCA exposure from retroactive claims — hence counsel-signed design and forward-looking capture only.

### #2 — Transfer-credit & transcript intelligence (HigherEd)
- **Why?** GAO-verified 43% credit loss; registrar teams of 4 processing 4,000 admits; students vote with feet on articulation speed.
- **Why now?** LLM parsing finally handles format long-tail; state articulation policy tailwinds; incumbents monetize document movement, not understanding.
- **Why agents?** Parse→match→recommend equivalency→route to faculty→track sign-off→post is a complete agentic workflow.
- **Pay?** Enrollment + provost budgets; 5–9× ROI stories; $199–340/document WTP already proven at evaluators [V].
- **Not solved?** Exchange networks (Parchment/Clearinghouse) move PDFs; DegreeSight proved demand but leaves semantic reasoning/JST/intl/TES-less niches open — a fast-follower window, honestly stated.
- **First buyer?** CC/regional-public transfer-heavy offices without TES maturity.
- **v1?** Equivalency-recommendation engine + faculty-review routing on parsed input; metered parsing.
- **Charge?** $15–25K creditable pilot → $45–75K/yr; $0.75–1.50/transcript metered.
- **Build?** High accuracy bar; catalog rot = ongoing ops, not launch-and-done.
- **Sell?** Medium; academic-authority concerns require human-final-word design.
- **Large company?** Yes — infrastructure rails position.
- **Intl?** Yes — credential evaluation (TruMerit 14-week chase) is the same core.
- **Failure mode?** DegreeSight executes well + Parchment ships native AI within 24 months → window shuts; also sub-95% parse accuracy kills trust instantly.

### #3 — Certification-body adjudication ops (Edu businesses)
- **Why?** Entire adjudication functions of 3 people running exams+CE+appeals+NCCA compliance simultaneously [V job postings]; handbooks are perfect RAG substrates; documents are OCR fodder.
- **Why now?** NCCA AI guidance + ATP human-oversight norms legitimize agent-prepares/human-signs designs; healthcare analogues (Medallion etc.) prove the playbook without having crossed over.
- **Why agents?** Intake completeness → rule-adjudication → exception packets → decision letters → audit trails is the canonical loop.
- **Pay?** Funded from exam-fee revenue; $150–400K/yr labor at stake per body [E].
- **Not solved?** AMS incumbents (Personify/Nimble) have zero adjudication AI; per-body variance kept consultants busy instead.
- **First buyer?** Mid-size allied-health specialty boards (70% of 304 NCCA programs are healthcare).
- **v1?** CE/recertification verification + audit-packet prep (lower legal stakes than eligibility denials), then eligibility module.
- **Charge?** $14–20K/yr + $3/file overage; $10K pilot.
- **Build?** Medium; config-productization ≤2 weeks per body is the make-or-break gate — test on 3 bodies before scaling.
- **Sell?** Easiest in study: private buyers, weeks not years.
- **Large company?** Modest ceiling (~$30–65M SAM, realistically less); excellent bootstrap economics, not a VC rocket.
- **Intl?** Partially (ISO 17024 markets share shape).
- **Failure mode?** Config treadmill + denial-accuracy liability cap autonomy; wallet concentration in top ~150 bodies.

### #4 — SPED casework copilot (K-12 → UK)
- **Why?** Loudest verified pain in education: 5 hrs/wk paperwork, 88% interference [V], extreme attrition language, hardest-to-staff role.
- **Why now?** LLMs make artifact-grounded drafting possible; suites haven't shipped it well; UK EHCP crisis (46% timeliness [V]) is a ready-made second market.
- **Why agents?** Timeline triggers → artifact gathering → draft → human approval → chase signatures → progress monitoring → due-process evidence room.
- **Pay?** IDEA flow-through budgets; districts already pay (splitting roles to prevent quitting [V-practitioner]); $125–270K/district addressable [E].
- **Not solved?** Incumbents are form-fillers; PowerSchool AI drafting is assistant-grade inside its own silo; Everway consolidation is the threat clock.
- **First buyer?** Suburban/exurban 3–8K districts on Embrace/SpedTrack/Frontline; timeline-battered SPED director champion; CMOs fastest.
- **v1?** Eval-PDF → present-levels extraction + goal-draft assist + timeline/chasing layer (own the evidence layer, not the form).
- **Charge?** $7.5–10K card-bought pilot → $2–3/SPED-student/mo ($15–35K ACV).
- **Build?** State-form variation + hallucination liability in legal documents + no write-back into systems of record = hard mode.
- **Sell?** Union sensitivity requires copilot-not-replacement framing; free teacher tools anchor WTP low.
- **Large company?** Yes if platform displacement lands; UK expansion doubles it.
- **Intl?** Yes — EHCP variant is nearly the same product.
- **Failure mode?** Bundling: "free AI in your existing suite" compresses ACV toward zero within ~18 months; 12-month race.

### #5 — Career-college regulatory filing factory (US → AU → IN)
- **Why?** Enumerable deadlines (BPPE Aug 1/Dec 1, accreditors, SARA), existential consequences (BloomTech fined/ceased [V]), owner-operator buyers, consultants charging $5–25K/cycle.
- **Why now?** Enforcement mills active; small-school economics never justified software until agents collapsed cost-to-serve.
- **Why agents?** Extract→reconcile→generate→attestation-chase→submit-ready packages; placement-definition judgment stays human-signed.
- **Pay?** Fear pays: retainer priced just under consultants.
- **Not solved?** Consultants are relationship-embedded but don't scale; SIS modules don't reason across jurisdictions.
- **First buyer?** CA beauty/allied-health single-campus schools; trucking #2; bootcamps as high-fear lighthouse accounts.
- **v1?** One full BPPE cycle done-for-you, then continuous ledger.
- **Charge?** $6K/$12K/$25–40K tiers per campus/yr.
- **Build?** Medium-low technically; jurisdiction churn = permanent ops tax.
- **Sell?** One call closes owners; associations/accreditor conferences as channels.
- **Large company?** No — boutique ($150–250M TAM thesis-assuming; realistic domestic $25–60M). Cash-flow excellent, venture-scale no.
- **Intl?** Yes — AU RTO and IN NAAC are the same product family (sequencing matters).
- **Failure mode?** Enforcement is politically cyclical (GCU fine rescinded); grind-it-out service-heavy growth burns small teams.

### #6 — Financial-aid verification & appeals pipeline (HigherEd, CC-first)
- **Why?** Statutorily mandated document workflow, 2.35M files/371K hrs federal estimate [V] before institutional overhead; ghost-student fraud shock opened wallets ($30M CCC losses since 2024).
- **Why now?** Anthology Chapter-11 split sent Student Verification to Ellucian mid-restructuring; CCs desperate.
- **Why agents?** Doc-request personalization → intake/OCR → field comparison → correction drafts → family chasing sequences → appeal case assembly.
- **Pay?** CC ACVs thin ($18–24K) but p-card pilots unlock instantly; regional publics $32–48K.
- **Not solved?** Requirement engines are rules, not resolution; nobody owns chase-and-resolve end-to-end.
- **First buyer?** 8–12K-student single-campus CC aid director, V4/V5-swamped, p-card authority.
- **v1?** Verification intake+matching+chasing for V1 groups; appeals module next.
- **Charge?** $10K one-term pilot → $18–24K CC license (+$6–10K appeals).
- **Build?** IRS-transcript parsing + FTI compliance architecture genuinely hard; <95% accuracy kills trust.
- **Sell?** Fast at CCs; policy headwinds later.
- **Large company?** Limited — FA-DDX and real-time fraud screening are deleting verification items on a published timetable; this is a **timed harvest** where appeals/PJ carry the long-term P&L.
- **Intl?** No (Title IV-specific).
- **Failure mode?** The payer (FSA) shrinking the workload faster than you land renewals; Ellucian bundling into SIS deals.

### #7 — Institution-side international-student compliance (global)
- **Why?** Visa-cap/sponsor-duty regimes hit CA/AU/UK simultaneously; 47%-of-refusals-are-money-paperwork hook [V]; institutions lose C$2M tuition per approval point [E].
- **Why now?** IRCC Jul-2026 source-of-funds scrutiny; UK BCA <5% refusal thresholds; AU MD111 prioritisation — compliance-mode retention spend rises when visas tighten (counter-cyclical).
- **Why agents?** Cross-document consistency reasoning (bank statements ↔ sponsor letters ↔ income claims) over messy multilingual scans.
- **Pay?** Institutions pay existential-grade prices; agencies pay little (thin margins, free-tool culture — treat them as design partners/channel, not the market).
- **Not solved?** Marketplaces (Adventus APS) built services, not sellable products; checklists + senior eyeballs elsewhere.
- **First buyer?** Canadian college intl office or UK provider near sponsor thresholds; agency pilots fund learning.
- **v1?** Refusal-risk report + supplementary-doc chase for financial documentation only.
- **Charge?** $30–60K/yr institutional; agency seats $99–249/mo.
- **Build?** Country-document variance huge; immigration-advice licensing walls (RCIC/OISC/OMARA) require strict decision-support framing — get written opinions before selling advice-adjacent features.
- **Sell?** Institutional cycles moderate; agency cycles days.
- **Large company?** Yes if positioned as global student-compliance infrastructure across destination countries.
- **Intl?** By construction.
- **Failure mode?** Visa-policy reversal (demand spike evaporates) or marketplace absorption; licensing misstep.

### #8 — Chronic-absenteeism documentation engine (K-12)
- **Why?** 2024–26 statutes (IA SF2435 ladder, VT document-before-court, MS attendance officers) turned absence into mandated document production — the unautomated layer.
- **Why now?** Statutes fresh; EDL's public price sheet ($5–9.75/student) commoditized messaging and priced your wedge for you.
- **Why agents?** Root-cause investigation + plan-document assembly + escalation packs ≠ broadcast nudges.
- **Pay?** ADA-linked funding in presence-funded states; superintendent accountability motive.
- **Not solved?** Comms tools broadcast; SchoolStatus just entered the first mile (reason capture) — narrow but real gap behind it.
- **First buyer?** Iowa district, 8–30K students, >20% chronic absence, not yet on EDL/SchoolStatus.
- **v1?** Statutory-pack generator + intervention-log completeness for ONE state.
- **Charge?** $6–9/student/yr with $30K floor; +$8–15K compliance pack.
- **Build?** Medium; SIS-API variance is the tax.
- **Sell?** Medium; attribution contested field-wide (measurement chaos [V]).
- **Large company?** Moderate; crowded adjacency.
- **Intl?** Yes (NZ/AU attendance crises).
- **Failure mode?** SchoolStatus Forms&Flows reaches statutory packs first; poverty-driven root causes limit software impact.

### #9 — Stop-out re-enrollment engine (conditional)
- **Why?** Best macro-demand evidence anywhere: 43.1M pool, +2.1M/yr, NSC shows paperwork removal alone completes degrees [V]; demographic cliff peak pressure.
- **Why now?** States funding re-engagement (NJ/IL/MN/MA); enrollment VPs desperate for non-traditional funnels.
- **Why agents?** Database mining → gap computation from old transcripts → hold triage → personalized sequencing → readmit paperwork completion.
- **Pay?** Performance-aligned: $30–60K base + $400–700/verified enrollee.
- **Not solved?** ReUp scaled with human coaches + locked four states; nobody automated the reconciliation layer.
- **First buyer?** CC/district with 40K+ stop-out records adjacent to ReUp's footprint gaps.
- **v1?** Contactability audit + gap-report generation for a 5K-record slice — **before building anything else**.
- **Charge?** Hybrid as above with contractual holdout cohort.
- **Build?** Legacy-data wrangling brutal; TCPA exposure on aged consents can silently break unit economics.
- **Sell?** VP Enrollment signs when shown money; attribution fights loom (~1M organic re-enrollments/yr muddies proof).
- **Large company?** Yes if contactability proves out — network effects across institutions sharing stopped-out pools.
- **Intl?** Partially (adult-learner re-engagement is universal).
- **Failure mode?** Contactability collapse → DEAD, not pivoted. Run the cheap test first.

### #10 — Yield/melt completion orchestrator (cash business, not SaaS bet)
- **Why?** Cleanest ROI math in study (1 saved depositor ≈ 2× annual price); deterministic checklist work; VP owns the number personally.
- **Why now?** Post-FAFSA-fiasco melt anxiety; demographic cliff raises stakes per depositor.
- **Why agents?** Per-student checklist orchestration + immunization-doc OCR validation + multilingual chasing.
- **Pay?** Flat $24–48K seasonal SKUs fit card/dept purchasing; Feb–Apr buying window.
- **Not solved?** EdSights/Mainstay sell messaging; MedProctor one vertical; nobody closes loops — but this sits on Slate with no ISV channel while Slate AI marches toward it.
- **First buyer?** Midwest/Northeast private comprehensive, $28–38K net, 800–1,800 deposits, melt >10%, Pell ≥30%.
- **v1?** Final-transcripts + immunizations verticals only, May–Aug.
- **Charge?** $36K seasonal median → $60–90K always-on year 2 if retained.
- **Build?** Low-medium — the easiest build in the top 10.
- **Sell?** Fast, seasonal, demo-able.
- **Large company?** No — seasonality breaks ARR; Text4College-scale null effects suggest melt is partly affordability, which software cannot fix; effect provably unprovable in season one without pre-registered controls.
- **Intl?** Mildly (yield ops universal).
- **Failure mode?** Slate ships execution natively within ~24 months → standalone thesis dies; treat as acquisition-shaped cash flow.

---

## CROSS-CUTTING STRATEGIC CONCLUSIONS

1. **The pilot→paid cliff is the whole game.** Micro-purchase lanes produce pilots everywhere and protect nothing at renewal, because renewal crosses board thresholds where "your incumbent will bundle this free" always wins. Design conversion mechanics (data lock-in via accumulated ledgers/corpora, multi-workflow stickiness) *into v1*, not later.
2. **All windows are 12–18 months.** In four of ten finalists, incumbents are 1–2 releases away (PowerSchool/Everway in SPED, DegreeSight+Parchment in transcripts, SchoolStatus in attendance, Slate in melt). Services-first funding must not consume the engineering runway that wins these races.
3. **Prefer non-circular ROI.** Opportunities where money measurably appears (Medicaid recoveries, retained tuition) survive budget cuts and skeptical boards better than hours×rate math that never cashes out in unionized institutions.
4. **Private buyers beat institutional buyers for a 1–5 person company.** Cert bodies, agencies, career colleges, and tutoring vendors pay in weeks. Institutions are worth entering only where a dated forcing function (BPPE Dec 1, IRCC Jul 2026, CRDC Dec 2026, CMS Jul 2026) does the selling.
5. **Recommended immediate action (next 90 days):** run three <$10K falsification tests in parallel — (a) Illinois Medicaid capture pilot with one district, counsel-reviewed contract; (b) cert-body CE-audit config gate with two allied-health boards; (c) stop-out contactability audit on one 5K-record slice. Concentrate on whatever passes; kill the rest without sentiment.

---

## APPENDIX — EVIDENCE BASE

| File | Contents |
|---|---|
| `00-raw-segment-research/k12-us.md` | 14 K-12 problems, NCES/CMS/OIG/HSPF citations |
| `00-raw-segment-research/higher-ed-us.md` | 16 HE problems, Federal Register/GAO/NSC/VA/ICE citations |
| `00-raw-segment-research/other-edu-businesses.md` | 15 business problems, BPPE/BloomTech/TruMerit/Adventus citations |
| `00-raw-segment-research/international.md` | 7 regions + global classification matrix, DfE EHCP/NAAC-CBI citations |
| `00-raw-segment-research/competitive-landscape.md` | Incumbent map, startup funding, procurement law (2 CFR 200.320), cautionary tales (AllHere, PowerSchool) |
| `00-raw-segment-research/practitioner-voices.md` | 50+ linked threads, hotspot scorecard, willingness-to-pay signals |
| `01-pain-map-and-database/opportunity-database.md` | Pain map + 52-problem scored database + finalist selection rationale |
| `02-deep-dives/*.md` | Ten 12-section deep dives with kill risks and pricing |
| `03-red-team/*.md` | Attack summaries, survival conditions, verdicts per finalist |
