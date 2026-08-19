# AI Automation Engineering Roadmap

> Target role: customer-facing AI Automation / AI Engineer in a small, high-ownership team.  
> Target date: June 2027.  
> Rule: every phase must ship a company-grade project, not just a tutorial clone.

---

## Roadmap Focus

This roadmap is structured around the capabilities required for modern AI Automation / AI Engineer roles:

- Python AI applications and automation workflows
- Full-stack product delivery
- REST, GraphQL, webhooks, SDK integrations, OAuth
- MCP servers, tools, resources, and client workflows
- LLM apps, RAG, agents, structured outputs, evaluation
- CRM / ERP / ticketing / collaboration system integrations
- Clean code, testing, CI/CD, deployment, demos, and support

## What You Need To Fully Master

These are the skills that move you from "can build demos" to "hireable for this exact role":

1. Python delivery fundamentals: FastAPI, background jobs, validation, testing, packaging, async I/O.
2. Full-stack execution: React or Next.js frontend, forms, tables, auth flows, dashboard UX.
3. Integration engineering: REST, GraphQL, webhooks, SDKs, retries, pagination, rate limits, idempotency.
4. Authentication and security: OAuth, API keys, RBAC, secret handling, webhook verification, audit logging.
5. MCP engineering: server design, tools, resources, prompts, client workflows, real integrations.
6. LLM application design: structured outputs, tool use, agent loops, RAG, prompt orchestration.
7. Evaluation and observability: golden datasets, LLM-as-judge, RAGAS/DeepEval, tracing, cost/latency tracking.
8. Deployment and operations: Docker, CI/CD, cloud hosting, environment configs, monitoring, incident handling.
9. Customer delivery: requirement discovery, solution design docs, demos, handoff docs, post-deploy support.

If you do not become strong in items 3, 4, 5, and 9, you will still look like a hobbyist builder rather than a company-grade AI engineer.

---

## Stage Map

| Stage | Phase | Title | Outcome |
|---|---|---|---|
| Stage 1 | Phase 1 | Junior AI Developer | Can build and expose basic AI automations safely |
| Stage 2 | Phase 2 | AI Automation Developer | Can deliver CRM-centered business workflows end to end |
| Stage 3 | Phase 2.5 | AI Engineer | Can build production-style AI systems with RAG, evals, security, and MCP |
| Stage 4 | Phase 3 | Mid-Level AI Engineer / Solutions Engineer | Can solve customer operational problems with integrated AI systems |
| Stage 5 | Phase 4 | Senior AI Engineer Track | Can package, deploy, explain, and defend production-ready solutions across domains |

Note: Stage 5 is a senior trajectory stage, not automatic proof of true seniority. Actual seniority also requires repeated delivery, architecture judgment, and ownership under real constraints.

---

## Progress Tracker

| Phase | Focus | Stage | Status | Exit Milestone |
|---|---|---|---|---|
| Phase 1 | Workflow automation, FastAPI, LLM utilities, security basics | Junior AI Developer | In Progress | 2 workflow automations + reusable LLM service + tested API |
| Phase 2 | CRM automation, nurturing, reporting, integration patterns | AI Automation Developer | Not Started | Working CRM pipeline with reporting and operator UI |
| Phase 2.5 | Security, RAG, evals, observability, Docker, MCP | AI Engineer | Not Started | Deployed authenticated AI system with metrics and MCP support |
| Phase 3 | Customer ops systems, intake, document automation, dashboards | Mid-Level AI Engineer / Solutions Engineer | Not Started | Multi-system operational solution with demo and support docs |
| Phase 4 | Content automation, portfolio, delivery polish, domain expansion | Senior AI Engineer Track | Not Started | Portfolio with production-style case studies and deployment proof |

---

## Stage 1: Junior AI Developer

**Phase:** Phase 1  
**Goal:** Build reliable AI automations and Python services that another system can safely call.

### You must master

- n8n or Make fundamentals
- FastAPI request/response modeling with `pydantic`
- `.env` secrets, config hygiene, API key auth
- calling LLM APIs with retries and structured output
- logging, validation, error handling
- basic tests for utility modules and endpoints

### Company-grade projects

1. `n8n-email-to-task/`
   Internal operations workflow: classify inbound emails, create structured tasks, alert on urgency, and log outcomes.
2. `n8n-lead-intake-form/`
   Webhook-driven intake workflow with validation, secret verification, and routing logic.
3. `prompt-toolkit/`
   Reusable `llm_utils.py` package with provider abstraction, schema validation, retries, and usage logging.
4. `llm-service-api/`
   FastAPI wrapper for internal AI actions with auth, input validation, tests, and OpenAPI docs.

### Stage exit standard

You are ready to leave this stage when you can build a workflow plus a Python API without copy-pasting from tutorials, and you can explain how validation, auth, retries, and logs work.

---

