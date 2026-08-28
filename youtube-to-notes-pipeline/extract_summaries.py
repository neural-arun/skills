import os
import json
import glob

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
BRAIN_DIR = "/home/arun/.gemini/antigravity-cli/brain"

CONVERSATIONS = [
    ("01", "13db78e5-f8e6-4a3b-9658-7339e9e03728"),
    ("02", "ffa49586-833b-4792-8dd1-8191ec6d43a2"),
    ("03", "9147a32e-b1e2-49ed-a00e-bd0a2320d510"),
    ("04", "a064ad10-d058-43d8-8d2f-1533557426bb"),
    ("05", "6473d529-d51b-4b1b-a61b-fb167f817772"),
    ("06", "3e570d62-a4ff-48a9-8cf3-31356eab87cb"),
    ("07", "b0d4b0d7-a415-411c-a654-5e74f98873c9"),
    ("08", "48e4cbd9-a7d2-44b5-8232-f50e60b89fa4"),
    ("09", "cebee294-02ce-462a-9bf5-3901548327a3"),
    ("10", "a5210a4f-e5b9-491f-8d9f-39a100f5a5e5"),
    ("11", "b1596641-2eb0-4b8e-88fd-644018041fec"),
    ("12", "31fbe5cb-506a-4d3b-ab94-45916df63462"),
    ("13", "275f5d2e-99bf-4419-831a-2334b8c650ce"),
    ("14", "da65393d-66e7-456f-a7f0-f5ba92024653"),
    ("15", "9696fa65-cc26-4422-806c-80a91855f7eb"),
]

def main():
    extracted_count = 0
    for part_id, cid in CONVERSATIONS:
        out_file = os.path.join(OUTPUT_DIR, f"summary_{part_id}.md")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 100:
            print(f"summary_{part_id}.md already exists.")
            extracted_count += 1
            continue
            
        transcript_full = os.path.join(BRAIN_DIR, cid, ".system_generated", "logs", "transcript_full.jsonl")
        transcript = os.path.join(BRAIN_DIR, cid, ".system_generated", "logs", "transcript.jsonl")
        
        target_path = transcript_full if os.path.exists(transcript_full) else transcript
        if not os.path.exists(target_path):
            print(f"Transcript not found for part_{part_id}: {target_path}")
            continue
            
        found = False
        with open(target_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get("type") == "PLANNER_RESPONSE":
                        for tc in data.get("tool_calls", []):
                            if tc.get("name") in ["write_to_file", "write_file", "replace_file_content"]:
                                content = tc.get("args", {}).get("CodeContent") or tc.get("args", {}).get("ReplacementContent")
                                if content:
                                    with open(out_file, "w", encoding="utf-8") as out:
                                        out.write(content)
                                    print(f"Extracted summary_{part_id}.md from transcript ({len(content)} chars)")
                                    extracted_count += 1
                                    found = True
                                    break
                            elif tc.get("name") == "run_command":
                                cmd = tc.get("args", {}).get("CommandLine", "")
                                if "cat << 'EOF' >" in cmd or "cat <<EOF >" in cmd:
                                    parts = cmd.split("EOF", 2)
                                    if len(parts) >= 2:
                                        content = parts[1].strip()
                                        if content.startswith(">"):
                                            content = content.split("\n", 1)[1]
                                        with open(out_file, "w", encoding="utf-8") as out:
                                            out.write(content)
                                        print(f"Extracted summary_{part_id}.md from cat command ({len(content)} chars)")
                                        extracted_count += 1
                                        found = True
                                        break
                except Exception as e:
                    pass
                if found:
                    break
                    
    print(f"\nTotal extracted summaries: {extracted_count}/15")

if __name__ == "__main__":
    main()
