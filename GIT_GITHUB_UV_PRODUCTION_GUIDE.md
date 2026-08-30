# Git + GitHub + uv — End-to-End Production-Grade Pipeline on Linux

> **Goal:** Start from `0` on a fresh Linux machine and ship a maintainable, team-ready Python project.
> **Stack:** `git` (CLI) + `GitHub` (remote) + `uv` (Python env + package manager)
> **OS:** Linux (Ubuntu/Debian — commands adapt to Arch/Fedora with `pacman`/`dnf`)
> **Audience:** Solo dev → small team → production. No prior git/uv mastery assumed.

---

## Table of Contents

1. [Mental Model: How The Three Pieces Fit](#1-mental-model-how-the-three-pieces-fit)
2. [Phase 0: One-Time Linux Setup](#2-phase-0-one-time-linux-setup-linux)
3. [Phase 1: Git Core Concepts — The Complete Dictionary](#3-phase-1-git-core-concepts--the-complete-dictionary)
4. [Phase 2: GitHub Core Concepts — The Collaboration Layer](#4-phase-2-github-core-concepts--the-collaboration-layer)
5. [Phase 3: uv Core Concepts — Python Env Done Right](#5-phase-3-uv-core-concepts--python-env-done-right)
6. [Phase 4: End-to-End Pipeline — New Project From Scratch](#6-phase-4-end-to-end-pipeline--new-project-from-scratch)
7. [Phase 5: Daily Workflows & Branching Strategies](#7-phase-5-daily-workflows--branching-strategies)
8. [Phase 6: Production Hardening Checklist](#8-phase-6-production-hardening-checklist)
9. [Phase 7: CI/CD with GitHub Actions + uv](#9-phase-7-cicd-with-github-actions--uv)
10. [Cheat Sheet & Troubleshooting](#10-cheat-sheet--troubleshooting)

---

## 1. Mental Model: How The Three Pieces Fit

```
Your Machine (Linux)                  The Internet
┌─────────────────────┐               ┌──────────────────────┐
│  Working Directory   │  git push     │  GitHub Repository    │
│  (your code)         │ ───────────► │  (origin/main)        │
│        │             │               │     │                 │
│  Staging Area        │  git pull     │  Pull Requests        │
│  (.git/index)  ──────┤ ◄─────────── │  Actions (CI/CD)      │
│        │             │               │  Issues / Releases    │
│  Local Repo          │               └──────────────────────┘
│  (.git/objects)      │
│        │             │
│  uv venv (.venv) ────┘   isolated Python + deps
│  pyproject.toml + uv.lock  → reproducible builds
└─────────────────────┘
```

*   **git** = Time machine for code. Tracks *every* change locally. Distributed — you have the full history.
*   **GitHub** = Hub for that time machine. Adds collaboration (PRs, reviews, CI) and is the *source of truth* for a team.
*   **uv** = Lightning-fast Python manager (from Astral). Replaces `pyenv` + `pip` + `venv` + `pip-tools` + `poetry` in one binary. 10-100x faster.

**Golden rule:** `git` versions your *code*, `uv.lock` versions your *environment*, `GitHub` versions your *team's truth*.

---

## 2. Phase 0: One-Time Linux Setup (Linux)

Do this once per machine.

### 2.1 Install / Update Essentials

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install git, curl, gh (GitHub CLI), build tools
sudo apt install -y git curl build-essential gh

# Install uv (official installer — no pip needed)
curl -LsSf https://astral.sh/uv/install.sh | sh
# Restart shell or run:
source $HOME/.cargo/env  # or $HOME/.local/bin/env
uv --version  # should print e.g. 0.11.x
```

> **Fedora/RHEL:** `sudo dnf install git curl gh`
> **Arch:** `sudo pacman -S git curl github-cli`

### 2.2 Configure Git Identity (CRITICAL)

```bash
git config --global user.name "Arun Kumar"
git config --global user.email "you@example.com"  # MUST match your GitHub email

# Helpful defaults for production work
git config --global init.defaultBranch main
git config --global pull.rebase false          # merge strategy for `git pull`
git config --global core.editor "code --wait"  # or nano, vim
git config --global core.autocrlf input        # Linux: fix line endings
git config --global fetch.prune true           # auto-clean deleted remote branches
git config --global --list                     # verify
```

### 2.3 Authenticate with GitHub (SSH — Recommended for Linux)

HTTPS asks for password/token every time. SSH is key-based and standard for production.

```bash
# 1. Generate key (ed25519 is modern best)
ssh-keygen -t ed25519 -C "you@example.com" -f ~/.ssh/id_ed25519_github
# Press Enter for no passphrase, or set one for security

# 2. Start ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github

# 3. Make it persistent (add to ~/.bashrc or ~/.zshrc)
cat >> ~/.bashrc <<'EOF'
eval "$(ssh-agent -s)" > /dev/null
ssh-add -q ~/.ssh/id_ed25519_github
EOF

# 4. Copy public key to GitHub
cat ~/.ssh/id_ed25519_github.pub
# → Copy output, then: GitHub → Settings → SSH and GPG keys → New SSH key → Paste

# 5. Test
ssh -T git@github.com
# Expect: "Hi username! You've successfully authenticated..."

# ALTERNATIVE: via GitHub CLI (easier if you prefer HTTPS)
gh auth login
# Choose: GitHub.com → HTTPS → Yes → Paste Token → Authenticate
```

---

## 3. Phase 1: Git Core Concepts — The Complete Dictionary

You need these ~20 concepts. Nothing more, nothing less for production.

### 3.1 The Three Areas & Commit Anatomy

```
Working Directory  →  Staging Area (Index)  →  Local Repository (.git)
   (edit files)       (git add)                (git commit)
                                   →  Remote (git push)
```

A **Commit** = snapshot + metadata (hash, author, date, message, parent) + diff. Immutable. Identified by SHA-1 hash (`a1b2c3d...`).

### 3.2 Essential Commands & What They Actually Do

| Concept | Command | What It Does | Production Note |
|---|---|---|---|
| **Init** | `git init` | Creates `.git/` folder — starts tracking | Run once. `uv init` already does this. |
| **Clone** | `git clone git@github.com:user/repo.git` | Downloads remote repo + history | Use SSH. Creates `origin` automatically. |
| **Status** | `git status` | Shows staged / unstaged / untracked | Run *constantly*. Your compass. |
| **Add** | `git add <file>` / `git add .` | Moves changes to Staging Area | Stage intentionally. Never `git add .` with secrets. |
| **Commit** | `git commit -m "feat: add parser"` | Saves staged snapshot to local history | Message matters. Use Conventional Commits. |
| **Log** | `git log --oneline --graph --all -n 20` | History visualization | Add `--graph` to see branches. |
| **Diff** | `git diff` / `git diff --staged` | What changed (unstaged / staged) | Review before every commit. |
| **Remote** | `git remote -v` / `git remote add origin <url>` | Links local ↔ GitHub | `origin` is convention for main remote. |
| **Fetch** | `git fetch origin` | Downloads remote changes *without* merging | Safe, non-destructive. Always fetch before pull. |
| **Pull** | `git pull origin main` | `fetch` + `merge` — updates your branch | Pull often. Handle conflicts here. |
| **Push** | `git push origin main` | Uploads local commits to GitHub | Only after pull + tests pass. |
| **Branch** | `git branch` / `git branch feature/x` | Isolated line of development | Branches are *cheap* pointers (~40 bytes). |
| **Switch** | `git switch feature/x` / `git switch -c feature/x` | Move between branches | Modern replacement for `checkout`. `-c` creates. |
| **Merge** | `git merge feature/x` | Combines branches (creates merge commit) | Preserves history. Default for PRs. |
| **Rebase** | `git rebase main` | Replays commits on top of target (linear history) | **Never rebase shared/pushed branches.** Use to clean local history. |
| **Stash** | `git stash push -m "wip"` / `git stash pop` | Shelves uncommitted changes temporarily | Use when you need to switch branches with dirty workdir. |
| **Reset** | `git reset --soft HEAD~1` / `--hard HEAD~1` | Moves `HEAD` pointer back | `--soft`=keep changes staged, `--hard`=destroy. Dangerous. |
| **Revert** | `git revert <hash>` | Creates *new* commit that undoes old commit | Safe for shared history (unlike reset). |
| **Cherry-pick** | `git cherry-pick <hash>` | Copies a single commit to current branch | For hotfixes. |
| **Tag** | `git tag v1.0.0` / `git push origin v1.0.0` | Marks a release point | Use SemVer (`vMAJOR.MINOR.PATCH`). |
| **.gitignore** | file | Tells git what to *never* track | Commit it. Never commit `.env`, `.venv`, `__pycache__`. |

### 3.3 HEAD, Branches, and Detached HEAD

*   `HEAD` = pointer to "where you are now" (usually a branch, e.g., `main`).
*   Branch = movable pointer to a commit. `main` is just the default branch.
*   **Detached HEAD** = `HEAD` points to a commit directly, not a branch (happens when you `checkout <hash>`). Don't commit here — create a branch.

### 3.4 Undoing Things — Decision Tree

```
Need to undo...                          Use...
─────────────────────────────────────────────────────────
Unstaged file (haven't added)      → git restore <file>
Staged file (added, not committed) → git restore --staged <file>
Last commit (local only)           → git reset --soft HEAD~1 (edit) or --hard (delete)
Published commit (already pushed)  → git revert <hash> (then push revert commit)
Need to discard all local changes  → git restore . && git clean -fd
```

### 3.5 Conventional Commits (Production Standard)

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:** `feat` (new feature), `fix` (bug), `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `perf`, `build`

**Examples:**
```bash
git commit -m "feat(api): add /users pagination"
git commit -m "fix(auth): handle expired JWT correctly"
git commit -m "chore: bump uv lock — security patch"
git commit -m "feat!: drop Python 3.9 support"  # ! = breaking change
```

This enables auto-changelogs, semantic releases, and clear `git log`.

---

## 4. Phase 2: GitHub Core Concepts — The Collaboration Layer

### 4.1 Repository Basics

*   **Repo** = Project + history + issues + settings. Create via `gh repo create` or GitHub UI.
*   **README.md** = Front door. Must have: what, how to install, how to run, example.
*   **LICENSE** = Legal protection. `MIT` for open-source, proprietary if closed.
*   **Origin vs Upstream:** `origin` = your fork, `upstream` = original repo (when contributing to others).

### 4.2 Branches & Protection

*   `main` (or `master`) = production-ready code. **Never commit directly** — always via PR.
*   **Branch Protection Rules** (`Settings → Branches → Add rule`):
    *   Require PR before merging
    *   Require status checks (CI must pass)
    *   Require 1+ approvals
    *   Dismiss stale approvals on new commits
    *   Do not allow bypassing

### 4.3 Pull Requests (PRs) — The Core Workflow

PR = Request to merge a branch. Code review + CI + discussion happen here.

**Lifecycle:**
1.  `git switch -c feat/new-thing` → commit → `git push origin feat/new-thing`
2.  GitHub → "Compare & pull request" → fill template → assign reviewer
3.  CI runs (tests, lint) → reviewer approves → `Squash and merge` or `Merge commit`
4.  Delete branch.

**PR Best Practices:**
*   Small (<400 lines), one concern per PR.
*   Title = Conventional Commit style. Description = Why, What, How to test, Screenshots.
*   Link issues: `Closes #42`.

### 4.4 Issues, Projects, and Discussions

*   **Issues** = tasks/bugs. Use labels (`bug`, `enhancement`), milestones, assignees.
*   **Projects (Beta)** = Kanban board for issues/PRs.
*   **Templates:** `.github/ISSUE_TEMPLATE/` and `PULL_REQUEST_TEMPLATE.md` enforce consistency.

### 4.5 GitHub Actions — Automation

YAML files in `.github/workflows/*.yml` run on events (`push`, `pull_request`, `schedule`).

Key concepts: **Workflow → Jobs → Steps → Actions** (reusable steps like `actions/checkout@v4`).

### 4.6 Forking vs Branching

| Model | When | How |
|---|---|---|
| **Branching** (same repo) | Team with write access | `feat/*` branches in `origin` |
| **Forking** (copy repo) | Open-source / no write access | Fork → clone fork → PR from fork → upstream |

### 4.7 Releases & Tags

*   `git tag v0.1.0 && git push origin v0.1.0` → GitHub → `Releases → Draft new release` → auto-generates notes from commits.
*   Use SemVer strictly.

### 4.8 Secrets & Environments

*   `Settings → Secrets and variables → Actions` — store `PYPI_TOKEN`, `API_KEYS`. Never hardcode secrets.
*   Access in Actions via `${{ secrets.PYPI_TOKEN }}`.

---

## 5. Phase 3: uv Core Concepts — Python Env Done Right

### 5.1 Why uv (vs pip/poetry/conda)

*   **Single binary** (Rust) — no Python needed to install.
*   Manages **Python versions** (`uv python pin 3.12`), **virtualenvs** (`uv venv`), and **packages** (`uv add`).
*   **Lockfile** (`uv.lock`) guarantees reproducible installs across machines/CI.
*   Drop-in `pip` replacement but 10-100x faster resolver.

### 5.2 The Key Files

```
pyproject.toml   → human-edited. Project metadata + direct deps.
uv.lock          → machine-generated. Exact pinned versions + hashes. COMMIT THIS.
.python-version  → pinned Python version (e.g., 3.12). COMMIT THIS.
.venv/           → virtual environment folder. NEVER COMMIT (in .gitignore).
```

### 5.3 Essential uv Commands

| Goal | Command | Notes |
|---|---|---|
| **Create project** | `uv init my-app` | Creates `my-app/` with `pyproject.toml`, `src/`, `README`, `.git` + `.gitignore` |
| **Create/app mode** | `uv init --app my-app` | No installable package, just scripts (scripts/services) |
| **Create/library mode** | `uv init --lib my-app` | Installable library (`src/my_app/`) |
| **Python version** | `uv python pin 3.12` | Writes `.python-version`. Installs Python if missing. |
| **List Pythons** | `uv python list` | Available interpreters |
| **Create venv** | `uv venv --python 3.12` | Creates `.venv/` |
| **Add dependency** | `uv add fastapi` | Adds to `pyproject.toml` + updates `uv.lock` + installs |
| **Add dev dep** | `uv add --dev pytest ruff` | Under `[dependency-groups.dev]` or `tool.uv.dev-dependencies` |
| **Add with extras** | `uv add "fastapi[standard]"` | Extras |
| **Remove** | `uv remove fastapi` | Removes + re-locks |
| **Install/Sync** | `uv sync` | Installs *exact* versions from `uv.lock`. Use in CI/fresh clone. |
| **Sync with groups** | `uv sync --group dev` | Include dev deps |
| **Run without activate** | `uv run python main.py` | Auto-uses `.venv`, no `source .venv/bin/activate` needed |
| **Run tool isolated** | `uvx ruff check .` | Like `pipx` — run ephemeral tool without adding to project |
| **Lock only** | `uv lock` | Re-resolve without installing |
| **Upgrade** | `uv lock --upgrade` / `uv lock --upgrade-package fastapi` | Bump versions |
| **Tree** | `uv tree` | Show dependency tree |
| **Pip compat** | `uv pip install -r requirements.txt` | If migrating legacy projects |
| **Build** | `uv build` | Builds `dist/*.whl` + `sdist` |
| **Publish** | `uv publish` | To PyPI (needs `UV_PUBLISH_TOKEN`) |

### 5.4 `pyproject.toml` Anatomy (Production)

```toml
[project]
name = "my-app"
version = "0.1.0"
description = "One-line what it does"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
  "fastapi>=0.115",
  "pydantic>=2.9",
]

# Optional deps
[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.8"]

# uv dev groups (uv-specific, not installed on `pip install .`)
[dependency-groups]
dev = ["pytest>=8", "ruff>=0.8", "mypy>=1.13"]

# Tool configs live here too
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

## 6. Phase 4: End-to-End Pipeline — New Project From Scratch

Copy-paste this sequence. It is the **canonical production pipeline**.

### Step 0 — Create & Navigate

```bash
mkdir -p ~/projects && cd ~/projects
```

### Step 1 — Scaffold with uv (creates git repo automatically)

```bash
uv init --app my-awesome-project
# --app = application (no installable package). Omit for library.
# Adds: pyproject.toml, README.md, main.py or src/, .gitignore, .python-version, .venv

cd my-awesome-project
cat pyproject.toml  # inspect
cat .gitignore      # note: .venv/ already ignored
```

### Step 2 — Pin Python & Verify

```bash
uv python pin 3.12          # or 3.11/3.13 — pick one and stick to it
uv python list              # verify installed
uv run python --version     # should match pin
```

### Step 3 — Initial Commit Locally

```bash
git status
git log --oneline  # uv init already made an initial commit? Check.
# If no commit yet (older uv):
git add .
git commit -m "feat: initial scaffold via uv init"
```

### Step 4 — Create GitHub Repo & Push

**Option A — GitHub CLI (fastest):**

```bash
gh repo create my-awesome-project --public --source=. --remote=origin --push
# --public or --private
# --source=. links local dir, --push does initial push
# Done. Skip to Step 5.
```

**Option B — Manual (if no `gh`):**

```bash
# 1. On GitHub.com → New repository → Name: my-awesome-project → Create (no README/.gitignore)
# 2. Link & push
git remote add origin git@github.com:YOUR_USERNAME/my-awesome-project.git
git branch -M main
git push -u origin main  # -u sets upstream so future `git push` works bare
```

Verify: `git remote -v` should show `origin`.

### Step 5 — Add Dependencies (Example Stack)

```bash
# Runtime
uv add fastapi uvicorn pydantic python-dotenv

# Dev (tests, lint, types)
uv add --dev pytest pytest-cov ruff mypy pre-commit httpx

# Verify
uv tree
cat pyproject.toml
```

### Step 6 — Production `.gitignore` (Merge with uv's default)

Ensure this exists — uv generates a minimal one, expand it:

```bash
cat > .gitignore <<'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.venv/
venv/
*.egg-info/
dist/
build/

# Env & secrets
.env
.env.*
!.env.example

# OS / IDE
.DS_Store
.idea/
.vscode/
*.swp
*.swo

# uv
.uv/

# Coverage & tools
.coverage
htmlcov/
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Logs
*.log
EOF
git add .gitignore && git commit -m "chore: harden .gitignore for production"
```

### Step 7 — Add Tooling Configs

**`ruff` + `mypy` + `pytest` — already in `pyproject.toml`:**

```toml
# Append to pyproject.toml if not present
[tool.ruff]
line-length = 100
target-version = "py312"
lint.select = ["E", "F", "I", "B", "C4", "UP", "SIM"]
lint.ignore = []

[tool.ruff.format]
quote-style = "double"

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers --cov --cov-report=term-missing"
```

**Pre-commit (runs checks before each `git commit`):**

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.6
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: detect-private-key
```

```bash
uv run pre-commit install
uv run pre-commit run --all-files  # first run
git add .pre-commit-config.yaml pyproject.toml
git commit -m "chore: add ruff/mypy/pre-commit tooling"
```

### Step 8 — Project Structure (Production Layout)

```
my-awesome-project/
├── .github/
│   ├── workflows/ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── src/my_awesome_project/  # or just my_awesome_project/ for --app
│   ├── __init__.py
│   ├── main.py
│   └── core/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_main.py
├── .python-version
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── uv.lock
└── README.md
```

```bash
mkdir -p src/my_awesome_project tests
touch src/my_awesome_project/__init__.py tests/__init__.py
```

### Step 9 — README & License

```bash
# README.md — minimal production template
cat > README.md <<'EOF'
# my-awesome-project

One-sentence description of what this does.

## Quickstart

```bash
# 1. Clone
git clone git@github.com:YOUR_USERNAME/my-awesome-project.git
cd my-awesome-project

# 2. Install (requires uv: https://docs.astral.sh/uv/)
uv sync

# 3. Run
uv run python -m my_awesome_project.main
# or
uv run pytest
```

## Development

```bash
uv sync --group dev
uv run ruff check .
uv run ruff format .
uv run mypy src/
uv run pytest --cov
```

EOF

# License (MIT example)
# gh repo license MIT  # or pick at creation, or add manually
git add README.md
git commit -m "docs: add production README"
```

### Step 10 — First Feature Branch + PR Flow

```bash
git switch -c feat/health-endpoint
# ... edit code ...
uv run ruff check . --fix
uv run pytest -q
git add -p              # stage hunks interactively (more precise than git add .)
git commit -m "feat(api): add /health endpoint with tests"
git push -u origin feat/health-endpoint

# Create PR via CLI
gh pr create --title "feat(api): add /health endpoint" --body "Closes #1

- Adds GET /health
- Includes unit test
- Tested with: uv run pytest
" --assignee "@me"

# After review + CI green → merge on GitHub, then:
git switch main
git pull origin main
git branch -d feat/health-endpoint
```

### Step 11 — Versioning & Release

```bash
# On main, after PR merged and tests pass
git tag -a v0.1.0 -m "release: v0.1.0 — initial health endpoint"
git push origin v0.1.0

# On GitHub: Releases → Draft new release → choose tag v0.1.0 → Generate release notes → Publish
```

---

## 7. Phase 5: Daily Workflows & Branching Strategies

### 7.1 The 30-Second Daily Loop (Trunk-Based — Recommended for Most Teams)

```bash
git switch main
git pull origin main          # start fresh
git switch -c feat/short-desc # branch
# ... code ...
uv add <new-dep>              # if needed
uv run ruff check . --fix && uv run pytest -q
git add -p && git commit -m "feat: ..."
git push -u origin feat/short-desc
gh pr create --fill           # or via UI
# Wait for CI + review → merge → clean up
git switch main && git pull && git branch -d feat/short-desc
```

### 7.2 Branching Strategy Comparison

| Strategy | How | Pros | When to Use |
|---|---|---|---|
| **GitHub Flow** (recommended) | `main` + short-lived `feat/*` branches → PR → merge | Simple, fast, CI-gated | Solo + small teams, continuous deployment |
| **Trunk-Based** | Same as GitHub Flow but branches live <1 day | Fastest, forces small PRs | High-velocity teams, 2–10 devs |
| **Git Flow** | `main` + `develop` + `feature/*` + `release/*` + `hotfix/*` | Structured releases | Scheduled versioned releases (monthly), large teams |
| **Forking Flow** | Forks + upstream PRs | Safe for strangers | Open-source |

**Production default:** Start with **GitHub Flow / Trunk-Based**. Add `develop` only if you need a staging branch.

### 7.3 Naming Conventions

*   Branches: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`, `hotfix/` + kebab-case → `feat/user-auth`
*   Commits: Conventional Commits (see 3.5)
*   Tags: `vMAJOR.MINOR.PATCH` → `v2.1.0`

### 7.4 Handling Conflicts (Inevitable)

```bash
git fetch origin
git merge origin/main          # or git rebase origin/main
# → CONFLICT in file.py
# 1. Open file.py, resolve <<<<<<< ======= >>>>>>> markers
# 2. Test:
uv run pytest -q
# 3. Mark resolved:
git add file.py
git commit  # or git rebase --continue
git push
```

### 7.5 Stashing, Cherry-Picks, Hotfixes

```bash
# Stash dirty work to switch branches
git stash push -m "wip: half-done auth"
git switch main
# ... do hotfix ...
git switch feat/auth && git stash pop

# Hotfix flow
git switch main && git pull
git switch -c hotfix/critical-bug
# ... fix ...
git commit -m "fix: patch critical auth bypass"
git push -u origin hotfix/critical-bug
gh pr create --title "hotfix: critical auth bypass"
# After merge → tag patch release
git switch main && git pull
git tag v0.1.1 && git push origin v0.1.1

# Cherry-pick a commit from another branch
git cherry-pick a1b2c3d
```

---

## 8. Phase 6: Production Hardening Checklist

Copy this into your repo's `CONTRIBUTING.md` or keep as a mental gate before `v1.0.0`.

### Repo Hygiene

- [ ] `main` protected: require PR + 1 approval + CI pass
- [ ] `CODEOWNERS` file (`.github/CODEOWNERS`): `* @your-team`
- [ ] Templates: `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/*.md`
- [ ] `LICENSE` present, `README` has install + run + dev instructions
- [ ] `.gitignore` covers `.venv`, `.env`, caches, `dist/`, `*.pyc`
- [ ] No secrets in history — scan with `gitleaks` or `detect-private-key` hook

### Git Discipline

- [ ] Conventional Commits enforced (via `commitlint` or PR title check)
- [ ] No direct pushes to `main` — ever
- [ ] Small PRs, linear history preferred (`Squash and merge` for features)
- [ ] Tags are annotated (`git tag -a`) and pushed, releases have notes
- [ ] `git fetch --prune` hygiene — deleted branches cleaned

### uv / Python Discipline

- [ ] `.python-version` pinned (e.g., `3.12`), `requires-python` in `pyproject.toml` matches
- [ ] `uv.lock` committed (never `.gitignore` it) — ensures reproducible CI
- [ ] `uv sync` used in CI/Docker, not `uv pip install`
- [ ] `uv add --dev` separates dev deps, `uv sync --group dev` for contributors
- [ ] `uv tree` reviewed for bloat / duplicate deps
- [ ] `uv run` used everywhere — no manual `source .venv/bin/activate` in docs/CI

### Quality Gates

- [ ] `pre-commit` installed + CI runs same hooks
- [ ] Formatter: `ruff format`, Linter: `ruff check`, Types: `mypy --strict` (or at least default)
- [ ] Tests: `pytest` + `coverage` ≥ 80% on core paths, CI fails below threshold
- [ ] `uv run pytest --cov --cov-fail-under=80`

### Security

- [ ] `uv lock` hashes committed, Dependabot / Renovate enabled for updates
- [ ] Secrets via GitHub `Settings → Secrets`, never in `pyproject.toml` / code
- [ ] `uv publish` uses trusted publishing (OIDC) or token in secrets

---

## 9. Phase 7: CI/CD with GitHub Actions + uv

### 9.1 Minimal CI (`.github/workflows/ci.yml`)

Runs on every push/PR: install → lint → typecheck → test.

```yaml
# .github/workflows/ci.yml
name: ci

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          python-version: "3.12"

      - name: Install deps (locked)
        run: uv sync --group dev

      - name: Lint
        run: uv run ruff check .

      - name: Format check
        run: uv run ruff format --check .

      - name: Type check
        run: uv run mypy src/

      - name: Tests
        run: uv run pytest --cov --cov-report=term-missing --cov-fail-under=80
```

### 9.2 Release Workflow (Tag → Publish to PyPI)

```yaml
# .github/workflows/release.yml
name: release

on:
  push:
    tags: ["v*"]

permissions:
  contents: write
  id-token: write  # for trusted publishing

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          python-version: "3.12"

      - name: Build
        run: uv build

      - name: Publish to PyPI
        # Option A: Trusted publishing (no token needed — configure on PyPI first)
        run: uv publish
        # Option B: Token
        # env:
        #   UV_PUBLISH_TOKEN: ${{ secrets.PYPI_TOKEN }}
        # run: uv publish

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          files: dist/*
```

### 9.3 Dependabot for `uv` (auto-update PRs)

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"  # Dependabot reads pyproject.toml + uv.lock via pip ecosystem
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

### 9.4 Docker (Optional — Production Deploy)

```dockerfile
# Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project  # cache deps layer
COPY . .
RUN uv sync --frozen

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "-m", "my_awesome_project.main"]
```

---

## 10. Cheat Sheet & Troubleshooting

### 10.1 Daily Cheatsheet (Print This)

```bash
# Status & history
git status                          # what's changed
git diff && git diff --staged       # unstaged vs staged
git log --oneline --graph --all -n 20
git show HEAD                       # last commit detail

# Branching
git switch -c feat/x                # create + switch
git branch -a                       # all branches
git switch main && git pull         # update main
git branch -d feat/x                # delete (merged)
git branch -D feat/x                # force delete (unmerged)

# Staging & commits
git add -p                          # patch/interactive add
git add <file> && git commit -m "feat: ..."
git commit --amend -m "fix: typo"   # fix last commit (local only)
git commit --amend --no-edit        # add staged files to last commit

# Sync
git fetch origin --prune            # download + clean
git pull origin main                # fetch + merge
git push                            # push (if -u set)
git push -u origin feat/x           # first push sets upstream

# Undo (see decision tree in 3.4)
git restore <file>                  # discard unstaged
git restore --staged <file>         # unstage
git revert <hash>                   # safe undo of pushed commit
git reset --soft HEAD~1             # undo last local commit, keep changes

# uv
uv sync                             # install from lock (CI / fresh clone)
uv add <pkg>                        # add runtime dep
uv add --dev <pkg>                  # add dev dep
uv remove <pkg>                     # remove
uv run <cmd>                        # run inside venv without activating
uv tree && uv lock --upgrade-package <pkg>
```

### 10.2 Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Permission denied (publickey)` on push | SSH not set up | Re-run Section 2.3, check `ssh -T git@github.com` |
| `failed to push — updates were rejected` | Remote has commits you don't have | `git pull --rebase origin main` → resolve → `git push` |
| `uv: command not found` | Shell not reloaded | `source ~/.local/bin/env` or restart terminal |
| `ERROR: Failed to pin Python` | Python version not available | `uv python install 3.12` then `uv python pin 3.12` |
| `pre-commit` blocks commit | Lint/type error | Run `uv run ruff check . --fix`, fix mypy errors, `git add` fix |
| Committed `.env` by mistake | Secret in history | `git rm --cached .env`, add to `.gitignore`, rotate secret, consider `git filter-repo` or BFG for history purge |
| Merge conflict markers `<<<<<<<` | Concurrent edits | Edit file, remove markers, keep correct code, `git add` + `git commit` |
| `.venv` shows in `git status` | Not ignored | Add `.venv/` to `.gitignore`, `git rm -r --cached .venv` |
| `uv sync` fails with lock mismatch | `pyproject.toml` edited manually | Run `uv lock` to re-resolve, then `uv sync` |
| Want to change last commit message | Local only | `git commit --amend -m "new message"` then `git push --force-with-lease` (only if not shared) |
| Need to move commit to another branch | Wrong branch | `git branch feat/fix` (creates branch at current commit), `git reset --hard origin/main` on original, switch and push |

### 10.3 Recommended `.github/` Additions

```
.github/
├── workflows/
│   ├── ci.yml
│   └── release.yml
├── CODEOWNERS          # * @your-username
├── PULL_REQUEST_TEMPLATE.md
└── ISSUE_TEMPLATE/
    ├── bug_report.md
    └── feature_request.md
```

**`PULL_REQUEST_TEMPLATE.md`:**

```markdown
## What & Why
<!-- Link issue: Closes #... -->

## Changes
- 

## How to Test
```bash
uv sync --group dev && uv run pytest -q
```

## Screenshots (if UI)

## Checklist
- [ ] Tests added/updated
- [ ] `uv run ruff check .` passes
- [ ] Docs updated
```

### 10.4 Learning Path (In Order)

1.  **Day 1:** Run the pipeline in Section 6 end-to-end on a throwaway repo. Push 3 branches, open 3 PRs, merge them.
2.  **Day 2:** Break things on purpose — create a conflict, stash, revert, cherry-pick. Recovery builds confidence.
3.  **Day 3:** Add CI (9.1) and watch it fail/pass. Protect `main`.
4.  **Week 1:** Use Conventional Commits religiously. Tag `v0.1.0`.
5.  **Ongoing:** `git log --graph` is your friend — read history weekly.

### 10.5 Quick Reference: When to Use What

```
I want to...                         Do...
─────────────────────────────────────────────────────────
Start a new project        → uv init my-proj && gh repo create ...
Add a package              → uv add <pkg>  (not pip install)
Run code/tests             → uv run python ... / uv run pytest
Share my work              → git push + PR
Get others' work           → git fetch + git pull
Fix a bug on main          → hotfix/* branch → PR → tag vX.Y.Z+1
Undo a pushed mistake      → git revert <hash> → push
Clean local history        → git rebase -i HEAD~3 (only if not pushed)
See what will be pushed    → git log origin/main..HEAD
Nuke local changes         → git restore . && git clean -fd  (CAREFUL)
```

---

## Appendix: One-Command Project Bootstrap Script

Save as `~/bin/new-py-project` (`chmod +x`):

```bash
#!/usr/bin/env bash
set -euo pipefail
NAME="${1:?Usage: new-py-project <name> [--private]}"
VISIBILITY="${2:---public}"

uv init --app "$NAME"
cd "$NAME"
uv python pin 3.12
uv add --dev pytest pytest-cov ruff mypy pre-commit httpx
uv run pre-commit install 2>/dev/null || true

# Harden .gitignore if needed (see Section 6 Step 6)

gh repo create "$NAME" "$VISIBILITY" --source=. --remote=origin --push
echo "✅ $NAME ready at $(git remote get-url origin)"
echo "   Next: cd $NAME && git switch -c feat/initial"
```

---

**Version:** 1.0 — August 2026 | **Tested with:** `uv 0.11.x`, `git 2.5x`, `GitHub CLI 2.6x` on Ubuntu 24.04
**Feedback:** Open an issue or PR on this repo — this guide is itself versioned with git.
