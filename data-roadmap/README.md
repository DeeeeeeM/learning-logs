# Data Path Roadmap

> Target path: Data Analyst -> Data Engineer -> Data Scientist  
> Stretch target: Applied AI / ML roles with production ownership.  
> Rule: every phase must ship a company-grade project, not just a notebook.

---

## Roadmap Focus

This roadmap is structured around the capabilities required for strong Data Analyst, Data Engineer, and Data Scientist progression:

- strong Python for analysis, modeling, and production implementation
- predictive models and advanced analytics
- LLM workflows with RAG, tool calling, routing, and structured outputs
- end-to-end model delivery from dataset prep to deployment
- batch and real-time pipelines
- monitoring, retraining, reliability, and cost control
- cloud or containerized environments
- governance, evaluation, and documentation
- reusable internal services and business-facing communication

## What You Need To Fully Master

These are the skills that move you from "can analyze data" to "can own applied AI/ML systems":

1. SQL and business analysis fundamentals: joins, CTEs, window functions, KPI framing, metric definitions.
2. Python data work: pandas, NumPy, data cleaning, testing, packaging, notebooks plus scripts.
3. Visualization and communication: dashboards, insight writing, tradeoff explanation, stakeholder summaries.
4. Data engineering: batch pipelines, orchestration, modeling layers, data quality checks, warehousing.
5. ML delivery: feature engineering, model training, validation, metrics, experiment tracking, inference design.
6. GenAI systems: embeddings, retrieval, structured outputs, tool calling, evaluation, guardrails.
7. Production operations: Docker, CI/CD, monitoring, alerts, incident notes, retraining cadence.
8. Governance: lineage, documentation, model cards, responsible AI review, access controls.
9. Business translation: convert vague business questions into measurable technical outcomes.

If you do not become strong in items 4, 5, 6, 7, and 9, you will remain analyst-shaped rather than hireable for Applied AI / ML roles.

---

## Stage Map

| Stage | Phase | Title | Outcome |
|---|---|---|---|
| Stage 1 | Phase 1 | Junior Data Analyst | Can query, clean, and explain business data reliably |
| Stage 2 | Phase 2 | Data Analyst | Can deliver full analyses with SQL, Python, statistics, and written recommendations |
| Stage 3 | Phase 3 | Data Engineer | Can build dependable data models, dashboards, and pipelines for repeated use |
| Stage 4 | Phase 4 | Data Scientist | Can build, evaluate, deploy, and explain predictive and GenAI solutions |

Note: This is a progression roadmap, not an automatic title ladder. Real title readiness depends on repeated delivery quality, depth, and business ownership.

---

## Progress Tracker

| Phase | Focus | Stage | Status | Exit Milestone |
|---|---|---|---|---|
| Phase 1 | Python, SQL, Excel, business data fundamentals | Junior Data Analyst | In Progress | 2 analysis utilities + 25 business SQL queries + documented findings |
| Phase 2 | EDA, statistics, advanced SQL, analyst communication | Data Analyst | Not Started | 2 strong analysis case studies with recommendations and stakeholder-ready writeups |
| Phase 3 | dashboards, data modeling, orchestration, warehousing, quality checks | Data Engineer | Not Started | A repeatable analytics pipeline and dashboard stack with tests and refresh logic |
| Phase 4 | predictive ML, GenAI, deployment, evaluation, governance | Data Scientist | Not Started | A deployed or production-like ML/GenAI service with monitoring and documentation |

---

## Stage 1: Junior Data Analyst

**Phase:** Phase 1  
**Goal:** Build strong data fundamentals so your analysis is reproducible, queryable, and business-readable.

### You must master

- Python basics for data tasks
- SQL fundamentals and query debugging
- CSV and spreadsheet hygiene
- exploratory thinking through business questions
- writing findings in plain English
- simple reusable scripts instead of manual repetition

### Company-grade projects

1. `phase-1-foundations/python/subtitle-analyzer/`
   Turn unstructured text into summary metrics, categories, and trend outputs with a clean README.
2. `phase-1-foundations/sql/analytics-queries.sql`
   Build 25 business-style SQL questions covering revenue, retention, top segments, and anomaly slices.
3. New required project: `phase-1-foundations/excel-ops-report/`
   Create a recurring business operations report in Excel using pivots, lookups, cleaning steps, and a short analyst memo.
