import os
import re
import math
import json

SOURCE_DIR = "./outputs/Backend_engineering"
WORK_DIR = "./outputs/Backend_engineering_work"

def split_text_into_chunks(text, max_words=3000):
    words = text.split()
    if len(words) <= max_words:
        return [text]

    num_chunks = math.ceil(len(words) / max_words)
    chunk_size = math.ceil(len(words) / num_chunks)

    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))

    return chunks

def main():
    os.makedirs(WORK_DIR, exist_ok=True)
    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith(".md")])

    manifest = []

    for f_name in files:
        src_path = os.path.join(SOURCE_DIR, f_name)
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()

        base_name = os.path.splitext(f_name)[0]
        lesson_dir = os.path.join(WORK_DIR, base_name)
        os.makedirs(lesson_dir, exist_ok=True)

        chunks = split_text_into_chunks(text, max_words=3000)
        chunk_files = []

        for idx, chunk_text in enumerate(chunks, 1):
            c_filename = f"part_{idx:02d}.md"
            c_path = os.path.join(lesson_dir, c_filename)
            with open(c_path, "w", encoding="utf-8") as cf:
                cf.write(chunk_text)
            chunk_files.append({
                "part": idx,
                "file": c_path,
                "words": len(chunk_text.split())
            })

        manifest.append({
            "lesson": base_name,
            "title": base_name.replace("_", " "),
            "source_file": src_path,
            "lesson_dir": lesson_dir,
            "total_words": len(text.split()),
            "total_chunks": len(chunks),
            "chunks": chunk_files
        })

    manifest_path = os.path.join(WORK_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, indent=2)

    print(f"Successfully chunked {len(manifest)} lessons into {WORK_DIR}.")

if __name__ == "__main__":
    main()
