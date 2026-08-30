import sys
import re
import os

def split_chunks(out_dir, chunk_count):
    raw_path = os.path.join(out_dir, 'transcript_raw.md')
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"File not found: {raw_path}")

    with open(raw_path, 'r', encoding='utf-8') as f:
        transcript = f.read()

    words = transcript.split()
    total_words = len(words)
    target_per_chunk = total_words // chunk_count

    print(f"Total words: {total_words}")
    print(f"Target per chunk: {target_per_chunk}")

    # Split at sentence boundaries near target points
    sentences = re.split(r'(?<=[.!?])\s+', transcript)

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        sentence_word_count = len(sentence.split())
        
        if current_word_count + sentence_word_count > target_per_chunk and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_word_count = sentence_word_count
        else:
            current_chunk.append(sentence)
            current_word_count += sentence_word_count

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    # Adjust chunk count if needed
    while len(chunks) < chunk_count and len(chunks) > 0:
        largest_idx = max(range(len(chunks)), key=lambda i: len(chunks[i].split()))
        largest = chunks[largest_idx]
        largest_words = largest.split()
        if len(largest_words) < 2:
            break
        mid = len(largest_words) // 2
        chunks[largest_idx] = ' '.join(largest_words[:mid])
        chunks.insert(largest_idx + 1, ' '.join(largest_words[mid:]))

    while len(chunks) > chunk_count:
        smallest_idx = min(range(len(chunks)), key=lambda i: len(chunks[i].split()))
        if smallest_idx > 0:
            chunks[smallest_idx - 1] = chunks[smallest_idx - 1] + ' ' + chunks[smallest_idx]
            del chunks[smallest_idx]
        elif smallest_idx + 1 < len(chunks):
            chunks[smallest_idx] = chunks[smallest_idx] + ' ' + chunks[smallest_idx + 1]
            del chunks[smallest_idx + 1]

    for i, chunk in enumerate(chunks, 1):
        filename = f"part_{i:02d}.md"
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(chunk.strip())
        wc = len(chunk.split())
        print(f"{filename}: {wc} words")

    print(f"Total chunks created: {len(chunks)}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python split_chunks.py <out_dir> <chunk_count>")
        sys.exit(1)
    split_chunks(sys.argv[1], int(sys.argv[2]))
