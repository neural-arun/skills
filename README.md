# Skills

Agent-ready workflows for study, work, and daily life. Each folder is a documented pipeline a coding agent (or human) can follow to get a job done — instructions in, verified result out.

## What's in here

| Folder | What it does | Start with |
|--------|--------------|------------|
| [youtube-to-notes-pipeline](youtube-to-notes-pipeline/) | Turn any YouTube video into structured study notes (`md` + `html` + `pdf` + diagrams) | `automate_notes.md`, see `outputs/` for 15+ examples |
| [posts](posts/) | Outcome-driven social post generator for LinkedIn, Twitter/X, Reddit | [posts/README.md](posts/README.md) |
| [posts/writing_skill.md](posts/writing_skill.md) | Meta-guide: how to write good `SKILL.md` files (trigger descriptions, progressive disclosure, plan-act-verify) | Read before creating a new skill |
| [research](research/) | Evidence-driven market research system for finding AI-agent business opportunities | [research/education-market-research/README.md](research/education-market-research/README.md) |
| [pc_cleanup](pc_cleanup/) | 2-minute Windows + WSL cleanup to reclaim 15–30 GB | [CLEANUP_GUIDE.md](pc_cleanup/CLEANUP_GUIDE.md) |
| [my_profile](my_profile/) | Who I am, what I build, and how I pitch it (personal mission, client-facing profile, Upwork bio) | [personal_who_am_i.md](my_profile/personal_who_am_i.md) |
| [ttrounce](ttrounce/) | Research dossier on T-Trounce Prayagraj + founder Shubhra Chaturvedi (offerings, socials, reviews, contact) | [overview.md](ttrounce/overview.md), [index.md](ttrounce/index.md) |

### Details

**1. `youtube-to-notes-pipeline/` — Video → Notes**
Give it a YouTube URL, get back clean study notes. `outputs/` already has 15+ real runs (UPSC Art & Culture, backend roadmap, sales, AI Security, MCP course, etc.) in Markdown/HTML/PDF form.

**2. `posts/` — Social Post Crafting Suite**
Three platform skills with strict rules:
- `linkedin/` — hook in first 140 chars ("See More" fold), outcome bullets, CTA + 3–5 hashtags
- `twitter/` — 280-char counting, numbered threads with hook → deliverables → CTA
- `reddit/` — value-first community posts + `[FOR HIRE]` hiring format
- All require **Step 0: Trend Alignment** — check live trends before drafting.

**3. `research/` — AI-Agent Market Research**
- `education_research_instruction.md` — the full brief: find painful, expensive, repetitive education workflows an AI agent could own end-to-end (pain × value × willingness-to-pay × accessibility).
- `education-market-research/` — completed study (Aug 2026): 20-agent pipeline, ~65K words, ~200 cited sources, 52 scored problems, 10 deep dives, red-team. **Start at `FINAL_REPORT.md`.** Top pick: school Medicaid billing capture.
- `antigravity/`, `claude..md` — alternate/contra takes (notably: sell to private-pay owners, not districts — faster sales cycle).

**4. `pc_cleanup/` — PC & WSL Maintenance**
Copy-paste PowerShell + WSL blocks: clean Docker/NPM/UV/pip caches, Windows Temp, Update cache, shrink the WSL `.vhdx`, reduce hibernation. Includes safety guardrails (what *not* to delete) and specs for Acer Aspire A715-79G / Win11 / i5-13420H / 24GB RAM in `my_pc_specification.md`.

**5. `my_profile/` — Identity & Positioning**
- `personal_who_am_i.md` — mission: Systems Builder for healthcare + education
- `who_am_i_for_clients.md` — client-facing version: Problem → Workflow → Data → Software → AI → Verification → Deployment
- `upwork_bio.md` — Upwork title, rate ($40–50/hr), skill tags, portfolio items

**6. `ttrounce/` — Client Research Example**
Complete dossier for T-Trounce Prayagraj (est. 1990, Spoken English + Personality Development, 4.8★): overview, founder profile, socials (4K IG), reviews, contact info. Useful as a template for "research a local business" tasks.

## How to use

**With an agent (OpenCode, Claude, Antigravity):**
```text
"Use the LinkedIn skill in posts/ to draft a launch post for my project."
"Follow pc_cleanup/CLEANUP_GUIDE.md — my C: drive is full."
"Turn this YouTube video into notes using youtube-to-notes-pipeline/."
```

**As a human:** open the folder README / `SKILL.md` and follow the steps top-to-bottom.

## Conventions

Each skill follows the same shape where applicable:
- `README.md` / `SKILL.md` — instructions (frontmatter with `name` + `description` trigger)
- `scripts/` — deterministic code the agent runs instead of guessing
- `references/` — heavy docs loaded on-demand
- `outputs/` / data folders — results, never edit by hand

Core loop: **Plan → Act → Verify** (inspect, make scoped edits, run tests/build and confirm 0 errors).

## Status

Active use: `youtube-to-notes-pipeline`, `posts`, `pc_cleanup`.
Reference: `research`, `my_profile`, `ttrounce`.
More skills coming.
