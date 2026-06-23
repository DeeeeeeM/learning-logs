# 🗂️ Git → GitHub → GitLab Learning Path

> Simple, linear path — learn Git first, then apply it to GitHub for personal projects, then GitLab for team/work repos. All workflows are VSCode-first.

No fixed dates. Work through each stage before moving to the next.

---

## 🔵 Stage 1 — Git Core (Local)

**Goal:** Understand what Git is doing locally before touching any remote. Everything else depends on this.

### What to Learn

- What version control is and why it matters
- Installing Git + first-time config (`user.name`, `user.email`)
- The three states: working directory → staging area → commit history
- Core commands: `init`, `add`, `commit`, `status`, `log`, `diff`
- Undoing things: `restore`, `reset`, `revert` — and when to use each
- Branching: `branch`, `checkout`/`switch`, `merge`
- Merge conflicts: what they are, how to read them, how to resolve them
- `.gitignore` — what to ignore and why (secrets, `__pycache__`, `.env`)
- Stashing: `git stash`, `stash pop` — saving work without committing

### Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) — free, the definitive reference; Chapters 1–3 cover everything in Stage 1. Widely recommended across Reddit and GitHub community discussions as the single best Git resource.
- [Learn Git Branching](https://learngitbranching.js.org) — free, interactive browser-based visualizer; consistently the #1 recommended resource on Reddit for understanding branches and merge visually before touching a terminal
- [Oh My Git!](https://ohmygit.org) — free, open source game that teaches Git commands by showing the repo graph in real time; great for the first weekend
- [Git official docs — gittutorial](https://git-scm.com/docs/gittutorial) — short official tutorial for absolute first steps

### VSCode Setup (Stage 1)

Install these extensions before starting:
- **GitLens** (`eamodio.gitlens`) — shows blame, history, and branch visualization inline; the most recommended Git extension on VSCode Reddit threads
- **Git Graph** (`mhutchie.git-graph`) — visual commit graph inside VSCode, replaces needing a separate GUI

Daily workflow in VSCode:
1. Make changes to files
2. Open **Source Control** panel (`Ctrl+Shift+G`) — stage files with `+`
3. Write a commit message and hit ✓ to commit
4. Use Git Graph to inspect history visually

### Practice Project

Create a local repo for one of your existing `yt-toolkits` scripts:
- `git init` inside the folder
- Add a `.gitignore` (ignore `.env`, `__pycache__`, `*.pyc`, `outputs/`)
- Make 5+ commits — one per logical change, not one giant dump
- Create a `dev` branch, make changes, merge back to `main`
- Deliberately create a merge conflict, then resolve it

**Milestone:** Comfortable with the full local Git loop — stage, commit, branch, merge, resolve conflicts — without needing to look up every command.

---

## 🟢 Stage 2 — GitHub (Remote + Portfolio)

**Goal:** Push your local repos to GitHub and learn remote collaboration concepts. This is where your portfolio lives.

### What to Learn

- Creating a GitHub account and first remote repo
- SSH key setup — authenticating without a password every push
- Remote commands: `remote add`, `push`, `pull`, `fetch`, `clone`
- The difference between `fetch` and `pull`
- Pull Requests — opening, reviewing, merging a PR (even solo, for practice)
- GitHub Issues — linking commits to issues with `closes #N` in commit messages
- Branch protection rules — why `main` should be protected
- GitHub Actions basics — automated checks that run on every push (linting, tests)
- Writing good READMEs — your portfolio depends on this
- GitHub Pages — hosting a static site from a repo (useful for portfolio)

### Resources

- [GitHub Skills](https://skills.github.com) — free, official, interactive courses built by GitHub; covers Introduction to GitHub, Code with Codespaces, Review Pull Requests, and more. Each course is a guided hands-on repo exercise.
- [Pro Git Book — Chapter 6](https://git-scm.com/book/en/v2/GitHub-Account-Setup-and-Configuration) — covers GitHub workflows specifically
- [GitHub Docs — Hello World](https://docs.github.com/en/get-started/quickstart/hello-world) — official quickstart, good for first push
- [Colt Steele — Git & GitHub Bootcamp (Udemy)](https://www.udemy.com/course/git-and-github-bootcamp/) — paid (~$10 on sale), the most consistently recommended paid course on Reddit for covering both Git and GitHub end-to-end with great explanations

### VSCode Setup (Stage 2)

- **GitHub Pull Requests** (`GitHub.vscode-pull-request-github`) — create, review, and merge PRs directly inside VSCode without opening a browser
- Sign in to GitHub in VSCode: `Ctrl+Shift+P` → "GitHub: Sign In"
- Clone repos directly from VSCode: `Ctrl+Shift+P` → "Git: Clone" → paste GitHub URL

Daily workflow:
1. Pull latest: `git pull origin main`
2. Create a feature branch: `git switch -c feature/my-thing`
3. Work, stage, commit
4. Push branch: `git push -u origin feature/my-thing`
5. Open PR via GitHub Pull Requests extension inside VSCode
6. Merge → delete branch → pull main again

### Practice Project

Push your `learning-logs` repo to GitHub:
- Set up SSH key, push the full repo
- Write a proper README (already done ✅)
- Open a pull request from a `dev` branch — merge it
- Set up a simple GitHub Actions workflow that runs `echo "pushed"` on every push to `main` — just to understand the CI trigger
- Pin the repo on your GitHub profile

**Milestone:** Comfortable pushing, pulling, opening PRs, and reading GitHub Actions logs. Profile has at least one clean, documented public repo.

---

## 🟡 Stage 3 — GitLab (Work + CI/CD)

**Goal:** Get fluent in GitLab specifically — since your team already uses it for work. Focus on the differences from GitHub and on CI/CD pipelines, which is a real skill for your AI Engineer target role.

### What to Learn

- GitLab vs. GitHub — key differences: Merge Requests (not PRs), GitLab CI/CD built-in, `.gitlab-ci.yml`
- GitLab project structure — groups, projects, namespaces
- Merge Requests — creating, reviewing, approving, and merging MRs
- GitLab CI/CD basics:
  - `.gitlab-ci.yml` — pipeline config file, stages, jobs, scripts
  - Runners — what they are, shared vs. self-hosted
  - Pipeline stages: `build → test → deploy`
  - Artifacts — saving output files between jobs
  - Variables — storing secrets safely in GitLab CI settings
- Personal Access Tokens — for API access and VSCode auth
- GitLab Issues and Boards — basic project management inside GitLab

### Resources

- [GitLab University — GitLab with Git Essentials](https://university.gitlab.com/courses/gitlab-with-git-essentials-s2) — free, official, self-paced; covers Git fundamentals inside the GitLab context
- [GitLab University — GitLab CI/CD for beginners](https://university.gitlab.com/courses/continuous-integration-and-delivery-cicd-with-gitlab) — free, official CI/CD fundamentals course
- [GitLab Docs — CI/CD Quickstart](https://docs.gitlab.com/ee/ci/quick_start/) — the fastest way to write your first `.gitlab-ci.yml`
- [GitLab Docs — `.gitlab-ci.yml` reference](https://docs.gitlab.com/ee/ci/yaml/) — the complete pipeline config reference; bookmark this
- [TechWorld with Nana — GitLab CI/CD (YouTube)](https://www.youtube.com/watch?v=qP8kir2GUgo) — free, highly rated practical walkthrough of GitLab CI/CD from scratch

### VSCode Setup (Stage 3)

- **GitLab Workflow** (`GitLab.gitlab-workflow`) — official GitLab extension; authenticate with a Personal Access Token; gives you:
  - Pipeline status in the VSCode status bar
  - View and create Merge Requests from inside VSCode
  - Validate `.gitlab-ci.yml` without pushing (`Ctrl+Shift+P` → "GitLab: Validate GitLab CI/CD Configuration")
  - View issues and MRs in the sidebar

Setup steps:
1. Install the GitLab Workflow extension
2. Generate a Personal Access Token in GitLab (Settings → Access Tokens → `api` scope)
3. `Ctrl+Shift+P` → "GitLab: Authenticate" → paste token
4. Open a cloned GitLab repo — pipeline status appears in the bottom status bar

### Practice Project

Write your first `.gitlab-ci.yml` for one of your `learning-logs` projects:

```yaml
stages:
  - lint
  - test

lint-python:
  stage: lint
  image: python:3.11
  script:
    - pip install flake8
    - flake8 . --max-line-length=100

run-tests:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - python -m pytest tests/ -v
  artifacts:
    paths:
      - test-results/
    expire_in: 1 week
```

Steps:
1. Add this `.gitlab-ci.yml` to an existing project repo
2. Push to GitLab — watch the pipeline run in the Pipelines tab
3. Break it intentionally (bad syntax) — read the error, fix it
4. Add a secret variable (e.g., an API key) via GitLab → Settings → CI/CD → Variables; use it in a job script as `$MY_SECRET`
5. Validate the `.gitlab-ci.yml` inside VSCode before pushing using the GitLab extension

**Milestone:** A working `.gitlab-ci.yml` pipeline on one of your work/learning repos with at least 2 stages, plus the VSCode extension fully set up and authenticated.

---

## 📋 Quick Command Reference

### Git Core
```bash
git init                        # start a new repo
git add .                       # stage all changes
git commit -m "message"         # commit with message
git status                      # see what's staged/unstaged
git log --oneline               # compact commit history
git diff                        # see unstaged changes
git switch -c feature/name      # create + switch to new branch
git merge feature/name          # merge branch into current
git stash                       # save uncommitted work temporarily
git stash pop                   # restore stashed work
```

### Remote (GitHub / GitLab)
```bash
git remote add origin <url>     # connect local repo to remote
git push -u origin main         # first push, sets upstream
git push                        # subsequent pushes
git pull                        # fetch + merge remote changes
git fetch                       # fetch without merging
git clone <url>                 # copy a remote repo locally
```

### Undo
```bash
git restore <file>              # discard unstaged changes to a file
git restore --staged <file>     # unstage a file (keep changes)
git reset --soft HEAD~1         # undo last commit, keep changes staged
git revert <commit>             # create a new commit that undoes a commit
```

---

## 🔧 Recommended VSCode Extensions Summary

| Extension | ID | Purpose |
|---|---|---|
| GitLens | `eamodio.gitlens` | Blame, history, branch view inline |
| Git Graph | `mhutchie.git-graph` | Visual commit graph |
| GitHub Pull Requests | `GitHub.vscode-pull-request-github` | PRs inside VSCode |
| GitLab Workflow | `GitLab.gitlab-workflow` | Pipeline status, MRs, CI validation |

---

## ✅ Completion Checklist

- [ ] **Stage 1:** Can init, commit, branch, merge, and resolve conflicts locally without googling
- [ ] **Stage 2:** `learning-logs` repo on GitHub, public, SSH-authenticated, first PR opened and merged
- [ ] **Stage 3:** `.gitlab-ci.yml` running on a work/learning repo with 2+ stages; GitLab extension in VSCode showing pipeline status

---

*Git is infrastructure. Learn it once, use it on every project forever.*