## Stage 2: AI Automation Developer

**Phase:** Phase 2  
**Goal:** Deliver business workflows tied to CRM systems, lifecycle automation, and reporting.

### You must master

- HubSpot or GoHighLevel data model
- CRM lifecycle design: contacts, deals, stages, properties
- webhook-driven business logic
- sequence automation and attribution tracking
- integration reliability: retries, dedupe, idempotency, pagination
- simple operator-facing frontend or dashboard

### Company-grade projects

1. `crm-lead-pipeline/`
   Intake to CRM pipeline with source tracking, stage assignment, deduplication, and audit logging.
2. `lead-nurture-sequence/`
   Multi-step personalized sequence with stop conditions, reply detection assumptions, and reporting.
3. `pipeline-reporting-sheet/`
   Weekly performance report with conversion metrics and operational summaries.
4. New expectation:
   Add a lightweight operator UI in React or Next.js to view intake status, pipeline metrics, and failed jobs.

### Stage exit standard

You are ready to leave this stage when you can take a lead flow from form submission to CRM record, follow-up sequence, metrics dashboard, and failure recovery path.

---

## Stage 3: AI Engineer

**Phase:** Phase 2.5  
**Goal:** Build secure, measurable, production-style AI systems with retrieval, evaluation, deployment, and MCP.

### You must master

- OWASP LLM and API security basics
- vector databases and chunking tradeoffs
- hybrid retrieval and reranking
- golden datasets, LLM-as-judge, RAGAS or DeepEval
- tracing and observability
- Docker and cloud deployment
- MCP server design: tools, resources, and auth model
- OAuth concepts and scoped access

### Company-grade projects

1. `rag-security-redteam/`
   Threat model and red-team report covering prompt injection, data leakage, and unsafe tool execution.
2. `rag-pipeline-basics/`
   Document ingestion, embedding, retrieval, answer generation, and source citation.
3. `rag-evaluation-framework/`
   Reusable evaluation harness with golden set, synthetic tests, and score reporting.
4. `hybrid-search-upgrade/`
   Dense + sparse retrieval with measurable accuracy improvements and latency tradeoff notes.
5. `docker-deploy/`
   Containerized FastAPI AI service with Qdrant, auth, rate limiting, and tracing.
6. New required project: `mcp-customer-systems-server/`
   Build an MCP server that exposes at least:
   - a CRM lookup tool
   - a ticket summary tool
   - a customer knowledge resource
   - one safe write action with strict validation

### Stage exit standard

You are ready to leave this stage when you can defend your retrieval choices, show evaluation results, deploy the app, and demonstrate a real MCP workflow that connects AI to external systems.

---

## Stage 4: Mid-Level AI Engineer / Solutions Engineer

**Phase:** Phase 3  
**Goal:** Solve customer operational problems by combining intake, AI processing, retrieval, dashboards, and system integrations.

### You must master

- translating ambiguous requirements into architecture and scope
- multi-system integration design
- document workflows and domain-specific extraction
- operator dashboards and support workflows
- solution demos, implementation notes, and post-deploy runbooks

### Company-grade projects

1. `client-intake-workflow/`
   Customer onboarding flow with validation, CRM sync, classification, notifications, and status visibility.
2. `contract-summarizer/`
   RAG-backed document review tool with structured output, trace logs, and evaluation reports.
3. `matter-pipeline-dashboard/`
   Operational dashboard showing load, SLA risk, overdue items, and trend reporting.
4. New expectation:
   Extend one project beyond legal ops into a broader business system:
   - support desk triage
   - internal knowledge assistant
   - sales proposal assistant
   - customer success action board

### Stage exit standard

You are ready to leave this stage when you can run a customer-style demo from problem statement to live workflow, dashboard, and support documentation.

---

## Stage 5: Senior AI Engineer Track

**Phase:** Phase 4  
**Goal:** Prove breadth, production readiness, communication quality, and reusable engineering standards.

### You must master

- content and communication automation as a business workflow
- portfolio packaging that highlights architecture, tradeoffs, and outcomes
- CI/CD, release readiness, and environment management
- cost, latency, and quality comparisons across providers
- stakeholder communication: demos, writeups, handoff docs, incident notes

### Company-grade projects

1. `content-repurposing-pipeline/`
   Multi-format content generation workflow with structured outputs and local-vs-API provider comparison.
2. `automated-email-sequence-builder/`
   Sequence generator that creates drafts and pushes them into a business system through API automation.
3. Portfolio consolidation
   Turn each major project into a case study with:
   - problem
   - architecture
   - security decisions
   - evaluation method
   - deployment proof
   - demo flow
4. New required capstone: `customer-ops-ai-workbench/`
   A polished full-stack app that combines:
   - authenticated frontend
   - FastAPI backend
   - one MCP integration
   - one CRM or ticketing integration
   - one document or knowledge workflow
   - monitoring and support notes

