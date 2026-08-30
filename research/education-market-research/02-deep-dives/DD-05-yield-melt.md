# DD-05: Yield/Melt Completion Orchestrator
**Deep-dive date:** Aug 25, 2026 · **Parent research:** `00-raw-segment-research/higher-ed-us.md` (P7), `competitive-landscape.md` (§1.3/1.4)
**Concept:** AI-agent layer ON TOP of Slate/Salesforce that owns deposit-to-move-in checklist execution per admitted student — detects gaps (final transcript, immunization, housing, MPN, orientation registration), chases via personalized SMS/email/calls in family language, ingests & validates documents (OCR immunization records), escalates financial-gap conversations to counselors, reports daily melt-risk to the VP Enrollment.

**Labeling:** **VERIFIED** = fetched this session with URL. **ESTIMATE** = reasoned from verified anchors + domain knowledge. **UNKNOWN** = not defensibly established. Skepticism flags inline.

---

## 1. Problem & scope

**The problem is real and the literature is deep, but its size is routinely overstated by vendors.**

- Summer melt = deposited/college-intending students who never matriculate. Castleman & Page document summer attrition of **10–40% among college-intending high school graduates** (accepted + stated intent) — that headline number covers *intenders*, not *depositors* ([Castleman & Page 2013, NEJHE via ERIC](https://eric.ed.gov/?q=summer+melt+AND+text+message); [Harvard Education Press 2014](https://eric.ed.gov/?q=summer+melt+AND+text+message)). Melt among students who have paid a deposit at the specific institution is materially lower — practitioner range **~8–18% at non-selective four-years, low-single-digits at selective privates** (**ESTIMATE**; no national depositor-level time series found this session — **UNKNOWN**, RNL/Encoura yield reports not fetched).
- The mechanism matters: melt is driven by a mix of **logistics maze** (final transcript, housing form, immunization compliance, orientation registration, loan MPN, billing setup), **family information gaps**, and **affordability shocks**. Only the first two are addressable by an execution agent.
- **Intervention evidence:** Castleman & Page's original RCT showed personalized text campaigns raised enrollment **+7pp** among low-income students with limited college-going support (**VERIFIED** as characterized in [LiCalsi et al. 2024 SREE abstract](https://eric.ed.gov/?q=summer+melt+AND+text+message)); Georgia State's Pounce chatbot reduced summer melt **>20% relative** ([Page & Gehlbach, cited in Barret et al. 2019, Inquiry](https://eric.ed.gov/?q=summer+melt+AND+text+message)). **Critical counterweight:** the 4-state Text4College scale-up found **+1.7pp, not statistically significant** overall (+4.2pp marginal in Alabama only; null in AZ/KY/MN), and explicitly cites further mixed/null replications (Bird et al. 2021; Oreopoulos 2020) (**VERIFIED**, same SREE source). Translation for ROI modeling: *plan on 1–3pp absolute melt reduction, not 7.*
- **Scope of the opportunity:** own the *execution* layer — per-student checklist state across systems, document intake/validation, multi-party chase (student + parent/guardian in home language), human escalation for money conversations, daily risk dashboard. Not another texting campaign: EdSights already sells that to 290+ campuses (**VERIFIED**, [edsights.io](https://www.edsights.io/)).
- **Why now:** LLM OCR/extraction makes chaotic immunization/transcript docs machine-readable at viable accuracy; Slate's API allows per-client integrations (**VERIFIED**, [technolutions.com/integrations](https://www.technolutions.com/integrations)); post-2024 FAFSA chaos and demographic-cliff panic put melt on every VP Enrollment's dashboard (Chronicle coverage of colleges touting deposit counts, May 2026, via Google News index — **VERIFIED headline existence, paywalled content UNKNOWN**).

## 2. Workflow today + failure modes

**Today (from P7 raw research + practitioner pattern):**
1. Student pays deposit (May 1 national deadline; rolling elsewhere) → record lives in Slate/Salesforce.
2. Checklist items are tracked in *fragments*: application checklist in Slate (admissions docs), health compliance in MedProctor-style portal or student-health spreadsheets, housing contract in StarRez/Adirondack-type system, orientation RSVP in Guidebook/Presence-style tool or Slate events, MPN on studentaid.gov, billing in bursar system. **No single owner of "is this kid actually showing up?"** (**ESTIMATE** — consistent with P7 and vendor landscape; no single source states this).
3. Chase = mass emails, printed mailers, call blitzes by admissions staff and student callers during June–August; parents often unreachable in English-only comms.
4. Financially stuck students hide; counselors find out at census when it's too late.

**Failure modes (each maps to a product feature):**
- **Fragmented state:** item completed in one system ≠ marked complete where staff look → duplicate chasing or missed gaps. 
- **Document chaos:** immunization records arrive as photos of shot cards, foreign-language records, partial PDFs; health center staff manually review each (**pain VERIFIED indirectly**: MedProctor sells exactly this burden-relief to "hundreds of colleges" with "proactive student communications" and dedicated service [VERIFIED, medproctor.com](https://www.medproctor.com/) — an outsourcer exists because the pain is real).
- **Family language gap:** Spanish/other-language households can't navigate English portals; one bilingual call saves what five emails can't.
- **Affordability silence:** unpaid balance / missing MPN / aid package confusion surfaces too late; nobody wants the awkward call — agent should detect and escalate to a human counselor.
- **Staffing seasonality:** summer coverage is thinnest exactly when workload peaks (P7: ~1,000+ staff-hours per campaign, ESTIMATE).
- **No measurement:** most schools know their melt rate only after census; no leading indicators per student.

## 3. Buyer & economic math

**Buyer:** VP Enrollment Management (owns class-size targets) — confirmed pattern in cross-cutting observation #1 of raw research ("net tuition revenue protection unlocks enrollment money"). Secondary champions: Dean of Admissions / Director of Yield & Operations; health/orientation directors consulted for verticals.

**ROI model (VP Enrollment view), mid-size private:**
| Variable | Value | Basis |
|---|---|---|
| Deposited class | 1,500 | ESTIMATE mid-size private |
| Net tuition/yr | $30K | ESTIMATE, consistent w/ $25–40K band in P7 |
| Baseline depositor melt | 10–12% | ESTIMATE (lit range 10–40% is for intenders; depositor melt lower) |
| Achievable reduction | 2pp | Conservative read of nudge lit incl. null-at-scale results (§1) |
| Students saved | 30 | arithmetic |
| **Gross retained revenue** | **$900K/yr** | 30 × $30K |

**Skeptic's haircut (apply before quoting this to anyone):**
1. **Backfill effect:** many schools run summer melt lists/waitlists; some melted seats get refilled at zero marketing cost → true value < full net tuition (maybe 50–70% capture) (**ESTIMATE**).
2. **Counterfactual cannibalization:** aggressive chasing sometimes flips students who would have melted here but enrolled somewhere *worse for them* — retention quality issue, not revenue.
3. Even after a 50% haircut, **$400–500K/yr against a $36K price ≈ 11x ROI** — the math is why this sells; the *proving* of the math is the hard part (see §8 pilot design).

**Segment differences:**
- **Selective privates ($25–40K net, 500–2,000 deposits):** low baseline melt (<5%) BUT highest net-per-student, all-Slate shops, fastest budget authority. Best ACV; smallest headroom (can't improve what's already 3%).
- **Regional/mid privates & publics ($15–30K net, 1,000–4,000 deposits, melt >8%):** sweet spot — real melt, real dollars, real pain. Publics add state procurement friction (**ESTIMATE**).
- **Community colleges (net $4–6K, huge volumes):** melt manifests as "registered but never attends"; enormous caseloads, tiny net-per-student, grant-funded budgets. Volume play, low ACV; deprioritize for v1 (**ESTIMATE**).

**Seasonality:** work concentrates May 1 → late August (~14 weeks). Product is near-idle Sep–Apr unless expanded to year-round completion/retention (§9–10). Implications: (a) price must be a *seasonal* SKU, not an annual license pretending to be always-on; (b) vendor support load spikes in summer — plan staffing; (c) renewal conversations must happen Feb–Mar for the next cycle (§8).

**TAM:** ~1,200–1,500 US four-year institutions with meaningful deposit classes and melt exposure (**ESTIMATE** from ~2,600 degree-granting 4-year institutions, NCES ballpark; not fetched this session). Beachhead SAM at $25–50K seasonal ACV ≈ **$30–60M**; expansion to year-round completion, publics, CCs, grad, intl pushes ceiling toward **$150–300M** (**ESTIMATE**). This is a solid niche business, not a venture-scale market unless §10 expansion lands.

## 4. Pricing

**Recommended structure: flat seasonal SKU tiered by cohort size, with per-vertical add-ons.**

| Tier | Cohort (deposits) | Seasonal price (May–Aug) |
|---|---|---|
| Base | ≤750 | $24K |
| Core | 751–1,500 | $36K |
| Scale | 1,501–3,000 | $48K |
| Add-on: immunization/doc OCR validation | any | +$12–18K |
| Always-on annual (yr 2+, through first year) | — | $60–90K |

- **Benchmarks:** Slate itself: $30K entry license, "most clients pay $50K," flat for 20+ years (**VERIFIED**, [technolutions.com/licensing](https://www.technolutions.com/licensing)). EAB Navigate: six figures, services-wrapped (**REPORTED**, competitive-landscape §1.3). EdSights/Mainstay texting: mid-five-figures typical (**ESTIMATE**; EdSights pricing unpublished — **UNKNOWN**). A $36K seasonal fee sits credibly between "cheap chatbot" and "EAB program."
- **Flat vs per-deposit-student:** per-deposit ($20–40/deposit) aligns cost to value but produces variable invoices that complicate procurement and cap upside perception. Flat tiers keep deals **below the ~$50K institutional bid threshold** → p-card/director-level purchase, exactly the mechanism competitive-landscape §4.2 identifies ("Slate's flat $30K tier shows how fixed-price dept-level SKU unlocks card-level purchasing").
- **Target ACV:** selective/mid privates $36–54K; regional publics $30–45K; CCs $15–25K (or grant-funded pilots).
- **Why fixed-price unlocks card-level purchase:** under threshold → no formal RFP, 4–8 week cycles, VP signature; also makes ROI story trivial ("one saved student pays for it twice over").

## 5. Competitive teardown

| Player | What they do | Why they don't *execute* |
|---|---|---|
| **Slate native (Technolutions)** | Checklists (application materials), events (orientation RSVPs), deliver campaigns, payments; Slate AI ships AI Identity Verification, AI Dashboards, Reader AI, and *forthcoming* AI Rules (personalized content with approval queues) + AI Voice (AI robocalls) (**VERIFIED**, [slate-ai page](https://www.technolutions.com/slate-ai)) | Everything is *content generation and workflow configuration*, human-operated. No agent owns per-student checklist state across external systems; no doc ingestion/validation beyond ID verification; no multilingual family orchestration. Incentive note: Technolutions monetizes stability + partner consultants, not autonomous labor |
| **EAB Navigate** (+ Signal Vine absorbed 2022) | Onboarding checklists, advising campaigns, Navigate AI assistant | Rule-based campaigns + consulting delivery; oriented to enrolled-student success, not yield-season execution; six-figure contracts and slow velocity (**REPORTED/INFER**, §1.3 landscape file) |
| **EdSights Admit** | Closest competitor: managed SMS/AI framework for admitted pool; claims 96% opt-in, 72% engagement, 290+ institutions (**VERIFIED**, [edsights.io/edsights-admit](https://www.edsights.io/edsights-admit)) | It is a *communication-and-insight* framework: "EdSights builds and manages all the communication," surfaces barriers, alerts staff. It does not ingest/validate documents, does not reconcile checklist state against SIS/housing/health systems, does not close loops — staff still execute. Their moat (humans writing weekly campaigns) is precisely the labor a productized agent replaces |
| **Mainstay** (ex-AdmitHub) | Conversational texting, evidence-backed nudges (GSU Pounce heritage) | Same category: conversation, not execution; pre-LLM architecture retrofitted (landscape §2.2) |
| **Element451** | AI-native CRM ("Bolt agents") for mid-market | Asks schools to *replace* the CRM — opposite wedge; doesn't sit atop installed Slate base |
| **MedProctor / ImmuniCare-class** | Immunization-compliance intake + chasing for hundreds of colleges (**VERIFIED** MedProctor, medproctor.com) | Vertical-only outsourcers; validate the document pain AND compete for that single vertical; no whole-checklist ownership, weak CRM integration story |
| **Startups doing yield-protection AI 2024–26** | Landscape scan (Google News RSS queries, ERIC) surfaced **no funded startup owning deposit-to-move-in execution** — adjacent players only (chatbots, texting, CRMs) (**INFER from absence**; search was noisy, treat as tentative — **UNKNOWN**) |

**Build-on-Slate partnership reality check:** Technolutions lists **Platinum/Gold/Silver implementation partners** — all consulting firms (Huron, Carnegie, Encoura/RNL, Solidan, Ferrilli…), i.e., a services bench, **not an AppExchange-style third-party product marketplace** (**VERIFIED** absence on licensing/partners pages). Integration path is per-client: "institutions are able to create their own integrations … using scheduled web services, batched file transfers, or our API" (**VERIFIED**, [integrations page](https://www.technolutions.com/integrations)) — meaning *the institution* sponsors your API keys inside their instance. There is no co-sell channel; expect informal goodwill, conference visibility (Slate Summit), and partner consultants as referral sources, not a formal program.

**Platform risk — will Slate ship this natively?** Real. Slate's AI roadmap (Rules→Voice→Identity Verification) marches toward automation, and Slate already owns the data + channel + trust. Counterarguments: (a) Slate's DNA is configurability-with-humans; autonomous cross-system execution + OCR validation + multilingual family ops is operationally heavy and un-Slate-like; (b) Technolutions hasn't raised prices in 20 years and ships deliberately slowly; (c) precedent: Slate built video interviewing and payments in-house rather than leaving them to partners. Assume a native "completion agent" within 2–3 years and design to be acquired-or-deep (§11).

## 6. Technical feasibility (1–5 people)

- **Slate API surface:** RESTful web services, scheduled query exports (CSV/SFTP), web-form POSTs, configurable exports/imports; bi-directional SIS integrations exist institution-side (**VERIFIED**, integrations page). Gaps: webhook granularity and rate limits not publicly documented (**UNKNOWN** — knowledge base behind login); expect poll-based sync (15-min cadence) rather than event-driven. Verdict: sufficient for v1 with client-sponsored keys.
- **Document ingestion (immunization OCR):** hardest vertical. Inputs: phone photos of shot cards, foreign records, clinic printouts; needs vaccine/lot/date extraction, dose-interval logic against CDC schedules + institutional requirements, confidence thresholds, human-in-loop review queue. Modern VLM-based extraction makes this tractable but **false-clear risk is a liability** (clearing a non-immune student). Final transcripts (v1 candidate) are far more regular — NSC/Parchment status checks + OCR sanity-check on uploaded PDFs. **Do transcripts-first; immunization second.**
- **Multilingual comms:** LLM translation + Twilio WhatsApp/SMS in family language is commodity; parent-contact capture at deposit is the operational unlock (consent flows, §7).
- **LMS/housing touchpoints:** optional v2; housing (StarRez/Adirondack) APIs exist but are account-gated (**ESTIMATE/UNKNOWN**); orientation RSVP can ride Slate events initially.
- **v1 scope in weeks:** **6–8 weeks, 3 people** — final-transcript vertical only: nightly Slate export diff → gap detection → sequenced student+parent SMS/email with escalation rules → upload portal with OCR receipt-validation (name/HS/date match) → counselor escalation queue → daily melt-risk dashboard. Immunization vertical adds ~6–8 weeks incl. validation-rules engine.
- **Hardest three technical risks:**
  1. **Ground truth without APIs:** knowing an item is truly done requires reading state out of systems (SIS holds, health portal status, housing contracts) with creaky or gated interfaces; wrong state = wrong chase (annoying) or missed gap (melt).
  2. **OCR precision on health docs:** recall-oriented extraction must not auto-clear invalid records; building per-vaccine validation logic for 50 state/institutional rule variants is grinding work.
  3. **Channel hygiene at scale:** TCPA-compliant opt-in state per recipient (student vs parent), A2P 10DLC registration, deliverability, and quiet hours — unglamorous and unforgiving; one spam complaint cluster kills the campus channel.

## 7. Regulatory / deployment

- **FERPA:** deposited-but-not-yet-enrolled students are generally NOT "students" under FERPA (no attendance relationship) — prospective-student records fall outside FERPA's protections, which sounds liberating but actually means **state privacy laws + institutional policy + contractual data-protection terms govern** (and several state student-privacy statutes reach prospective students; **ESTIMATE** — legal review required). Once enrolled (orientation/matriculation), education-record rules attach; if the platform touches student-health-center records, those are typically FERPA-exempt "treatment records" rather than HIPAA once enrolled — messy enough that HIPAA-grade safeguards regardless is the sane default (**ESTIMATE**).
- **Minors/parents:** many depositors are 17; FERPA rights transfer at 18 or post-enrollment. Practical rule: collect **student consent at deposit** to communicate with listed guardians in specified languages/channels; log consent per recipient; honor student-only preference.
- **TCPA:** autodialed/prerecorded texts and calls to cell phones require prior express written consent for marketing; transactional/institutional messages live in a grayer zone — mitigate with explicit double opt-in language at deposit, per-channel opt-out handling, A2P 10DLC campaign registration, and keeping "informational about enrollment steps" framing documented (**ESTIMATE** — TCPA jurisprudence on edu texts is fact-specific; counsel needed).
- **AI disclosure:** growing state patchwork (e.g., Utah AI-disclosure law, Colorado AI Act effective 2026) plus plain reputational logic: disclose bot identity in chats/calls ("campus assistant"), never claim to be a named human counselor; keep human handoff one message away (**ESTIMATE** on legal specifics).
- **Deployment posture:** least-privilege scoped Slate keys, per-tenant data isolation, short retention on raw documents post-validation, SOC 2 in year 1 — PowerSchool-breach paranoia applies to higher-ed buyers too (landscape §3.7).

## 8. GTM

- **First customer profile:** mid-size private comprehensive, Midwest/Northeast/South, **net tuition $28–38K, 800–1,800 deposits, melt >10%, Slate shop, Pell ≥30%, thin summer staff**. These schools bleed the most absolute dollars and buy at department level.
- **Who signs:** VP Enrollment Management (economic buyer) with Director of Admissions Ops as champion; IT/security signs a lightweight DPA; health center consulted only when immunization vertical added. Under $50K, expect VP signature + procurement rubber stamp (**ESTIMATE**, consistent with §4.2 bands).
- **Pilot design (be honest about power):** randomized cohort — e.g., 70% treatment / 30% control stratified by Pell, first-gen, distance-from-campus, deposit date — measuring melt pp delta + secondary metrics (per-item completion velocity, staff hours, counselor escalations resolved). **Power check:** detecting 3pp melt reduction (12%→9%) at 80% power needs roughly 700–800 per arm; most target classes can't spare that holdout. So either (a) accept a small holdout within high-risk strata plus historical-year baseline adjustment, or (b) sell on process metrics year 1 and outcome proof in year 2. Do **not** promise statistical significance you can't deliver — cite the Text4College lesson (null results at scale) proactively to build credibility (**VERIFIED** lit basis, ESTIMATE power math shown).
- **Procurement timing:** sign **Feb–Apr** (budget flush + setup window before May 1 deposits); implementation April; live chase May–Aug; renewal decision Sep–Oct for following year. Cycle length: 4–8 weeks warm, 10–16 cold (**ESTIMATE**).

## 9. Service→product ladder

1. **Year 0–1 — Managed summer-melt service:** we operate the chase loop (agent + human QA) for one season, transcript vertical. Price $30–50K seasonal. Purpose: prove melt delta, harvest integration learnings, accumulate validation rules. (Deliberately mirrors EdSights' managed model to be credible, then out-products them.)
2. **Year 1–2 — Always-on completion platform:** same engine runs year-round: deposit→move-in, then first-term completion (billing clearance, spring registration, first-6-weeks persistence pulses). Converts seasonal buyer into annual $60–90K contract; fixes utilization/seasonality economics.
3. **Year 2+ — Retention expansion (DD-04 territory):** the chase-and-close-loop machinery generalizes to early-alert follow-through and stop-out re-enrollment (P8/P9) — same buyer division, same integration spine, 2–4x ACV expansion.

## 10. Expansion paths

- **First-year completion:** fall-to-spring persistence tasks (registration, payment plans, SAP warnings) — natural always-on extension feeding ladder step 2.
- **Housing/orientation partnerships:** integrate or co-sell with StarRez/Adirondack (housing) and Guidebook/Presence-class tools (orientation) — they own item state we need; partner rather than replace (**ESTIMATE** on integration openness).
- **Grad programs:** deposit-to-start gaps (transcripts, MPNs, employer funding letters) with higher net-per-student; Slate Grad licenses common (**ESTIMATE**).
- **International yield:** visa-document chasing (I-20 acks, financial docs, SEVIS timelines) — synergistic with P12 SEVIS compliance product; intl melt is expensive and document-dense (**ESTIMATE**; DHS fixed-period-of-admission rule raises stakes, VERIFIED in raw research).
- **Health-compliance standalone:** spin the immunization OCR validator at MedProctor-class incumbents as an OEM/module — validated demand, existing budget line.

## 11. Kill risks (top 5) + falsification tests

| # | Risk | Falsification test |
|---|---|---|
| 1 | **Seasonality kills ARR math** — product idles 9 months/yr; renewals stall | Sell 2 consecutive seasons; track conversion to always-on tier ≥40%. If seasonal buyers churn instead of upgrading, unit economics fail |
| 2 | **Slate ships native AI completion agent** (roadmap trajectory visible: Rules/Voice/ID Verify already shipped, VERIFIED) | Quarterly Slate Summit/webinar monitoring; ask "what happens when Technolutions demos this?" in every win/loss. Mitigation: depth they won't build (doc validation, family multilingual, cross-system truth) + exit optionality |
| 3 | **Melt is mostly affordability, not logistics** — agent detects money problems it cannot fix; nudge-lit nulls at scale support this fear (Text4College, VERIFIED) | During pilot, code every detected barrier: % affordability vs logistics vs motivation. If >60% affordability AND counselor escalations don't convert, the ROI thesis collapses → pivot to aid-office products (P1/P2) |
| 4 | **Institutions refuse vendor access** to Slate data + SMS channel for pre-enrollment minors (security/trust climate post-PowerSchool) | Run 10 discovery calls with security questionnaires before writing more code: ≥5 pass legal/security review without exceptions, else reposition as institution-hosted deployment |
| 5 | **Effect too small to prove in one season** (power math above) | Pre-register pilot analysis; if achievable cohorts can't detect ≥2pp, shift success metric to item-completion velocity + staff-hour savings (defensible even with null melt effect) and extend outcome proof to year-2 pooled data |

## 12. Verdict: **BUILD-CAREFULLY**

This is one of the few opportunities in the segment where the buyer's ROI math is immediate, personal (VP Enrollment owns the melt number), and large relative to price — one retained student pays for the season twice over, and the procurement path (sub-$50K flat SKU, Feb–Apr signing) matches how these offices actually buy. The evidence base cuts both ways: nudging works in careful hands (Castleman/Page +7pp; GSU >20% relative melt reduction) but famously fades at scale (Text4College nulls), which is exactly why the wedge must be *execution and document truth*, not another texting layer — EdSights Admit already rents that position to 290+ campuses, and their managed-campaign moat is precisely the labor an agent replaces. The genuine threats are structural: brutal seasonality that punishes anything resembling an annual license until the always-on tier exists, Technolutions' steady march toward native AI automation on top of the exact customer base you'd sell to, and the possibility that the melt you're paid to reduce turns out to be a money problem wearing a paperwork costume. Build the transcript-first v1 in eight weeks, sell one managed season to a melting mid-size private, and let the pilot data decide whether this becomes the always-on completion platform or a profitable niche service.

**Re-scored dimensions (1–10):**
| Dimension | Score | Note |
|---|---|---|
| Pain severity / urgency | 9 | Class targets = job security; post-cliff anxiety |
| Budget & ROI legibility | 9 | Net-tuition math trivially clears price |
| Technical feasibility | 7 | Transcript vertical easy; immunization OCR hard but tractable |
| Competitive whitespace | 5 | EdSights/Mainstay adjacent & entrenched; MedProctor owns health vertical |
| Durability / platform risk | 4 | Slate could absorb; no formal ISV channel to anchor to |
| Business quality (seasonality-adjusted) | 5 | Great margins in-season; utilization problem until always-on |
| Regulatory complexity | 6 | Manageable: TCPA discipline, FERPA nuance, AI disclosure |
| **Weighted verdict** | **BUILD-CAREFULLY** | Prove melt delta + always-on conversion before scaling |

---
### Source appendix (this session)
- ERIC API (api.ies.ed.gov) — Castleman & Page 2013 NEJHE (10–40% attrition); Castleman & Page 2014 (Harvard Education Press); LiCalsi et al. 2024 SREE Text4College abstract (+7pp original RCT characterization; +1.7pp ns scale-up; Bird et al. 2021/Oreopoulos 2020 nulls); Beard 2023 CC texting evaluation; Barret et al. 2019 Inquiry (GSU Pounce >20% melt reduction, citing Page & Gehlbach); Sanchez 2021 NCAN Text Steps brief
- Technolutions: /licensing (tiers $30K–$175K, $50K typical, 20-yr flat), /integrations (API/web services/batched transfers; SIS/payment/document integrations), /slate-ai (Identity Verification, Dashboards, Rules, Voice, Reader), partner roster (consulting firms only)
- EdSights: / and /edsights-admit (290+ universities, managed SMS framework, engagement stats)
- MedProctor: / (hundreds of colleges, immunization intake + proactive comms)
- Google News RSS indexes: Chronicle May 2026 deposit-anxiety headline; no funded yield-execution startup surfaced (absence-of-evidence caveat)

**Not verified this session (flagged):** depositor-level melt rates by segment (RNL/NACAC reports); Slate KB webhook/rate-limit details (login-walled); EdSights/Mainstay/MedProctor pricing; EAB Navigate contract values; ImmuniCare current status.
