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

**Calculate chunk count** from duration:

| Duration | Chunks |
|----------|--------|
| < 10 min | 2 |
| 10–30 min | 4 |
| 30–60 min | 6 |
| 60–120 min | 10 |
| > 120 min | 15 |

Formula: `chunks = max(2, min(20, round(duration_seconds / 360)))` (~1 chunk per 6 min)

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

## Step 6: User Context (Personalized)

The user is **Arun Yadav (neural-arun)** — an AI Systems Engineer building AI systems for Healthcare and Medical Education. His stack includes RAG Pipelines, Agentic AI, MCP, FastAPI, LangChain, LangGraph, ChromaDB, Pinecone, and Playwright.

His GitHub bio reads:
> AI Systems Engineer | Building AI systems for Healthcare and Medical Education | RAG Pipelines • Agentic AI • MCP • FastAPI • SQL • Data Scraping

This bio is the **default context** for all summaries. Every subagent uses this to tailor notes to Arun's background — connecting concepts back to AI systems, healthcare, automation, and RAG pipelines.

**If the user wants a different context**, they can override by passing an explicit bio/background in the initial prompt.

---

## Step 7: Create N Subagent Summaries

Launch **N subagents in parallel** (N = chunk_count from Step 2), one per chunk. Each agent:

```
Input:  {output_dir}/part_{XX}.md
Task:   Summarize the content as concise, actionable study notes
Style:  Extract key concepts, frameworks, and lessons clearly
Context: Arun Yadav (neural-arun) — AI Systems Engineer building AI for Healthcare & Medical Education.
         Stack: RAG Pipelines, Agentic AI, MCP, FastAPI, LangChain, LangGraph, ChromaDB, Pinecone.
         Connect lessons to what Arun builds — AI systems, automation, document intelligence.
Output: {output_dir}/summary_{XX}.md
```

Each subagent returns a confirmation. Collect all N confirmations before proceeding.

---

## Step 8: Combine & Polish

**8a. Concatenate:**

```bash
cat {output_dir}/summary_01.md ... {output_dir}/summary_{N}.md > {output_dir}/combined.md
```

**8b. Restructure for coherence:**

Read `combined.md` and rewrite it so topics flow logically:

1. Identify recurring themes across all summaries
2. Group related concepts from different parts into unified sections
3. Order them in a natural learning progression
4. Remove redundant headings and section artifacts
5. Merge duplicate topics into single sections
6. Give each section a meaningful title

**8c. Write final output:**

Write the restructured document to `{output_dir}/{normalized_title}.md`.

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
