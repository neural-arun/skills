# YouTube to Structured Study Notes — Automation Pipeline

## Overview

This pipeline takes a YouTube video URL and produces a structured, polished study notes document. It downloads auto-generated subtitles, splits the transcript into a dynamic number of chunks (based on video length), summarizes each chunk via parallel subagents, and merges everything into one coherent file.

**Output:** A new folder `./outputs/{video_title}/` containing all intermediate files and a final `{video_title}.md`.

---

## Prerequisites

- Python 3 with `yt-dlp` installed (`pip install yt-dlp`)
- The agent has access to the Task/Subagent tool for parallel work

---

## Step 1: Accept Input

Accept a YouTube URL from the user. Write it to `youtube.txt` in the current directory.

```bash
echo "$URL" > youtube.txt
```

Or read from an existing `youtube.txt` if the user has already created one.

---

## Step 2: Get Metadata & Determine Chunk Count

Get the video title and duration using `yt-dlp` (no download):

```bash
yt-dlp --print title --print duration "$URL" > /tmp/video_meta.txt
```

Read the first line as title, second line as duration (in seconds).

**Normalize the title** for use as both folder name and filename:
- Replace spaces with underscores
- Remove special characters (keep letters, numbers, underscores, hyphens)
- Truncate if longer than 80 chars

**Calculate chunk count** from duration (~1 chunk per 20 minutes):

| Duration | Chunks |
|----------|--------|
| < 20 min | 1 |
| 20–40 min | 2 |
| 40–60 min | 3 |
| 60–90 min | 4 |
| > 90 min | 5+ |

Formula: `chunks = max(1, min(10, round(duration_seconds / 1200)))` (~1 chunk per 20 min)

**Allow user override** — if the user specifies a chunk count in their prompt, use that instead.

Create the output directory:

```bash
mkdir -p "./outputs/{normalized_title}"
```

All subsequent files go inside this directory.

---

## Step 3: Download Subtitles

```bash
yt-dlp --write-auto-subs --sub-lang en --skip-download \
  -o "./outputs/{normalized_title}/%(title)s [%(id)s]" \
  "$URL"
```

This produces a `.vtt` file in the output directory. Capture the exact file path with `ls "./outputs/{normalized_title}/*.en.vtt"`.

**If no auto-generated captions exist**, try `--sub-lang en` without `--write-auto-subs`, or ask the user for a different approach.

---

## Step 4: Extract & Clean Transcript

Read the `.vtt` file. Parse it to extract only the text content:

1. Skip VTT header lines (WEBVTT, language metadata, timestamps, empty lines)
2. Strip HTML-like tags (`<c>`, `</c>`, `<00:00:00.000>`, etc.)
3. Remove speaker labels in angle brackets like `<v SpeakerName>`
4. Join lines into clean paragraphs (a paragraph is text between two consecutive timestamps)
5. Strip leading/trailing whitespace per segment

**Output:** `transcript_raw.md` in the output directory.

---

## Step 5: Split into N Chunks

1. Count total words in `transcript_raw.md`
2. Target words per chunk = `total_words / chunk_count` (from Step 2)
3. Split at natural sentence boundaries near each target point
4. Write each chunk to `part_01.md` through `part_{chunk_count}.md` (zero-padded to 2 digits) in the output directory

**Important:** Keep the raw transcript text — no summaries, no analysis.

---

## Step 6: User Context (Personalized & Blended Integration)

The user is **Arun Yadav (neural-arun)** — an AI Systems Engineer building AI systems for Healthcare and Medical Education. His stack includes RAG Pipelines, Agentic AI, MCP, FastAPI, LangChain, LangGraph, ChromaDB, Pinecone, and Playwright.

> **CRITICAL INSTRUCTION FOR CONTEXT:**  
> Do **NOT** put personalized context as a separate section at the very end of the notes.  
> Instead, **seamlessly blend** context mappings (AI systems, RAG pipelines, FastAPI, vector search, clinical data governance, MCP) **throughout the entire note** within each relevant technical topic.

---

## Step 7: Create Subagent Summaries & Note Formatting Rules

Each summary must be **concise yet complete**, providing thorough explanations without being overly verbose:
- Include complete explanations, architectural diagrams (Mermaid), and practical code/config snippets (FastAPI, Python, SQL, NGINX).
- Ensure 100% technical completeness while maintaining clear headings, bullet points, and high readability.

