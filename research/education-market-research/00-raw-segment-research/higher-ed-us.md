# Higher Education US Operational Pain Research

Research date: Aug 25, 2026. Method: direct fetches of primary sources (Federal Register API, FSA Handbook, GAO via Wayback, National Student Clearinghouse Research Center, ICE/SEVIS, SACSCOC, VA/GI Bill, NCES/Wikipedia triangulation). Search engines were bot-blocked during this session; where a number could not be pulled live it is labeled **ESTIMATE** (with reasoning shown) or **UNKNOWN**. No AI-vendor marketing used as primary source.

Labeling: **VERIFIED** = fetched this session, URL cited inline. **ESTIMATE** = reasoned bottom-up from verified anchors + domain knowledge. **UNKNOWN** = no defensible number found.

---

## Executive Summary

US higher ed runs ~4,000 Title IV institutions on decades-old SISs (Banner, Colleague, PeopleSoft, Datatel→Anthology) glued together by email, spreadsheets, PDF portals, and human "chasing." The recurring pattern across every problem below: **a regulated document pipeline between humans, agencies, and systems that nobody owns end-to-end**, executed by understaffed offices whose workload spikes seasonally (admissions cycle, aid disbursement, census dates, accreditation visits). Failure costs are asymmetric — lost tuition (melt/stop-out), federal liability (Title IV clawbacks, SEVIS termination, GI Bill overpayments), or existential (loss of accreditation = loss of Title IV access).

Ranked pains by economic weight (logic below, detailed per problem):

1. **Financial aid verification & document chasing** — ED's own PRA filing admits 2.35M responses/371K hours annually *before* institutional overhead; sits directly on top of every enrolled dollar.
2. **Stop-out re-enrollment (Some College, No Credential)** — 43.1M-person pool growing 2.1M/year; each recovered student = full net tuition; almost pure revenue lever.
3. **Transfer credit evaluation/articulation** — 35% of students transfer and lose avg 43% of credits; credits not awarded = either lost revenue (student leaves) or extra terms billed.
4. **Summer/yield melt operations** — 10–20% of committed freshmen melt without aggressive summer chasing; each melted freshman at a $25–40K net-tuition school = $25–40K/yr lost.
5. **R2T4/withdrawal processing & Title IV reconciliation** — direct federal liability; routine audit findings; highly deterministic math done by hand.
6. **Registrar transcript/degree-audit exceptions** — manual exception memos gate graduation; errors delay credentials (completion-rate penalties) and drive help-desk volume.
7. **Veterans certifying (SCO)** — per-student-per-term certification, monthly verification mandates added Jan 2026; errors create VA debt for students and school liability.
8. **SEVIS/DSO compliance** — nonresident tuition ($30–60K) per international student rides on timely SEVIS updates; 2026 fixed-period-of-admission rule adds registration-like workload.
9. **Accreditation self-study/evidence assembly** — 5–10-year mega-project plus fifth-year interim; hundreds of faculty-hours hunting documents; sanction risk.
10. **Professional judgment & SAP appeals** — discretionary casework with big dollar consequences, currently ad-hoc email/PDF workflows.
11. **Admissions application reading/materials chasing** — reading is judgment (assist), missing-documents chasing is automatable (agent-owned).
12. **Early-alert follow-through** — flags exist (Navigate/Civitas), closing the loop doesn't happen; retention dollars leak.
13. **Institutional reporting (IPEDS/Clery/state auth)** — annual mandatory assembly across offices; fines and access-to-participation risk.
14. **Curriculum approval & faculty credential files** — committee routing measured in months; accreditor audits punish missing credential files.
15. **Research pre-award administration** — proposal assembly/budget compliance taxes every grant dollar; effort reporting/subrecipient monitoring are audit magnets.
16. **Community-college placement & adult re-engagement** — placement policy determines gateway completion; WIOA/Perkins reporting is grant-contingent.

