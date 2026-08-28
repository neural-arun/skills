import os

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"

summary_05_content = """# भाग 05: रैखिक बहुपद, सर्वसमिका $a + b + c = 0$ एवं विशेष पैटर्न ($x + \\frac{1}{x} = 1, \\sqrt{3}$)

## 1. मुख्य अवधारणाएँ एवं रैखिक बहुपद (Linear Polynomials & Special Patterns)
- **रैखिक बहुपद (Linear Polynomial):** ऐसा बहुपद जिसमें चर (Variable) की अधिकतम घात 1 हो, जैसे $7x + 5$।
- **सर्वसमिका $a + b + c = 0$ की भूमिका:** जब समीकरण में $a + b + c = 0$ दिया गया हो, तो त्रिघातीय व्यंजकों का मान अत्यंत सरलता से निकाला जा सकता है।
- **विशेष पैटर्न $x + \\frac{1}{x} = 1$:** 
  $$\\left(x + \\frac{1}{x}\\right)^2 = 1 \\implies x^2 + \\frac{1}{x^2} + 2 = 1 \\implies x^2 + 1 = -x \\implies x^3 = -1 \\text{ तथा } x^3 + 1 = 0$$
- **विशेष पैटर्न $x + \\frac{1}{x} = \\sqrt{3}$:**
  $$x^2 + \\frac{1}{x^2} = (\\sqrt{3})^2 - 2 = 1 \\implies x^6 = -1 \\text{ तथा } x^6 + 1 = 0$$

## 2. गणितीय सूत्र एवं सिद्धता (Mathematical Proofs & Identities)
1. **$a + b + c = 0 \\implies a^3 + b^3 + c^3 = 3abc$**
2. **बीजीय भिन्न सूत्र:**
   $$\\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab} = \\frac{a^3 + b^3 + c^3}{abc} = \\frac{3abc}{abc} = 3 \\quad (\\text{यदि } a+b+c=0)$$

## 3. पवन सर की शॉर्ट ट्रिक्स (Short Tricks & Instant Rules)
- **3 के अंतर वाली घातों का योग शून्य:** यदि $x + \\frac{1}{x} = 1$ हो, तो व्यंजक में 3 के अंतर वाले घातों का पद-युग्म ($x^{n+3} + x^n = x^n(x^3+1) = 0$) शून्य हो जाता है।
- **6 के अंतर वाली घातों का योग शून्य:** यदि $x + \\frac{1}{x} = \\sqrt{3}$ हो, तो 6 के अंतर वाले घातों का पद-युग्म ($x^{n+6} + x^n = x^n(x^6+1) = 0$) शून्य हो जाता है।

## 4. विस्तृत उदाहरण एवं चरणबद्ध समाधान (Step-by-Step Solved Examples)

### उदाहरण 1:
यदि $a + b + c = 0$ हो, तो $\\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab}$ का मान ज्ञात कीजिए।
- **हल:**
  $$\\text{ल.स.व. (LCM)} = abc$$
  $$\\frac{a^3 + b^3 + c^3}{abc}$$
  चूँकि $a+b+c=0$, अतः $a^3+b^3+c^3 = 3abc$।
  $$\\text{मान} = \\frac{3abc}{abc} = 3$$

### उदाहरण 2:
यदि $x + \\frac{1}{x} = 1$ हो, तो $x^{18} + x^{15} + x^{12} + x^9 + x^3 + 1$ का मान ज्ञात कीजिए।
- **हल:**
  चूँकि $x + \\frac{1}{x} = 1 \\implies x^3 = -1$ तथा $x^3 + 1 = 0$।
  $$x^{15}(x^3 + 1) + x^9(x^3 + 1) + (x^3 + 1) = 0 + 0 + 0 = 0$$

## 5. परीक्षा टिप्स एवं पैटर्न (Exam Tips)
- Super TET एवं UPTET Junior में $a+b+c=0$ पर आधारित सीधे प्रश्न पूछे जाते हैं। 

## 6. AI Systems Engineering Connections (फॉर अरुण यादव - neural-arun)
- **Periodicity & Modular Reduction:** Dynamic state space pruning in AI agents where periodic state loops cancel out, preventing infinite recursion in search graphs.
"""

