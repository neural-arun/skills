# DD-06: Transcript & Transfer-Credit Intelligence

**Research date:** Aug 25, 2026. **Method:** direct fetches of primary sources (Parchment, National Student Clearinghouse, WES, ECE, DegreeSight, TCCNS, California CCC system sites, Wikipedia/Instructure) building on raw-segment files (higher-ed-us.md P5/P6; other-edu-businesses.md P2; competitive-landscape.md §1.4). Search engines and several vendor/govt sites (CollegeSource, GAO search, DANTES, Florida SCNS, Ohio DOE) blocked bots this session — those items are labeled REPORTED/UNKNOWN. Labeling follows project convention: **VERIFIED** = fetched with URL cited; **ESTIMATE** = reasoned from verified anchors + domain knowledge; **UNKNOWN** = not defensibly sourced; **REPORTED** = widely known, not re-verified this session.

**Opportunity:** one document-intelligence core serving three buyers — (a) admissions transcript parsing/keying, (b) registrar transfer-equivalency recommendation with faculty-review routing, (c) credential-evaluator primary-source chase + validation.

---

## 1. Problem & scope (which wedge first)

The three wedges share one technical core (messy document → structured course data → matched decision) but have different buyers, incumbents, and risk profiles:

| | (a) Admissions parse/key | (b) Transfer-equivalency engine | (c) Evaluator doc-chase |
|---|---|---|---|
| Buyer | VP Enrollment / admissions ops | Registrar + Academic Affairs jointly | COO of eval agency / staffing firm |
| Incumbent pressure | HIGH: Parchment Receive/Data Automation + Clearinghouse exchange already own the pipe; DegreeSight DocSight sells "99% OCR" | MEDIUM: TES is a content library + tracker, not a recommender; DegreeSight InBound touches prospect-facing only | LOW: human services (TruMerit/WES/ECE), no software |
| Economic story | Labor hours ($100–250K/institution ESTIMATE) | Retention revenue + labor (~$400K+/institution ESTIMATE) | Throughput/WIP release (VERIFIED 14-week pain anchor) |
| Liability | Low (admission reading stays human) | Medium-high (credit posting affects degree audits, aid) | Medium (fraud/authenticity calls) |

