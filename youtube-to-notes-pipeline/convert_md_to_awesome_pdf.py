import os
import subprocess
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIR = "./outputs/UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir"
MD_FILE = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir.md")
HTML_FILE = os.path.join(OUTPUT_DIR, "notes_preview.html")
PDF_FILE = os.path.join(OUTPUT_DIR, "UP_SUPER_TET_Maths_Classes_2026_Sampurna_Beejganit_Pawan_Sir.pdf")

# Custom HTML Template with Google Fonts (Noto Sans Devanagari + Inter), KaTeX Math, Mermaid.js, and Print CSS
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<title>UP SUPER TET Maths 2026 | सम्पूर्ण बीजगणित</title>

<!-- Google Fonts for Hindi (Noto Sans Devanagari) & English (Inter, Fira Code) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- KaTeX CSS & JS for Mathematical Equation Rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

<!-- Mermaid.js for Diagrams -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

<style>
@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
}

body {
    font-family: 'Noto Sans Devanagari', 'Inter', -apple-system, sans-serif;
    font-size: 13.5px;
    line-height: 1.7;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

/* Headings */
h1 {
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
    page-break-after: avoid;
}

h2 {
    font-size: 19px;
    font-weight: 700;
    color: #1e3a8a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 25px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h3 {
    font-size: 16px;
    font-weight: 600;
    color: #0d9488;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h4 {
    font-size: 14px;
    font-weight: 600;
    color: #334155;
    margin-top: 15px;
    margin-bottom: 8px;
}

/* Paragraphs & Lists */
p {
    margin-top: 0;
    margin-bottom: 12px;
}

ul, ol {
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 24px;
}

li {
    margin-bottom: 6px;
}

/* Blockquotes & Callouts */
blockquote {
    margin: 16px 0;
    padding: 12px 18px;
    background-color: #f8fafc;
    border-left: 5px solid #2563eb;
    border-radius: 4px;
    font-size: 13.5px;
    color: #334155;
    page-break-inside: avoid;
}

blockquote.important {
    background-color: #eff6ff;
    border-left-color: #2563eb;
    color: #1e40af;
}

blockquote.note {
    background-color: #f0fdf4;
    border-left-color: #16a34a;
    color: #166534;
}

blockquote.tip {
    background-color: #fffbeb;
    border-left-color: #d97706;
    color: #92400e;
}

/* KaTeX Math Blocks */
.katex-display {
    margin: 16px 0 !important;
    padding: 10px;
    background-color: #f8fafc;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    page-break-inside: avoid;
    overflow-x: auto;
}

.katex {
    font-size: 1.1em !important;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 13px;
    page-break-inside: avoid;
}

th {
    background-color: #1e293b;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 10px 12px;
    border: 1px solid #334155;
}

td {
    padding: 9px 12px;
    border: 1px solid #cbd5e1;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

/* Horizontal Rule */
hr {
    border: 0;
    height: 1px;
    background: #cbd5e1;
    margin: 24px 0;
}

/* Mermaid Diagram Styling */
.mermaid {
    text-align: center;
    margin: 20px 0;
    page-break-inside: avoid;
}

/* Code blocks */
code {
    font-family: 'Fira Code', monospace;
    background-color: #f1f5f9;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 12px;
    color: #0f172a;
}

pre code {
    display: block;
    padding: 14px;
    overflow-x: auto;
    line-height: 1.5;
}
</style>
</head>
<body>

<div id="content">
{{BODY}}
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // 1. Process GitHub style blockquotes
    document.querySelectorAll("blockquote").forEach(function(bq) {
        var text = bq.innerText.trim();
        if (text.startsWith("[!IMPORTANT]")) {
            bq.classList.add("important");
            bq.innerHTML = bq.innerHTML.replace("[!IMPORTANT]", "<strong>IMPORTANT</strong>");
        } else if (text.startsWith("[!NOTE]")) {
            bq.classList.add("note");
            bq.innerHTML = bq.innerHTML.replace("[!NOTE]", "<strong>NOTE</strong>");
        } else if (text.startsWith("[!TIP]")) {
            bq.classList.add("tip");
            bq.innerHTML = bq.innerHTML.replace("[!TIP]", "<strong>TIP</strong>");
        }
    });

    // 2. Initialize Mermaid
    mermaid.initialize({ startOnLoad: true, theme: 'neutral' });

    // 3. Render KaTeX Math
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

def generate_pdf():
    print("Step 1: Running Pandoc to convert Markdown to HTML body...")
    # Convert markdown to html fragment using pandoc
    cmd = ["pandoc", MD_FILE, "-f", "markdown", "-t", "html"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Pandoc error: {res.stderr}")
        return False
    
    html_body = res.stdout
    full_html = HTML_TEMPLATE.replace("{{BODY}}", html_body)
    
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"HTML saved to {HTML_FILE}")

    print("Step 2: Using Playwright to render HTML to PDF with full fonts, KaTeX math & Mermaid diagrams...")
    abs_html_path = f"file://{os.path.abspath(HTML_FILE)}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(abs_html_path, wait_until="networkidle")
        
        # Wait a extra 3 seconds for WebFont, KaTeX math and Mermaid SVG rendering
        page.wait_for_timeout(3000)
        
        # Print to PDF with headers, footers and backgrounds
        page.pdf(
            path=PDF_FILE,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template='<div style="font-size: 8px; font-family: sans-serif; color: #94a3b8; width: 100%; text-align: center;">UP SUPER TET 2026 — सम्पूर्ण बीजगणित (Complete Algebra)</div>',
            footer_template='<div style="font-size: 9px; font-family: sans-serif; color: #64748b; width: 100%; text-align: center;">पृष्ठ <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
            margin={
                "top": "20mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm"
            }
        )
        browser.close()

    print(f"SUCCESS! Awesome PDF generated at {PDF_FILE}")
    return True

if __name__ == "__main__":
    generate_pdf()
