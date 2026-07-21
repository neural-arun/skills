# Think Fast, Talk Smart: Communication Techniques — Study Notes

> **Speaker:** Matt Abrahams, Stanford GSB
> **Core topic:** Spontaneous speaking — cold calls, Q&A, introductions, feedback, toasts
> **Context for:** Arun Yadav — AI Systems Engineer, Healthcare & Medical Education AI

---

## 1. Core Thesis

Spontaneous speaking is **more prevalent** than planned speaking in daily work — yet most people are unprepared for it. Small shifts in approach, attitude, and practice make the biggest difference.

| Planned Speaking | Spontaneous Speaking |
|---|---|
| Keynotes, conference talks, formal toasts | Cold calls, Q&A, introductions, giving feedback, surprise toasts |
| Slides, rehearsal, scripted | In the moment, no prep |
| Less common day-to-day | **More common day-to-day** |

---

## 2. Anxiety Management (Not Elimination)

85% of people are nervous speaking in public. Public speaking ranks among the top 5 human fears. The goal is **not** to eliminate anxiety — it gives energy, focus, and signals importance.

### Technique 1: Greet Your Anxiety
When symptoms appear (gurgly stomach, shaky legs), most people spiral: *"I'm nervous → they'll know → this will fail."*

**Fix:** Acknowledge it non-judgmentally. *"This is me feeling anxious. I'm about to do something of consequence."* This stops the spiral. It may not reduce anxiety, but it **prevents escalation**.

### Technique 2: Reframe Performance → Conversation
Most presenters treat speaking as a **performance** (right/wrong way, mistakes are catastrophic). **Reframe:** It's a **conversation**. There is no single right way, only better and worse.

**How to operationalize:**
- Ask questions (rhetorical, polling, eliciting responses)
- Outline as **questions, not bullet points** — *"Right now I'm answering the question: How do we manage our anxiety?"*
- Structure AI walkthroughs as Q&A sessions, not feature dumps

### Technique 3: Present-Moment Orientation
Research by Phil Zimbardo: Future-oriented thinking (worrying about outcomes) drives anxiety. Staying present reduces it.

**Present-moment techniques:**
- Physical activity (walk, push-ups)
- Music/playlist focus
- Counting backwards by hard numbers
- **Tongue twisters** — force presence + warm up voice

---

## 3. The Four-Step Spontaneous Speaking Process

| Step | Maxim | What It Means | AI Engineering Parallel |
|------|-------|--------------|------------------------|
| **1. Get out of your own way** | Dare to be dull | Stop trying to be perfect. The harder you try to be great, the more you freeze. | Don't over-constrain agent prompts with excessive guardrails. Give agents room to be "dull" in chain-of-thought before producing polished output. |
| **2. See opportunity, not threat** | Yes, and | Reframe Q&A, cold calls as chances to connect, not tests to pass. Accept what's given, then build on it. | Design agents with a "yes, and" posture — when a user asks something unexpected, build on it rather than deflect. |
| **3. Slow down and listen** | Don't just do something, stand there | Listen first, then respond. You cannot multitask genuine listening. | Implement a "listen-first" pattern in conversational agents — explicit listening/rephrasing step before answering. |
| **4. Use structures** | Structure sets you free | Deploy frameworks like PSB or What-So What-Now What on instinct. Externalize the *how* to free cognitive load for the *what*. | Enforce structured output frameworks in agents (Problem-Solution-Benefit as default response schema). |

---

## 4. Step 1 — Get Out of Your Own Way

### The Problem
Perfectionism and Type-A striving block authentic response. Your brain stockpiles patterns to "master the situation" — this planning is the *only* way to fail.

### "Shout the Wrong Name" Exercise
Point at objects and call them anything but what they really are. No planning, no stockpiling — just react.

### "Thank Your Brain" Technique
When your brain offers a pattern or stockpile, mentally say **"thank you brain"** and disregard it — like a **windshield wiper**. Acknowledge the suggestion, wipe it away, see what happens next.

> **Core lesson:** There is no way to get it right. Just doing it gets it right.

### "Dare to Be Dull"
The harder you try to be great, the more you freeze. By daring to be dull — accepting mediocrity — you release the pressure and actually become effective.

---

## 5. Step 2 — See Opportunity, Not Threat

### The Imaginary Gift Game
- Partner A mimes handing Partner B a gift (no description)
- Partner B "opens" it and says the **first thing** that comes to mind
- Partner B then gives a gift back — repeat
- Giver must accept and justify the receiver's reality

**Why it works:** Reframes spontaneous speaking as **co-creation** rather than performance. When you treat it as a fun opportunity to co-create, you become less nervous, less defensive, and more present.

### The "Yes, And" Principle
Most people live their communication lives saying **"No"** (defensive, blocking). "Yes, and" opens up opportunities — not literal agreement, but an open, building mindset.

### Reacting vs. Responding
- **Reacting** = think first, then act — too slow, too rehearsed
- **Responding** = genuine, authentic, in-the-moment

---

## 6. Step 3 — Slow Down and Listen

### The Spelling Game
Partners spell out letter-by-letter a fun thing they plan to do today. Person A spells, Person B decodes.

**Key lessons:**
- **Pause between words** — speed = noise, not clarity
- **Deep listening requires presence** — you cannot plan your response while decoding spelled letters
- **"Don't just do something, stand there... listen and then respond"** — the counterintuitive truth

Your job as communicator = **serve your audience**. You can't serve what you don't understand. We often listen just enough to think we got it, then mentally race ahead.

---

## 7. Step 4 — Use Structures

Structured information is processed **40% more efficiently** (processing fluency). Structures externalize the *how*, freeing cognitive load for the *what*.

