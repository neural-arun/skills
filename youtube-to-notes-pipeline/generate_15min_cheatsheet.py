import os
import subprocess
from playwright.sync_api import sync_playwright

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
CHEATSHEET_MD = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_15Min_Revision_CheatSheet.md")
CHEATSHEET_HTML = os.path.join(OUTPUT_DIR, "cheatsheet_preview.html")
CHEATSHEET_PDF = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_15Min_Revision_CheatSheet.pdf")

CHEATSHEET_CONTENT = """# ⚡ सम्पूर्ण बीजगणित (Complete Algebra) — 15-मिनट सुपर क्विक रिवीजन चीट शीट

> [!IMPORTANT]
> **क्विक रिवीजन चीट शीट** | **लक्ष्य:** UP Super TET, UPTET, KVS, DSSSB | **शिक्षक:** Pawan Sir
> **प्रयोग:** परीक्षा से ठीक 15 मिनट पहले पूरे 2.5 घंटे के व्याख्यान की त्वरित पुनरावृत्ति के लिए।

---

## 1. 🚀 पवन सर की 10 मास्टर ट्रिक्स (Direct Exam Shortcuts)

1. **$x + \\frac{1}{x} = 2 \\implies x = 1$:** व्यंजक में $x=1$ रखकर 5 सेकंड में उत्तर प्राप्त करें।
2. **$x + \\frac{1}{x} = -2 \\implies x = -1$:** $(-1)^{\\text{सम}} = +1$ तथा $(-1)^{\\text{विषम}} = -1$ लें।
3. **वर्ग मौखिक ट्रिक:** $x + \\frac{1}{x} = k \\implies x^2 + \\frac{1}{x^2} = k^2 - 2$ | $x - \\frac{1}{x} = k \\implies x^2 + \\frac{1}{x^2} = k^2 + 2$
4. **घन मौखिक ट्रिक:** $x + \\frac{1}{x} = k \\implies x^3 + \\frac{1}{x^3} = k^3 - 3k$ | $x - \\frac{1}{x} = k \\implies x^3 - \\frac{1}{x^3} = k^3 + 3k$
5. **$x + \\frac{1}{x} = 1 \\implies x^3 = -1$ ($x^3 + 1 = 0$):** 3 के अंतर वाले घातों का पद-युग्म कटकर 0 होता है।
6. **$x + \\frac{1}{x} = \\sqrt{3} \\implies x^6 = -1$ ($x^6 + 1 = 0$):** 6 के अंतर वाले घातों का पद-युग्म कटकर 0 होता है।
7. **शेषफल प्रमेय (Zero Method):** $P(x)$ को $(x-a)$ से भाग देने पर शेषफल $R = P(a)$ (अतः $x = a$ व्यंजक में रखें).
8. **द्विघात विविक्तकर जांच ($D = b^2 - 4ac$):** $D > 0$ (वास्तविक असमान), $D = 0$ (वास्तविक समान), $D < 0$ (काल्पनिक).
9. **रैखिक निकाय 10-सेकंड अनुपात तुलना:** $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$ (अद्वितीय हल), $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$ (अनंत हल), $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$ (कोई हल नहीं).
10. **त्रिघात $a+b+c=0$ नियम:** यदि $a+b+c=0 \\implies a^3 + b^3 + c^3 = 3abc$ तथा $\\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab} = 3$.

---

## 2. 📊 मास्टर फार्मूला टेबल (Master Formula Reference)

| क्र.सं. | स्थिति / पैटर्न | परिणामी सूत्र / उत्तर | मुख्य उदाहरण |
|---|---|---|---|
| 1 | $x + \\frac{1}{x} = 2$ | $x = 1$ | $x^{17} + \\frac{1}{x^{20}} = 1 + 1 = 2$ |
| 2 | $x + \\frac{1}{x} = -2$ | $x = -1$ | $x^{10} + \\frac{1}{x^{15}} = (+1) + (-1) = 0$ |
| 3 | $x + \\frac{1}{x} = 3$ | $x^2 + \\frac{1}{x^2} = 3^2 - 2 = 7$ | $x^3 + \\frac{1}{x^3} = 3^3 - 3(3) = 18$ |
| 4 | $x - \\frac{1}{x} = 4$ | $x^2 + \\frac{1}{x^2} = 4^2 + 2 = 18$ | $x^3 - \\frac{1}{x^3} = 4^3 + 3(4) = 76$ |
| 5 | $x + \\frac{1}{x} = 1$ | $x^3 = -1, x^3 + 1 = 0$ | $x^{18} + x^{15} + x^{12} + x^9 + 1 = 0 + 0 + 1 = 1$ |
| 6 | $x + \\frac{1}{x} = \\sqrt{3}$ | $x^6 = -1, x^6 + 1 = 0$ | $x^{18} + x^{12} + x^6 + 1 = (-1)^3 + (-1)^2 + (-1) + 1 = 0$ |
| 7 | शेषफल प्रमेय | $R = P(a)$ | $x^3 - 2x + 5$ को $(x-1)$ से भाग $\\implies 1^3 - 2(1) + 5 = 4$ |
| 8 | द्विघात मूल | $\\alpha + \\beta = -\\frac{b}{a}, \\alpha\\beta = \\frac{c}{a}$ | $x^2 - 5x + 6 = 0 \\implies \\alpha+\\beta = 5, \\alpha\\beta = 6$ |
| 9 | $a+b+c = 0$ | $a^3+b^3+c^3 = 3abc$ | $\\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab} = 3$ |

---

## 3. 🎯 15-अध्याय माइक्रो रीकैप (15-Part Micro Recap)

- **भाग 01 (Pattern 1):** $x + 1/x = 2 \\implies x=1$. उदाहरण: $3x^5 - 2x^3 + 5x - 2 = 3(1) - 2(1) + 5(1) - 2 = 4$.
- **भाग 02 (Pattern 2):** $x + 1/x = -2 \\implies x=-1$. ध्यान रखें: $(-1)^n = +1$ (यदि $n$ सम) तथा $-1$ (यदि $n$ विषम).
- **भाग 03 (Square & Cube Rules):** $x + 1/x = k \\implies x^2 + 1/x^2 = k^2 - 2$ एवं $x^3 + 1/x^3 = k^3 - 3k$.
- **भाग 04 (Higher Powers):** $x^4 + 1/x^4 = (k^2 - 2)^2 - 2$. $x^5 + 1/x^5 = (x^2 + 1/x^2)(x^3 + 1/x^3) - (x + 1/x)$.
- **भाग 05 ($x^3=-1$ & $x^6=-1$):** $x + 1/x = 1 \\implies x^3 = -1$ | $x + 1/x = \\sqrt{3} \\implies x^6 = -1$.
- **भाग 06 (Quadratic Equations):** $ax^2 + bx + c = 0$. मूल $x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$.
- **भाग 07 (Remainder Theorem):** $P(x)$ को $(x-a)$ से विभाजित करने पर शेष $R = P(a)$.
- **भाग 08 (Polynomials & Degree):** चर की उच्चतम घात = बहुपद की घात. चर की घात केवल गैर-ऋणात्मक पूर्णांक होनी चाहिए.
- **भाग 09 (Linear Systems):** $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$ (अद्वितीय), $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$ (अनंत), $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$ (कोई नहीं).
- **भाग 10 (Identity $a^3+b^3+c^3-3abc$):** यदि $a+b+c=0$, तो $a^3+b^3+c^3 = 3abc$.
- **भाग 11 (Simplification & Value Put Method):** जब विकल्प अचर हों, तो $a=1, b=1, c=1$ रखकर 10 सेकंड में हल करें.
- **भाग 12 (Indices & Surds):** $a^m \\cdot a^n = a^{m+n}$, $\\frac{a^m}{a^n} = a^{m-n}$, $(a^m)^n = a^{mn}$, $a^0 = 1$.
- **भाग 13 (PYQ Practice):** सुपर टेट के विगत प्रश्नों में $x+1/x=2$ एवं शेषफल प्रमेय से सर्वाधिक प्रश्न आए.
- **भाग 14 (Word Problems):** $(x-y)^2 = (x+y)^2 - 4xy$ का प्रयोग कर संख्यात्मक समस्याएं हल करें.
- **भाग 15 (Final Exam Strategy):** पहले आसान पैटर्न 1 एवं 2 के प्रश्न चिन्हित कर हल करें, फिर शेषफल प्रमेय लागू करें.

---

## 4. ✅ परीक्षा हॉल चेकलिस्ट (Exam Hall Checklist)

- [ ] क्या $x + 1/x = 2$ है? $\\rightarrow$ सीधा $x = 1$ रखें।
- [ ] क्या $x + 1/x = -2$ है? $\\rightarrow$ $x = -1$ रखकर सम/विषम घात देखें।
- [ ] क्या $x + 1/x = 1$ है? $\\rightarrow$ $x^3 = -1$ रखें एवं 3 के अंतर वाले पद काटें।
- [ ] क्या $x + 1/x = \\sqrt{3}$ है? $\\rightarrow$ $x^6 = -1$ रखें एवं 6 के अंतर वाले पद काटें।
- [ ] क्या शेषफल पूछा है? $\\rightarrow$ $(x-a)=0 \\implies x=a$ मान रखें।
- [ ] क्या द्विघात मूलों का प्रकार पूछा है? $\\rightarrow$ $D = b^2 - 4ac$ का चिन्ह देखें।
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<title>15-Min Revision CheatSheet | सम्पूर्ण बीजगणित</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

<style>
@page { size: A4; margin: 12mm 10mm 12mm 10mm; }
body {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 11.5px;
    line-height: 1.5;
    color: #0f172a;
    background-color: #ffffff;
    margin: 0; padding: 0;
}
h1 { font-size: 19px; font-weight: 700; color: #1e3a8a; border-bottom: 2px solid #2563eb; padding-bottom: 4px; margin-top: 10px; margin-bottom: 8px; }
h2 { font-size: 15px; font-weight: 700; color: #0f766e; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 3px; margin-top: 14px; margin-bottom: 8px; }
ol, ul { padding-left: 18px; margin-top: 4px; margin-bottom: 8px; }
li { margin-bottom: 4px; }
blockquote { margin: 8px 0; padding: 8px 12px; background: #eff6ff; border-left: 4px solid #2563eb; border-radius: 4px; font-size: 11px; }
table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 11px; }
th { background: #1e293b; color: #fff; padding: 6px 8px; text-align: left; border: 1px solid #334155; }
td { padding: 5px 8px; border: 1px solid #cbd5e1; }
tr:nth-child(even) { background: #f8fafc; }
.katex { font-size: 1.05em !important; }
hr { border: 0; height: 1px; background: #cbd5e1; margin: 12px 0; }
</style>
</head>
<body>
<div id="content">
{{BODY}}
</div>
<script>
document.addEventListener("DOMContentLoaded", function() {
    if (window.renderMathInElement) {
        renderMathInElement(document.body, {
            delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false}
            ],
            throwOnError: false
        });
    }
});
</script>
</body>
</html>
"""

