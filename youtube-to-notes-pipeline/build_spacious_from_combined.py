import os
import re

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
TITLE = "UP SUPER TET Maths Classes 2026 | सम्पूर्ण बीजगणित (Complete Algebra) | By Pawan Sir"
MASTER_FILE_PATH = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir.md")
COMBINED_FILE_PATH = os.path.join(OUTPUT_DIR, "combined.md")

def clean_and_format_for_general_students(text):
    # 1. Remove any personal bio / AI engineer references
    text = re.sub(r'## 6\. AI Systems Engineering Connections.*?(?=\n#|\Z)', '', text, flags=re.DOTALL)
    text = re.sub(r'## AI Systems Engineering Connections.*?(?=\n#|\Z)', '', text, flags=re.DOTALL)
    text = re.sub(r'- \*\*AI Systems Engineering.*?\n', '', text)
    text = re.sub(r'> \*\*कस्टमाइज़्ड फॉर:\*\*.*?\n', '', text)
    text = re.sub(r'> \*\*AI Systems.*?\n', '', text)
    text = re.sub(r'- \*\*Periodicity & Modular Reduction:\*\*.*?\n', '', text)
    text = re.sub(r'- \*\*Linear Constraint Solvers.*?\n', '', text)

    # 2. Make math formulas display on separate lines with clean spacing
    # Ensure display math $$ ... $$ has empty lines before and after
    text = re.sub(r'([^\n])\n\$\$\n?', r'\1\n\n$$\n', text)
    text = re.sub(r'\$\$\n([^\n])', r'$$\n\n\1', text)
    
    # Space out inline LaTeX formulas if they contain complex terms
    # Format step-by-step math problems nicely
    text = re.sub(r'(\n\s*-\s*\*\*उदाहरण\s*\d+:?\*\*|\n\s*###\s*उदाहरण\s*\d+:?)', r'\n\n---\n\1', text)
    
    # 3. Clean up multiple empty lines
    text = re.sub(r'\n{4,}', '\n\n', text)
    return text.strip()

