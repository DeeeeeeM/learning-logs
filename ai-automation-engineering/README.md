# 🤖 AI Automation Engineering

> Building AI-powered automation systems — workflow orchestration, LLM integrations, CRM automation, agentic pipelines, and operational dashboards. Every phase ships something real and portfolio-ready.

**Primary focus path. Target role by June 2027.**



---

## 🔍 Average Requirements Analysis

| Requirement | Status | Phase That Closes It |
|---|---|---|
| n8n / Make — automated workflows | 🟡 Learning | Phase 1 |
| OpenAI / LLM — summarization, drafting, classification | ✅ Strong (yt-toolkits) | Phase 1 (formalize) |
| CRM automation — HubSpot / GoHighLevel | ❌ Not started | Phase 2 |
| APIs, integrations, data flow logic | ✅ Strong | Phase 1 (formalize) |
| Pipeline dashboards — enquiry, capacity, conversion | ❌ Not started | Phase 3 |
| AI-assisted document review / contract summary | ❌ Not started | Phase 3 |
| Automated client intake workflows | ❌ Not started | Phase 3 |
| Content automation — SEO, email, social repurposing | ❌ Not started | Phase 4 |
| Practice management tool integrations | ❌ Nice-to-have | Phase 4 |

---

## 📈 Progress Tracker

| Phase | Focus | Status | Key Milestone |
|---|---|---|---|
| 🔵 Phase 1 | n8n + LLM API Foundations | 🔄 In Progress | 3 working n8n workflows + `llm_utils.py` |
| 🟢 Phase 2 | CRM Automation + Lead Nurturing | ⬜ Not Started | HubSpot/GHL automation + lead pipeline |
| 🟡 Phase 3 | Legal Ops + Document Automation | ⬜ Not Started | Intake system + contract summarizer + dashboard |
| 🟣 Phase 4 | Content Automation + Portfolio | ⬜ Not Started | Content pipeline + 4 polished portfolio tools |

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

## 🟡 Phase 3 — Legal Ops + Document Automation

**Goal:** Build the operational infrastructure the target role specifically calls for — client intake automation, AI-assisted document review, contract summarization, matter status updates, and pipeline dashboards. This is the most job-specific phase.

### What to Learn

- Structured document processing — parsing PDFs and Word docs in Python (`pdfplumber`, `python-docx`)
- AI-assisted document review — chunking long documents, summarizing with LLMs, extracting key clauses
- Client intake system design — form → validation → CRM → document generation → notification
- Template-based document generation — filling `.docx` templates with dynamic data
- Matter pipeline dashboards — visualizing turnaround times, capacity, bottlenecks
- Automated notification workflows — status update emails/SMS triggered by matter stage changes
- Webhook + n8n for ops triggers — matter updated → n8n fires → client gets status SMS

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
Build an AI tool that reads a contract or legal document and returns a structured summary.
Steps:
1. Accept PDF or `.docx` input via a simple Gradio UI or CLI
2. Extract text with `pdfplumber` (PDF) or `python-docx` (Word)
3. Chunk document into segments with overlap to preserve context across boundaries
4. Send each chunk to `llm_utils.py` with a legal summarization prompt — extract: parties, key dates, obligations, risks, termination clauses
5. Aggregate chunk summaries into a final structured output (JSON + human-readable Markdown)
6. Test on 3 real or sample contracts, document accuracy and any hallucination patterns

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
4. Record a 1–2 min demo GIF/video for each of the 4 phase capstone projects
5. Write a LinkedIn summary post: "I spent 12 months building AI automation systems — here's what I shipped"
6. Update CV with: n8n, Make, HubSpot, GoHighLevel, LLM API integration, OpenAI, document automation, CRM automation, Playwright, Streamlit

**Milestone:** Portfolio of 8+ documented automation tools across 4 phases, CV updated, LinkedIn active, applications live.

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

---

*Target: AI Engineer role at a professional services firm. June 2027. Every commit closes the gap.*
