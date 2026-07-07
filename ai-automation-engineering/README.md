# 🤖 AI Automation Engineering

> Building AI-powered automation systems — workflow orchestration, LLM integrations, CRM automation, agentic pipelines, and operational dashboards. Every phase ships something real and portfolio-ready.

**Primary focus path. Target role by June 2027.**

---

## 🔍 Job Requirements Gap Analysis

| Requirement | Status | Phase That Closes It |
|---|---|---|
| n8n / Make — automated workflows | 🟡 Learning | Phase 1 |
| OpenAI / LLM — summarization, drafting, classification | ✅ Strong (yt-toolkits) | Phase 1 (formalize) |
| CRM automation — HubSpot / GoHighLevel | ❌ Not started | Phase 2 |
| APIs, integrations, data flow logic | ✅ Strong | Phase 1 (formalize) |
| RAG pipelines — retrieval-augmented generation | ❌ Not started | Phase 2.5 |
| Vector databases — Qdrant, embeddings, hybrid search | ❌ Not started | Phase 2.5 |
| AI evaluation — RAGAS, LLM-as-Judge, golden datasets | ❌ Not started | Phase 2.5 |
| AI observability — tracing, logging, monitoring | ❌ Not started | Phase 2.5 |
| Docker — containerized deployment | ❌ Not started | Phase 2.5 |
| Pipeline dashboards — enquiry, capacity, conversion | ❌ Not started | Phase 3 |
| AI-assisted document review / contract summary | ❌ Not started | Phase 3 (RAG-powered) |
| Automated client intake workflows | ❌ Not started | Phase 3 |
| Content automation — SEO, email, social repurposing | ❌ Not started | Phase 4 |
| Practice management tool integrations | ❌ Nice-to-have | Phase 4 |

---

## 📈 Progress Tracker

| Phase | Focus | Status | Key Milestone |
|---|---|---|---|
| 🔵 Phase 1 | n8n + LLM API Foundations | 🔄 In Progress | 3 working n8n workflows + `llm_utils.py` |
| 🟢 Phase 2 | CRM Automation + Lead Nurturing | ⬜ Not Started | HubSpot pipeline + nurture sequence + weekly report |
| 🟠 Phase 2.5 | AI Systems Foundations (RAG, Eval, Deploy) | ⬜ Not Started | RAG pipeline + evaluation framework + Docker deploy |
| 🟡 Phase 3 | Legal Ops + Document Automation | ⬜ Not Started | RAG-powered intake + contract summarizer + dashboard |
| 🟣 Phase 4 | Content Automation + Portfolio | ⬜ Not Started | Content pipeline + 8+ polished tools + CV updated |

---

## 🔵 Phase 1 — n8n Workflow Automation + LLM API Foundations