summary_09_content = """# भाग 09: दो चरों वाले रैखिक समीकरण निकाय (System of Linear Equations in Two Variables)

## 1. मुख्य अवधारणाएँ एवं समीकरण निकाय (System of Equations & Solution Conditions)
दो चरों वाले रैखिक समीकरणों का सामान्य रूप:
$$a_1 x + b_1 y + c_1 = 0$$
$$a_2 x + b_2 y + c_2 = 0$$

समीकरण निकाय की संगति (Consistency) एवं समाधान की तीन प्रमुख स्थितियाँ होती हैं:

### 1. अद्वितीय हल / संगत निकाय (Unique Solution / Intersecting Lines)
जब दोनों रेखाएं एक-दूसरे को केवल एक बिंदु पर काटती हैं:
$$\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$$

### 2. अपरिमित रूप से अनेक हल / संपाती रेखाएं (Infinitely Many Solutions / Coincident Lines)
जब दोनों रेखाएं एक ही रेखा पर स्थित होती हैं:
$$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$$

### 3. कोई हल नहीं / असंगत निकाय (No Solution / Parallel Lines)
जब दोनों रेखाएं समांतर होती हैं और कभी नहीं मिलतीं:
$$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$$

## 2. गणितीय सूत्र तालिका (Mathematical Conditions Table)

| स्थिति (Condition) | रेखाओं का स्वरूप (Graph Type) | हलों की संख्या (Number of Solutions) | निकाय का प्रकार (System Nature) |
|---|---|---|---|
| $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$ | प्रतिच्छेदी रेखाएं (Intersecting) | केवल एक (Unique Solution) | संगत (Consistent) |
| $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$ | संपाती रेखाएं (Coincident) | अनंत (Infinitely Many) | संगत एवं आश्रित (Consistent & Dependent) |
| $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$ | समांतर रेखाएं (Parallel) | शून्य (No Solution) | असंगत (Inconsistent) |

## 3. पवन सर की शॉर्ट ट्रिक्स (Short Tricks for Ratio Verification)
- **10 सेकंड अनुपात जांच:** समीकरण को तुरंत $a_1/a_2$ और $b_1/b_2$ के रूप में लिखें। यदि प्रथम दो भिन्न असमान हैं, तो उत्तर 'अद्वितीय हल' होगा।

## 4. विस्तृत उदाहरण एवं चरणबद्ध समाधान (Step-by-Step Solved Examples)

### उदाहरण 1:
समीकरणों $2x + 3y = 7$ तथा $4x + 6y = 14$ के हलों का स्वरूप ज्ञात कीजिए।
- **हल:**
  $$a_1 = 2, b_1 = 3, c_1 = -7$$
  $$a_2 = 4, b_2 = 6, c_2 = -14$$
  $$\\frac{a_1}{a_2} = \\frac{2}{4} = \\frac{1}{2}, \\quad \\frac{b_1}{b_2} = \\frac{3}{6} = \\frac{1}{2}, \\quad \\frac{c_1}{c_2} = \\frac{-7}{-14} = \\frac{1}{2}$$
  चूँकि $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} = \\frac{1}{2}$, अतः इसके **अनंत हल (Infinitely Many Solutions)** होंगे।

### उदाहरण 2:
$k$ का वह मान ज्ञात कीजिए जिसके लिए निकाय $kx + 2y = 5$ तथा $3x + y = 1$ का कोई हल न हो।
- **हल:**
  कोई हल न होने की शर्त: $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$
  $$\\frac{k}{3} = \\frac{2}{1} \\implies k = 6$$

## 5. परीक्षा टिप्स (Exam Tips)
- Super TET परीक्षा में अचर $k$ का मान ज्ञात करने वाले प्रश्न बार-बार आते हैं।

## 6. AI Systems Engineering Connections (फॉर अरुण यादव - neural-arun)
- **Linear Constraint Solvers & Determinants:** Matrix rank condition ($A x = b$) in constraint satisfaction problem (CSP) solvers used in AI Agent planning engines.
"""

with open(os.path.join(OUTPUT_DIR, "summary_05.md"), "w", encoding="utf-8") as f:
    f.write(summary_05_content)

with open(os.path.join(OUTPUT_DIR, "summary_09.md"), "w", encoding="utf-8") as f:
    f.write(summary_09_content)

print("Created summary_05.md and summary_09.md successfully!")
