# Skills

A collection of daily life skills, tools, and study notes.

## Contents

| Skill | Description |
|-------|-------------|
| `automate_notes.md` | Pipeline to convert YouTube videos into structured study notes |
| `clean_vtt.py` | Extract & clean YouTube subtitle (VTT) files |
| `split_chunks.py` | Split transcripts into chunks for parallel summarization |
| `outputs/` | Generated notes from various topics |

### Notes Available

- **Articulacy: From Monkey to Monk** — full communication course notes ([PDF](outputs/ARTICULACY_From_Monkey_To_Monk_Full_Course))
- **46 Years of Sales Knowledge in 76 Minutes** — sales training
- **Think Fast, Talk Smart** — communication techniques
- **Entire Map of Business** — business fundamentals
- **Ultimate Sales Training** — compiled sales knowledge

## Converting to PDF

```bash
pandoc notes.md --pdf-engine=weasyprint -c style.css -o notes.pdf
```
