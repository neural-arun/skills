import re
import glob
import os

vtt_files = glob.glob("./outputs/Entire_Map_of_Business_in_41_Minutes/*.en.vtt")
if not vtt_files:
    print("No VTT file found")
    exit(1)

vtt_path = vtt_files[0]
out_dir = os.path.dirname(vtt_path)

with open(vtt_path, 'r') as f:
    content = f.read()

# Remove VTT header
lines = content.split('\n')
text_lines = []
in_header = True
for line in lines:
    stripped = line.strip()
    if in_header:
        if stripped == '':
            in_header = False
        continue
    # Skip timestamp-only lines
    if re.match(r'^\d{2}:\d{2}:\d{2}\.\d+', stripped):
        continue
    # Skip empty lines
    if not stripped:
        continue
    # Remove HTML-like tags
    cleaned = re.sub(r'<[^>]+>', '', stripped)
    # Remove text that's just a continuation marker
    if cleaned.strip():
        text_lines.append(cleaned.strip())

# Join with spaces
transcript = ' '.join(text_lines)
# Clean up multiple spaces
transcript = re.sub(r' +', ' ', transcript)

output_path = os.path.join(out_dir, 'transcript_raw.md')
with open(output_path, 'w') as f:
    f.write(transcript)

word_count = len(transcript.split())
print(f"Transcript written to {output_path}")
print(f"Total words: {word_count}")