def main():
    # 1. Save MD CheatSheet file
    with open(CHEATSHEET_MD, "w", encoding="utf-8") as f:
        f.write(CHEATSHEET_CONTENT)
    print(f"Saved 15-minute revision markdown cheatsheet to {CHEATSHEET_MD}")

    # 2. Convert to HTML using pandoc
    res = subprocess.run(["pandoc", CHEATSHEET_MD, "-f", "markdown", "-t", "html"], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Pandoc error: {res.stderr}")
        return

    full_html = HTML_TEMPLATE.replace("{{BODY}}", res.stdout)
    with open(CHEATSHEET_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    # 3. Convert to PDF using Playwright Chromium
    abs_html_path = f"file://{os.path.abspath(CHEATSHEET_HTML)}"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(abs_html_path, wait_until="networkidle")
        page.wait_for_timeout(2000)
        page.pdf(
            path=CHEATSHEET_PDF,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template='<div style="font-size: 7px; font-family: sans-serif; color: #94a3b8; width: 100%; text-align: center;">⚡ 15-MIN REVISION CHEATSHEET — सम्पूर्ण बीजगणित</div>',
            footer_template='<div style="font-size: 8px; font-family: sans-serif; color: #64748b; width: 100%; text-align: center;">पृष्ठ <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
            margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"}
        )
        browser.close()

    print(f"Awesome 15-Minute Revision PDF CheatSheet created at {CHEATSHEET_PDF}")

if __name__ == "__main__":
    main()