def main():
    if not os.path.exists(COMBINED_FILE_PATH):
        print("combined.md not found!")
        return

    with open(COMBINED_FILE_PATH, "r", encoding="utf-8") as f:
        raw_combined = f.read()

    cleaned_chapters = clean_and_format_for_general_students(raw_combined)

    doc = f"# {TITLE}\n\n"
    doc += f"> [!IMPORTANT]\n"
    doc += f"> **सम्पूर्ण बीजगणित (Complete Algebra) - मास्टर अध्ययन नोट्स**\n"
    doc += f"> **लक्ष्य:** UP Super TET, UPTET, KVS, DSSSB एवं अन्य प्रतियोगी परीक्षाओं के छात्रों के लिए विस्तृत गाइड\n"
    doc += f"> **विशेषता:** स्पष्ट गणितीय सूत्र ($$ ... $$) | पवन सर की 10 शॉर्ट ट्रिक्स | चरणबद्ध हल किए गए प्रश्न | सुस्पष्ट संरचना\n\n"

    doc += "## विषय-सूची (Table of Contents)\n\n"
    doc += "1. [बीजगणितीय माइंडमैप एवं फ्लोचार्ट](#1-बीजगणितीय-माइंडमैप-एवं-फ्लोचार्ट)\n"
    doc += "2. [महत्वपूर्ण बीजगणित सूत्र चीट शीट (Master Formula Cheat Sheet)](#2-महत्वपूर्ण-बीजगणित-सूत्र-चीट-शीट-master-formula-cheat-sheet)\n"
    doc += "3. [पवन सर की 10 मास्टर ट्रिक्स एवं शॉर्टकट नियम](#3-पवन-सर-की-10-मास्टर-ट्रिक्स-एवं-शॉर्टकट-नियम)\n"
    doc += "4. [सम्पूर्ण 15 अध्यायवार विस्तृत गणितीय ब्रेकडाउन](#4-सम्पूर्ण-15-अध्यायवार-विस्तृत-गणितीय-ब्रेकडाउन)\n\n"

    doc += "---\n\n"
    doc += "## 1. बीजगणितीय माइंडमैप एवं फ्लोचार्ट\n\n"
    doc += """```mermaid
mindmap
  root((सम्पूर्ण बीजगणित Complete Algebra))
    बीजीय सर्वसमिकाएँ Algebraic Identities
      Pattern 1: x + 1/x = 2 => x = 1
      Pattern 2: x + 1/x = -2 => x = -1
      Pattern 3: x + 1/x = 1 => x^3 = -1
      Pattern 4: x + 1/x = sqrt3 => x^6 = -1
      Higher Powers: x^2, x^3, x^4, x^5, x^6
    द्विघात समीकरण Quadratic Equations
      ax^2 + bx + c = 0
      Shreedharacharya Formula
      Discriminant D = b^2 - 4ac
      Sum & Product of Roots
    बहुपद एवं शेषफल प्रमेय Polynomials & Remainder Theorem
      Degree of Polynomial
      Remainder Theorem P(a)
      Factor Theorem
    रैखिक समीकरण निकाय System of Linear Equations
      Unique Solution: a1/a2 != b1/b2
      Infinitely Many: a1/a2 = b1/b2 = c1/c2
      No Solution: a1/a2 = b1/b2 != c1/c2
```\n\n"""

    doc += """```mermaid
graph TD
    Input[बीजगणितीय प्रश्न Algebra Problem] --> CheckPattern{पैटर्न पहचानिए Pattern Identification}
    CheckPattern -->|x + 1/x = 2| DirectSub1[x = 1 सीधे रखिए Direct Substitution]
    CheckPattern -->|x + 1/x = -2| DirectSub2[x = -1 सीधे रखिए Even/Odd Power Rule]
    CheckPattern -->|x + 1/x = k| FormulaSquare[x^2 + 1/x^2 = k^2 - 2 & x^3 + 1/x^3 = k^3 - 3k]
    CheckPattern -->|x + 1/x = 1| CubeRule[x^3 = -1 स्थानपन्न कीजिए]
    CheckPattern -->|x + 1/x = sqrt3| SixthPowerRule[x^6 = -1 स्थानपन्न कीजिए]
    CheckPattern -->|ax^2 + bx + c = 0| DiscriminantEval[D = b^2 - 4ac से मूलों की प्रकृति जांचिए]
    CheckPattern -->|a1 x + b1 y + c1 = 0| RatioCheck[अनुपात तुलना a1/a2, b1/b2, c1/c2 कीजिए]
    
    DirectSub1 --> Output[त्वरित उत्तर Fast Solution < 10 sec]
    DirectSub2 --> Output
    FormulaSquare --> Output
    CubeRule --> Output
    SixthPowerRule --> Output
    DiscriminantEval --> Output
    RatioCheck --> Output
```\n\n"""

    doc += "---\n\n"
    doc += "## 2. महत्वपूर्ण बीजगणित सूत्र चीट शीट (Master Formula Cheat Sheet)\n\n"
    doc += "> [!NOTE]\n"
    doc += "> **परीक्षा में बार-बार पूछे जाने वाले प्रमुख सर्वसमिका सूत्र:**\n\n"

    doc += "### (A) मूलभूत सर्वसमिकाएँ (Basic Identities)\n\n"
    doc += "$$(a + b)^2 = a^2 + 2ab + b^2$$\n\n"
    doc += "$$(a - b)^2 = a^2 - 2ab + b^2$$\n\n"
    doc += "$$a^2 - b^2 = (a - b)(a + b)$$\n\n"
    doc += "$$(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)$$\n\n"

    doc += "### (B) व्युत्क्रम पद सर्वसमिकाएँ ($x + \\frac{1}{x}$ Patterns)\n\n"
    doc += "1. यदि $x + \\frac{1}{x} = 2$ हो, तो:\n\n"
    doc += "$$x = 1$$\n\n"

    doc += "2. यदि $x + \\frac{1}{x} = -2$ हो, तो:\n\n"
    doc += "$$x = -1 \\quad \\implies \\quad (-1)^{\\text{सम}} = +1, \\quad (-1)^{\\text{विषम}} = -1$$\n\n"

    doc += "3. यदि $x + \\frac{1}{x} = k$ हो, तो:\n\n"
    doc += "$$x^2 + \\frac{1}{x^2} = k^2 - 2$$\n\n"
    doc += "$$x^3 + \\frac{1}{x^3} = k^3 - 3k$$\n\n"

    doc += "4. यदि $x - \\frac{1}{x} = k$ हो, तो:\n\n"
    doc += "$$x^2 + \\frac{1}{x^2} = k^2 + 2$$\n\n"
    doc += "$$x^3 - \\frac{1}{x^3} = k^3 + 3k$$\n\n"

    doc += "5. यदि $x + \\frac{1}{x} = 1$ हो, तो:\n\n"
    doc += "$$x^3 = -1 \\quad \\text{तथा} \\quad x^3 + 1 = 0$$\n\n"

    doc += "6. यदि $x + \\frac{1}{x} = \\sqrt{3}$ हो, तो:\n\n"
    doc += "$$x^6 = -1 \\quad \\text{तथा} \\quad x^6 + 1 = 0$$\n\n"

    doc += "### (C) त्रिघात सर्वसमिकाएँ (Cubic Identities)\n\n"
    doc += "$$a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)$$\n\n"
    doc += "विशेष स्थिति: यदि $a + b + c = 0$ हो, तो:\n\n"
    doc += "$$a^3 + b^3 + c^3 = 3abc$$\n\n"

    doc += "### (D) द्विघात समीकरण सूत्र (Quadratic Equations)\n\n"
    doc += "मानक रूप: $ax^2 + bx + c = 0$\n\n"
    doc += "1. श्रीधराचार्य द्विघाती सूत्र:\n\n"
    doc += "$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$\n\n"

    doc += "2. विविक्तकर (Discriminant):\n\n"
    doc += "$$D = b^2 - 4ac$$\n\n"
    doc += "- यदि $D > 0 \\implies$ मूल वास्तविक एवं असमान (Real & Distinct)\n\n"
    doc += "- यदि $D = 0 \\implies$ मूल वास्तविक एवं समान (Real & Equal)\n\n"
    doc += "- यदि $D < 0 \\implies$ मूल काल्पनिक (Imaginary)\n\n"

    doc += "3. मूलों का योग एवं गुणनफल:\n\n"
    doc += "$$\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha \\cdot \\beta = \\frac{c}{a}$$\n\n"

    doc += "### (E) दो चरों वाले रैखिक समीकरण निकाय (System of Linear Equations)\n\n"
    doc += "समीकरण: $a_1 x + b_1 y + c_1 = 0$ तथा $a_2 x + b_2 y + c_2 = 0$\n\n"
    doc += "1. अद्वितीय हल (Unique Solution): $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$\n\n"
    doc += "2. अनंत हल (Infinitely Many Solutions): $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$\n\n"
    doc += "3. कोई हल नहीं (No Solution): $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$\n\n"

    doc += "---\n\n"
    doc += "## 3. पवन सर की 10 मास्टर ट्रिक्स एवं शॉर्टकट नियम\n\n"
    doc += "> [!TIP]\n"
    doc += "> **कम समय में 100% सही उत्तर निकालने के लिए पवन सर के 10 गोल्डन रूल्स:**\n\n"

    doc += "1. **समीकरण में 2 दिखे तो सीधा $x = 1$ रखिए:**\n"
    doc += "   जब भी $x + \\frac{1}{x} = 2$ दिया हो, तो बिना किसी लंबी प्रक्रिया के $x = 1$ रखकर उत्तर निकालें।\n\n"

    doc += "2. **$-2$ दिखने पर घात (Power) की जांच कीजिए:**\n"
    doc += "   यदि $x + \\frac{1}{x} = -2$ दिया हो, तो $x = -1$ होगा। घात सम (Even) होने पर $+1$ तथा विषम (Odd) होने पर $-1$ लें।\n\n"

    doc += "3. **वर्ग एवं घन का मौखिक नियम ($k^2 - 2$ तथा $k^3 - 3k$):**\n"
    doc += "   - $x + \\frac{1}{x} = k \\implies x^2 + \\frac{1}{x^2} = k^2 - 2$\n"
    doc += "   - $x + \\frac{1}{x} = k \\implies x^3 + \\frac{1}{x^3} = k^3 - 3k$\n\n"

    doc += "4. **$x + \\frac{1}{x} = 1$ में $x^3 = -1$ नियम:**\n"
    doc += "   यदि प्रश्न में $x + \\frac{1}{x} = 1$ दिया हो, तो $x^3 = -1$ रखें। 3 के अंतर वाले घातों का पद-युग्म ($x^{n+3} + x^n$) कटकर 0 हो जाता है।\n\n"

    doc += "5. **$x + \\frac{1}{x} = \\sqrt{3}$ में $x^6 = -1$ नियम:**\n"
    doc += "   जब $x + \\frac{1}{x} = \\sqrt{3}$ दिया हो, तो $x^6 = -1$ रखें। 6 के अंतर वाले घातों का योग 0 हो जाता है।\n\n"

    doc += "6. **शेषफल प्रमेय में शून्यीकरण विधि (Zero Substitution Method):**\n"
    doc += "   बहुपद $P(x)$ को $(x - a)$ से भाग देने पर शेषफल $R = P(a)$ होगा। अतः $(x - a) = 0 \\implies x = a$ व्यंजक में रखें।\n\n"

    doc += "7. **द्विघात समीकरण में विविक्तकर ($D = b^2 - 4ac$) से विकल्पों का चयन:**\n"
    doc += "   प्रश्नों में मूलों का प्रकार पूछा जाए तो पूरा समीकरण हल करने के बजाय केवल $D$ का चिन्ह (+, 0, -) देखें।\n\n"

    doc += "8. **रैखिक निकाय में 10-सेकंड अनुपात तुलना:**\n"
    doc += "   गुणांकों के अनुपात $\\frac{a_1}{a_2}, \\frac{b_1}{b_2}, \\frac{c_1}{c_2}$ लिखकर सीधा हलों का स्वरूप पहचानें।\n\n"

    doc += "9. **मान रखने की विधि (Value Put Method):**\n"
    doc += "   जब बीजीय विकल्पों में $a, b, c$ के स्थान पर संख्याएं दी हों, तो $a = 1, b = 1, c = 1$ या $a = 0$ मानकर उत्तर पाएं।\n\n"

    doc += "10. **त्रिघात में $a + b + c = 0$ शॉर्टकट:**\n"
    doc += "    यदि पदों का योग शून्य बन रहा हो, तो $a^3 + b^3 + c^3 = 3abc$ सूत्र का उपयोग करें।\n\n"

    doc += "---\n\n"
    doc += "## 4. सम्पूर्ण 15 अध्यायवार विस्तृत गणितीय ब्रेकडाउन\n\n"
    doc += cleaned_chapters + "\n\n"

    with open(MASTER_FILE_PATH, "w", encoding="utf-8") as out:
        out.write(doc.strip() + "\n")

    print("Master notes updated successfully with spacious formulas and general student focus!")

if __name__ == "__main__":
    main()