### Problem-Solution-Benefit (PSB)
| Phase | Question | Example (RAG pipeline) |
|-------|----------|----------------------|
| Problem | What's the issue? | Users get hallucinated answers |
| Solution | What do you propose? | Add a self-verify retriever |
| Benefit | What's the outcome? | Accuracy goes from 72% → 94% |

Can be reframed as **Opportunity-Solution-Benefit** when it's a gap to capture rather than a problem.

### What-So What-Now What
| Phase | Question | Example (Code Review) |
|-------|----------|----------------------|
| What | Describe what it is | This LangGraph node adds memory persistence |
| So What | Why it matters | It keeps context across patient sessions |
| Now What | Next steps | Deploy to staging next sprint |

Adapt for introductions: **Who** they are → **So What** why important → **Now What** what happens next.

> **"Structure sets you free."** — The irony is real: having a rigid framework reduces cognitive load, letting you focus on content.

---

## 8. Conversational Language

Nervous speakers **distance** themselves — physically and linguistically.

| Instead of | Use |
|---|---|
| "One must consider the ramifications" | "This is important to you — we all need to be concerned with..." |
| "Step one, step two, step three..." | "First, what we need to do is this. The second thing you should consider is..." |
| "Today we're going to cover..." | "Here's what I want to share with you..." |

**Key mechanism:** Use **inclusive pronouns** (we, you, us) — they signal collaboration, not broadcast.

---

## 9. Handling Hostile / Challenging Q&A

### Three-Step Protocol
1. **Acknowledge the emotion** — but don't name it. Never say "you sound angry." Say: *"I hear you have a lot of passion on this issue."*
2. **Reframe** — redirect to a question you're comfortable answering.
3. **Truly listen** — don't get defensive. See every challenging question as an opportunity.

### Paraphrasing (Swiss Army Knife)
When a tough question lands, **paraphrase it back** before answering: *"So what you're really asking about is X, Y, and Z."* This buys you time, reframes the question in your terms, and confirms understanding.

### Remote / Distributed Audiences
- Actively remember the remote audience exists
- Use polling, shared docs, real-time engagement
- **Imagery:** *"Imagine what it would be like if..."* — pulls people in
- **Pacing:** Talk 10-15 min → apply → repeat

### Hostile Planned Situations (Cross-Examination)
- **Prepare themes, not scripts** — identify 3-5 themes with concrete examples
- Don't memorize exact phrasing; hold ideas and assemble dynamically

---

## 10. Asking Better Questions

| Technique | How It Works | AI Systems Application |
|-----------|-------------|----------------------|
| **"Why"** | Ask "why" a few times to cut through rehearsed answers to deeper truth | Requirements gathering: keep asking why to surface actual clinical workflow needs |
| **Ask for advice** | *"What advice would you give someone in this situation?"* — changes dynamic from interrogation to guidance | *"What advice would you give a junior doctor using this system?"* → richer requirements than *"How should the UI work?"* |

---

## 11. Humor — Risks & Rewards

- Humor is powerfully connecting but **high-risk** across cultures
- **Self-deprecating humor** is safest — lowest risk of backfire
- Before using a joke: (1) Is it funny? (2) What's the backup plan? (3) If worried, skip it
- A failed joke sets you back further than no joke at all

---

## 12. Quick Reference Card

| Situation | Strategy |
|---|---|
| Pre-talk jitters | Greet anxiety: *"This is me feeling anxious"* |
| Feeling performative | Reframe: *"I'm having a conversation"* |
| Audience feels distant | Ask a question (any question) |
| Notes feel stiff | Rewrite as questions, not bullet points |
| Language feels formal | Swap impersonal for inclusive (we/you/us) |
| Tough question lands | Paraphrase it back before answering |
| Hostile pushback | Acknowledge emotion → reframe → listen |
| Demo goes wrong | Conversational framing makes recovery natural |
| Need to structure answer | Use PSB or What-So What-Now What |
| Unexpected question | "Yes, and" — build on it, don't deflect |

---

## 13. AI Systems Engineering Parallels

| Communication Skill | AI Engineering Application |
|---|---|
| **"Thank you brain" (wipe stockpiles)** | Stop over-planning the perfect retrieval strategy. Run the query, observe output, iterate. |
| **Dare to be dull** | Don't over-constrain agent prompts with excessive guardrails. Give agents room in chain-of-thought. |
| **"Yes, and"** | When user asks something unexpected, build on it rather than deflect — especially in RAG where queries don't perfectly match indexed docs. |
| **Listen fully before responding** | Agentic workflows should gather all context first (tool calls, DB lookups) before generating. Don't hallucinate answers mid-stream. |
| **Structure sets you free** | Use LangChain LCEL or LangGraph StateGraph as your communication structure — framework handles *how*, you focus on *what*. |
| **Problem-Solution-Benefit** | Pitch a RAG upgrade: "Users get hallucinated answers → self-verify retriever → 94% accuracy." |
| **What-So What-Now What** | Code review: "This node adds memory → keeps context across sessions → deploy next sprint." |
| **Paraphrase for alignment** | Stakeholder says "make it faster" → "So you want query latency under 200ms at P99?" |
| **Prepare themes, not scripts** | Architecture reviews: hold 3-5 themes (security, accuracy, speed) with concrete benchmarks — adapt to the moment. |
| **Acknowledge emotion without labeling** | Doctor questions your diagnostic suggestion → "I hear real caution about clinical accuracy" → reframe to validation process. |
| **Ask for advice, not answers** | *"What advice would you give a junior doctor using this system?"* — extracts richer requirements. |
| **Cultural adaptation** | Demo to clinicians vs. engineers vs. execs with different vocabulary, depth, and visuals. |