4. New required project: `phase-1-foundations/ph-ecommerce-analysis/`
   Analyze a local or regional commerce dataset and present actionable findings, not just charts.

### Stage exit standard

You are ready to leave this stage when you can take raw tabular data, clean it, query it, summarize it, and explain what matters to a non-technical stakeholder.

---

## Stage 2: Data Analyst

**Phase:** Phase 2  
**Goal:** Deliver full analyses that combine SQL, Python, statistics, and business recommendations.

### You must master

- pandas deeply: merge, groupby, reshape, null handling, time-based analysis
- NumPy fundamentals for analytical computing
- statistics for analysts: distributions, variance, correlation, hypothesis basics
- advanced SQL: window functions, CTEs, subqueries
- notebook-to-report discipline
- turning findings into decisions and next actions

### Company-grade projects

1. `phase-2-analytics/customer-retention-analysis/`
   Analyze churn or repeat purchase behavior, define drivers, and recommend interventions.
2. `phase-2-analytics/pricing-or-revenue-analysis/`
   Build a case study around pricing, conversion, basket size, or seasonality with quantified recommendations.
3. `phase-2-analytics/sql-python-reporting-pipeline/`
   Combine SQL extraction and pandas transformation into a repeatable reporting flow.
4. New required deliverable:
   Each project must include an executive summary, KPI definitions, assumptions, and a business recommendation section.

### Stage exit standard

You are ready to leave this stage when you can independently answer an ambiguous business question with a clean dataset, a defensible analysis, and a recommendation someone could act on.

---

## Stage 3: Data Engineer

**Phase:** Phase 3  
**Goal:** Move from one-off analysis into dependable data systems, modeled datasets, and reusable reporting layers.

### You must master

- dimensional modeling basics: facts, dimensions, grain, surrogate keys
- ELT thinking and data warehouse structure
- orchestration basics: scheduled jobs, dependencies, retries, alerts
- data quality checks and expectation tests
- dashboard data modeling and refresh design
- versioned transformations and environment separation
- basic cloud warehouse or local warehouse setup

### Company-grade projects

1. `phase-3-dashboards/business-metrics-warehouse/`
   Build a modeled analytics layer from raw files or source tables into clean fact and dimension tables.
2. `phase-3-dashboards/pipeline-monitoring-dashboard/`
   Create an operator-facing dashboard showing freshness, failures, row counts, and KPI drift.
3. `phase-3-dashboards/scheduled-etl-project/`
   Build a scheduled pipeline with transformations, tests, retries, and documented lineage.
4. New required project: `phase-3-dashboards/realtime-or-near-realtime-feed/`
   Simulate or implement a small event stream or incremental ingestion flow with latency tracking.

### Stage exit standard

You are ready to leave this stage when you can build a repeatable data pipeline that other people can trust, refresh, troubleshoot, and extend.

---

## Stage 4: Data Scientist

**Phase:** Phase 4  
**Goal:** Build predictive ML and GenAI systems from problem framing through evaluation, deployment, and governance.

### You must master

- supervised learning workflows with `scikit-learn`
- feature engineering and train/validation/test design
- metric selection tied to business cost
- model packaging and inference interfaces
- experiment tracking and regression testing
- embeddings, RAG, tool calling, and structured outputs
- evaluation approaches for ML and LLM systems
- monitoring, retraining strategy, and governance documentation
- Docker and cloud-adjacent deployment habits

### Company-grade projects

1. `phase-4-job-ready/risk-or-churn-model/`
   Build a predictive model end to end: problem framing, feature engineering, training, evaluation, error analysis, and deployment notes.
2. `phase-4-job-ready/model-monitoring-suite/`
   Track model metrics, drift signals, retraining triggers, and failure conditions with a simple monitoring dashboard.
3. `phase-4-job-ready/llm-research-assistant/`
   Build a RAG workflow with retrieval, structured outputs, citations, and an evaluation set.
4. `phase-4-job-ready/agentic-controls-workflow/`
   Create a business-process assistant with routing, tool calling, guardrails, and measurable task outcomes.
5. New required capstone: `phase-4-job-ready/applied-ai-service/`
   A production-style service that includes:
   - data preparation pipeline
   - one predictive model or ranking model
   - one LLM-assisted workflow
   - evaluation and regression tests
   - Docker packaging
   - stakeholder-facing documentation

### Stage exit standard

