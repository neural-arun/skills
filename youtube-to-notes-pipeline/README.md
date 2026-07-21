# YouTube to Notes Pipeline

Turns any YouTube video into structured study notes.

## How It Works

1. Download auto-generated subtitles from a YouTube video
2. Clean and extract the transcript text
3. Split into chunks (based on video length)
4. Summarize each chunk in parallel
5. Combine and polish into one cohesive document

## Usage

```bash
# 1. Save the video URL
echo "https://youtu.be/VIDEO_ID" > youtube.txt

# 2. Follow automate_notes.md step by step
```

## Files

| File | Purpose |
|------|---------|
| `automate_notes.md` | Full step-by-step instructions |
| `clean_vtt.py` | Extract text from .vtt subtitle files |
| `split_chunks.py` | Split transcript into N equal chunks |
