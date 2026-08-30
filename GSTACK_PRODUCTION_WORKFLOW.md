# GSTACK — Build Production-Grade (Wall Page)

> OpenCode: `/gstack-<name>` | Claude Code: `/<name>`

| Phase | Skill | When to Use |
|-------|-------|-------------|
| **1 THINK** | `/office-hours` | New idea / empty repo — reframes problem, writes design doc |
| | `/spec` | Idea still vague — turns intent → executable spec |
| **2 PLAN** | `/plan-ceo-review` | Right after design doc — choose Expand / Selective / Hold / Reduce |
| | `/plan-eng-review` | After CEO — locks architecture, data flow, tests, failure modes |
| | `/plan-design-review` | Users see UI |
| | `/plan-devex-review` | Devs use API / SDK / CLI |
| | `/autoplan` | Shortcut — CEO → Design/DX → Eng in one go |
| **3 BUILD** | `/guard` (=`/careful`+`/freeze`) | Before risky edits / prod data |
| | `/investigate` | Bug or hallucination — root cause first |
| | `/context-save` / `restore` | End of day / branch switch |
| **4 VERIFY** | `/review` | Branch ready — finds prod bugs CI misses |
| | `/codex` | High-stakes diff — 2nd opinion (GPT vs Claude) |
| | `/cso` | Any PII / auth / upload — OWASP + STRIDE audit |
| | `/qa` | Staging URL — real browser, auto-fix + regression tests |
| | `/benchmark` | Perf matters — baseline & compare |
| | `/health` | Weekly — type / lint / tests / dead-code |
| **5 SHIP** | `/document-release` | Before PR — sync READMEs / docs |
| | `/ship` | Tests → cover → push → PR |
| | `/land-and-deploy` | PR approved — merge → CI → deploy → prod check |
| | `/setup-deploy` | Once per repo — configures deploy |
| **6 OBSERVE** | `/canary` | Right after deploy — watches errors / perf |
| | `/retro` | Weekly — streaks + debt |
| | `/learn` | When you learn something durable |

**CHECKLIST**
```
/office-hours → /plan-ceo-review → /plan-eng-review → /guard → code → /review → /cso → /qa → /document-release → /ship → /land-and-deploy → /canary
```

**Skip unless needed:** `ios-*`, `browse`, `design-shotgun/html`, `scrape/skillify`, `diagram`, `make-pdf`, `pair-agent`
