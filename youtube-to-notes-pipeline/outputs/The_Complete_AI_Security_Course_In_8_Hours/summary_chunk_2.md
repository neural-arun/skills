# Masterclass Technical Notes: AI Guardrails, LLM Evals, Memory & AgentOps
## Chunk 2 Deep-Dive (Timestamps: 02:00:00 – 04:00:01)
**Instructors:** Divesh (Evals), Chirantan (Agentic Memory)  
**Modules Covered:** 
1. **Module 2 (Continuation):** LLM Evaluations (Evals) & RAG Triad Metrics
2. **Module 3 (Inception):** Agentic Memory Architectures & Memory Lineage (Techniques 1–4)

---

## Executive Summary & Conceptual Map

Chunk 2 spans the critical transition between **measuring AI system quality (LLM Evaluations via Ragas)** and **maintaining state across agent interactions (Agentic Memory Architectures)**.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PART 1: PRODUCTION LLM EVALS (02:00:00 - 02:47:50)                              │
│ • LLM-as-a-Judge Context Load Management (~20% saturation rule)                 │
│ • Rate-limiting & Async Cool-downs (Sample: 25s, Experiment: 35s)               │
│ • Core Ragas Metrics: Faithfulness, Answer Relevancy, Context Precision,        │
│   Context Recall, Answer Correctness (Factual F1 + Semantic Similarity)         │
│ • Streamlit / Ragas Automated Dashboard & Multi-Provider Judge/Generator Setup  │
└──────────────────────────────────────┬──────────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PART 2: AGENTIC MEMORY ARCHITECTURES (02:47:50 - 04:00:01)                      │
│ • Enterprise Case Study: 500k Clinical Trials / PubMed GCP Multi-Agent System   │
│ • Agent Memory Lineage & Fundamental Statelessness of LLMs                      │
│ • Technique 1: Conversational Buffer Memory & Token Bloating (O(N²) scaling)    │
│ • Technique 2: Sliding Window Memory (Fixed K turns, eviction & context loss)   │
│ • Technique 3: Summary Memory (Abstractive & Progressive, Lossy Compression)    │
│ • Technique 4: Summary Buffer Memory (Verbatim recent buffer + running summary) │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

# SECTION 1: LLM Evaluations (Evals) & RAG Triad Deep Dive

### 1. Context Load Management & Execution Strategy for LLM-as-a-Judge
When an LLM evaluates another LLM's outputs, the evaluator's context window must not be overloaded.
* **The 20% Context Saturation Rule:** LLMs perform optimal semantic reasoning when their context window is roughly **≤ 20% full**. Overcrowding causes attention diffusion, bias, and evaluator hallucination.
* **Per-Call Granularity:** Rather than evaluating all goldens and metrics in a single prompt, each golden is judged via dedicated, atomic LLM calls per metric (e.g., 5 goldens × 5 metrics = 25 distinct LLM calls).
* **API Rate-Limit Cool-downs:** 
  * `sample_cool_down = 25s` (between metric evaluations of a single sample)
  * `experiment_cool_down = 35s` (between goldens/experiments)
  * Implemented via asynchronous execution (`asyncio.sleep`) to prevent bursting Groq/Gemini TPM/RPM rate limits.
* **Model Separation (Mitigating Self-Preference Bias):**
  * **Generator Model:** Google Gemini (generates RAG responses).
  * **Judge Model:** Meta Llama 3.1 8B via Groq (evaluates metrics).
  * *Best Practice:* Never evaluate an LLM using the same model family/provider that generated the response to eliminate inherent architectural self-bias.

---

### 2. The 5 Core Evaluation Metrics (Formulas, Mechanics & Diagnostics)