**$ logic anchor points (VERIFIED):** 43.1M SCNC population and 2.1M new stop-outs/yr ([NSC SCNC 2025](https://nscresearchcenter.org/some-college-no-credential/)); avg 43% credit loss among transfers ([GAO-17-574](https://www.gao.gov/products/gao-17-574)); 2,345,626 verification responses & 371,252 burden hours ([91 FR 13825](https://www.federalregister.gov/documents/2026/03/23/2026-05615/agency-information-collection-activities-comment-request-student-assistance-general)); 780+ SACSCOC institutions ([sacscoc.org](https://sacscoc.org/)). Net-tuition figures used in bottom-up math labeled ESTIMATE throughout.

---

## Problem Detail

### P1. Financial aid verification: document collection, review & correction loop
- **Workflow:** ED/FSA flags ISIRs into verification tracking groups (V4/V5 etc.) → school sends notification listing required docs (tax transcripts, W-2s, household size, SNAP, child support) → family mails/uploads PDFs (often wrong ones) → counselor compares doc vs FAFSA data field-by-field → corrections submitted → reprocessed ISIR → possibly repeat. Disbursement is blocked until complete. Per [FSA Handbook 2024-25, Application & Verification Guide Ch.4](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/application-and-verification-guide/ch4-verification-updates-and-corrections): acceptable documentation rules, tracking groups, exclusion logic all school-executed.
- **Who performs:** financial aid counselors/administrators. **Who suffers:** low-income students (disbursement delayed/denied), aid staff (seasonal overload). **Budget owner:** Enrollment division (aid office usually reports to VP Enrollment/Student Affairs; CFO cares about cash timing).
- **Volume/cost:** **VERIFIED**: ED's PRA filing for Subpart E verification: **2,345,626 annual responses; 371,252 annual burden hours** ([91 FR 13825](https://www.federalregister.gov/documents/2026/03/23/2026-05615/agency-information-collection-activities-comment-request-student-assistance-general)) — i.e., ~9.5 min/response by ED's optimistic estimate. **ESTIMATE**: real institutional cost is 1–4 hrs/file including chasing and re-review (families submit wrong/incomplete docs; multiple touch-points); at fully-loaded $35–55/hr staff cost, a 10,000-filer school verifying ~20% (2,000 files × 2 hrs) ≈ $140–220K/yr labor, plus attrition effects when aid arrives late.
- **Consequence of bad/late:** students never receive Pell/loans → melt/stop-out; program review findings if verification sloppy → liabilities/repayments ([FSA Handbook Vol2 Ch8 program reviews/sanctions](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/vol2/ch8-program-reviews-sanctions-closeout)).
- **Current software:** SIS aid modules (Banner FA, PeopleSoft CS, Colleague), Document self-service portals (e.g., Verify My FAFSA-style tools), imaging (OnBase). Pain persists because families don't read requests, documents arrive in any format, comparison against IRS data is judgment-y at edges, and correction loops span FSA's system + SIS + email.
- **Why still exists:** regulatory process is school-borne; FSA gives data (FA-DDX reduces some items post-FUTURE Act) but discrepancy resolution remains human; vendors digitize intake, few own the chase-and-resolve loop end-to-end.
- **Judgment vs repetitive:** doc-type validation, completeness checks, field-matching, status nudges = deterministic; edge cases (household composition, conflicting info per [AVG Ch5](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/application-and-verification-guide/ch5-special-cases)) = human.
- **Documents/portals:** tax return transcripts, W-2s, verification worksheets (PDF), SNAP/child-support letters, ISIRs, SIS screens, upload portals, email/SMS.
- **Agent rating:** **WORKFLOW-AUTOMATION trending AGENT-OWNED** (intake OCR + matching + nudge sequences + draft corrections with counselor sign-off).
- **Value/institution:** labor savings ~$100–250K/yr (mid-size) **ESTIMATE** + retained enrollment from faster disbursement (each saved low-income enrollee ≈ net tuition; see P7/P8 math).

### P2. Professional judgment (PJ) & SAP appeals casework
- **Workflow:** student/family submits appeal (job loss, medical, death; SAP: failed progress) with narrative + evidence (termination letter, medical bills, transcripts) → counselor reviews against handbook criteria → decision memo → recalculation/reinstatement → sometimes documentation round-trips. Governed by [AVG Ch5 Special Cases (PJ)](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/application-and-verification-guide/ch5-special-cases) and [Vol1 Ch1 SAP section](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/vol1/ch1-school-determined-requirements#pid_1390382)/[Vol2 Ch3 SAP](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/vol2/ch3-fsa-administrative-and-related-requirements#pid_1433840).
- **Who performs:** aid counselors (PJ); aid + academic advisors (SAP). **Who suffers:** students in crisis (slow decisions = drop-out), staff (unstructured caseloads). **Budget owner:** Enrollment division.
- **Volume/cost:** **UNKNOWN** precise counts; **ESTIMATE**: 2–8% of filers hit SAP warnings/appeals at open-admission institutions (thousands/yr at CCs); PJ surges after recessions/disasters (COVID precedent: appeals became mainstream — see Washington Post/Chronicle coverage cited in [Wikipedia FAFSA article](https://en.wikipedia.org/wiki/Free_Application_for_Federal_Student_Aid)). Each case ~0.5–2 hrs staff time.
- **Consequence:** wrongly denied → lost retention dollars; wrongly granted sloppily → program review finding (inconsistent PJ documentation is a classic FSA review item).
- **Software:** none dominant; email + PDF forms + shared drives; some schools use Maxient (conduct) analogues poorly fitted.
- **Why persists:** inherently discretionary, so vendors avoided it; but 70% is structured intake/checklist/document extraction.
- **Judgment vs repetitive:** decision = human; intake completeness, evidence classification (does this prove job loss?), deadline tracking, decision-letter drafting from templates = automatable.
- **Docs:** appeal forms, employer letters, medical records, court docs, transcripts, degree audits.
- **Rating:** **WORKFLOW-AUTOMATION** (assistant drafts, human decides) — high trust-barrier but tractable.
- **Value:** retention of even 10–20 appealed-at-risk students/semester at $10–30K net = $200–600K/yr **ESTIMATE**.

### P3. Withdrawal processing: Return to Title IV (R2T4) & reconciliation ops
- **Workflow:** student withdraws (official/unofficial — including faculty-reported last-attendance hunts) → registrar feeds date → aid officer computes earned % per [Vol5 Ch1-2](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/vol5/ch1-general-requirements-withdrawals-and-return-title-iv-funds) → returns funds to programs via G6 → notifies student of balances → bursar posts charges; weekly/monthly reconciliation of Pell/DL drawdowns vs disbursement records ([Vol4 Ch5-6](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025/vol4/ch5-reconciliation-pell-grant-and-campus-based-programs)).
- **Who performs:** aid office + bursar + registrar. **Who suffers:** withdrawing students (surprise debts), institution (liability). **Budget owner:** CFO (bursar) + enrollment (aid).
- **Volume/cost:** **ESTIMATE**: 25–40% of aid recipients stop/withdraw annually at CCs (consistent with 2.1M new stop-outs nationally [NSC](https://nscresearchcenter.org/some-college-no-credential/)); each withdrawal triggers a 45-day-deadline calc (~30–60 min incl. last-date-of-attendance forensics); reconciliation continuous.
- **Consequence:** late/incorrect R2T4 = repayments, fines, limitation statuses; unofficial-withdrawal errors are perennial single-audit findings (**UNKNOWN** aggregate $ but recurring in A-133/single audit universe).
- **Software:** SIS modules (Banner FA RTIV calculators), third-party (e.g., FastR2T4-type tools exist); pain persists because inputs (last attendance, module participation) live with faculty/LMS and are chased manually.
- **Judgment vs repetitive:** the calculation itself = fully deterministic; input gathering (last date of attendance across LMS rosters) = agent-friendly chase problem.
- **Docs:** withdrawal forms, LMS activity logs, faculty attestations, G6 screens, SAS (School Account Statement).
- **Rating:** **AGENT-OWNED** for the input-gathering + calc-drafting loop; final filing human-approved.
- **Value:** avoided findings/liability **UNKNOWN**; staff time savings tens of $Ks **ESTIMATE**; also unlocks faster refund-to-student (retention goodwill).

### P4. FAFSA-cycle disruption ops (the 2024 fiasco pattern)
- **Workflow (2024 cycle as documented):** ED released form late (Dec 31, 2023 vs statutory Oct 1), ISIR deliveries lagged months, contributor-invite bugs, correction backlogs → schools repackaged aid late, extended deposit deadlines, ran triage comms, manually rebuilt award packages from partial data. Congress letter (108 members, Feb 2024), FSA COO Cordray resigned June 2024 ([Wikipedia FAFSA, sourced to PBS/The Hill](https://en.wikipedia.org/wiki/Free_Application_for_Federal_Student_Aid)). 2025-26 opened Nov 21, 2024; [FAFSA Deadline Act](https://www.congress.gov/bill/118th-congress/house-bill/8932/summary/00) now forces Oct 1.
- **Who performs:** entire aid + admissions + IT apparatus. **Who suffers:** first-gen/low-income students disproportionately ([PBS via Wikipedia](https://en.wikipedia.org/wiki/Free_Application_for_Federal_Student_Aid)). **Budget owner:** Enrollment division; CFO funds overtime/temp staffing.
- **Volume/cost:** **UNKNOWN** systematic cost study; **ESTIMATE**: schools reported weeks-months of overtime; a 10K-filer school absorbing a 90-day ISIR delay easily burns 1,000–3,000 staff-hours in re-comms/manual packaging.
- **Consequence:** yield/melt spike, deposit refunds, enrollment shortfalls (state funding formulas feel it at publics).
- **Software:** Slate/Salesforce for comms; SIS packaging; nothing handles "rebuild packages from corrected ISIR waves."
- **Why persists:** ED-side failures recur (2017 rollout, 2024 fiasco); schools need surge capacity they can't staff.
- **Judgment vs repetitive:** exception triage (which ISIR changed → who must be re-contacted → which package invalid) = deterministic rules over messy data.
- **Docs:** ISIR batches, SARs, award letters, deadline calendars, CRM comms.
- **Rating:** **WORKFLOW-AUTOMATION** (surge copilot); true ownership limited by FSA system access.
- **Value:** insurance premium framing — 1pp yield protection on 3,000 deposits × $300 deposit + downstream net tuition = high six figures in bad years **ESTIMATE**.

### P5. Admissions transcript intake & evaluation (domestic + international)
- **Workflow:** applicant/self-upload/mail transcript arrives (PDF, image, sealed paper) → admissions clerk keys courses/grades/credits into SIS or reads for admission decision → international docs require credential evaluation (NACES-member agencies like WES charge applicants $150–250 and add weeks) → GPA recalcs → test scores matched to files → missing-transcript chasing until file completes.
- **Who performs:** admissions processors; evaluators for intl. **Who suffers:** applicants (delays), readers (garbage data), registrars downstream. **Budget owner:** Enrollment division.
- **Volume/cost:** **ESTIMATE**: selective undergrad offices process 20K–80K applications; each with 1–4 transcripts; keyed entry 5–15 min/transcript plus chase cycles. International eval outsourcing costs students directly and adds 2–6 weeks. **UNKNOWN** aggregated industry cost; AACRAO publishes transfer/processing practice surveys (annual publications) — not fetched this session (**label: practice exists, numbers UNKNOWN**).
- **Consequence:** incomplete files → rejected/applicant melts elsewhere; mis-keyed data → wrong merit awards or placement downstream.
- **Software:** Slate (reading/CRM), Clearinghouse/Parchment eTranscripts (only covers sending institutions), Ellucian/PeopleSoft integrations; international: WES/ECE/SpanTran outside the wall.
- **Why persists:** long-tail of 20K+ US HS schedules + global formats defeats fixed parsers; self-reported grades need verification; e-transcript adoption uneven (esp. international, homeschool, workforce adults).
- **Judgment vs repetitive:** parsing/keying/matching/dedupe = machine; anomalies (grade-scale inference, suspicious edits) escalate to human.
- **Docs:** transcripts everywhere, test-score reports (College Board/ACT files), passport/visa scans, syllabi for intl equivalency.
- **Rating:** **AGENT-OWNED** for intake-through-complete-file; reading essays stays human.
- **Value:** processor productivity (2–4 FTE equiv at mid-size) **ESTIMATE** + conversion gains from faster complete-file decisions.

### P6. Transfer credit articulation & evaluation
- **Workflow:** incoming transfer student submits transcripts → evaluator maps course-by-course to equivalents using articulation database/equivalency tables → gaps go to department faculty for review (email + syllabus attachments) → posting to degree audit → student disputes → re-review. **VERIFIED scale:** 35% of students transfer at least once; transfers lose an estimated **43% of credits on average** (37% public↔public; 94% for-profit→public); ~half received Pell ([GAO-17-574](https://www.gao.gov/products/gao-17-574)).
- **Who performs:** admissions evaluators + registrar + faculty reviewers. **Who suffers:** students (extra semesters, exhausted aid), institutions (capacity waste), states (attainment goals). **Budget owner:** split — Enrollment (processing) + Academic Affairs (faculty equivalency decisions).
- **Volume/cost:** **ESTIMATE**: mid-size regional: 2–5K transfers/yr × 30–90 min processing + faculty escalations; national re-enrollment/completion drag documented by GAO/NSC.
- **Consequence:** credit loss extends time-to-degree (extra tuition billed OR student walks to competitor with better articulation); state performance funding penalizes slow completions.
- **Software:** Transferology/Acasaurus? (public-facing), SIS equivalency tables, DegreeWorks planning; TES (CollegeSource) is the de facto evaluation content library. Pain persists because equivalencies rot (courses change) and faculty review is unstructured email.
- **Why still exists:** local catalog autonomy; no universal course ontology; political control of curriculum stays with departments.
- **Judgment vs repetitive:** exact/existing equivalencies = lookup; novel course → syllabus-based recommendation = LLM-strong; final academic authority = human.
- **Docs:** transcripts, syllabi/archives, catalog descriptions, learning outcomes, articulation MOUs.
- **Rating:** **WORKFLOW-AUTOMATION → AGENT-OWNED** (recommend + route + track faculty sign-offs).
- **Value:** each additional term avoided saves student $8–30K and improves completion metrics; institutional upside = retained transfers (each worth full remaining net tuition) + performance funding. A school converting even 25 extra transfer stops/yr into persistence at $15K net ≈ $375K **ESTIMATE**.

### P7. Yield/melt operations: deposit-to-move-in completion chasing
- **Workflow:** admitted/deposited student must finish: housing contract, final transcript, immunization records, orientation registration, advising hold clearance, loan MPNs, billing setup → each gap tracked by admissions/orientation staff via mass emails and call blitzes → summer melt = committed student never shows. Research base: Castleman & Page summer-melt studies (10–20%+ of college-intending low-income students melt; text-nudge interventions reduce it) ([Wikipedia Summer melt w/ JPAM citations](https://en.wikipedia.org/wiki/Summer_melt)).
- **Who performs:** admissions yield team, orientation, advising. **Who suffers:** students (logistics maze), enrollment VP (missed class targets). **Budget owner:** Enrollment division (directly owns class-size targets).
- **Volume/cost:** **ESTIMATE**: entering class 1,500–5,000; checklist items 6–12/student; melt baseline ~10–18% of deposits at many non-selectives; staff summer campaign = 1,000+ hrs.
- **Consequence:** each melted depositor = forfeited net tuition; **ESTIMATE math:** school with 2,000 target class, $28K net tuition, melting 12% vs achievable 9% → 60 students × $28K ≈ **$1.68M/yr** left on table; 1pp melt reduction ≈ **$560K**.
- **Software:** Slate events/checklists, EAB Navigate onboarding, CRMs; pain persists because checklists are school-specific, documents (immunization forms!) are chaotic, and families go dark.
- **Judgment vs repetitive:** nearly all chase/triage is deterministic; financial-gap conversations = human.
- **Docs:** final transcripts, immunization forms, housing contracts, loan docs, visa docs (intl), placement results.
- **Rating:** **AGENT-OWNED** (per-student checklist orchestration + doc intake + escalation).
- **Value:** see math above — among the highest ROI items in this list.

### P8. Stop-out re-enrollment & financial-hold triage
- **Workflow:** identify stopped-out students with momentum (60+ credits) → outreach campaigns (mail/email/SMS/call) → respond to "why I stopped" (money, holds, life) → clear bursar holds/negotiate payment plans → readmit paperwork → re-enroll → monitor first term. **VERIFIED macro:** SCNC population **43.1M**; **2.1M newly stopped out** Jan 2022–Jul 2023 alone; only ~1M re-enrolled/yr; 4.7% earn a credential in first year back; community colleges both main source and destination ([NSC SCNC 2025](https://nscresearchcenter.org/some-college-no-credential/)). Notably NSC: ~1 in 4 SCNC credential-earners complete **without re-enrolling** via administrative barrier removal — evidence that paperwork automation alone creates degrees.
- **Who performs:** retention/re-engagement teams (often tiny or nonexistent), bursar, registrar. **Who suffers:** the 36.8M working-age adults stuck; institutions starving for enrollment. **Budget owner:** hybrid — Enrollment (revenue) / Student Affairs / state initiatives fund at publics.
- **Volume/cost:** **ESTIMATE**: a 15K-student university has 30–60K historical stop-outs in its database; campaign cost trivial vs one recovered student's net revenue ($8–25K/yr); recovery rates for well-run campaigns ~1–5%.
- **Consequence of neglect:** permanent enrollment decline (demographic cliff amplifies); states now pay institutions per re-enrolled completer in several attainment programs.
- **Software:** CRMs (Slate/Salesforce), EAB Navigate "stop-out" modules, DegreeSight-style transcript tools for prior-credit audit; pain persists because prior-credit reconciliation + hold negotiation is bespoke per student.
- **Judgment vs repetitive:** list-building, contact sequencing, prior-transcript parsing, degree-gap computation, payment-plan drafting = automatable; personal counseling = human.
- **Docs:** old transcripts (any format!), outstanding balance ledgers, readmit apps, FAFSA renewal, military/JST transcripts.
- **Rating:** **AGENT-OWNED** (outreach + document reconciliation pipeline; humans close deals).
- **Value:** recovering 100 former students/yr at a CC ($6K net) = $600K; at a private ($25K) = $2.5M **ESTIMATE**. Plus degree-revocation-free "reverse transfer" wins.

### P9. Early-alert follow-through & advising caseload execution
- **Workflow:** analytics (Civitas/EAB Navigate, homegrown) flag risk (absences from LMS, grade dips) → advisor/case-manager assigned → outreach attempted → student responds (or not) → referrals to tutoring/food pantry/counseling → **loop often dies here**: no closure tracking, no verification service was delivered → next alert ignored due to backlog.
- **Who performs:** professional advisors (caseloads 300:1+ **ESTIMATE**), faculty reporters, success coaches. **Who suffers:** students flagged but untouched; advisors drowning. **Budget owner:** Student Affairs / Academic Affairs jointly; provost funds advising.
- **Volume/cost:** **UNKNOWN** national totals; **ESTIMATE**: 4K-alerts/semester at a 20K-student campus; effective closed-loop handling ~30–60 min/alert → 2,000–4,000 hrs/semester needed vs available fraction.
- **Consequence:** retention dip compounds directly into tuition loss; state/federal (Title III/V grants) measure persistence — weak follow-through endangers grant renewals.
- **Software:** EAB Navigate, Civitas (now EAB), Starfish (Anthology) — all generate alerts; none reliably executes multi-party follow-through (they're databases, not workers). Why pain persists: alerts ≠ labor; labor is scarce.
- **Judgment vs repetitive:** triage, scheduling, referral routing, reminder cadence, closure verification = automatable; sensitive conversations = human.
- **Docs:** degree audits, LMS gradebooks, appointment notes, referral forms, CARE-team reports.
- **Rating:** **WORKFLOW-AUTOMATION** (agent works the queue, escalates to humans).
- **Value:** 1pp retention on 5,000-student cohort × $12K avg net × persistence years ≈ $600K–1M/yr **ESTIMATE** (first-year effect alone).

### P10. Registrar operations: transcript processing, degree-audit exceptions, enrollment verifications
- **Workflow:** (a) external transcripts posted to student records; (b) degree audits run (DegreeWorks/Banner DBA/CUNY-style systems) produce false negatives → students petition → exceptions ("substitutions/waivers") drafted, routed to faculty/dept chair, entered by hand; (c) graduation clearance sweeps each term catch thousands of audit mismatches; (d) enrollment verifications (NSC batch + manual letters for lenders/employers/insurers) and veteran/insurance certifications processed continuously.
- **Who performs:** registrar staff + faculty committees. **Who suffers:** students near graduation (delays = one more semester), registrar (backlogs). **Budget owner:** Academic Affairs (registrar typically reports to provost side); CFO touches via bursar interplay.
- **Volume/cost:** **UNKNOWN** published hours; **ESTIMATE**: mid-size university: 3–8K exception entries/yr (many schools' DegreeWorks exception queues are visibly this size in practitioner forums), 10–20 min each + routing latency of days-weeks; graduation-audit season = crunch.
- **Consequence:** delayed graduations → tuition + state completion-funding hits; erroneous certifications → lender/liability issues; backlog → reputational damage (registrars are the office students sue/rant about).
- **Software:** DegreeWorks (Ellucian), CAPP (PeopleSoft), Oracle/Workday Student emerging; NSC Enrollment Reporting automates the easy half of verifications. Pain persists because audit rules encode decades of catalog exceptions; SIS migrations stall on exactly this complexity.
- **Judgment vs repetitive:** exception intake/classification/routing/reminders = automatable; policy-violating substitutions = human committee.
- **Docs:** petitions (PDF/forms), catalogs (year-specific!), transfer equivalencies, NSC files, degree plans.
- **Rating:** **WORKFLOW-AUTOMATION → AGENT-OWNED** for intake/routing/drafting; committee keeps authority.
- **Value:** shaving 2 weeks off average graduation-clearance avoids summer-slide melt of near-completers; each saved near-completer ≈ $10–30K; staff savings 1–3 FTE **ESTIMATE**.

### P11. Veterans certifying officials (SCO): GI Bill certification workload
- **Workflow:** veteran enrolls → SCO collects Certificate of Eligibility, builds VA Form 22-1995/22-5495 changes, certifies enrollment per term (VA-ONCE/EBenefits), reports every change (adds/drops/withdrawals/program changes) within windows, monitors tuition/fee payments + Yellow Ribbon splits, now also verifies monthly beneficiary enrollment (VA-side, but school data feeds it). **VERIFIED:** VA mandates monthly verification by beneficiaries as of Jan 2026 and is implementing Rudisill entitlement re-reviews; Dole Act §209 changes school program approvals ([benefits.va.gov/gibill](https://www.benefits.va.gov/gibill/)).
- **Who performs:** SCO (often a registrar staffer wearing a second hat; schools certify 1–1,500+ veterans). **Who suffers:** veterans (payment interruptions = rent money), SCO (personal liability culture). **Budget owner:** Registrar/Academic Affairs; veterans office small.
- **Volume/cost:** **ESTIMATE**: ~700K–800K GI Bill beneficiaries served yearly (see VA Annual Benefits Report, [benefits.va.gov/REPORTS/abr](https://www.benefits.va.gov/REPORTS/abr/) — exact FY number not pulled this session: **UNKNOWN**); per-certification handling 15–45 min × 2–3 events/student/term.
- **Consequence:** late/erroneous certs → VA overpayments → student debt + school compliance scrutiny (VA Oversight & Accountability Division reviews, [oversight page](https://www.benefits.va.gov/gibill/oversight-accountability-division.asp)); veterans abandon schools that fumble payments (direct tuition loss).
- **Software:** VA-ONCE (ancient), homegrown trackers; commercial SCO tools niche. Persists because VA processes/rules churn and school-side data (schedule changes) flows through SIS not designed for VA semantics.
- **Judgment vs repetitive:** change detection (schedule diff → does it alter benefit?), certification drafting, deadline tracking = automatable; unusual entitlement cases = human.
- **Docs:** Certificates of Eligibility, VA-ONCE screens, enrollment certs, DD-214s, tuition/fee ledgers, Yellow Ribbon agreements.
- **Rating:** **WORKFLOW-AUTOMATION → AGENT-OWNED** (diff-driven certification queue with human approval).
- **Value:** retaining even 10 veteran students/yr ($15–40K each with housing stipend economics) ≈ $150–400K; plus avoiding VA findings.

### P12. International student services: SEVIS/DSO compliance ops
- **Workflow:** admit intl student → issue I-20 (SEVIS record) → track arrival/registration/report enrollment in SEVIS within regulatory windows → maintain records (address, program extensions, CPT/OPT authorizations, reduced course load approvals) → report drops/terminations → prepare for site visits/recertification. **VERIFIED infrastructure:** SEVIS run by ICE SEVP; annual "SEVIS By the Numbers" reporting cycle ([ice.gov/sevis](https://www.ice.gov/sevis); 2024 report PDF linked there). **VERIFIED new burden:** DHS final rule (published Jul 17, 2026 per ICE notice) establishes **fixed periods of admission + extension-of-stay procedures** for F/J — converting today's duration-of-status regime into something closer to periodic re-application, i.e., a step-function increase in DSO casework.
- **Who performs:** DSO/RO (PDSO often a dean wearing another hat). **Who suffers:** students (status violations = removal from US), institution (certification risk; [school alerts page](https://www.ice.gov/sevis/school-alerts) lists withdrawn schools). **Budget owner:** Enrollment (intl admissions revenue) / Student Affairs.
- **Volume/cost:** **ESTIMATE**: ~1.1–1.6M active F/M/J records (see latest SEVIS BTN report; exact current-year count **UNKNOWN** this session); a school with 2,000 F-1s = thousands of SEVIS transactions/yr; each mishandled event can cost a student paying $30–60K nonresident tuition.
- **Consequence:** SEVIS errors → terminated records → lost students + federal exposure; recertification failures end intl enrollment entirely.
- **Software:** Terra Dotta, ISO-organized spreadsheets, SEVIS RTI batch; persists because triggers live in SIS/registrar data while DSO works in parallel silo.
- **Judgment vs repetitive:** event detection (student dropped below full-time → draft reinstatement/reduced-load path), deadline clocks, document assembly (I-20 reprint packets) = automatable; adjudications = human.
- **Docs:** passports/visas/I-94s, financial support letters (bank statements!), I-20s, CPT employer letters, EAD cards.
- **Rating:** **WORKFLOW-AUTOMATION** (compliance-critical; human signs every federal action).
- **Value:** protecting even 5 intl enrollments/yr at $40K net = $200K; extension-of-stay era multiplies addressable workload.

### P13. Accreditation self-study, program review & evidence assembly
- **Workflow:** decennial reaffirmation (or HLC assurance argument, WSCUC CFRs): compliance certification + QEP drafted → standards mapped to evidence → dozens of offices hunted for artifacts (assessment results, syllabi, credential files, financial policies) → stored in share drives/institutional repository → off-site review → focal visit → fifth-year interim report between cycles; plus annual program review cycles feeding state/budget processes. **VERIFIED frame:** SACSCOC 2024 Principles + Resource Manual define standard-by-standard evidence expectations for 780+ member institutions ([sacscoc.org](https://sacscoc.org/), [Resource Manual PDF](https://sacscoc.org/app/uploads/2024/02/2024-POA-Resource-Manual.pdf); [reaffirmation process](https://sacscoc.org/accrediting-standards/reaffirmation-process/)).
- **Who performs:** accreditation liaison officer (ALO), IR office, faculty committees, deans. **Who suffers:** everyone (faculty burn weeks); ALO herding cats. **Budget owner:** Provost/Academic Affairs (existential importance → funded when crisis hits).
- **Volume/cost:** **ESTIMATE**: 2,000–6,000 staff/faculty hours per reaffirmation cycle spread over 18–24 months + 200–400 hrs for fifth-year reports; consulting market (e.g., ALO consultants) thrives on this.
- **Consequence:** monitoring/probation/public sanctions (disclosed lists, [accreditation actions page](https://sacscoc.org/institutions/accreditation-actions-and-disclosures/)) → enrollment collapse; worst case loss of accreditation = loss of Title IV = closure. Includes faculty credential documentation audits (SACSCOC policy requires credential justification files; missing files are a classic finding) and substantive-change reporting for new sites/programs.
- **Software:** SharePoint/shared drives, Watermark/Campus Labs assessment modules, Weave; none assemble evidence autonomously. Persists because evidence is scattered across systems and formats and requirements are narrative/judgment-heavy.
- **Judgment vs repetitive:** narrative quality = human; evidence discovery, mapping artifacts→standards, freshness checks, gap identification, version assembly = machine-strong.
- **Docs:** assessment reports, syllabi, CVs/credential docs, board policies, financial statements, survey data, minutes.
- **Rating:** **WORKFLOW-AUTOMATION** (continuous evidence locker + draft narratives; humans own claims).
- **Value:** avoided consultant spend ($50–150K/cycle **ESTIMATE**) + sanction risk mitigation (existential) + reclaimed faculty time.

### P14. Institutional reporting assembly: IPEDS, Clery, state authorization/SARA, gainful employment disclosures
- **Workflow:** annual IPEDS cycles (multiple seasonal collections: IC/HD, ADM, SFA, GR, HR, AL, Finance) compiled by IR from SIS+HR+finance extracts; Clery Act: daily crime-log maintenance, annual security report assembly with emergency procedures + VAWA programs, fire safety reports; SARA/state authorization renewals track enrollment-by-state + complaint logs; GE/FVT disclosures compute program-level outcomes.
- **Who performs:** IR analysts (IPEDS "keyholders"), campus police + legal (Clery), compliance officers. **Who suffers:** IR (keyholder stress), police clerks (log discipline), general counsel. **Budget owner:** Provost (IR) + CFO (finance component) + police dept budget (Clery).
- **Volume/cost:** **UNKNOWN** rigorous hour studies this session; **ESTIMATE**: 150–400 hrs/yr IPEDS at comprehensive institutions (plus error resubmission cycles); Clery ASR production 200–600 hrs/yr at residential campuses; fines for Clery violations exist (DOE fining authority) though enforcement varies (**UNKNOWN** typical penalty).
- **Consequence:** late/incorrect IPEDS → access/participation warnings (Title IV administrative capability signal); inaccurate Clery → DOE fines + litigation exposure after incidents; lapsed SARA → unable to teach online students in other states (direct revenue loss for online programs).
- **Software:** IPEDS online system (free-form misery), Banner/PeopleSoft extracts, spreadsheets; Clery: vendor log tools sparse. Persists because definitions (e.g., HR staff categories, finance chart strings) map badly onto local systems.
- **Judgment vs repetitive:** extract-map-validate-reporting = highly automatable; interpretation edge cases (crime geography) = human/legal.
- **Docs:** SIS/HR/finance extracts, crime logs, MOUs with local police, state authorization inventories, program outcome files.
- **Rating:** **WORKFLOW-AUTOMATION** (data assembly + validation agents with human submission).
- **Value:** mostly risk-adjustment + analyst-time savings ($50–150K/yr equivalent **ESTIMATE**) + keeping online revenue channels legally open.

### P15. Research administration: pre-award assembly, budget compliance, effort reporting, subrecipient monitoring
- **Workflow:** faculty finds RFP → grants officer helps build proposal (budget justification, biosketch/current-&-pending, facilities & admin rate application, subaward packages, data management plan, compliance certifications) → routing through internal approvals (department/college/ORSP) → submission portal (Grants.gov/Research.gov/NSF-era eRA Commons quirks) → post-award: effort certifications each term, subrecipient invoices monitored, no-cost extensions requested. Pre-award crunch concentrates at agency deadlines.
- **Who performs:** department grant admins, central sponsored-programs officers, faculty themselves (nights/weekends). **Who suffers:** faculty (admin tax on research time — widely surveyed, e.g., Federal Demonstration Partnership faculty burden surveys; specific % **UNKNOWN/ESTIMATE** ~30–42% of researcher time on admin per FDP tradition), staff (deadline crunches). **Budget owner:** VP Research (funded partly by F&A indirect recoveries).
- **Volume/cost:** **ESTIMATE**: research universities process 3,000–6,000 proposals/yr; prep cost commonly modeled at $2–10K/proposal (staff + faculty time); **UNKNOWN** authoritative national figure this session.
- **Consequence:** missed deadline = 6–12 month funding slip; noncompliant budget/effort = audit disallowances (single audits routinely flag effort and subrecipient monitoring) → repayments; reputational harm with sponsors.
- **Software:** Cayuse, Kuali Research, Rushmore/InfoEd, Coeus legacy; SciENcv/biosketch generators; still enormous PDF wrangling. Persists because sponsor requirements churn and each RFP is bespoke; subrecipient docs arrive in any format.
- **Judgment vs repetitive:** document assembly from CVs/grants databases, eligibility/limit checks (page limits, budget caps), routing reminders, invoice-vs-scope sanity checks = automatable; science strategy = human.
- **Docs:** RFPs, biosketches, current&pending, budget justifications, subaward statements, effort reports, F&A rate agreements.
- **Rating:** **WORKFLOW-AUTOMATION** (proposal-assembly copilot + compliance checker; AGENT-OWNED for subrecipient doc-chasing).
- **Value:** raising proposal output 10–20% at a $100M-award university ≈ $10–20M new awards potential; even 1 extra win/yr pays for years of software **ESTIMATE**.

### P16. Community college specifics: remediation placement decisions, adult re-engagement, workforce grant reporting (Perkins/WIOA)
- **Workflow:** (a) Placement: incoming students take (post-pandemic often skipped) tests or supply HS GPA/transcript → algorithmic or statewide multiple-measures placement → developmental ed assignment; CAPR/CCRC randomized evaluations show multiple-measures systems shift gateway completion modestly and require heavy transcript/data plumbing ([CAPR MMA project pages](https://postsecondaryreadiness.org/research/projects/alternative-placement-systems/)). (b) Adult re-engagement overlaps P8 with extra layers: prior-transcript recovery, PLA/prior-learning assessment portfolios. (c) Workforce reporting: Perkins V local uses/performance data, WIOA participant tracking (co-enrollment, measurable skill gains) compiled from SIS+LMS+employment records for state/federal filings tied to continued funding.
- **Who performs:** testing/placement staff + IR; workforce deans + grant coordinators. **Who suffers:** students misplaced into dead-end dev-ed or blocked from gateway courses; grant staff buried in cross-system joins. **Budget owner:** Academic Affairs (placement) + CFO/workforce deans (grant-funded positions).
- **Volume/cost:** **UNKNOWN** consolidated; **ESTIMATE**: typical CC: 5–15K new placements/yr; Perkins/WIOA reporting consumes 1–4 FTE-equivalents across IR/grant offices; misplacement costs students semesters (documented dev-ed attrition literature, CCRC corpus).
- **Consequence:** placement errors → gateway completion collapse → state funding metrics; WIOA/Perkins reporting failures → grant clawbacks/local eligibility risk.
- **Software:** statewide placement platforms, Navigate/other CC deployments, Colleague/Banner; Perkins/WIOA often Excel + state portals. Persists because data (HS transcripts, employment records) is fragmented and consent-gated.
- **Judgment vs repetitive:** transcript-driven placement calc, MSG computations, participant-record stitching = automatable; override counseling = human.
- **Docs:** HS transcripts, test scores, placement waivers, PLA portfolios, WIOA individual employment plans, employer wage files.
- **Rating:** **WORKFLOW-AUTOMATION** (placement pipeline + grant-report assembly).
- **Value:** moving 2pp of 3,000 placed students into gateway-pass trajectory compounds through retention math (~$2–5M lifetime institutional revenue per graduating-cohort improvement **ESTIMATE**, conservative per-year capture lower); grant continuity protects $0.5–5M/yr awards.

---

## Cross-cutting observations

1. **The buyer is usually Enrollment Management (VP Enrollment/VP Student Affairs) for anything touching melt/stop-out/aid; Academic Affairs/Provost for accreditation, registrar, curriculum, research; CFO for R2T4/bursar/AP.** Products framed as "compliance automation" get provost/CFO money; products framed as "net tuition revenue protection" unlock enrollment money — the latter budgets move faster.
2. **Document chaos is the common substrate:** tax transcripts, academic transcripts (domestic/international/military), bank letters, immunization forms, syllabi, credential files, subaward invoices. An OCR+extraction+matching core amortizes across P1, P5, P6, P8, P10, P12, P15.
3. **Why incumbents haven't solved it:** SIS vendors sell systems of record, not labor; EAB/Civitas sell analytics+consulting, not executed workflows; point solutions (TES, Parchment, Terra Dotta, Cayuse) each cover one pipe segment and stop at the human handoff. Nobody owns "chase, verify, reconcile, resolve."
4. **Regulatory tailwinds:** FAFSA Deadline Act (Oct 1 hard date), 2026 VA monthly-verification mandate + Rudisill re-reviews, DHS fixed-period-of-admission rule (Jul 2026), ongoing FSA verification notices ([90 FR 34486](https://www.federalregister.gov/documents/2025/07/22/2025-13740/free-application-for-federal-student-aid-fafsa-information-to-be-verified-for-the-2025-2026-award), [90 FR 54316](https://www.federalregister.gov/documents/2025/11/26/2025-21303/free-application-for-federal-student-aid-fafsa-information-to-be-verified-for-the-2026-2027-award)) each convert directly into new institutional workload.
5. **Evidence gaps to fill in deep-dives:** AACRAO transcript-processing hour surveys; NASFAA verification workload survey (site blocked this session); VA ABR beneficiary counts; SEVIS BTN current-year counts; IPEDS respondent-hour PRA filings (fetchable via federalregister.gov API — same trick as 91 FR 13825); single-audit findings frequency for R2T4 (facilities: federalauditclearinghouse via census.gov API).

## Sources

Primary (fetched this session):
- National Student Clearinghouse Research Center, *Some College, No Credential 2025*: https://nscresearchcenter.org/some-college-no-credential/
- GAO-17-574, *Higher Education: Students Need More Information to Help Reduce Challenges in Transferring College Credits* (via Wayback): https://www.gao.gov/products/gao-17-574
- Federal Register 91 FR 13825 (Mar 23, 2026), ED/FSA PRA notice, Verification ICR — 2,345,626 responses / 371,252 burden hours: https://www.federalregister.gov/documents/2026/03/23/2026-05615/...
- Federal Register verification notices: 90 FR 34486 (Jul 22, 2025); 90 FR 54316 (Nov 26, 2025) (via FR API search)
- FSA Handbook 2024–2025 (Application & Verification Guide Ch.1–5; Vol1 SAP; Vol2 compliance; Vol4 reconciliation; Vol5 R2T4): https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2024-2025
- Wikipedia, *Free Application for Federal Student Aid* (2024 FAFSA fiasco timeline w/ PBS/The Hill/WSJ refs): https://en.wikipedia.org/wiki/Free_Application_for_Federal_Student_Aid
- Wikipedia, *Summer melt* (Castleman & Page citations): https://en.wikipedia.org/wiki/Summer_melt
- ICE SEVP/SEVIS portal incl. SEVIS By the Numbers 2024 PDF link + Jul 2026 fixed-admission rule notice: https://www.ice.gov/sevis
- SACSCOC (780+ institutions; 2024 Principles Resource Manual; reaffirmation/fifth-year/substantive-change pages; sanctions disclosure): https://sacscoc.org/
- VA Education Service / GI Bill (monthly enrollment verification mandate eff. Jan 2026; Rudisill/Perkins implementation; Dole Act §209; Oversight & Accountability; ABR index): https://www.benefits.va.gov/gibill/
- CAPR (Teachers College/MDRC) multiple-measures placement project pages: https://postsecondaryreadiness.org/
- Congress.gov, FAFSA Deadline Act (H.R.8932): https://www.congress.gov/bill/118th-congress/house-bill/8932/summary/00

Contextual (known corpus, not refetched; treat accordingly): NASFAA verification workload surveys; AACRAO transfer/practice publications; FDP faculty burden surveys; NACUBO tuition discounting; EAB/Navigate product landscape; practitioner communities (r/financialaid, r/professors, r/StudentAffairs) — inaccessible to bots this session.
