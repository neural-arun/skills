# 🧠 Comprehensive Guide: Writing Skills for Agentic Coding Agents

> **Shift your mindset from "prompting a chatbot" to "building an engineering system."**  
> A **Skill** in Agentic AI is a modular, directory-based instruction package (`SKILL.md`) that acts as an expert onboarding manual for your AI coding agent.

---

## 📌 1. What is a Skill (`SKILL.md`)?

Instead of re-explaining project conventions, API schemas, and workflow steps in every chat session, you package institutional knowledge into reusable skills. 

When an agent receives a user prompt, it continuously scans available skill descriptions and **automatically activates the skill** if the task matches its trigger criteria.

```
my-agent-skill/
├── SKILL.md          # (Required) Frontmatter + step-by-step instructions
├── scripts/          # Deterministic scripts (Python/Bash) run by the agent
├── references/       # Detailed docs, schemas, and specs loaded on-demand
└── examples/         # Gold-standard reference implementations
```

---

## 🏗️ 2. Structure of a `SKILL.md` File

Every `SKILL.md` consists of two main parts:

### Part 1: YAML Frontmatter (Metadata)
Scanned by the agent at startup to determine **when** to activate the skill.

```yaml
---
name: social-media-post-generator
description: Use when generating, formatting, or reviewing posts for LinkedIn, Reddit, or Twitter. Do not use for generic web scraping.
---
```

### Part 2: Markdown Instructions (Body)
Loaded into the agent's context window **only after** the skill triggers.

---

## ⚡ 3. Five Golden Rules for Writing High-Impact Skills

### Rule 1: Master Trigger-Optimized Descriptions
* ❌ **Bad Description**: `description: Helps with posting.` (Too vague, won't trigger reliably).
* ✅ **Good Description**: `description: Use when creating outcome-driven posts for LinkedIn, Reddit, or X. Triggers on requests to draft, format, or review social content.`
* **Key**: Include specific trigger keywords, exact use cases, and negative constraints (when *not* to use).

### Rule 2: Practice "Progressive Disclosure"
Keep your main `SKILL.md` file focused on high-level procedures and decision trees. Place heavy documentation, large API schemas, and complex reference material in a separate `references/` directory. The agent loads references *only when needed*, keeping its context window clean.

### Rule 3: Prefer Deterministic Scripts over LLM Generation
If a task is repetitive, fragile, or requires exact precision (e.g. data formatting, linter checks, database migrations), package it as an executable Python or Bash script in `scripts/`. Instruct the agent to **run the script** rather than generating complex code from scratch.

### Rule 4: Implement "Plan-Act-Verify" Control Loops
Never let an agent work in the dark without verification checkpoints:
1. **Plan**: Inspect codebase, review requirements, and propose a step-by-step plan.
2. **Act**: Make precise, non-destructive, scoped edits.
3. **Verify**: Execute independent tests, linters, or build commands (`pytest`, `npm test`, or verification scripts) before claiming success.

### Rule 5: Provide Explicit Edge-Case Guards
Avoid generic phrases like "handle errors properly." Write explicit rules:
* *Verify non-null objects before property dereferencing.*
* *Inspect full error tracebacks before forming a diagnostic hypothesis.*
* *Never mask failures with silent fallbacks or delete failing unit tests.*

---

## 📝 4. Standard Template for `SKILL.md`

```markdown
---
name: skill-name
description: Use when [specific task/condition]. Triggers when user asks to [action 1] or [action 2].
---

# [Skill Name] Guide

## 🎯 Goal
A concise, outcome-driven summary of what this skill achieves.

## 📋 Prerequisites & Context
- Required tools, packages, or environmental setup.
- References to inspect: `references/api_schema.json`

## 🛠️ Step-by-Step Workflow

### Step 1: Investigation & Planning
1. Inspect target files using file search or view tools.
2. Draft a clear execution plan.

### Step 2: Implementation
1. Follow existing codebase conventions and docstring rules.
2. Keep edits focused and modular.

### Step 3: Empirical Verification
1. Run build and test commands.
2. Confirm 0 errors before reporting completion.

## 🚫 Critical Rules & Constraints
- DO NOT mask errors with silent fallbacks.
- DO NOT guess file paths or variable names without inspecting source code.
```

---

## 🎯 5. Agentic vs. Standard Prompting Mindset

| Standard Prompting | Agentic Skill Architecture |
| :--- | :--- |
| Single disposable chat prompt | Reusable, version-controlled repository skill |
| Vague instructions ("write good code") | Deterministic rules + independent verification |
| LLM guesses entire logic | LLM orchestrates proven scripts & reference schemas |
| Hallucinates success | Requires empirical test/build execution before done |
