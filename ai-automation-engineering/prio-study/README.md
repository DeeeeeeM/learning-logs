# Weekend Learning Roadmap for AI Engineering (Large Python Codebase)

## Goal

Successfully remodel and maintain a large Python AI subtitling infrastructure using GitHub Copilot Pro while developing the skills to work effectively with AI coding assistants.

---

## Development Tools

* Python 3.12
* uv (or Conda if CUDA/scientific packages are required)
* Ruff
* Pyright
* pytest
* Docker
* Git
* Windows Terminal

Optional:

* Ollama
* Qwen Coder
* DeepSeek Coder

---

# Weekend Learning Priorities

## 1. Context Engineering ⭐⭐⭐⭐⭐

**Why**

The most important skill for working with AI on large codebases.

Instead of providing the entire repository, learn to provide only the relevant context needed for the task.

### Deliverable

Create an `AI_CONTEXT.md` (or `AGENTS.md`) containing:

* Project overview
* Repository structure
* Coding conventions
* Architecture
* Common commands
* Constraints
* Testing workflow
* Important business rules

### Resources

* Anthropic — Context Engineering guides
* OpenAI Codex documentation
* Aider documentation (repository maps and workflow)

---

## 2. Prompt Engineering for Software Engineering ⭐⭐⭐⭐⭐

**Why**

AI performs significantly better when given structured prompts.

### Learn

* Goal-based prompting
* Architecture prompts
* Refactoring prompts
* Debugging prompts
* Code review prompts
* Asking AI to compare multiple approaches before implementation

### Prompt Template

```
Goal:
...

Current architecture:
...

Constraints:
...

Relevant files:
...

Expected output:
1. Explain the approach.
2. Identify risks.
3. Implement.
4. Explain why.
```

### Resources

* Anthropic Prompt Engineering Guide
* OpenAI Prompting Guide
* Simon Willison's articles on LLM workflows

---

## 3. Git for Large Refactors ⭐⭐⭐⭐☆

**Why**

Allows safe experimentation and easy recovery while AI assists with code changes.

### Learn

* git worktree
* git rebase -i
* git reflog
* git cherry-pick
* git stash

### Resources

* Learn Git Branching
* Official Git documentation

---

## 4. GitHub Copilot Workflow ⭐⭐⭐⭐☆

Learn how to effectively use:

* Inline completions
* Copilot Chat
* Agent mode
* Workspace context
* Custom instructions
* Keyboard shortcuts

### Resource

GitHub Copilot documentation

---

# Recommended Books

## Read later (not this weekend)

* Architecture Patterns with Python — Harry Percival & Bob Gregory
* Designing Data-Intensive Applications — Martin Kleppmann
* Clean Architecture — Robert C. Martin

---

# Recommended YouTube Channels

* Anthropic
* OpenAI
* Fireship
* ArjanCodes
* Hussein Nasser

---

# AI Development Workflow

For every feature or refactor:

1. Understand the subsystem.
2. Gather only the relevant context.
3. Write a structured prompt.
4. Ask Copilot to propose a solution.
5. Review the generated code.
6. Run linting and tests.
7. Commit small, focused changes.
8. Repeat.

---

# Long-Term Learning Roadmap

## Weekend 1

* Context Engineering
* Prompt Engineering
* Git for Refactoring
* GitHub Copilot Workflow

---

## Week 2

* Python Architecture
* Testing Strategy
* Repository Documentation

---

## Week 3+

* AI Engineering Best Practices
* RAG
* Agent Design
* LLM Evaluation
* Advanced System Design

---

# Success Criteria

By the end of the weekend, you should be able to:

* Write structured prompts for complex coding tasks.
* Provide effective repository context to AI.
* Safely perform large refactors using Git.
* Use GitHub Copilot efficiently for day-to-day development.
* Create an AI-friendly repository with clear documentation and architecture notes.

The goal is not to let AI write all of your code. The goal is to become highly effective at directing AI to help you safely evolve a complex software system.