```
                       ┌─────────────────────────┐
                       │       User Query        │
                       └───────────┬─────────────┘
                                   │
              Context Precision    │    Answer Relevancy
             (Context Relevancy)   │
                                   ▼
┌──────────────────────┐  Faithfulness   ┌──────────────────────┐
│  Retrieved Context   │ ◄─────────────► │    Model Response    │
│   (Knowledge Base)   │ (Groundedness)  │  (RAG Actual Output) │
└──────────────────────┘                 └──────────────────────┘
           ▲                                        ▲
           │          Context Recall                │  Answer Correctness
           └────────────────────────────────────────┴────────────────────
                                   ▲
                       ┌───────────┴─────────────┐
                       │ Ground Truth Reference  │
                       └─────────────────────────┘
```

#### Metric 1: Faithfulness (Groundedness)
* **Definition:** Measures whether the LLM's generated response is strictly grounded in and inferable from the retrieved context chunks (checks for hallucinations).
* **Evaluation Workflow:**
  1. The LLM judge parses the generated response and decomposes it into discrete **atomic claims** ($C_1, C_2, \dots, C_n$).
  2. For each atomic claim, the judge asks: *"Can this claim be fully inferred from the retrieved context?"* (Yes / No).
  3. Claims with no support in the retrieved chunks are flagged as **hallucinations**.
* **Formula:**
  $$\text{Faithfulness} = \frac{|\text{Grounded Claims}|}{|\text{Total Generated Claims}|}$$
* **Lecture Example:**
  * Response contains 4 claims regarding account rules and online transfer fees. 3 claims are directly found in the chunks; 1 claim ("transfer funds online at no extra cost") is absent from the text.
  * Score: $3 / 4 = 0.75$. If threshold is set to $0.80$, the test fails.

#### Metric 2: Answer Relevancy
* **Definition:** Measures whether the response directly addresses the user's input query, penalizing off-topic, evasive, or padded answers.
* **Evaluation Workflow (Inverse Question Generation):**
  1. The LLM judge reads **only the generated output** (without seeing the original user query).
  2. The judge generates $N$ hypothetical questions that this output would directly answer.
  3. A dense semantic embedding model (or cross-encoder) computes the cosine similarity between each generated question ($q_i$) and the original user query ($q_{\text{orig}}$).
* **Formula:**
  $$\text{Answer Relevancy} = \frac{1}{N} \sum_{i=1}^N \text{CosineSimilarity}(E(q_i), E(q_{\text{orig}}))$$
* **Failure Modes:** 
  * Off-topic wandering.
  * Excessive boilerplate / conversational filler padding.
  * Incomplete responses failing to answer core intent.

#### Metric 3: Context Precision (Ranking Quality)
* **Definition:** Evaluates the retriever's ranking performance—whether the most relevant chunks are placed at the top (rank 1, 2) rather than buried beneath irrelevant noise.
* **Evaluation Workflow:**
  1. For each retrieved chunk in Top-$K$, the judge checks binary relevance to the golden query.
  2. Calculates cumulative precision at each relevant rank position (Mean Average Precision logic).
  3. Relevant chunks that appear *after* irrelevant chunks suffer rank penalties.
* **Formula (Precision@K / Mean Average Precision):**
  $$\text{Context Precision@K} = \frac{\sum_{k=1}^K (\text{Precision}@k \times I_k)}{|\text{Total Relevant Chunks in Top-}K|}$$
  *(where $I_k \in \{0, 1\}$ indicates relevance of chunk $k$)*.
* **Remediation:** If context precision is low despite accurate embeddings, integrate a **Cross-Encoder Re-ranker** (e.g., Cohere Rerank, BGE-Reranker) downstream of vector search.

#### Metric 4: Context Recall
* **Definition:** Measures whether the retrieval pipeline fetched **all** facts necessary to formulate the ground truth answer.
* **Evaluation Workflow:**
  1. The judge decomposes the **Ground Truth (Golden Reference)** into atomic claims ($R_1, R_2, \dots, R_m$).
  2. Each reference claim is verified against the retrieved context: *"Can this ground truth claim be attributed to any retrieved chunk?"*
* **Formula:**
  $$\text{Context Recall} = \frac{|\text{Reference Claims Attributable to Retrieved Chunks}|}{|\text{Total Reference Claims}|}$$
