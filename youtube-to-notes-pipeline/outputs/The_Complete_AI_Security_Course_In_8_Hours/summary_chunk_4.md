# Masterclass Summary: Module 4 — AgentOps & Production Workflows
**Course:** *The Complete AI Security Course In 8 Hours — AI Guardrails, LLM Evals & Memory And AgentOps*  
**Chunk 4 Coverage:** 06:00:02 – 07:48:40  
**Instructor / Mentor:** Sourangshu Paul  
**Reference Repository:** `github.com/sourangshupal/Agentic-RAG-project`

---

## Executive Summary

Chunk 4 delivers the capstone module of the course, transitioning an **Agentic Retrieval-Augmented Generation (RAG)** application from local prototype to enterprise-grade production deployment. The lecture covers end-to-end **AgentOps**: automated document ingestion using **Apache Airflow**, hybrid search combining **Okapi BM25** and **dense embeddings** in **OpenSearch**, multi-tiered security via **AWS Bedrock Guardrails**, dual-layer observability using **Pydantic Logfire** and **Langfuse**, exposure of agent capabilities via the **Model Context Protocol (MCP)**, and deployment on **Amazon EKS (Elastic Kubernetes Service)** with **Horizontal Pod Autoscaling (HPA)** validated through live **Locust load testing**.

---

## 1. System Architecture & Tech Stack

```
[ External Clients / Omnichannel ]
  ├─ MCP Inspector / Claude Code Agent
  ├─ Telegram Bot (BotFather)
  └─ REST / Streaming Clients (FastAPI :8000)
             │
             ▼
[ FastAPI Gateway & Agent Layer ]
  ├─ FastMCP Server (:8000/mcp)
  ├─ Pydantic Logfire (Application / Service Logging)
  ├─ Upstash Redis Cache (Exact Hash Match, 6h TTL)
  └─ LangGraph Orchestration
             │
      ┌──────┴──────────────────────────────┐
      ▼                                     ▼
[ Security & Safety Layer ]       [ Observability & HITL ]
  AWS Bedrock Guardrails            Langfuse Tracing & HITL Evals
  ├─ Topic Denial (Domain Filter)    ├─ Trace ID & Tool Latency
  ├─ Content Filters (Hate/Violence) ├─ Document Grading
  ├─ PII Masking & Redaction         └─ Async Human Feedback API
  └─ Grounding (70%) & Relevancy (70%)
             │
             ▼
[ Hybrid Retrieval Engine ]
  ├─ BM25 Sparse Search (Okapi BM25)
  ├─ Dense Vector Search (Jina AI 1024-dim Embeddings)
  └─ Reciprocal Rank Fusion (RRF) / Score Fusion (RSF)
             │
      ┌──────┴──────────────────────────────┐
      ▼                                     ▼
[ OpenSearch Vector DB ]          [ Neon DB (PostgreSQL) ]
  ArXiv Paper Chunks & Vectors      Paper Metadata, Ingestion Runs, DAG logs
             ▲
             │ (Scheduled Ingestion Pipeline)
[ Apache Airflow (:8080) ]
  ArXiv API -> Docling Parser -> Section Chunker -> Embed -> OpenSearch
```

### Component Overview

| Layer | Technology | Role & Key Configuration |
|---|---|---|
| **Data Ingestion** | Apache Airflow 2.x | Orchestrates automated extraction of ArXiv CS/AI papers, parsing, and chunk indexing. |
| **Parsing & Chunking** | Docling + Custom Section Chunker | Preserves document semantic sections; factory pattern architecture (`factory.py`). |
| **Vector Database** | OpenSearch | Stores ~317 chunk embeddings + sparse indices (1024-dim vector space). |
| **Relational / State DB**| Neon DB (Serverless Postgres) | Tracks DAG run logs, paper metadata, ArXiv IDs, and ingestion statuses. |
| **Caching** | Upstash Redis | Hash-based exact query caching with 6-hour TTL (drops latency from ~25s to ~250ms). |
| **Application API** | FastAPI (`main.py`) | Exposes `/ask`, `/stream`, `/agent`, `/health`, and `/feedback` routes. |
| **Agent Framework** | LangGraph / LangChain | StateGraph-based workflow with query rewriting, dynamic tool invocation, and fallbacks. |
| **LLM Providers** | AWS Bedrock (Meta Llama 3 70B) / OpenAI | Switchable via single `.env` flag (`LLM_PROVIDER`). |
| **AI Guardrails** | AWS Bedrock Guardrails | Topic denial, content moderation (hate/violence/NSFW), PII redaction, grounding checks. |
| **Observability & Evals**| Pydantic Logfire & Langfuse | System-level logging (Logfire) + deep graph execution tracing and HITL scoring (Langfuse). |
| **Tool Protocol** | FastMCP (`@modelcontextprotocol`) | Exposes backend RAG pipelines as standard MCP tools over HTTP. |
| **Orchestration / Infra**| AWS EKS (Kubernetes) | Multi-node cluster with IRSA, managed via `eksctl` and Docker Compose for local dev. |
| **Autoscaling & Monitoring**| HPA + Grafana Cloud | Scales pods from 2 to 6 based on 70% CPU/memory thresholds; monitored via Grafana. |
| **Load Testing** | Locust (:8089) | Concurrency and stress testing (evaluated at 10, 20, and 50 concurrent users). |

