import os
import glob
import re

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
TITLE = "UP SUPER TET Maths Classes 2026 | सम्पूर्ण बीजगणित (Complete Algebra) | By Pawan Sir"
MASTER_FILE_PATH = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir.md")
COMBINED_FILE_PATH = os.path.join(OUTPUT_DIR, "combined.md")

def check_summaries_exist():
    summaries = sorted(glob.glob(os.path.join(OUTPUT_DIR, "summary_*.md")))
    return len(summaries) == 15, summaries

def build_master_notes():
    success, summaries = check_summaries_exist()
    if not success:
        print(f"Only found {len(summaries)}/15 summaries. Waiting or checking status...")
        return False
    
    # 8a: Concatenate all summaries into combined.md
    combined_content = []
    for sf in summaries:
        with open(sf, 'r', encoding='utf-8') as f:
            combined_content.append(f.read().strip())
    
    combined_text = "\n\n---\n\n".join(combined_content)
    with open(COMBINED_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(combined_text)
    print(f"Saved combined summaries to {COMBINED_FILE_PATH}")
    
    # 8b: Build Master Notes Document with Zero Content Loss, Mermaid diagrams, Master Formula Sheet, TOC
    doc = f"# {TITLE}\n\n"
    doc += f"> [!IMPORTANT]\n"
    doc += f"> **सम्पूर्ण बीजगणित (Complete Algebra) - मास्टर स्टडी नोट्स** | **लक्ष्य:** UP Super TET 2026 / Competitive Exams\n"
    doc += f"> **कस्टमाइज़्ड फॉर:** अरुण यादव (neural-arun) | AI Systems Engineer\n"
    doc += f"> **संरचना:** 15 विस्तृत अध्याय | गणितीय सूत्र ($...$, $$...$$) | पवन सर की शॉर्ट ट्रिक्स | चरणबद्ध समाधान | शून्य विषय-वस्तु हानि (Zero Content Loss)\n\n"
    
    doc += "## विषय-सूची (Master Table of Contents)\n\n"
    doc += "1. [बीजगणितीय माइंडमैप एवं सिस्टम आर्किटेक्चर](#बीजगणितीय-माइंडमैप-एवं-सिस्टम-आर्किटेक्चर)\n"
    doc += "2. [संपूर्ण बीजगणित सूत्र चीट शीट (Master Formula Cheat Sheet)](#संपूर्ण-बीजगणित-सूत्र-चीट-शीट-master-formula-cheat-sheet)\n"
    doc += "3. [पवन सर की 10 मास्टर ट्रिक्स एवं शॉर्टकट नियम](#पवन-सर-की-10-मास्टर-ट्रिक्स-एवं-शॉर्टकट-नियम)\n"
    doc += "4. [भाग 01 से 15: संपूर्ण विस्तृत अध्यायवार गणितीय ब्रेकडाउन](#भाग-01-से-15-संपूर्ण-विस्तृत-अध्यायवार-गणितीय-ब्रेकडाउन)\n"
    doc += "5. [AI Systems Engineering Connections (फॉर अरुण यादव)](#ai-systems-engineering-connections-फॉर-अरुण-यादव)\n\n"
    
    doc += "## बीजगणितीय माइंडमैप एवं सिस्टम आर्किटेक्चर\n\n"
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
    त्रिघातीय सर्वसमिकाएँ Cubic Identities
      a^3 + b^3 + c^3 - 3abc
      If a + b + c = 0 => a^3 + b^3 + c^3 = 3abc
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

    doc += "## संपूर्ण बीजगणित सूत्र चीट शीट (Master Formula Cheat Sheet)\n\n"
    doc += "| क्र.सं. | स्थिति / समीकरण | परिणामी सूत्र / शॉर्टकट नियम | टिप्पणी / ध्यान देने योग्य बिंदु |\n"
    doc += "|---|---|---|---|\n"
    doc += "| 1 | $x + \\frac{1}{x} = 2$ | $x = 1$ | व्यंजक में $x=1$ रखकर सीधे मान ज्ञात करें |\n"
    doc += "| 2 | $x + \\frac{1}{x} = -2$ | $x = -1$ | $(-1)^{\\text{even}} = +1$, $(-1)^{\\text{odd}} = -1$ |\n"
    doc += "| 3 | $x + \\frac{1}{x} = k$ | $x^2 + \\frac{1}{x^2} = k^2 - 2$ | दोनों पक्षों का वर्ग करने पर |\n"
    doc += "| 4 | $x - \\frac{1}{x} = k$ | $x^2 + \\frac{1}{x^2} = k^2 + 2$ | चिह्नों का विशेष ध्यान रखें |\n"
    doc += "| 5 | $x + \\frac{1}{x} = k$ | $x^3 + \\frac{1}{x^3} = k^3 - 3k$ | घन करने का सूत्र |\n"
    doc += "| 6 | $x - \\frac{1}{x} = k$ | $x^3 - \\frac{1}{x^3} = k^3 + 3k$ | माइनस वाले में $+3k$ होता है |\n"
    doc += "| 7 | $x + \\frac{1}{x} = 1$ | $x^3 = -1$ तथा $x^3 + 1 = 0$ | 3 के अंतर वाले घातों का योग शून्य होगा |\n"
    doc += "| 8 | $x + \\frac{1}{x} = \\sqrt{3}$ | $x^6 = -1$ तथा $x^6 + 1 = 0$ | 6 के अंतर वाले घातों का योग शून्य होगा |\n"
    doc += "| 9 | $ax^2 + bx + c = 0$ | $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$ | श्रीधराचार्य द्विघाती सूत्र |\n"
    doc += "| 10 | द्विघात मूल गुणधर्म | $\\alpha + \\beta = -\\frac{b}{a}$, $\\alpha \\beta = \\frac{c}{a}$ | मूलों का योग एवं गुणनफल |\n"
    doc += "| 11 | विविक्तकर $D = b^2 - 4ac$ | $D>0$: वास्तविक भिन्न; $D=0$: समान; $D<0$: काल्पनिक | मूलों की प्रकृति |\n"
    doc += "| 12 | शेषफल प्रमेय | $P(x)$ को $(x-a)$ से भाग देने पर शेष $R = P(a)$ | $x-a=0 \\implies x=a$ मान रखें |\n"
    doc += "| 13 | रैखिक निकाय संगति | $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$ (अद्वितीय); $\\frac{a_1}{a_2}=\\frac{b_1}{b_2}=\\frac{c_1}{c_2}$ (अनंत); $\\frac{a_1}{a_2}=\\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$ (कोई हल नहीं) | संगति एवं असंगत निकाय |\n"
    doc += "| 14 | त्रिघाती सर्वसमिका | $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ | यदि $a+b+c=0 \\implies a^3+b^3+c^3 = 3abc$ |\n\n"

    doc += "## पवन सर की 10 मास्टर ट्रिक्स एवं शॉर्टकट नियम\n\n"
    doc += "1. **समीकरण में 2 दिखे तो 1 रखिए:** यदि $x + 1/x = 2$ है तो किसी भी जटिल व्यंजक में सीधा $x=1$ रखकर 5 सेकंड में उत्तर प्राप्त करें।\n"
    doc += "2. **-2 दिखने पर घात सम/विषम जांचें:** यदि $x + 1/x = -2$ है, तो घात सम होने पर $+1$ और विषम होने पर $-1$ लें।\n"
    doc += "3. **वर्ग एवं घन का मौखिक नियम:** $x+1/x=k$ के लिए वर्ग $\\implies k^2 - 2$ तथा घन $\\implies k^3 - 3k$ मौखिक निकालें।\n"
    doc += "4. **$x+1/x=1$ में $x^3 = -1$ नियम:** $x^3 = -1$ रखते ही बड़ी घात वाले बहुपदों को 3 के अंतर पर काट कर शून्य कर दें।\n"
    doc += "5. **$x+1/x=\\sqrt{3}$ में $x^6 = -1$ नियम:** घातों का अंतर 6 होने पर पदों का युग्म 0 हो जाता है।\n"
    doc += "6. **शेषफल प्रमेय में शून्यीकरण (Zero Method):** $(x-a)$ से भाग देना हो तो $x=a$ व्यंजक में रखकर सीधा शेषफल निकालें।\n"
    doc += "7. **द्विघात समीकरण में विविक्तकर जांच:** प्रश्नों में हल करने से पहले $D = b^2 - 4ac$ का मान देखकर विकल्प छांटें।\n"
    doc += "8. **रैखिक निकाय में अनुपात तुलना:** गुणांकों का अनुपात $\\frac{a_1}{a_2}, \\frac{b_1}{b_2}, \\frac{c_1}{c_2}$ लिखकर सीधा 10 सेकंड में निकाय की स्थिति ज्ञात करें।\n"
    doc += "9. **मान रखने की विधि (Value Put Method):** जब विकल्प $a, b, c$ में न होकर अचर संख्याओं में हों तो $a=1, b=1, c=1$ रखकर व्यंजक हल करें।\n"
    doc += "10. **त्रिघात में $a+b+c=0$ शॉर्टकट:** यदि पदों का योग शून्य बन रहा हो तो $a^3+b^3+c^3 = 3abc$ से गुणनफल निकालें।\n\n"

    doc += "## भाग 01 से 15: संपूर्ण विस्तृत अध्यायवार गणितीय ब्रेकडाउन\n\n"
    
    # Process cleaned summaries and remove individual document headers to flow seamlessly
    for idx, sf in enumerate(summaries, 1):
        with open(sf, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        # Smooth stitching - clean top level duplicate headers if needed
        doc += f"\n\n---\n\n"
        doc += content + "\n\n"

    doc += "\n\n---\n\n"
    doc += "## AI Systems Engineering Connections (फॉर अरुण यादव)\n\n"
    doc += "> [!NOTE]\n"
    doc += "> **AI Systems & Mathematical Engineering Mapping for neural-arun:**\n"
    doc += "> 1. **Deterministic State Pinning ($x+1/x=2 \implies x=1$):** AI Agent architectures rely on invariant state checks where complex non-deterministic graph conditions resolve to constant values, reducing graph search complexity.\n"
    doc += "> 2. **Polynomial Reduction & Cycle Elimination ($x^3=-1, x^6=-1$):** In Vector DB indexing (ChromaDB / Pinecone) and RAG embeddings, dimensional reduction algorithms eliminate redundant periodic dimensions similar to algebraic exponent modular reduction.\n"
    doc += "> 3. **Linear Consistency & Constraint Solvers ($a_1/a_2 = b_1/b_2$):** Multi-agent orchestration frameworks (LangGraph / MCP) evaluate tool-calling prerequisites using strict solvability criteria identical to linear system consistency checks.\n"
    doc += "> 4. **Discriminant Analysis ($b^2 - 4ac$):** Optimization loss functions in machine learning models evaluate second-order derivatives and determinants to verify convex convergence vs unstable saddle points.\n"

    with open(MASTER_FILE_PATH, 'w', encoding='utf-8') as out:
        out.write(doc)

    print(f"Master notes successfully generated at {MASTER_FILE_PATH}!")
    return True

if __name__ == "__main__":
    build_master_notes()
