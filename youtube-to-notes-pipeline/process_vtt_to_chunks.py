import re
import os
import glob
import math

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
VTT_PATH = os.path.join(OUTPUT_DIR, "subtitles.hi.vtt")

def clean_vtt(vtt_file):
    with open(vtt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    seen = set()
    last_line = ""
    
    in_header = True
    for line in lines:
        stripped = line.strip()
        if in_header:
            if stripped == "":
                in_header = False
            continue
        # Skip VTT timestamp headers
        if '-->' in stripped or re.match(r'^\d{2}:\d{2}:', stripped):
            continue
        if not stripped:
            continue
        # Strip html tags like <c> or timestamps
        text = re.sub(r'<[^>]+>', '', stripped).strip()
        if not text:
            continue
        # Deduplicate immediate consecutive identical lines
        if text != last_line:
            cleaned_lines.append(text)
            last_line = text
            
    transcript = " ".join(cleaned_lines)
    transcript = re.sub(r'\s+', ' ', transcript)
    return transcript

def split_into_chunks(transcript, num_chunks=15):
    words = transcript.split()
    total_words = len(words)
    chunk_size = math.ceil(total_words / num_chunks)
    
    chunks = []
    for i in range(0, total_words, chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def main():
    transcript = clean_vtt(VTT_PATH)
    words = transcript.split()
    print(f"Total cleaned words: {len(words)}")
    
    raw_path = os.path.join(OUTPUT_DIR, "transcript_raw.md")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"Saved raw transcript to {raw_path}")
    
    chunks = split_into_chunks(transcript, num_chunks=15)
    for idx, c in enumerate(chunks, 1):
        chunk_path = os.path.join(OUTPUT_DIR, f"part_{idx:02d}.md")
        with open(chunk_path, "w", encoding="utf-8") as cf:
            cf.write(c)
        print(f"Chunk {idx:02d}: {len(c.split())} words -> {chunk_path}")

if __name__ == "__main__":
    main()