---

## 2. Ingestion Pipeline & Data Architecture

### Airflow DAG Workflow (`archive_paper_ingestion`)
1. **Environment Setup:** Validates connectivity to OpenSearch, Neon DB, and embedding models.
2. **Fetch Papers:** Queries ArXiv API for the latest papers in computer science, machine learning, and AI.
3. **Parse Documents:** Uses **Docling** for deep structural document parsing (handles layout, tables, and sections).
4. **Metadata Persistence:** Stores extracted paper IDs, titles, abstracts, and authors in **Neon DB**.
5. **Section-Aware Chunking:** Chunks text respecting document sections rather than arbitrary sliding windows.
6. **Vectorization & Indexing:** Generates 1024-dimensional embeddings via **Jina AI Embeddings** (Elastic) and indexes documents into OpenSearch.
7. **Report & Cleanup:** Emits daily ingestion summary reports and cleans temporary downloaded PDFs.

---

## 3. Retrieval Architecture: Hybrid Search & Caching

### Hybrid Search Implementation
- **Sparse (Keyword) Retrieval:** Okapi BM25 implementation for lexical matching (crucial for exact terminology, equations, paper IDs, and model names).
- **Dense Retrieval:** 1024-dimensional vector similarity search via Jina AI embeddings in OpenSearch.
- **Fusion:** Merges result sets using **Reciprocal Rank Fusion (RRF)**:
  $$RRF\_Score(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$
  *(Configurable to Relative Score Fusion / RSF via `.env` parameters).*
- **Metadata Filtering:** Pre-filters search space using Neon DB metadata (e.g., specific ArXiv IDs or publication windows) before executing heavy vector similarity calculations.

### Dual-Path Caching Architecture
- **Hit Path (Upstash Redis):** Hash-based key matching on normalized input prompts with a 6-hour TTL. Serves responses in **200ms – 300ms**.
- **Miss Path (Agentic RAG):** Invokes the full LangGraph agent workflow taking **20s – 30s**.
- *Production Note:* Standard Redis hash matching requires exact string equality. Semantic caching (vector-based cache lookup) can be layered on top via Redis extensions or gateways such as Bifrost.

---

## 4. Enterprise Guardrails & Security (AWS Bedrock Guardrails)

The agent integrates safety checks before retrieval and generation:

```
User Query ──► [ AWS Bedrock Guardrails ]
                    │
                    ├──► [ Topic Denial ] ────► Off-Topic? ──► Reject (Domain Warning)
                    │
                    ├──► [ Content Safety ] ──► Hate/Violence/NSFW? ──► Block Query
                    │
                    ├──► [ PII Detection ] ───► Email/Phone/Card? ──► Redact In-Place
                    │
                    └──► Passed? ──► [ Retrieval & Generation ]
                                           │
                                           ▼
                                 [ Post-Retrieval Checks ]
                                 ├─ Grounding Score (Threshold: 70%)
                                 └─ Answer Relevancy (Threshold: 70%)
```

1. **Topic Denial (Closed-Domain Enforcement):**
   - System restricts domain to CS/AI/ML research papers.
   - Out-of-domain queries (e.g., *"What is the pasta recipe?"*, *"Who won the US presidential elections?"*) trigger immediate topic denial blocks (`topic_blocked`) before hitting vector search or LLMs, conserving token costs.
2. **Content Safety Moderation:**
   - Filters explicit harmful categories: Hate speech, violence, illegal misconduct, and NSFW/sexual content.
   - Example: Malicious prompts attempting to target AI safety researchers are flagged under `content_blocked: violence`.
3. **PII Masking & Redaction:**
   - Detects sensitive entities (emails, US phone numbers, credit/debit card numbers).
   - Rather than dropping benign queries containing personal data, it redacts the sensitive tokens before internal processing.
4. **Grounding & Faithfulness Checks:**
   - Post-retrieval threshold set at **70% grounding** (ensures answers are strictly anchored to retrieved chunks) and **70% relevancy** (evaluates semantic alignment with the prompt).

---

## 5. Agentic Orchestration, Observability & HITL

### LangGraph Agent State Machine
- **Start Node:** Captures user query and context.
- **Guardrails Node:** Runs AWS Bedrock guardrail evaluation.
- **Conditional Routing:**
  - *Blocked / Out-of-Scope:* Diverts to query reformulation (rewriting with higher temperature for query relaxation) or returns a safety disclaimer.
  - *Valid:* Dispatches to the `Retrieve Tool Node`.
- **Tool Execution:** OpenSearch is treated as an external tool rather than an internal node.
- **Document Grading Node:** Filters retrieved chunks for factual relevance prior to LLM synthesis.
- **Fallback Mechanisms:** Built-in retries for chunk retrieval, model fallback (e.g., Bedrock -> OpenAI), and graceful degradation.

### Dual-Layer Observability & Human-in-the-Loop (HITL)
- **Pydantic Logfire:** Captures service-level and runtime telemetry (environment tags: `staging`/`prod`, container health, database connection pools, Telegram bot events).
- **Langfuse:** Captures deep LLM and agent traces (tool invocation journeys, execution latency, guardrail audit logs, token consumption).
- **HITL Feedback Loop:** An internal `/feedback` endpoint allows annotators to submit review scores (0.0 – 1.0) and critique notes mapped directly to Langfuse Trace IDs asynchronously, keeping user-facing inference fast.

---

## 6. Model Context Protocol (MCP) & Omnichannel Interfaces

### FastMCP Server Integration
- Built using the `fastmcp` Python framework mounted directly onto FastAPI at `/mcp` over HTTP transport.
- Translates existing FastAPI REST endpoints into standardized MCP tools:
  - `ask_question`: Invokes the agentic RAG search and generation.
  - `list_recent_papers`: Direct relational database query to Neon DB.
  - `search_paper` / `get_paper_details`: Fetches paper metadata and abstracts by ArXiv ID.
  - `submit_feedback`: Registers HITL feedback into Langfuse traces.
- **Testing & Verification:** Verified locally using `@modelcontextprotocol/inspector` and connected to external IDE agents (e.g., Claude Code).
- **Telegram Bot:** Connected using `python-telegram-bot` via BotFather for live chat interaction. *(Instructor caution: Polling bots crash in multi-replica production environments due to duplicate getUpdates calls; production requires webhooks).*

---

## 7. Kubernetes Deployment on AWS EKS & Scalability

### Cluster Specifications
- **Cluster Provisioning:** Configured via `eksctl` with `cluster.yaml` and bash automation.
- **Security:** IAM Roles for Service Accounts (IRSA) for least-privilege AWS resource access.
- **Compute:** 2 worker nodes (`m5.xlarge`, 16 GB RAM each, 32 GB cluster total).
- **Namespaces:**
  - `production`: Runs Airflow (single pod, internal ingestion) and RAG API pods.
  - `monitoring`: Agents forwarding telemetry to Grafana Cloud.

### Pod Scaling Configurations
- **Vertical Scaling (Resource Limits):** Requests set at 6 GB RAM, limits set at 8 GB RAM per pod to avoid `OOMKilled` terminations during heavy embedding and parsing jobs.
- **Horizontal Pod Autoscaling (HPA):**
  - Minimum replicas: 2
  - Maximum replicas: 6
  - Trigger metric: 70% CPU / Memory utilization
  - Stabilization window: 5-minute cool-down period before downscaling.

---

## 8. Live Load Testing & Failure Mode Analysis (Locust)

The instructor conducts real-time load testing using **Locust** (`localhost:8089`):

| Test Phase | Peak Concurrency | Active Pods | System Behavior & Failure Rates | Root Cause & Bottlenecks |
|---|---|---|---|---|
| **Phase 1: Low Concurrency** | 10 users (ramp 2/s) | 2 baseline pods | 0% – 1% failure rate. Memory utilization stable at ~40%. | Handled comfortably within baseline resource limits. |
| **Phase 2: Medium Load** | 20 users (ramp 2/s) | Scaled from 2 to 4 pods | CPU surged to 63% → 89%. Transient 5% failure rate, dropping to 1–3% after new pods initialized. | HPA triggered horizontal scale-out; temporary latency spikes during container startup. |
| **Phase 3: Stress Concurrency** | 50 users | Scaled to 6 pods (maximum) | Failure rate peaked at 40%, stabilizing around 22%. Cluster reached 33 GB memory limit (node saturation). | Multiple pending pods due to node capacity limits; upstream API rate limits (Bedrock concurrent quotas ~20 requests, Jina AI limits ~100 requests, Neon async connection pool saturation). |

### Key Production Takeaways for High-Scale AgentOps
1. **Upstream Quota Governance:** LLM application scalability is constrained by external rate limits (AWS Bedrock concurrency limits, embedding API quotas, serverless DB connection limits). High-scale enterprise architectures (>10k users) must self-host open-source models (vLLM / TGI) on internal VPC infrastructure.
2. **Compute Sizing:** Agentic RAG workflows are memory- and CPU-intensive. Sizing pods with at least 6–8 GB prevents out-of-memory errors during multi-tool execution.
3. **Simplicity Over Complexity:** For startups and traffic under 100k requests/day, AWS ECS with Fargate and an Nginx reverse proxy provides a simpler, more cost-effective alternative to full Kubernetes (EKS) clusters.

---

## Summary Wrap-Up
Chunk 4 synthesizes the entire masterclass curriculum into an operational blueprint: combining **security (Bedrock Guardrails)**, **rigorous evaluation (Langfuse + HITL)**, **advanced context retrieval (Hybrid BM25 + Dense RRF + Redis)**, and **resilient deployment (EKS + HPA + MCP)** into a battle-tested, production-ready AI agent architecture.