**Goal:** Get fluent in n8n (the primary tool in the target job's stack) while formalizing existing LLM API knowledge into a reusable multi-provider module. These two outputs — n8n fluency and `llm_utils.py` — are the foundation every later phase builds on.

### What to Learn

**n8n:**
- Core concepts — nodes, triggers, connections, credentials, expressions
- HTTP Request node — calling any external API from an n8n workflow
- Webhook triggers — receiving external events (form submissions, CRM updates, etc.)
- Branching logic — IF node, Switch, Merge, error handling paths
- Loop/split nodes — processing lists of items in bulk
- Scheduling — Cron trigger for recurring automations
- n8n + OpenAI node — calling GPT directly from a workflow without code
- Connecting n8n to Google Sheets, Gmail, Airtable as lightweight data stores
- Self-hosting n8n on a free/cheap VPS (Railway, Render, or local) vs. n8n Cloud

**LLM API (multi-provider, free-first):**
- Messages API shape — Anthropic, OpenAI, Gemini, Groq
- Structured JSON output — schema enforcement, `pydantic` validation
- Prompt patterns for classification, summarization, extraction, drafting
- Retry logic with exponential backoff + jitter
- Provider cost comparison — Gemini Flash (free), Groq (free), OpenRouter free models, OpenAI (pay-as-you-go for final QA)

**Make (Integromat) — basics only:**
- Enough to read/maintain Make scenarios if a client uses it instead of n8n
- Core concepts mirror n8n: modules, routers, filters, schedulers

### LLM API Options (Free-First)

| Provider | Free Tier | Best For |
|---|---|---|
| Google Gemini API | ✅ Yes — generous limits on `gemini-flash` | Daily practice, structured output |
| Groq API | ✅ Yes — fast inference on Llama, Mixtral | High call volume, agent loops |
| OpenRouter | ✅ Free-tagged models (Llama, DeepSeek, Gemini) | Provider comparisons |
| Ollama (local) | ✅ Always free — runs on GPU | Offline, zero cost |
| OpenAI API | ❌ Pay-as-you-go | Final quality checks on real pipeline runs |

### Resources

- [n8n Official Docs](https://docs.n8n.io) — node reference, expressions, self-hosting guide
- [n8n YouTube Channel](https://www.youtube.com/@n8n-io) — official walkthroughs, workflow breakdowns
- [NetworkChuck — n8n beginner playlist](https://www.youtube.com/@NetworkChuck) — practical beginner-friendly n8n builds
- [Cole Medin (YouTube)](https://www.youtube.com/@ColeMedin) — n8n + AI agent builds, very practical for this exact use case
- [Anthropic Prompt Engineering Tutorial](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — 9 interactive chapters
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) — "ChatGPT Prompt Engineering for Developers" as starting point
- [Google AI Studio / Gemini API docs](https://ai.google.dev/) — free tier setup, JSON mode
- [Groq API docs](https://console.groq.com/docs) — free tier, model list, API reference
- [OpenRouter docs](https://openrouter.ai/docs) — unified API, filtering free models
- [Make (Integromat) Academy](https://www.make.com/en/academy) — free beginner course

### Projects

**Project 1: `n8n-email-to-task/`**
Build an n8n workflow that watches a Gmail inbox → extracts key info using OpenAI → creates a structured task in Google Sheets or Airtable.
Steps:
1. Set up n8n (self-hosted on Railway or local)
2. Connect Gmail trigger → watch for new emails matching a label
3. Add OpenAI node → extract sender, intent, urgency, action needed as JSON
4. Add Google Sheets node → append a new row with extracted data
5. Add an IF branch → if urgency is "high", send a Slack/Telegram alert
6. Test end-to-end with 5 real emails, document results

**Project 2: `n8n-lead-intake-form/`**
Build a webhook-triggered workflow that receives form submissions → enriches with LLM → routes to the right output.
Steps:
1. Create a simple HTML form (or use Tally/Typeform free tier) that POSTs to an n8n webhook
2. n8n receives submission → sends to OpenAI for classification (lead type, urgency, practice area)
3. Route output: high-priority → Gmail draft reply + Google Sheets log; low-priority → Sheets log only
4. Add error handling path — if OpenAI call fails, log raw data and send alert
5. Document the workflow with screenshots and a short README

**Project 3: `llm_utils.py` — multi-provider module**
Build a Python utility module that abstracts LLM provider calls behind a single interface.
Steps:
1. `call_llm(prompt, system, model, provider)` supporting Gemini, Groq, OpenRouter, OpenAI
2. `call_llm_json(prompt, schema, provider)` — enforced JSON output with pydantic validation and one retry
3. Retry wrapper with exponential backoff + jitter
4. Usage logger → CSV: timestamp, provider, model, tokens, latency, cost, error
5. Run a side-by-side comparison test (same classification prompt across 3 providers) → document in `COMPARISON.md`
6. Write a clean README — this module gets imported by all later projects

**Milestone:** 2 working n8n workflows with documented results + `llm_utils.py` with provider comparison notes.

---

## 🟢 Phase 2 — CRM Automation + Lead Nurturing

**Goal:** Get hands-on with HubSpot and/or GoHighLevel — the CRM tools listed in the target job — and build real lead management automations: tracking enquiries, automated follow-up sequences, referral source logging, and pipeline visibility.

### What to Learn

- HubSpot free tier — contacts, deals, pipelines, properties, workflows (automation)
- GoHighLevel (GHL) — sub-accounts, pipelines, triggers, automated SMS/email sequences
- CRM concepts — lead lifecycle stages, pipeline stages, contact properties, deal tracking
- n8n ↔ CRM integration — using n8n to push/pull data from HubSpot or GHL via API
- Lead nurturing sequences — multi-step email/SMS drips triggered by behavior
- Referral source tracking — UTM parameters, source tagging, attribution
- Webhook-based CRM triggers — CRM fires webhook → n8n takes action

### Resources

- [HubSpot Academy — HubSpot CRM free certification](https://academy.hubspot.com/courses/hubspot-crm) — free, covers the full CRM including automation workflows
- [HubSpot Academy — Marketing Automation certification](https://academy.hubspot.com/courses/marketing-hub-marketing-automation) — free, covers sequences, workflows, lead nurturing
- [GoHighLevel YouTube channel](https://www.youtube.com/@GoHighLevel) — official tutorials
- [Nate Freedman (YouTube)](https://www.youtube.com/@NateFreedman) — practical GHL automation builds
- [n8n HubSpot node docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/) — connecting n8n to HubSpot
- [HubSpot API docs](https://developers.hubspot.com/docs/api/overview) — for custom n8n HTTP Request integrations

### Projects

**Project 1: `crm-lead-pipeline/`**
Build a full lead tracking system: form submission → CRM contact created → deal created → pipeline stage assigned → follow-up sequence triggered.
Steps:
1. Set up HubSpot free account — create a pipeline with stages: New Enquiry → Contacted → Proposal Sent → Won/Lost
2. Build an n8n workflow: webhook (from intake form) → create HubSpot contact → create deal → assign to stage
3. Tag referral source on the contact from form data (e.g., "website", "referral", "Google")
4. Add a HubSpot workflow (native) that sends an automated acknowledgment email when a new contact is created
5. Test with 5 simulated enquiries, verify all show correctly in pipeline

**Project 2: `lead-nurture-sequence/`**
Build a multi-step nurture sequence for leads who enquired but didn't convert.
Steps:
1. Define a 3-email drip sequence: Day 1 — acknowledgment, Day 3 — value/FAQ, Day 7 — soft CTA
2. Use AI (via `llm_utils.py` or n8n OpenAI node) to personalize each email based on the enquiry topic
3. Trigger sequence in HubSpot when a deal sits in "Contacted" stage for 2+ days with no response
4. Add an exit condition — sequence stops if the lead replies or books a call
5. Document open rates or test results in a short report

**Project 3: `pipeline-reporting-sheet/`**
Build an automated weekly pipeline report.
Steps:
1. n8n Cron trigger (every Monday AM) → pull deal data from HubSpot API
2. Calculate: total enquiries this week, conversion rate, deals by source, average time per stage
3. Format as a Google Sheets dashboard with color-coded cells (red/yellow/green by threshold)
4. Optional: use OpenAI to write a plain-English summary of the week's pipeline health
5. Email the report automatically to a set recipient

**Milestone:** A working CRM pipeline + lead nurture sequence + automated weekly report — documented and demo-ready.

---

## 🟠 Phase 2.5 — AI Systems Foundations (RAG, Evaluation, Deployment)

**Goal:** Build the production AI engineering skills that are missing from the path but required to build serious document automation tools in Phase 3. This phase exists so that the `contract-summarizer` and `matter-pipeline-dashboard` are built the right way from the start — with proper retrieval, measurable accuracy, and deployable packaging — not retrofitted later.

This phase is directly informed by the NeoSage Engineer's RAG Accelerator curriculum, covered here with free resources.

### What to Learn

**RAG (Retrieval-Augmented Generation):**
- What RAG is and when to use it vs. pure LLM calls
- Data ingestion — handling PDF, Word, and plain text as document corpora
- The full RAG loop: index → retrieve → generate → evaluate
- Chunking strategies — naive, sentence, recursive, semantic, hybrid content-aware; how chunking choice affects retrieval accuracy more than model choice
- When to chunk large vs. small, how overlap preserves cross-boundary context

**Embeddings + Vector Databases:**
- How text becomes vectors — tokenization, embedding models, vector space
- Choosing an embedding model — FastEmbed (free, local), Voyage AI (quality), OpenAI `text-embedding-3-small` (balanced)
- Qdrant — the vector database used in production RAG systems; indexing, querying, metadata filtering
- HNSW (Hierarchical Navigable Small World) — how approximate nearest neighbor search works under the hood (conceptual, not implementation)

**Hybrid Search:**
- Dense retrieval (vector similarity) vs. sparse retrieval (BM25 keyword matching)
- Reciprocal Rank Fusion (RRF) — combining dense and sparse scores into a single ranked list
- When hybrid search beats pure vector search (keyword-heavy legal documents especially)
- Reranking — using a cross-encoder model to rerank top-k results for higher accuracy

**AI Evaluation:**
- Why measuring output quality is harder than building the system
- Golden dataset curation — creating ground truth question/answer pairs from your own documents
- Synthetic test generation — using LLMs to generate test cases when no ground truth exists
- LLM-as-Judge — using a second LLM to score the output of your primary LLM
- RAGAS metrics — answer relevancy, faithfulness, context precision, context recall
- DeepEval — open-source evaluation framework for LLM outputs
- Triangulating across 3 evaluation methods to find where a system breaks

**AI Observability:**
- Why observability matters in production — catching hallucinations, tracking latency, cost per call
- Opik (open source, self-hosted) — tracing LLM calls, logging inputs/outputs, monitoring pipelines
- What to log on every LLM call: prompt, response, model, tokens, latency, cost, retrieval sources used
- User feedback loops — thumbs up/down signals as production evaluation data

**Docker Basics:**
- What Docker is and why it matters for AI tools (reproducibility, deployment)
- Writing a `Dockerfile` for a Python FastAPI or Streamlit app
- `docker build`, `docker run`, `docker-compose` for multi-service setups (app + vector DB)
- Deploying a containerized app to Railway or Render (free tier)

**Semantic Caching (Redis) — optional:**
- How Redis stores recently-seen query embeddings to return cached responses
- Sub-50ms response times for repeated queries — relevant for a matter dashboard with frequent refreshes
- When caching is worth the complexity vs. when to skip it

### Resources

- [NeoSage — The Engineer's Guide to RAG](https://blog.neosage.io/p/the-engineers-guide-to-rag) — free, the best single starting read on RAG
- [Qdrant docs + quickstart](https://qdrant.tech/documentation/quickstart/) — vector DB setup, Python client, hybrid search guide
- [RAGAS docs](https://docs.ragas.io) — open source, full evaluation framework with examples
- [DeepEval docs](https://docs.confident-ai.com) — open source LLM evaluation, LLM-as-Judge pipelines
- [Opik GitHub (Comet ML)](https://github.com/comet-ml/opik) — free, self-hosted LLM observability and tracing
- [LangChain — RAG from scratch (YouTube playlist)](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) — 14 short videos building RAG from first principles
- [sentence-transformers / FastEmbed docs](https://sbert.net) — local embedding models, no API cost
- [Docker Getting Started](https://docs.docker.com/get-started/) — official beginner guide
- [Redis quickstart](https://redis.io/docs/getting-started/) — for semantic caching (Phase 2.5 optional project)
- [Hugging Face — MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — benchmark for choosing embedding models

### Projects

**Project 1: `rag-pipeline-basics/`**
Build a working RAG pipeline from scratch on real documents — the foundational pattern used in every Phase 3 project.
Steps:
1. Pick a document corpus (e.g., 10–20 sample legal FAQs, contract templates, or your own work documents in PDF/Word)
2. Ingest and parse documents with `pdfplumber` + `python-docx` → clean text
3. Implement and compare 3 chunking strategies: naive (fixed size), recursive (by separator), semantic (by topic shift) — log chunk counts and sizes for each
4. Embed chunks using FastEmbed (free, local) — store in a local Qdrant collection
5. Build a retrieval function: query → embed → search Qdrant → return top-k chunks
6. Add a generation step: retrieved chunks + user question → LLM answer via `llm_utils.py`
7. Test with 10 questions across the corpus — log retrieved chunks and answers
8. Document which chunking strategy produced the best retrieval in `CHUNKING-RESULTS.md`

**Project 2: `rag-evaluation-framework/`**
Build a reusable evaluation layer that measures RAG system accuracy — used to validate every later document tool.
Steps:
1. Create a golden dataset: 20 question/answer pairs manually written from the corpus used in Project 1
2. Use an LLM to generate 20 additional synthetic QA pairs from the same corpus (`llm_utils.py` + structured output)
3. Build an LLM-as-Judge scorer: given (question, retrieved context, generated answer), the judge LLM returns a score (1–5) with reasoning
4. Install and configure RAGAS — run faithfulness and answer relevancy metrics on the same test set
5. Compare manual scores vs. RAGAS metrics vs. LLM-as-Judge scores across all 40 test questions
6. Document discrepancies and conclusions in `EVALUATION-REPORT.md` — this report becomes proof of production thinking in your portfolio

**Project 3: `hybrid-search-upgrade/`**
Upgrade the RAG pipeline from Project 1 with hybrid search and reranking.
Steps:
1. Add BM25 sparse retrieval alongside Qdrant dense retrieval
2. Implement Reciprocal Rank Fusion to merge the two ranked lists into one
3. Add a reranking step using a cross-encoder model (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2` from Hugging Face — free)
4. Run the same 40-question evaluation from Project 2 on the upgraded pipeline
5. Compare accuracy before (dense only) vs. after (hybrid + rerank) in `HYBRID-RESULTS.md`
6. Document the tradeoff: accuracy gain vs. latency cost

**Project 4: `docker-deploy/`**
Package the RAG pipeline as a deployable containerized app.
Steps:
1. Wrap the RAG pipeline in a simple FastAPI app: `POST /ask` takes `{question, corpus_id}`, returns `{answer, sources, latency_ms}`
2. Add Opik tracing to every LLM call — log prompt, response, retrieved chunks, tokens, latency
3. Write a `Dockerfile` for the FastAPI app
4. Write a `docker-compose.yml` that starts both the app and a local Qdrant container
5. Test `docker compose up` — confirm the API is reachable and Qdrant is persisting data
6. Deploy to Railway or Render free tier — get a live public URL
7. Document the architecture with a simple diagram and add the live URL to the README

**Milestone:** A production-quality RAG pipeline with hybrid search, an evaluation framework with documented accuracy metrics, and a live deployed API — all reusable as the foundation for Phase 3 legal ops projects.

---

## 🟡 Phase 3 — Legal Ops + Document Automation

**Goal:** Build the operational infrastructure the target role specifically calls for — client intake automation, AI-assisted document review, contract summarization, matter status updates, and pipeline dashboards. This is the most job-specific phase.

### What to Learn

> Phase 3 builds directly on Phase 2.5. The RAG pipeline, evaluation framework, Docker setup, and Opik observability are already in place — this phase applies them to legal ops use cases.

- Structured document processing — `pdfplumber` (PDF), `python-docx` (Word) for ingestion into the RAG pipeline
- Legal document Q&A design — writing retrieval query templates for clause extraction (obligations, risks, parties, dates, termination)
- Client intake system design — form → validation → CRM → document generation → notification chain
- Template-based document generation — filling `.docx` templates with dynamic data from intake forms
- Matter pipeline dashboards — visualizing turnaround times, capacity, bottlenecks using Streamlit
- Automated notification workflows — matter stage changes triggering status update emails via n8n
- Connecting RAG output to n8n — Python RAG tool → REST endpoint → n8n HTTP Request node → downstream actions

### Resources

- [pdfplumber docs](https://github.com/jsvine/pdfplumber) — PDF text/table extraction in Python
- [python-docx docs](https://python-docx.readthedocs.io) — reading and generating Word documents
- [LangChain — Document Loaders + Text Splitters](https://python.langchain.com/docs/modules/data_connection/) — chunking long docs for LLM processing
- [Anthropic Academy — Tool Use + RAG modules](https://www.anthropic.com/learn) — retrieval-augmented generation for document Q&A
- [Retool docs](https://docs.retool.com) — building internal dashboards fast without heavy frontend work
- [Tally.so](https://tally.so) — free form builder with webhook output, good for intake forms
- [Streamlit docs](https://docs.streamlit.io) — quick Python dashboards (alternative to Retool)

### Projects

**Project 1: `client-intake-workflow/`**
Replace a manual email intake chain with a structured automated onboarding flow.
Steps:
1. Build an intake form (Tally or HTML) collecting: name, contact, matter type, brief description, urgency
2. n8n webhook receives submission → validates required fields → creates HubSpot contact + deal
3. OpenAI node classifies matter type and urgency → routes to correct pipeline stage
4. Auto-sends acknowledgment email with expected next steps and timeline
5. Logs all intake submissions to Google Sheets with timestamp, source, matter type, status
6. Document as a flowchart (can reuse SVG diagram format from work docs)

**Project 2: `contract-summarizer/`**
Build a RAG-powered contract review tool that retrieves relevant clauses and generates structured summaries — using the pipeline and evaluation framework built in Phase 2.5.
Steps:
1. Accept PDF or `.docx` input via a simple Gradio UI or CLI
2. Extract and clean text with `pdfplumber` / `python-docx`
3. Chunk and embed the document into a Qdrant collection (reuse Phase 2.5 pipeline)
4. Build query templates for key legal extractions: "What are the termination clauses?", "Who are the parties?", "What are the key obligations?", "What are the payment terms?", "What are the risk or liability clauses?"
5. Run each query through the RAG retriever → generate answer from retrieved chunks via `llm_utils.py`
6. Aggregate all answers into a structured JSON summary + human-readable Markdown report
7. Run the Phase 2.5 evaluation framework on 3 sample contracts — log faithfulness and answer relevancy scores
8. Add Opik tracing so every summarization run is logged with retrieved sources and LLM responses
9. Package as a Docker container using the Phase 2.5 `Dockerfile` pattern

**Project 3: `matter-pipeline-dashboard/`**
Build a matter status dashboard showing turnaround times, team capacity, and bottlenecks.
Steps:
1. Create a Google Sheet (or Airtable) as the matter data source — columns: matter ID, type, stage, assigned, opened date, last updated, closed date
2. Build a Streamlit or Retool dashboard that reads this data and displays: matters by stage (kanban counts), average days per stage by matter type, overdue matters (flagged red), weekly closed vs. opened trend
3. Add an n8n workflow: if a matter has had no update in 5+ days → auto-send a "status check" email to the assigned person
4. Optional: add an AI summary panel — OpenAI reads the current pipeline state and writes a 3-sentence health summary

**Milestone:** 3 working systems — intake workflow, contract summarizer, matter dashboard — each documented and demo-recorded.

---

## 🟣 Phase 4 — Content Automation + Portfolio Polish

**Goal:** Close the final job requirement gap (content automation for SEO, email, social media repurposing) and package all previous phase projects into a clean, professional portfolio ready for applications.

### What to Learn

- Content repurposing pipelines — taking one source (FAQ, blog post, service page) and generating: email, LinkedIn post, short-form social, meta description
- SEO basics for content automation — keyword targeting, meta tags, structured content output
- Email sequence automation — connecting AI-generated content to HubSpot or Mailchimp sequences
- Local LLMs with Ollama — running quantized models locally for zero-cost content generation drafts
- Portfolio packaging — clean READMEs, setup instructions, demo GIFs, "before/after time saved" framing

### Resources

- [Ollama docs + model library](https://ollama.com) — local model setup, GGUF quantization
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — picking hardware-appropriate models (GTX 1660 Super = 6GB VRAM)
- [HubSpot Academy — Email Marketing certification](https://academy.hubspot.com/courses/email-marketing) — free, covers sequences and automation
- [Anthropic Academy — Claude Code 101](https://www.anthropic.com/learn) — packaging and maintaining projects long-term
- [Ahrefs blog — SEO basics for content](https://ahrefs.com/blog/seo-basics/) — free content SEO fundamentals

### Projects

**Project 1: `content-repurposing-pipeline/`**
Build a pipeline that takes a single FAQ or service page input and outputs 4 content formats automatically.
Steps:
1. Input: a URL or pasted text block (service page, FAQ, blog post)
2. LLM pass 1 → extract core topic, target keyword, key points
3. LLM pass 2 → generate 4 outputs in parallel: LinkedIn post (150 words), email newsletter section (200 words), short social caption (50 words), meta description (155 chars)
4. Output to a Google Doc or formatted Markdown file with labeled sections
5. Add Ollama as a local provider option in `llm_utils.py` — test same pipeline locally vs. API
6. Test on 3 sample inputs from a legal services website, document quality

**Project 2: `automated-email-sequence-builder/`**
Build a tool that generates a 3-email nurture sequence from a single brief description of a service or topic, then loads it into HubSpot.
Steps:
1. Input: service name, target audience, goal of the sequence (e.g., "commercial lease enquiries, Gold Coast SMEs, book a consultation")
2. LLM generates 3 emails: Day 1 — educational value, Day 4 — social proof/FAQ, Day 8 — CTA
3. Each email is structured JSON: subject line, preview text, body (HTML-ready)
4. n8n workflow takes the JSON → creates 3 HubSpot email drafts via API
5. Document the full prompt chain in a README for reuse

**Project 3: Portfolio consolidation**
Steps:
1. Benchmark Ollama local model vs. GPT-4o-mini on one real task (contract summarization or email classification)
2. Document cost/quality/speed tradeoffs in a `BENCHMARK.md`
3. Polish all projects: consistent README structure, `requirements.txt`, `.env.example`, example output files
4. Record a 1–2 min demo GIF/video for each phase capstone project
5. Write a LinkedIn summary post: "I spent 12 months building AI automation systems — here's what I shipped"
6. Update CV with: n8n, Make, HubSpot, GoHighLevel, LLM API integration, OpenAI, RAG pipelines, Qdrant, RAGAS, Docker, document automation, CRM automation, Streamlit

**Milestone:** Portfolio of 10+ documented automation tools across 5 phases, CV updated, LinkedIn active, applications live.

---

## 📁 Folder Structure

```
ai-automation-engineering/
│
├── README.md
├── progress/
│   └── daily-log.md
│
├── phase-1-foundations/
│   ├── n8n-email-to-task/
│   ├── n8n-lead-intake-form/
│   └── prompt-toolkit/
│       ├── llm_utils.py
│       ├── COMPARISON.md
│       └── README.md
│
├── phase-2-crm-automation/
│   ├── crm-lead-pipeline/
│   ├── lead-nurture-sequence/
│   └── pipeline-reporting-sheet/
│
├── phase-2.5-ai-systems-foundations/
│   ├── rag-pipeline-basics/
│   │   └── CHUNKING-RESULTS.md
│   ├── rag-evaluation-framework/
│   │   └── EVALUATION-REPORT.md
│   ├── hybrid-search-upgrade/
│   │   └── HYBRID-RESULTS.md
│   └── docker-deploy/
│       ├── Dockerfile
│       └── docker-compose.yml
│
├── phase-3-legal-ops/
│   ├── client-intake-workflow/
│   ├── contract-summarizer/
│   └── matter-pipeline-dashboard/
│
└── phase-4-content-and-portfolio/
    ├── content-repurposing-pipeline/
    └── automated-email-sequence-builder/
```

---

## 📝 Daily Log Format

Every session logged in `progress/daily-log.md`:

```markdown
## YYYY-MM-DD · Day · Phase N

**Session:** AM / PM / Both  
**Hours:** X.X  
**Mood:** X/5  

**Topics:** what I studied or read  
**Built:** what I wrote, pushed, or shipped  
**Blockers:** what slowed me down  
**Next:** what to pick up next session  

---
```

---

## 🛠️ Target Stack (from job posting)

![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat&logo=n8n&logoColor=white)
![Make](https://img.shields.io/badge/Make-6D00CC?style=flat&logo=make&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![HubSpot](https://img.shields.io/badge/HubSpot-FF7A59?style=flat&logo=hubspot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_API-4285F4?style=flat&logo=google&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat&logo=qdrant&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

---

*Target: AI Engineer role at a professional services firm. June 2027. Every commit closes the gap.*
