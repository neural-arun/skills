import os
import re

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
MASTER_FILE_PATH = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir.md")

def refactor_notes():
    if not os.path.exists(MASTER_FILE_PATH):
        print("Master file not found.")
        return

    with open(MASTER_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove Arun Yadav / AI Systems references
    content = re.sub(r'> \*\*कस्टमाइज़्ड फॉर:\*\* अरुण यादव.*?\n', '', content)
    content = re.sub(r'## AI Systems Engineering Connections.*', '', content, flags=re.DOTALL)
    content = re.sub(r'## 6\. AI Systems Engineering Connections.*?\n', '', content)
    content = re.sub(r'- \*\*AI Systems Engineering.*?\n', '', content)
    content = re.sub(r'- \*\*Periodicity & Modular Reduction:\*\*.*?\n', '', content)
    content = re.sub(r'- \*\*Linear Constraint Solvers.*?\n', '', content)

    # Replace header badge
    old_badge = r'> \*\*सम्पूर्ण बीजगणित \(Complete Algebra\) - मास्टर स्टडी नोट्स\*\* \| \*\*लक्ष्य:\*\* UP Super TET 2026 / Competitive Exams'
    new_badge = r'> **सम्पूर्ण बीजगणित (Complete Algebra) - मास्टर स्टडी नोट्स** | **लक्ष्य:** UP Super TET, UPTET, KVS, DSSSB एवं प्रतियोगी परीक्षा छात्र'
    content = re.sub(old_badge, new_badge, content)

    # 2. Update Table of Contents
    content = re.sub(r'5\. \[AI Systems Engineering Connections.*?\n', '', content)

    # 3. Format formulas with clean spacing and display math blocks
    # Ensure display math $$ ... $$ has empty lines before and after
    content = re.sub(r'([^\n])\n\$\$\n?', r'\1\n\n$$\n', content)
    content = re.sub(r'\$\$\n([^\n])', r'$$\n\n\1', content)

    # Space out bullet points and steps to avoid dense text blocks
    lines = content.split('\n')
    spaced_lines = []
    for i, line in enumerate(lines):
        # Add spacing before major headers or steps
        if line.startswith('### ') or line.startswith('## ') or line.startswith('#### '):
            spaced_lines.append('')
            spaced_lines.append(line)
            spaced_lines.append('')
        elif line.startswith('- **उदाहरण') or line.startswith('- **Example') or line.startswith('### उदाहरण'):
            spaced_lines.append('')
            spaced_lines.append(line)
        else:
            spaced_lines.append(line)

    cleaned_content = '\n'.join(spaced_lines)
    # Clean redundant triple empty lines
    cleaned_content = re.sub(r'\n{4,}', '\n\n\n', cleaned_content)

    with open(MASTER_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(cleaned_content.strip() + "\n")

    print("Refactored master notes successfully for general students with spacious formulas!")

if __name__ == "__main__":
    refactor_notes()
