import sys
import os
import re
import glob

def clean_vtt(vtt_path_or_dir, output_path):
    if os.path.isdir(vtt_path_or_dir):
        matches = glob.glob(os.path.join(vtt_path_or_dir, "*.en.vtt"))
        if not matches:
            raise FileNotFoundError(f"No .en.vtt file found in {vtt_path_or_dir}")
        vtt_path = matches[0]
    else:
        vtt_path = vtt_path_or_dir

    if not os.path.exists(vtt_path):
        # Try glob in case of special unicode characters
        dir_name = os.path.dirname(vtt_path)
        matches = glob.glob(os.path.join(dir_name, "*.en.vtt"))
        if matches:
            vtt_path = matches[0]
        else:
            raise FileNotFoundError(f"File not found: {vtt_path}")

    with open(vtt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    clean_lines = []
    prev_line = ""

    for line in lines:
        line = line.strip()
        # Skip header, metadata, empty lines, note, or timestamp lines
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or line.startswith("NOTE"):
            continue
        if "-->" in line:
            continue
        
        # Remove HTML-like tags: <c>, </c>, <00:00:00.000>, <v SpeakerName> etc.
        line = re.sub(r'<[^>]+>', '', line)
        line = re.sub(r' align:[^\s]+', '', line)
        line = re.sub(r' position:[^\s]+', '', line)
        line = line.strip()

        if not line:
            continue

        # VTT auto-subs repeat text across cues. Deduplicate identical or substring lines.
        if line == prev_line:
            continue
        
        # If current line adds text to prev_line or is just repeated chunk, deduplicate
        if prev_line and line.startswith(prev_line):
            if clean_lines:
                clean_lines[-1] = line
                prev_line = line
                continue

        clean_lines.append(line)
        prev_line = line

    full_text = " ".join(clean_lines)
    full_text = re.sub(r'\s+', ' ', full_text).strip()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)

    word_count = len(full_text.split())
    print(f"Cleaned transcript written to {output_path} ({word_count} words)")
    return word_count

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python clean_vtt.py <input.vtt or directory> <output_raw.md>")
        sys.exit(1)
    clean_vtt(sys.argv[1], sys.argv[2])