* **Key Distinction vs. Faithfulness:** 
  * *Faithfulness* tests if the *Response* is bounded by *Context* (detects hallucination).
  * *Context Recall* tests if the *Context* covers the *Golden Reference* (detects retriever omission).
* **Failure Modes:**
  * Top-$K$ parameter is set too low (e.g., $K=3$, but the critical fact was chunk 4).
  * Semantic embedding mismatch / vocabulary gap.

#### Metric 5: Answer Correctness
* **Definition:** Compares the generated response against the ground truth reference across two distinct dimensions: factual accuracy and semantic alignment.
* **Two-Part Formulation:**
  1. **Factual Correctness ($F_1$ Score):** Claims from response and ground truth are categorized into True Positives ($TP$, grounded and true), False Positives ($FP$, hallucinated/incorrect), and False Negatives ($FN$, omitted ground truth claims).
     $$\text{Factual } F_1 = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$
  2. **Semantic Similarity:** Cosine similarity between dense embeddings of the response and the reference:
     $$\text{Semantic Sim} = \cos(\mathbf{e}_{\text{response}}, \mathbf{e}_{\text{ref}})$$
* **Composite Formula:**
  $$\text{Answer Correctness} = W_1 \cdot (\text{Factual } F_1) + W_2 \cdot (\text{Semantic Sim})$$
  *(where $W_1 + W_2 = 1.0$; typically weighted toward factual precision, e.g., $W_1 = 0.75, W_2 = 0.25$)*.

---

### 3. Automated Evaluation Dashboard & Workflow
* **Per-Golden Traceability:** Streamlit-based UI reports aggregate scores, per-golden radar/bar charts, and raw JSON export.
* **Failure Isolation:** Developers can pinpoint whether a RAG failure originated in the Ingestion/Retrieval stage (low Context Precision/Recall) or Generation stage (low Faithfulness/Answer Correctness).

---

# SECTION 2: Agentic Memory Systems & Architectures

### 1. Motivation: The Statelessness Imperative
* **The Nature of LLMs:** Modern foundation models are inherently stateless by design; each API call is completely isolated.
* **The Engineering Problem:** Agents requiring multi-turn autonomy, long-term collaboration, or workflow persistence must maintain **State** (shared memory across the workflow schema).
* **Production Architecture Reference Case Study:**
  * Real-world pipeline indexing **500,000 Clinical Trials** (`clinicaltrials.gov`) and **PubMed research papers**.
  * GCP Infrastructure: Google Cloud Storage (raw/parsed data), Cloud SQL + `pgvector` (hybrid relational & vector storage).
  * Memory Engine: `LangMem` managing episodic, procedural, and semantic memory layers.
  * Multi-Agent Core: 6 worker agents (Pattern Finder, Track Record Agent, etc.) + 1 Master Orchestrator, with Human-in-the-Loop confidence thresholds and LangSmith/GCP Cloud Logging.

### 2. The Comprehensive Agent Memory Lineage
As agent systems evolved, memory designs transitioned from naive in-memory buffers to complex multi-tiered storage:
1. **Conversational Buffer Memory** (Raw message appending)
2. **Sliding Window Memory** (Fixed-turn FIFO eviction)
3. **Summary Memory** (Progressive/abstractive compression)
4. **Summary Buffer Memory** (Hybrid: verbatim tail + compressed head)
5. **Token Buffer Memory** (Token-budget bounded truncation)
6. **Vector Store Memory** (Semantic embedding retrieval)
7. **Entity Memory** (Named-entity knowledge extraction)
8. **Episodic Memory** (Time-aware past session recall)
9. **Semantic Memory** (Distilled user facts and behavior patterns)
10. **Procedural Memory** (Dynamic system instructions & agent rule updates)
11. **Self-Reflection Memory** (Post-execution task postmortems)
12. **Memory Routing** (Intent-classified retrieval dispatching)
13. **Temporal Memory & Decay** (Ebbinghaus forgetting curves / half-life decay)