> **CRITICAL FORMATTING RULES FOR PDF & MARKDOWN CLEANLINESS:**  
> 1. **NO EMOJIS IN HEADINGS**: Do NOT use emojis (e.g. 🎯, 📘, 📌, 🌐, 🚫, 💡) in `#`, `##`, `###` headings or titles. Emojis cause missing glyph box (`.notdef` rectangle) artifacts in PDF font rendering.  
> 2. **NO RAW LATEX MATH IN TEXT**: Do NOT use LaTeX math code like `$\rightarrow$`, `\rightarrow`, `\times`, etc. in text or inline code blocks. Use clean Unicode characters (`→`, `*`, `x`) or ASCII (`->`).  
> 3. **NO RAW CHECKBOX ARTIFACTS**: Use standard bullet points (`-`) instead of `- [x]` or `- [ ]` in summary lists.  
> 4. **VALID MERMAID SYNTAX ONLY**: Ensure all Mermaid diagrams are valid flowcharts or sequence diagrams that render cleanly without syntax error boxes.

Each subagent returns a confirmation. Collect all N confirmations before proceeding.

---

## Step 8: Combine, Stitch & Polish (Zero Content Loss)

**8a. Concatenate:**

```bash
cat {output_dir}/summary_01.md ... {output_dir}/summary_{N}.md > {output_dir}/combined.md
```

**8b. Seamless Stitching & Flow Connection:**

Read `combined.md` and weave the chunks into a unified, unbroken master document without losing detail:

1. **ZERO Content Loss Rule:** Do NOT summarize, compress, or delete the substance of the subagent summaries. Retain 100% of the granular frameworks, case studies, dialogue teardowns, mathematical models, and tactical steps.
2. **Bridge Chunk Seams & Narrative Flow:** Where the end of Chunk $N$ transitions abruptly to Chunk $N+1$, craft smooth transition bridges so the narrative flows logically and continuously.
3. **Clean Boundary Artifacts:** Remove isolated subagent boilerplate (e.g., redundant bio intros per chunk, repetitive header fragments) and eliminate only local verbatim overlaps where adjacent chunk boundaries repeated transcript lines.
4. **Normalize Hierarchy & Architecture:** Unify header levels (`#`, `##`, `###`), ensure code/formula blocks are properly formatted, and insert a Master Table of Contents / Executive Roadmap at the top.
5. **Preserve Deep Analogies:** Ensure all personal context mappings (e.g., trust engineering, AI systems architecture, clinical reasoning) remain rich, actionable, and prominent.

**8c. Write final outputs:**

1. Write the comprehensive document to `{output_dir}/{normalized_title}.md`.
2. Generate Standalone HTML and Chrome Print PDF using `build_html_and_pdf.py`:

```bash
python3 build_html_and_pdf.py "{output_dir}/{normalized_title}.md" "{output_dir}/{normalized_title}.html" "{output_dir}/{normalized_title}.pdf"
```

---

## Step 9: Clean Up Intermediate Files

Delete all intermediate files — keep only the final output and the raw concatenation:

```bash
rm {output_dir}/*.vtt
rm {output_dir}/transcript_raw.md
rm {output_dir}/part_*.md
rm {output_dir}/summary_*.md
```

**Remaining files in output directory:**
- `{video_title}.md` — final polished study notes
- `combined.md` — raw concatenation of all summaries (kept as reference)

---

## File Reference (in output directory)

| File | Description |
|------|-------------|
| `transcript_raw.md` | Cleaned transcript text |
| `part_01.md` .. `part_{N}.md` | N raw transcript chunks |
| `summary_01.md` .. `summary_{N}.md` | N subagent summaries |
| `combined.md` | Raw concatenation of all summaries |
| `{video_title}.md` | Final polished study notes |
| `*.en.vtt` | Raw subtitle download |

---

## Reproducing for Another Video

1. Delete the previous folder in `outputs/` (or keep it — they're independent)
2. Run Steps 1–8 with the new URL
3. Output goes to a new folder under `outputs/` with a name matching the new video

---

## Optional Customizations

- **Override chunk count:** Pass `chunks: 5` in your prompt to override the auto-calculated value
- **Subtitle language:** Change `--sub-lang en` to `--sub-lang es`, `fr`, etc. in Step 3
- **Skip restructuring:** Stop after Step 8a if you want raw concatenated summaries
- **Custom folder name:** Override the normalized title with your own folder name
- **Different user context:** Replace Step 6 with a different bio for personalized notes
