import re
import os

out_dir = "./outputs/Entire_Map_of_Business_in_41_Minutes"
chunk_count = 7

with open(os.path.join(out_dir, 'transcript_raw.md'), 'r') as f:
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

# If we got fewer chunks than expected, redistribute
while len(chunks) < chunk_count:
    # Split the largest chunk
    largest_idx = max(range(len(chunks)), key=lambda i: len(chunks[i].split()))
    largest = chunks[largest_idx]
    largest_words = largest.split()
    mid = len(largest_words) // 2
    # Find a sentence boundary near the middle
    mid_text = ' '.join(largest_words[:mid])
    mid_sentences = re.split(r'(?<=[.!?])\s+', mid_text)
    split_point = 0
    if len(mid_sentences) > 1:
        split_point = len(' '.join(mid_sentences[:-1])) + 1
    
    chunks[largest_idx] = largest[:split_point]
    chunks.insert(largest_idx + 1, largest[split_point:])

# If we got more chunks, merge smallest
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
    with open(filepath, 'w') as f:
        f.write(chunk.strip())
    wc = len(chunk.split())
    print(f"{filename}: {wc} words")

print(f"\nTotal chunks: {len(chunks)}")