You are ready to present yourself for strong Data Scientist or Applied AI / ML roles when you can show an end-to-end system with measurable outcomes, deployment thinking, evaluation evidence, and governance-aware documentation.

---

## Phase-by-Phase Build Order

### Phase 1

- Finish Python and SQL fundamentals
- ship reusable scripts, not only notebooks
- add one Excel reporting artifact
- write plain-English findings for each project

### Phase 2

- build two analyst-grade case studies
- deepen SQL and statistics
- standardize notebook, README, and business-summary structure

### Phase 3

- learn dimensional modeling
- build scheduled transformations
- add data tests, freshness checks, and pipeline observability
- treat dashboards as outputs of a data system, not the system itself

### Phase 4

- build one predictive model
- build one GenAI workflow
- add evaluation, monitoring, and governance artifacts
- package at least one project like a real service

---

## Mastery Checklist

Use this as the real checklist, not "I finished the course":

| Area | Junior | Functional | Strong | Hireable |
|---|---|---|---|---|
| SQL | Can query one table | Can join and aggregate | Can use windows and CTEs | Can design analysis-ready queries for business use |
| Python data work | Can load files | Can clean and transform data | Can structure reusable analysis code | Can support production-style data workflows |
| Statistics | Knows definitions | Can apply common measures | Can choose appropriate tests and metrics | Can defend model and experiment choices |
| Dashboards | Can build charts | Can build useful reports | Can design business-facing dashboards | Can support operational dashboards with trusted data |
| Data engineering | Knows ETL conceptually | Can script transforms | Can orchestrate and test pipelines | Can maintain reliable data services |
| ML | Can train a model | Can compare models | Can evaluate and analyze failure cases | Can ship monitored predictive systems |
| GenAI | Can call an API | Can use structured outputs | Can build RAG and tool workflows | Can evaluate, guard, and operate LLM features |
| Production ops | Runs locally | Uses Docker | Adds monitoring and alerts | Can support deployed services responsibly |
| Communication | Can describe findings | Can write recommendations | Can explain tradeoffs and risks | Can align technical work to measurable business outcomes |

You should aim to reach at least `Strong` in every row and `Hireable` in SQL, Python data work, data engineering, ML, production ops, and communication.

---

## Highest-Priority Gaps To Close First

If you want the fastest improvement in job-fit for Applied AI / ML roles, prioritize these in order:

1. data engineering and warehouse thinking
2. supervised ML with disciplined evaluation
3. production pipeline habits: testing, retries, monitoring
4. GenAI workflows with RAG and structured outputs
5. Docker and deployment fundamentals
6. governance and documentation in regulated-style environments

---

## Folder Structure

```text
data-analyst/
|
├── README.md
├── progress/
│   └── daily-log.md
├── phase-1-foundations/
│   ├── python/
│   │   └── subtitle-analyzer/
│   ├── sql/
│   │   └── analytics-queries.sql
│   ├── excel-ops-report/
│   └── ph-ecommerce-analysis/
├── phase-2-analytics/
│   ├── customer-retention-analysis/
│   ├── pricing-or-revenue-analysis/
│   └── sql-python-reporting-pipeline/
├── phase-3-dashboards/
│   ├── business-metrics-warehouse/
│   ├── pipeline-monitoring-dashboard/
│   ├── scheduled-etl-project/
│   └── realtime-or-near-realtime-feed/
└── phase-4-job-ready/
    ├── risk-or-churn-model/
    ├── model-monitoring-suite/
    ├── llm-research-assistant/
    ├── agentic-controls-workflow/
    └── applied-ai-service/
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
**Evidence:** notebook, SQL file, dashboard, tests, deployment, or report
**Blockers:** what slowed you down
**Next:** the exact next deliverable
```

---

## Target Stack

- SQL
- Python
- pandas and NumPy
- Excel
- Power BI
- `scikit-learn`
- basic experiment tracking
- data modeling and warehousing
- orchestration and scheduling
- data quality checks
- Docker
- cloud-adjacent deployment
- embeddings, RAG, tool calling, structured outputs
- monitoring and governance documentation

---

## Final Standard

By the end of this roadmap, your portfolio should show that you can:

- analyze business problems with real rigor
- build trusted data pipelines and modeled datasets
- train and evaluate predictive models
- build and evaluate GenAI workflows
- package solutions in a production-style way
- explain technical decisions in business terms

That is the threshold for the path from Data Analyst to Data Engineer to Data Scientist.