*Key Research Citations:*
* **NUS (National University of Singapore) Breakthrough Paper (Jan 2026):** Taxonomy of memory carriers (Flat vs. Planar vs. Hierarchical token memory; Parametric vs. Latent memory).
* **Magma Architecture:** Multi-graph agentic memory for complex multi-agent workflows.
* **Graphiti (Neo4j):** Knowledge-graph based episodic-semantic agent memory.

---

### 3. Deep-Dive into the First 4 Memory Techniques

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ 1. Conversational Buffer Memory                                                 │
│    [Turn 1] -> [Turn 2] -> [Turn 3] -> ... -> [Turn N]   (Prompt grows O(N²))   │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 2. Sliding Window Memory (Window Size K=3)                                      │
│    [Turn 1 (EVICTED)] [Turn 2 (EVICTED)] | [Turn 3] [Turn 4] [Turn 5]           │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 3. Summary Memory                                                               │
│    [LLM Summarizer: "User is Chiru, earns 120k, expenses 60k..."]               │
│    -> Sent to Turn N as system context                                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 4. Summary Buffer Memory                                                        │
│    [Compressed Summary of Turns 1..N-K] + [Verbatim Buffer of Last K Turns]     │
└─────────────────────────────────────────────────────────────────────────────────┘
```

#### Technique 1: Conversational Buffer Memory
* **Mechanics:** Stores raw conversational message objects (`SystemMessage`, `HumanMessage`, `AIMessage`, `ToolMessage`) in an ordered list, passing the full unedited history in each subsequent prompt.
* **Token Compounding Problem:**
  * For turn $N$, the prompt contains all previous $N-1$ turns. Cumulative tokens across a session grow **quadratically ($O(N^2)$)**.
  * *Lecture Experiment (FinCoach):* In just 5 conversational turns, prompt tokens ballooned from 279 to 907 (consuming **18.3%** of a 4k token budget). By turn 10, token consumption increased by **6.6×**.
* **Trade-Off Matrix:**
  * *Pros:* 100% deterministic, perfect recall, zero latency overhead (no background LLM summarization calls).
  * *Cons:* Rapid context overflow, astronomical API costs, attention degradation over long context.
* **Production Reality:** Never used alone in production; only used within an active short-term session bounded by hard token limits.

#### Technique 2: Sliding Window Memory
* **Mechanics:** Bounded FIFO queue maintaining the last $K$ turns (where 1 turn = 1 User Message + 1 Assistant Message; $K$ is a hyperparameter, e.g., $K=3$ or $K=5$).
* **Eviction Behavior:** When turn $K+1$ arrives, turn 1 is **evicted** (pushed out of the context window).
* **The Forgetting Problem:**
  * Crucial entity facts established in early turns (e.g., "My salary is 120k", "I am allergic to equity") are evicted.
  * *Lecture Demo:* By Turn 6, when the user asks *"Based on my salary, what SIP should I buy?"*, the agent replies: *"I don't have access to your previous salary information. Could you remind me?"* — leading to catastrophic user experience degradation.
* **Crucial Concept: Eviction $\neq$ Deletion:**
  * In production architectures, evicted turns must not be dropped into void; they are streamed to a long-term vector store or knowledge graph (creating a Short-Term / Long-Term Hybrid).
* **Context Echo Phenomenon:** When adjacent conversation turns remain tightly focused on a single topic, context reverberates naturally across turns, masking short window limits until a context shift occurs.

#### Technique 3: Summary Memory (Abstractive & Progressive)
* **Mechanics:** When conversation history crosses a token or turn threshold, a secondary LLM call condenses older turns into a concise running textual summary paragraph, replacing the raw history.
* **Abstractive Summarization:** Uses instruction-tuned models (e.g., GPT-4o-mini) to extract meaning and re-synthesize facts rather than simply extracting raw sentences.
* **Progressive / Hierarchical Summarization:**
  * **Level 0:** Raw verbatim dialog turns.
  * **Level 1:** Rolling turn summaries.
  * **Level 2:** Session summaries (1 paragraph per full session).
  * **Level 3:** Distilled user profile / factual key-value invariants.
* **The Fundamental Vulnerability: Lossy Compression:**
  * Summarization is inherently a lossy algorithm.
  * **Low-Frequency, High-Importance Problem:** A critical constraint mentioned once (e.g., *"Diabetic patient; strictly no glucose-raising drugs"*) survives the 1st summary compression, but by compression cycle 3, 4, or 100, the LLM drops it as low-frequency noise.
  * In medical or financial agents, this causes fatal hallucinations (recommending equities to risk-averse users or sugar to diabetics).
* **Trigger Mechanics:** Summarization is triggered on threshold breach (e.g., every $M$ turns or when buffer exceeds $T$ tokens), never on every turn (to prevent excessive latency and token expenditure).

#### Technique 4: Summary Buffer Memory
* **Mechanics:** The optimal balance of sliding window and summarization. It maintains two distinct zones in the prompt context:
  1. **Verbatim Buffer (Recent Memory):** Keeps the last $K$ messages word-for-word to retain immediate conversational nuance, phrasing, and tool outputs.
  2. **Summarized Memory (Historical Context):** Messages pushed out of the verbatim buffer are piped into a summarizer LLM, which updates a running historical summary.
* **Prompt Assembly Pipeline:**
  $$\text{Context} = \text{System Prompt} + \text{Running Summary} + \text{Recent Verbatim Buffer} + \text{New User Query}$$
* **Human Cognitive Analogy:** Exactly mimics human memory during a long telephone call: you remember the immediate last 2–3 sentences verbatim, while everything spoken 20 minutes prior is retained purely as a summarized conceptual gist.

---

### Comparative Analysis: Memory Techniques 1–4

| Feature / Metric | Conversational Buffer | Sliding Window | Summary Memory | Summary Buffer |
| :--- | :--- | :--- | :--- | :--- |
| **Context Window Consumption** | Unbounded ($O(N^2)$ cumulative) | Constant / Strictly Bounded | Low & Stable | Bounded & Highly Controllable |
| **Recall Quality** | Perfect (until window limit) | Degrades rapidly beyond $K$ turns | High-level gist only | Nuanced recently, gist historically |
| **Information Loss Rate** | 0% (within context limit) | 100% for evicted turns | Progressive (lossy compression) | Moderate (lossy on older turns only) |
| **Additional LLM Call Overhead**| None ($0 extra calls) | None ($0 extra calls) | 1 extra call per compression trigger | 1 extra call per eviction trigger |
| **Determinism** | 100% Deterministic | 100% Deterministic | Non-deterministic summary output | Hybrid |
| **Production Applicability** | Restricted to toy / short tasks | Used only in hybrid pairs | Used for long dialog sessions | Standard enterprise pattern |

---

## Architectural Best Practices & Engineering Takeaways

1. **Decouple Generator & Judge:** Always use separate model families for RAG generation and LLM evaluation (e.g., Gemini for generation, Llama 3.1 8B for judging) to prevent self-evaluating optimism bias.
2. **Buffer Saturation Safeguard:** Never load an LLM judge beyond 20% of its native context capacity to ensure objective, hallucination-free evaluations.
3. **Async Cool-downs in Evals:** Rigorously inject sample (25s) and experiment (35s) cool-downs when evaluating high-volume datasets to prevent API rate-limit throttling.
4. **Context Precision Drives Re-ranking:** If Ragas logs high Context Recall but low Context Precision, do not alter chunk sizes; introduce a Cross-Encoder Re-ranker.
5. **Never Deploy Raw Buffers:** Conversational buffer memory fails in enterprise multi-turn scenarios due to quadratic cost and window explosion.
6. **Protect Low-Frequency, High-Impact Facts:** In summary memory architectures, critical user constraints (allergies, risk profiles, regulatory restrictions) must be extracted into explicit **Entity/Procedural Memory** stores rather than relying solely on progressive abstractive summarization.