### Stage exit standard

You are ready to present yourself for strong AI Engineer roles when you can show multiple integrated systems, explain tradeoffs cleanly, and walk through one polished capstone that feels like a real internal product.

---

## Phase-by-Phase Build Order

### Phase 1

- Finish the two n8n workflows
- Build `llm_utils.py` as a reusable package, not a loose script
- Create `llm-service-api/` with tests and docs
- Add a minimal test suite and request logging

### Phase 2

- Build the CRM pipeline
- Add nurture automations and weekly reporting
- Add a simple frontend or dashboard for operators

### Phase 2.5

- Build RAG correctly
- Add evaluation before you claim quality
- Deploy with Docker
- Build the MCP server

### Phase 3

- Turn the platform into a customer-style operations solution
- Add demo assets, architecture notes, and runbooks

### Phase 4

- Add content automation breadth
- Consolidate case studies
- Build the full-stack capstone

---

## Mastery Checklist

Use this as the real checklist, not "I watched the tutorial":

| Area | Junior | Functional | Strong | Hireable |
|---|---|---|---|---|
| Python / FastAPI | Can build endpoints | Can structure services | Can test and secure them | Can ship maintainable APIs |
| Frontend | Can build forms | Can build dashboard flows | Can handle auth and async state | Can ship usable operator UIs |
| Integrations | Can call one API | Can manage webhooks and retries | Can handle OAuth and rate limits | Can design reliable multi-system flows |
| LLM apps | Can call a model | Can use structured outputs | Can build RAG and tool use | Can evaluate and monitor quality |
| MCP | Has read docs | Can build a simple tool server | Can add resources and client workflow | Can integrate MCP into customer systems |
| Security | Knows `.env` | Can validate inputs | Can enforce auth and logging | Can design for safe production use |
| Deployment | Runs locally | Can use Docker | Can deploy and observe | Can support a live system |
| Customer delivery | Can explain code | Can demo a workflow | Can write scope and tradeoffs | Can own discovery to support |

You should aim to reach at least `Strong` in every row and `Hireable` in Python/FastAPI, integrations, LLM apps, MCP, and customer delivery.

---

## Highest-Priority Gaps To Close First

If you want the fastest improvement in job-fit, prioritize these in order:

1. MCP server implementation
2. React or Next.js operator UI
3. OAuth and enterprise auth patterns
4. CI/CD plus cloud deployment
5. broader business integrations beyond HubSpot
6. evals, tracing, and support documentation

---

## Folder Structure

```text
ai-automation-engineering/
|
├── README.md
├── progress/
│   └── daily-log.md
|
├── phase-1-foundations/
│   ├── n8n-email-to-task/
│   ├── n8n-lead-intake-form/
│   ├── llm-service-api/
│   └── prompt-toolkit/
|
├── phase-2-crm-automation/
│   ├── crm-lead-pipeline/
│   ├── lead-nurture-sequence/
│   └── pipeline-reporting-sheet/
|
├── phase-2.5-ai-systems-foundations/
│   ├── rag-security-redteam/
│   ├── rag-pipeline-basics/
│   ├── rag-evaluation-framework/
│   ├── hybrid-search-upgrade/
│   ├── docker-deploy/
│   └── mcp-customer-systems-server/
|
├── phase-3-legal-ops/
│   ├── client-intake-workflow/
│   ├── contract-summarizer/
│   └── matter-pipeline-dashboard/
|
└── phase-4-content-and-portfolio/
    ├── content-repurposing-pipeline/
    ├── automated-email-sequence-builder/
    └── customer-ops-ai-workbench/
```

---

## Daily Log Format

Every session logged in `progress/daily-log.md`:

```markdown
## YYYY-MM-DD · Phase X · Stage Name

**Session:** AM / PM / Both
**Hours:** X.X
**Focus:** what you studied or built
**Shipped:** repo changes or outputs completed
**Evidence:** tests, screenshots, demo, deployment, or docs
**Blockers:** what slowed you down
**Next:** the exact next deliverable
```

---

## Target Stack

- Python
- FastAPI
- React or Next.js
- n8n and basic Make literacy
- REST, GraphQL, webhooks, SDK integrations
- OAuth, API keys, RBAC
- MCP servers, tools, resources, clients
- OpenAI, Anthropic, Gemini, Groq, OpenRouter
- SQL plus one NoSQL / vector store
- Qdrant
- Docker
- CI/CD
- Cloud deployment
- observability and evaluation tooling

---

## Final Standard

By the end of this roadmap, your portfolio should show that you can:

- build AI-enabled products, not just scripts
- integrate with real business systems
- expose safe, tested, documented APIs
- build and use MCP servers
- evaluate and monitor AI behavior
- ship customer-facing solutions with clear tradeoff reasoning

That is the threshold for this role family.