**Recommendation: enter with wedge (b) — the transfer-equivalency recommendation engine with faculty-review routing — bundling wedge-(a) parsing as its input layer.** Reasons:
1. It attacks the largest verified value pool: 35% of students transfer and lose an average **43% of credits** ([GAO-17-574](https://www.gao.gov/products/gao-17-574), VERIFIED in prior session); credits not awarded are either lost tuition or an extra billed term — a revenue story, not a cost story (Enrollment money moves faster than compliance money; see higher-ed-us.md cross-cutting obs. 1).
2. The incumbent content layer (TES) is a *library*, not a *worker*: it stores equivalencies and routes evaluations, but the recommendation reasoning ("does this 2019 syllabus equal our BIO 201?") remains human eyeballs on email. Building ON TES data rather than against it fits the ecosystem strategy.
3. Wedge (a) alone is crowded faster than assumed: Parchment sells "Receive" and "Data Automation" into its network ([parchment.com nav](https://www.parchment.com/), VERIFIED) and DegreeSight markets DocSight Transcript OCR at claimed 99% accuracy to 100+ institutions ([degreesight.com](https://degreesight.com/), VERIFIED as vendor claims). Parsing-only positioning has a shrinking moat.
4. Wedge (c) is real but small-TAM and fraud-liability-heavy for a first product; keep it as expansion (§10).

Fallback: if TES integration access proves closed within 90 days (see kill risks), pivot wedge (b) delivery to institutions *without* TES (many CCs run SIS-native tables) and lead with wedge (a) batch backfill services for stop-out campaigns (ties to P8 in higher-ed-us.md).

## 2. Workflow today + failure modes across all three buyers

**(a) Admissions intake (P5):** applicant/self-upload/mail transcript (PDF, image, sealed paper, Parchment/Clearinghouse e-file if sender is on-network) → clerk keys courses/grades into SIS or Slate reader view → GPA recalc → test scores matched → chase missing docs until file completes. International files exit the wall entirely: applicant buys a NACES evaluation ($110–$340 all-in, see §4) adding weeks.
*Failure modes:* long-tail formats defeat fixed parsers (20K+ US HS schedules + global formats — higher-ed-us.md); self-reported grades unverified; mis-keys corrupt merit awards and placement downstream; incomplete files melt applicants elsewhere; seasonal spikes (Jan–Mar) exceed staffed capacity. Case-study anchor: UT-Arlington moved inbound processing "from 20 days to same-day" on Parchment ([parchment.com case study teaser](https://www.parchment.com/), VERIFIED as vendor claim).

**(b) Transfer articulation (P6):** incoming transcript arrives → evaluator maps course-by-course against equivalency table (TES/u.achieve/SIS tables) → unmatched courses go to faculty by email + syllabus attachment → decisions typed back → posted to degree audit → disputes re-open loops. Scale anchor: transfers lose ~43% of credits on average (GAO, VERIFIED); 37% public↔public.
*Failure modes:* equivalencies rot as catalogs change every year at both ends; no universal course ontology (local autonomy is political — departments own curriculum); faculty review is unstructured email with days–weeks latency; students wait on credit answers during the exact window when they're still shopping competitors (DegreeSight's own pitch cites 48% walk-away when credit answers lag — [degreesight.com](https://degreesight.com/), VERIFIED as vendor claim); state systems patch this with common numbering but only inside their borders (TCCNS: 137 TX institutions, [tccns.org](https://www.tccns.org/), VERIFIED; CA unified CCC numbering initiative + ADT guarantee, [icangotocollege.com](https://icangotocollege.com/about/common-course-numbering), VERIFIED; FL SCNS and OH TAG exist but were unreachable this session — REPORTED).

**(c) Credential-evaluation document chase (other-edu-businesses.md P2):** applicant applies → agency requests primary-source transcripts/license verifications direct from foreign issuers → issuers respond by mail/fax/email over weeks-months → authenticity screening → translation → expert writes comparability report.
*Failure modes:* TruMerit (ex-CGFNS) publishes that receiving primary documents averages **14 weeks** and is "the greatest delay," while 70–90% of reports issue within 7 business days once received ([trumerit.org](https://www.trumerit.org/application-processing-times/), VERIFIED) — i.e., ~2/3+ of cycle time is chasing, not evaluating. AI-supercharged credential fraud is growing (TruMerit fraud hub, VERIFIED); issuing institutions abroad have no API and no incentive to respond; WIP inventory compounds (ECE completes most orders in ~5 business days after complete docs — [ece.org](https://www.ece.org/), VERIFIED — proving the evaluator-side work is fast and the chase is the bottleneck).

## 3. Buyer & economic math per wedge

All figures ESTIMATE unless noted; fully-loaded staff cost assumed $40–55/hr.

**Wedge A — processor-hours math.** Mid-size selective office: 15,000 applicants × 1.8 transcripts = 27,000 transcripts/yr; 5–15 min keying/chasing each → 2,300–6,800 hrs ≈ 1.2–3.4 FTE ≈ $115–350K labor. International subset (say 10% of files) additionally costs *students* $280–$340 per all-in NACES evaluation (ECE competitor chart, VERIFIED) and 2–8 weeks of delay that lands on yield. Value sold: 60–80% hour reduction ≈ **$90–220K/institution/yr** plus conversion lift. TAM: 2,000+ Slate schools (VERIFIED, technolutions.com via competitive-landscape.md) plus non-Slate; realistically addressable ~900–1,200 offices × $25–50K ACV → **~$25–50M ARR ceiling domestic** (ESTIMATE).

**Wedge B — transfer-retention revenue math.** Regional university: 3,000 incoming transfers/yr. At GAO's 43% average loss (VERIFIED), suppose 30% lose ≥ one term of credits (≈900), 15% of those walk or delay graduation (≈135), product converts half (≈65 retained/persisted) × $12–20K remaining net tuition = **$0.8–1.3M/yr institutional revenue effect**, plus evaluator labor: 3,000 files × 45 min avg → 2,250 hrs ≈ 1.1 FTE ≈ $95K saved, plus faculty escalation latency cut (days→hours) improving completion metrics under performance funding. Even haircut 70% for skepticism: **~$300–450K/yr addressable value vs a $50–70K price** = 5–9× ROI story. TAM: ~4,000 Title IV institutions (raw file), realistic buyers ~1,000–1,400 (CCs + regionals + online-heavy privates) × $40–75K ACV → **~$50–90M ARR ceiling**, plus statewide/system deals upside (Parchment runs 10 state initiatives, so states do buy here — [parchment.com](https://www.parchment.com/), VERIFIED).

**Wedge C — evaluator throughput math.** Large agency: 20K open cases/yr, 14-week doc receipt (VERIFIED TruMerit). Cutting receipt to 6 weeks compresses cycle from ~16.5 to ~8.5 effective weeks → ~45–55% throughput gain on fixed staff, releasing WIP worth **$0.5–2M/yr** (carried ESTIMATE from other-edu-businesses.md P2). TAM narrow: ~80–100 NACES-member agencies (count UNKNOWN this session) + international recruitment/staffing firms; ACV $60–150K → **~$8–20M ARR** — a product line, not a company.

## 4. Pricing

Verified benchmarks:
- **Human evaluation fees (student-paid):** ECE Course-by-Course **$199 base**; General $110; General-with-GPA $135; Rush +$90; report copies $30–45; translation waiver $85; ECE's own comparison chart prices the full CBC experience at ECE **$281** vs "Evaluation Company A" **$302**, B **$329**, C **$340** (pricing as of 2/15/26) ([ece.org Services & Fees](https://www.ece.org/ECE/Credential-Evaluations/US-Institutions/Services-and-Fees), VERIFIED). WES sits in the same band (commonly $200–$300 all-in; exact current US fee schedule is behind an interactive flow — REPORTED/ESTIMATE).
- **Exchange/order economics:** Clearinghouse publishes a public fee schedule ([theclearinghouse.download/feeschedule](https://theclearinghouse.download/feeschedule), existence VERIFIED; contents not parsed this session — per-transcript student fees commonly ~$3–15, ESTIMATE). Parchment monetizes issuer/receiver plans + per-order (quote-gated, VERIFIED model).
- **Software subscriptions:** Slate tiers $30K–$175K, "most clients pay $50K" (VERIFIED, technolutions.com/licensing via raw file); TES subscription pricing quote-gated, historically low-to-mid five figures by institution size (REPORTED — site blocks bots).

**Recommended structure: platform fee + metered intelligence, never pure per-transaction.**
- Wedge B flagship: **$45–75K/yr platform** (includes unlimited parsing up to fair-use, equivalency engine, faculty-routing workflow) + optional success tier tied to audited credit-posting lift (mirrors DegreeSight's ROI guarantee, which validates guarantee-framing works in this category — [degreesight.com](https://degreesight.com/), VERIFIED claim).
- Wedge A standalone/batch: **$0.75–1.50 per parsed transcript** or $25–40K/yr bundled; batch backfill projects $15–40K one-time.
- Wedge C later: **per-document-chase fee $8–25** (success-based) + $50–120K/yr agency platform.
- Target blended ACV year 1–3: **$35–60K**; design the entry SKU under the ~$50K competitive-solicitation trigger typical of publics (competitive-landscape.md §4.2, INFER) so a registrar can card/dept-buy the pilot.

## 5. Competitive teardown

**Parchment (Instructure).** The network is the moat: **165M+ credentials exchanged, 5.8K+ K-12 districts, 6.1K+ HEIs, 7.3K+ receivers, 10 state initiatives**, GED/HiSET in 23 jurisdictions ([parchment.com](https://www.parchment.com/), VERIFIED). Already sells Receive, Data Automation, Transfer Articulation, Course Sharing, Records Digitization (VERIFIED nav) — i.e., they are *adjacent-active* in exactly our lanes. Parent context: Instructure taken private by KKR/Dragoneer for **$4.8B** (Nov 2024) ([Wikipedia/Instructure citing Reuters/PE Hub](https://en.wikipedia.org/wiki/Instructure), VERIFIED), then suffered the **May 2026 Canvas breach** (ShinyHunters; reported ~275M records affected; multiple lawsuits incl. naming KKR; called the largest education data breach on record) ([Wikipedia/Instructure](https://en.wikipedia.org/wiki/Instructure), VERIFIED). Read: enormous distribution + every transcript format on earth flows through their pipes (best possible training corpus), but post-breach trust damage, PE cost-discipline, and platform breadth make deep AI parsing investment slower than their theoretical advantage. Displacement risk: **HIGH within 24–36 months** if they ship AI receive-automation as a checkbox feature.

**National Student Clearinghouse.** Nonprofit; "nearly 100% of America's colleges" rely on it (VERIFIED, [studentclearinghouse.org](https://www.studentclearinghouse.org/)); owns Transcript Services, Data Exchange, verifications, StudentTracker, and now Sentinel 360 anti-fraud (VERIFIED). Monetizes exchange/compliance, not interpretation; culturally conservative; more likely a partner/data source than an AI-parser competitor near-term. Its reverse-transfer program (auto-award of associate degrees — REPORTED, well-known initiative) overlaps wedge-b outcomes at the margins.

**CollegeSource TES.** De facto shared content library + Evaluation Tracker routing (REPORTED this session — collegesource.com 403-blocks bots; consistent with raw-file characterization). Strength: decades of institution-contributed equivalency data — the single best existing training corpus for matching. Weakness: library-and-form paradigm; no semantic matching, no syllabus understanding, no LLM-era recommendation; Transferology consumer front-end exists but back-office reasoning is manual. Strategy: integrate (import/export equivalency tables, respect Tracker workflows), don't replace; they could bolt on AI too — watch them (kill risk #3).

**Human evaluators/agencies.** WES: 4M+ cumulative evaluations, relationships with 60,000+ institutions across 203 countries, and explicit **"seamless integration with Slate"** ([wes.org](https://www.wes.org/), VERIFIED) — they are embedded, trusted, and slow. ECE: ~5-day turnaround post-docs, aggressive value pricing (VERIFIED). Their moat is NACES membership acceptance conventions + liability-bearing expertise, not technology. They will not build software quickly; they are partners for wedge (c) and acquisition candidates eventually.

**AI-native entrants.** DegreeSight is the material one: DocSight Transcript OCR (claims 99% accuracy, "90% time savings"), Inbound self-service credit answers, Insight prospective degree audits, 100+ institutions, Slate Silver Preferred Partner, SOC 2/HECVAT/VPAT/FERPA-aligned, ROI guarantee ([degreesight.com](https://degreesight.com/), VERIFIED as marketing claims — treat numbers skeptically). This partially falsifies the raw file's "no strong AI-native player" note: an entrant exists and is winning small-private/regional logos. Gap left open: DegreeSight is recruitment/prospect-facing first; deep back-office evaluator productivity + faculty-review routing + intl/military formats remain underserved. Quottly (transfer-pathways mapping) returned 404 this session (VERIFIED dead URL — likely wound down; UNKNOWN details). Generic doc-AI (Hyperscience/Nanonets-class) lacks registrar semantics and equivalency logic.

**Why the gap persists:** (1) long-tail format chaos — 50 years of layouts, microfiche scans, faxed intl docs, homeschool/workforce-adult records that no fixed parser survives (higher-ed-us.md P5); (2) equivalency truth is *local and rotting* — every institution's table is bespoke and ages annually, so nobody can ship a static answer; (3) academic authority must stay human (faculty senates will never accept auto-posted credit), so vendors stopped at handoff points; (4) exchange incumbents monetize movement of documents, not understanding of them — misaligned incentives; (5) accuracy liability: a wrong parse corrupts degree audits and aid, and until VLM-era extraction nobody could clear the bar cheaply.

## 6. Technical feasibility (1–5 people)

Feasible with a deliberately scoped architecture. Layers:
1. **Extraction:** layout-aware VLM OCR (not template OCR) over PDF/image/fax-grade input → schema'd course rows (term, code, title, credits, grade, level) + header entities. Modern VLMs handle heterogeneous layouts far better than 2020-era parsers; expect >95% field accuracy on clean digital PDFs, 85–95% on scans, worse on dot-matrix/microfiche — hence confidence gating. ESTIMATE based on general doc-AI capability, no benchmark fetched (UNKNOWN pending pilot).
2. **Deterministic validators:** credit-hour sums, GPA recomputation, term-date sanity, duplicate-row detection, grade-scale inference flags. Cheap, catches most hallucination/extraction errors; this is where trust is earned.
3. **Equivalency matching:** tiered — exact hit against institutional/TES-imported tables (majority of CC-feeder volume) → embedding similarity over course descriptions + catalog metadata → LLM rationale drafting with citations to source descriptions/syllabi for novel courses. Confidence thresholds route below-bar cases to humans with evidence packets.
4. **Faculty-review routing:** structured queue replacing email (syllabus attach, deadline nudges, decision capture, audit trail). This is ordinary workflow engineering — low risk.
5. **Catalog ingestion:** crawl/version institutional catalogs and course descriptions; the versioning discipline is what fights catalog rot.

Team shape: 2 ML/doc-intel, 1 full-stack workflow, 1 integrations/SDET, founder on GTM/domain. Hardest three risks, honestly ranked:
- **Accuracy bar (hardest).** Wrong credit posting corrupts degree audits and can touch aid eligibility; institutions will compare you to their best human evaluator, not to zero. Mitigate: recommend-don't-post, human signature on every posting, field-level confidence display, blinded benchmarks. If verified field accuracy can't beat ~98% on structured fields with human-in-loop economics beating manual hours, the wedge dies.
- **Catalog/equivalency rot.** Your training data ages yearly at both ends; requires continuous ingestion + drift detection as a permanent ops cost, not a launch feature.
- **Integration surface.** Slate (partner program exists — DegreeSight badge proves third-party integration is possible, VERIFIED), SIS equivalency tables (Banner/Colleague/PeopleSoft/Jenzabar APIs are creaky), TES import/export (openness UNKNOWN — site bot-blocked; must be tested in first 90 days), HECVAT/security review at every campus IT shop. Post-Canvas-breach, campus security scrutiny of vendors is elevated (VERIFIED breach context above) — budget real time for SOC 2 groundwork.

## 7. Regulatory / deployment

- **FERPA:** operate as school official under institution control with DPAs; least-privilege scopes; no secondary use of student data without consent — and negotiate *de-identified* rights to parsed-equivalency pairs explicitly, because the cross-institutional match corpus is the compounding asset (design point, INFER). Post-Canvas-breach climate (275M-record class actions, VERIFIED) means security posture is a sales prerequisite, not a checkbox: SOC 2 Type I early, HECVAT completed, pen-test letter ready.
- **Accuracy liability in credit decisions:** keep **academic authority human by design** — the engine recommends, the evaluator/faculty signs; every posting carries provenance (source doc, extraction confidence, match rationale, approver ID). This is both the legal shield and the adoption path (registrars keep authority; faculty keep curriculum power). Do not market "automated credit awarding" — market "evaluator copilot."
- **Credential-eval report issuance:** formal NACES-style equivalency reports for licensure/immigration are a regulated-trust niche we should NOT enter initially (NACES acceptance conventions; fraud liability). Sell tooling to agencies instead (wedge c as infrastructure).
- **International-doc fraud screening:** genuine demand and precedent — TruMerit runs a dedicated fraud-prevention program citing AI-supercharged nursing-credential fraud (VERIFIED), and Clearinghouse sells ghost-student fraud detection (Sentinel 360, VERIFIED). Feasible scope for us: tamper heuristics (font/layout anomalies, metadata, cross-source consistency, issuer-response verification via chase agents), always flagging — never adjudicating. Authenticity judgment stays with credentialed evaluators.
- No federal transfer-credit mandate exists; policy energy is state-level (CA unified numbering + ADT, TX TCCNS — VERIFIED; FL SCNS/OH TAG REPORTED). GAO-17-574 recommendations to ED were accepted but federal follow-through has been limited (REPORTED — GAO search blocked this session); do not build the GTM on hoped-for regulation.

## 8. GTM

**First customer profile:** a community college (or CC district) + its dominant four-year transfer destination, sold into the registrar/admissions-eval office with the VP Enrollment as executive sponsor and Academic Affairs pre-briefed (they hold faculty review). Why CC-first: highest transfer volume, acute GAO-pattern pain, leaner procurement (competitive-landscape.md §4.3 INFER), and the CC→regional feeder pair lets one deployment exercise both ends of the equivalency problem. Secondary beachhead: regional publics losing transfer enrollment to online competitors (the retention math of §3 lands hardest there).

**Who signs:** University Registrar (owner) + Director of Admissions Ops (co-owner); pilot dollars usually under the $50–100K solicitation threshold (INFER from typical bands, competitive-landscape.md §4.2); coop piggyback (E&I) after 2–3 lighthouse wins. Cycles: 3–9 months; summer-budget timing; expect IT security review as the long pole (post-Canvas-breach climate, VERIFIED context).

**Pilot design (60–90 days, priced $15–25K, creditable):**
1. Backfill benchmark: 500–2,000 historical transcripts (mixed vintages/formats incl. JST + one international cohort) double-keyed vs staff baseline → report field-level parse accuracy (target ≥97% fields, ≥99% with human confirm pass), minutes/transcript before vs after (target −70%).
2. Live equivalency shadow: engine recommends silently for 500 incoming transfer courses; measure % recommendations evaluators accept unchanged (target ≥60%), faculty escalation count reduction, median faculty-decision latency (target days→<48 hrs).
3. Success gate for annual contract: combined labor + retention ROI ≥ 4× price, agreed up front in writing (guarantee framing validated by DegreeSight, VERIFIED claim).

## 9. Service → product ladder

1. **Batch parsing service (months 0–6):** done-for-you historical transcript digitization + structuring for stop-out re-enrollment campaigns (P8 pool: 43.1M SCNC nationally, VERIFIED NSC) — immediate cash, builds the format corpus, zero integration friction.
2. **Workflow SaaS (months 6–18):** wedge-B evaluator copilot + faculty routing live at lighthouse schools; Slate embed/partner listing.
3. **API/data layer (months 18+):** parse-and-match API for SIS/DegreeWorks/TES-class platforms, statewide systems, and agencies; usage-metered.
4. **Managed chase network (wedge c, year 2+):** multilingual primary-source doc-chase agents sold to evaluators/staffing firms — service-heavy start (humans supervise agent fleets), converting to product as reliability accrues.

## 10. Expansion paths

- **K-12 record transfers (O12 adjacency):** district-to-district mobility records are the same core (Parchment District Transfer/Cumulative Folders exist — VERIFIED nav); our differentiation would be interpretation (course placement, credit bearing) not movement; enter via districts already buying our HE products' feeder patterns.
- **Chase network as standalone product line:** the 14-week primary-source bottleneck is VERIFIED and spans healthcare licensure, immigration-adjacent eval, staffing — bigger than education alone; sellable to CGFNS-class bodies, recruitment agencies (Adventus-class scale, VERIFIED in other-edu file), and hospitals' credentialing desks.
- **Military/JST parsing:** JST exists as the joint transcript system ([jst.doded.mil](https://jst.doded.mil/), VERIFIED minimal response; adoption stats UNKNOWN this session; ACE credit-recommendation mapping REPORTED) — veterans are a priority enrollment segment (SCO pain, P11), and JST→ACE→equivalency is a high-value, low-format-diversity sub-problem; good second-year module.
- **UK/international:** Parchment Digitary operates national networks in 6 countries (VERIFIED) — partner-or-compete decision needed before committing; UK ENIC/NARIC-style advisory evaluation and UCAS-context parsing is a plausible line where exchange incumbency is weaker (UNKNOWN depth this session).
- **Statewide deals:** 10 Parchment state initiatives prove states buy transcript infrastructure (VERIFIED); a state that adopts common numbering (CA AB 1111 pattern) needs exactly an AI matching layer to operationalize it.

## 11. Kill risks (top 5) + falsification tests

1. **Parchment ships AI receive/parsing to its 6.1K HEI network.** Test: quarterly roadmap monitoring + ask every prospect "is this on your Parchment roadmap?"; if we lose 2+ head-to-heads to "we'll just wait for Parchment" in year 1, exit or pivot to wedge (c)/intl.
2. **Accuracy bar unreachable economically.** Test: blinded 1,000-transcript benchmark (incl. 1990s scans, JST, intl) vs current staff baseline before writing the full workflow layer; hard gate: ≥97% field accuracy AND ≥60% labor-hour reduction with human-confirm UI.
3. **CollegeSource closes the door (or ships its own AI).** Test: obtain written API/partner stance within 90 days; if refused AND two pilot institutions insist TES is non-negotiable, pivot to TES-less segment (CCs on SIS tables) or wedge (a) batch services.
4. **No budget: demographic-cliff austerity freezes discretionary buys.** Test: collect 5 signed pilot LOIs (even paid-small) from distinct institution types before building beyond MVP; if <2 after 100 qualified conversations, stop.
5. **The data moat never accrues to us.** Test: negotiate de-identified learning-rights clauses in the first 3 DPAs; if institutions/legal uniformly refuse, the business is a services treadmill — re-price or exit.

## 12. Verdict: BUILD-CAREFULLY

Honest paragraph: The demand is real and unusually well-evidenced for education ops — GAO's 43% credit-loss figure, a 14-week verified chase bottleneck, ECE/WES pricing that proves willingness to pay hundreds per document, and a competitor (DegreeSight) already selling transcript OCR to 100+ campuses, which simultaneously validates the market and shrinks the whitespace. The original thesis ("no AI-native entrant") needs correction: the open ground is narrower than assumed — it is the *back-office equivalency recommendation + faculty-routing workflow* layered on TES/Slate ecosystems, not generic parsing. That ground still holds a 5–9× ROI story per institution and a defensible position for roughly 24–36 months before Parchment (post-Instructure, post-breach, PE-disciplined) or CollegeSource responds. The honest worry is structural: incumbents own the pipes and therefore the future training corpus; our counter-moat must be workflow depth + cross-institutional match data contracted for in DPAs from day one. This is a good services-funded, capital-light build for a 3–5 person team with genuine doc-AI skill — and a bad bet for anyone hoping parsing alone is the product.

Re-scored dimensions (1–10):
| Dimension | Score | Note |
|---|---|---|
| Pain intensity / urgency | 8 | Revenue-linked, GAO-documented, seasonal crunches |
| Market size (serviceable) | 6 | $50–90M ARR ceiling wedge B (ESTIMATE); statewide upside |
| Competitive exposure | 4 | Network incumbents adjacent-active; DegreeSight present |
| Technical feasibility (small team) | 7 | VLM-era extraction feasible; accuracy bar is the gate |
| GTM difficulty | 5 | Known buyer, provable pilots; security review drag post-Canvas breach |
| Regulatory/liability | 6 | Manageable with human-authority design; FERPA routine |
| Data-moat durability | 5–7 | Depends entirely on DPA learning-rights discipline |

**Overall: BUILD-CAREFULLY (7/10)** — proceed with wedge B + bundled parsing, gated by the §11 falsification tests, funded by §9 ladder step 1 revenue.

## Sources

Fetched this session:
- Parchment homepage/network stats/products: https://www.parchment.com/
- National Student Clearinghouse homepage (scale claim, Transcript Services, Data Exchange, Sentinel 360): https://www.studentclearinghouse.org/
- Clearinghouse public fee schedule (existence; contents unparsed): https://theclearinghouse.download/feeschedule
- WES homepage (4M+ evaluations, 60K+ institutions, Slate integration): https://www.wes.org/
- ECE Services & Fees (CBC $199/$281 all-in, competitor chart $281–$340, 5-day turnaround, rush/copy fees): https://www.ece.org/ECE/Credential-Evaluations/US-Institutions/Services-and-Fees
- DegreeSight homepage (DocSight OCR claims, Inbound, Insight, 100+ institutions, Slate partner, SOC2/HECVAT, ROI guarantee): https://degreesight.com/
- Texas Common Course Numbering System (137 institutions, voluntary cooperative): https://www.tccns.org/
- California Community Colleges / I Can Go To College (ADT guarantee; common course numbering initiative): https://icangotocollege.com/ (sections: /associate-degree-for-transfer, /about/common-course-numbering)
- Instructure (KKR/Dragoneer $4.8B take-private 2024; Parchment acquisition; May 2026 Canvas/ShinyHunters breach, lawsuits): https://en.wikipedia.org/wiki/Instructure
- Joint Services Transcript portal (existence): https://jst.doded.mil/

Carried from prior session files (already cited there): GAO-17-574 (43% credit loss); Technolutions Slate licensing ($30K–$175K, 2,000+ schools); TruMerit application-processing times (14-week primary-doc receipt, fraud hub); NSC SCNC 2025; AACRAO/practitioner norms (UNKNOWNS flagged).

Blocked/unverifiable this session (labeled inline): collegesource.com (403), GAO site search (403), dantes.doded.mil (transport error), scns.fldoe.org (transport error), ohiohighered.org (transport error), quottly.com (404), WES exact US fee schedule (interactive page), TCCNS-equivalents outside TX, JST adoption counts, NACES member count.
