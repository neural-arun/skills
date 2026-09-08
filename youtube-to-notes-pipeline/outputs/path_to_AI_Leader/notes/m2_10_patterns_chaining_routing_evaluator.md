# Patterns: Prompt Chaining, Routing, and Evaluator Optimizer

## 1. Executive Mental Model

Enterprise AI system design is fundamentally an exercise in structural composition. Rather than relying on a single, complex monolithic prompt to handle an entire business process, leading AI architects employ **Core Agentic Workflow Patterns** (popularized by Anthropic).

The executive mental model is **The Modular Workflow Pattern Taxonomy**:

```
 1. PROMPT CHAINING (Sequential Decomposition)
 [ Input ] ---> [ Step 1: Extract ] ---> [ Step 2: Validate ] ---> [ Step 3: Format ] ---> [ Final Output ]

 2. ROUTING (Specialized Intent Classification)
                                    +---> [ Financial Classifier Prompt ]
 [ Input ] ---> [ Intent Router ] --|---> [ Technical Support Prompt ]
                                    +---> [ Executive Legal Escalation ]

 3. EVALUATOR-OPTIMIZER (Iterative Quality Feedback Loop)
                                     +-----------------------+
                                     v                       |
 [ Input ] ---> [ Generator LLM ] -------> [ Evaluator LLM ] --+ (If score < Threshold)
                      |                         |
                      +-------------------------+---> [ Approved Output ] (If score >= Threshold)
```

*   **Prompt Chaining:** Breaks a complex task into a deterministic sequence of smaller LLM calls, passing intermediate outputs down the chain.
*   **Routing:** Classifies incoming requests to direct them to specialized prompts, lightweight models, or domain microservices.
*   **Evaluator-Optimizer:** Sets up a generator model to draft content and an evaluator model to critique it against an enterprise rubric, looping iteratively until quality targets are met.

---

## 2. Real-World Enterprise Case Studies (Wins & Failures)

### Strategic Wins

#### Duolingo: Evaluator-Optimizer for Conversational Content Generation
* **Strategy:** Scale the generation of complex, error-free foreign language learning dialogues and exercise questions across 40+ languages.
* **Implementation:** Implemented an **Evaluator-Optimizer loop**. Generator LLM drafts curriculum scenarios; Evaluator LLM assesses CEFR language level compliance, pedagogical accuracy, and tone. If the score falls below 95%, the evaluator feeds explicit revision critiques back to the generator.
* **Empirical Metrics & ROI:**
  * Scaled course content creation by **67x** compared to human-only creation teams.
  * Achieved **99.8% grammatical accuracy** across generated lesson content.
  * Reclaimed millions in human contractor content review OpEx.

#### Stripe: Routing Pattern for Customer Support & Risk Escalation
* **Strategy:** Classify and resolve millions of incoming merchant inquiries across billing, API integration, and fraud disputes.
* **Implementation:** Deployed an **Intent Router** model at the front door. Simple queries are routed to instant, cheap RAG lookup prompts; complex dispute queries are routed to specialized human-in-the-loop workflows.
* **Empirical Metrics & ROI:**
  * Reduced average resolution time by **40%**.
  * Lowered overall API token costs by **65%** by routing 70% of volume to small, cheap 8B models instead of expensive frontier models.

### Strategic Cautionary Tale / Failure

#### Global Financial Advisory: Infinite Evaluator-Optimizer Feedback Trap
* **Strategy:** Implemented an Evaluator-Optimizer pattern to generate ultra-long equity research reports.
* **Failure Incident:** The Evaluator model was given a vague, overly subjective evaluation rubric (*"Ensure the report is highly engaging, thorough, and flawless"*). The Generator and Evaluator models entered an endless refinement loop, repeatedly revising minor stylistic preferences without converging.
* **Financial & Latency Impact:** Single report executions ran for 15 minutes, consuming **$45 per run in tokens** and timing out host server connections before failing.
* **Remediation:** Replaced subjective rubrics with deterministic programmatic assertions (checking table formatting, numerical validation) and enforced a hard exit cap (`max_iterations = 2`).

---

## 3. Business Value & Monetization Levers (P&L Impact, Revenue Growth, Margin Expansion)

| Pattern | Architectural Trade-Off | Cost & Latency Impact | Best Enterprise Use Case |
| :--- | :--- | :--- | :--- |
| **Prompt Chaining** | Replaces complex single prompts with modular code nodes | Low Latency; highly predictable token costs | Document parsing, multi-step data extraction, report assembly. |
| **Routing** | Adds a front-door intent classifier | **Drastically Lowers OpEx** (Directs 70%+ queries to cheap models) | Customer support triage, multi-tenant intent distribution. |
| **Evaluator-Optimizer** | Adds iterative verification loops | High Latency & Token multiplier (2x–5x base cost) | High-stakes copy drafting, code synthesis, regulatory compliance. |
| **Parallelization** | Executes multiple LLM queries simultaneously | Increases token rate, but **slashes latency by 50%+** | Section-by-section document analysis, voting consensus. |

### Architectural Optimization Equation
$$\text{Workflow Efficiency} = \frac{\text{Precision Gain (nDCG / Accuracy)}}{\sum \left( \text{Token Cost per Step} \times \text{Loop Multiplier} \right) + \text{Latency (s)}}$$

---

## 4. What to Do for Success (The Leadership Playbook)

1. **Deploy Routing to Maximize Margin Expansion:**
   - Always place a lightweight classifier model (e.g., Llama-3-8B or Claude Haiku) at the entry point of your system. Route 70–80% of routine queries to low-cost specialized prompts, reserving expensive frontier models (GPT-4o / Claude Sonnet) for complex edge cases.
2. **Cap Evaluator-Optimizer Loops at Maximum 2 Refinement Passes:**
   - Never allow an Evaluator-Optimizer loop to run indefinitely. Limit iterations to `max_refinements = 2`. If quality targets are not met after 2 passes, route the draft to human review.
3. **Use Programmatic Assertions Alongside LLM Evaluators:**
   - Combine LLM subjective evaluation with hard code assertions (regex check for required fields, JSON schema validation, numerical sum checks) to ensure deterministic reliability.
4. **Decompose Complex Prompts into Sequential Chains:**
   - If a system prompt exceeds 1,500 words or attempts to perform 4 distinct tasks simultaneously, split it into a 3-step **Prompt Chain** to improve task precision by over 25%.

---

## 5. What to Avoid (Anti-Patterns, Money Pits & Traps)

* **The Monolithic "Mega-Prompt" Anti-Pattern:** Attempting to force an LLM to extract data, analyze sentiment, translate language, and format JSON inside a single giant prompt, causing severe attention degradation.
* **Vague Evaluator Rubrics:** Providing subjective, ambiguous prompts to Evaluator LLMs (e.g., *"Make this sound better"*), leading to endless refinement loops and non-deterministic behavior.
* **Ignoring Sequential Chaining Latency:** Chaining 6 sequential LLM calls together without measuring latency, resulting in a 12-second user wait time that kills application UX.

---

## 6. The 80/20 High-Leverage Strategic Takeaway

> **Mastering enterprise AI is about composability, not magic prompts. 80% of architecture efficiency is achieved by placing a Routing classifier at the front door to save token costs, and using Prompt Chaining to turn complex probabilistic tasks into reliable, modular code steps.**
