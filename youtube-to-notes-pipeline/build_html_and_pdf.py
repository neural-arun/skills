import sys
import os
import re
import markdown
import subprocess
import asyncio
from playwright.async_api import async_playwright

def md_to_styled_html(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert Markdown to HTML
    html_body = markdown.markdown(md_text, extensions=["fenced_code", "tables", "toc", "attr_list"])

    # Clean up mermaid code blocks
    def clean_mermaid(match):
        code = match.group(1)
        code = code.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", "\"")
        return f'<div class="mermaid">\n{code}\n</div>'

    html_body = re.sub(r'<pre><code class="(?:language-)?mermaid">(.*?)</code></pre>', clean_mermaid, html_body, flags=re.DOTALL)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Study Notes</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <style>
    @page {{
      size: A4;
      margin: 20mm 15mm 20mm 15mm;
    }}
    
    * {{
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 10pt;
      line-height: 1.55;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    /* Title Block */
    h1 {{
      font-size: 18pt;
      font-weight: 700;
      color: #0f172a;
      letter-spacing: -0.4px;
      margin-top: 0;
      margin-bottom: 10pt;
      padding-bottom: 6pt;
      border-bottom: 2.5px solid #2563eb;
    }}

    /* Subsections */
    h2 {{
      font-size: 13pt;
      font-weight: 600;
      color: #0f172a;
      margin-top: 18pt;
      margin-bottom: 8pt;
      padding-bottom: 4pt;
      border-bottom: 1px solid #e2e8f0;
      break-after: avoid !important;
      page-break-after: avoid !important;
    }}

    h3 {{
      font-size: 11pt;
      font-weight: 600;
      color: #1e293b;
      margin-top: 12pt;
      margin-bottom: 5pt;
      break-after: avoid !important;
      page-break-after: avoid !important;
    }}

    p, li {{
      color: #334155;
    }}

    blockquote {{
      background: #f8fafc;
      border-left: 4px solid #2563eb;
      border-radius: 0 6px 6px 0;
      margin: 10pt 0;
      padding: 8pt 12pt;
      font-size: 9.5pt;
      color: #475569;
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }}

    blockquote p {{
      margin: 0;
    }}

    /* Code & Syntax Highlighting */
    code {{
      font-family: 'JetBrains Mono', 'Courier New', monospace;
      font-size: 8.5pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 2px 4px;
      border-radius: 4px;
    }}

    pre {{
      background-color: #0f172a !important;
      border-radius: 6px;
      padding: 10pt 12pt;
      margin: 10pt 0;
      overflow-x: auto;
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }}

    pre code {{
      background-color: transparent !important;
      color: #f8fafc !important;
      font-size: 8pt;
      line-height: 1.45;
      padding: 0;
    }}

    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12pt 0;
      font-size: 9pt;
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }}

    th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 600;
      text-align: left;
      padding: 6pt 8pt;
      border: 1px solid #cbd5e1;
    }}

    td {{
      padding: 6pt 8pt;
      border: 1px solid #e2e8f0;
      color: #334155;
    }}

    tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}

    /* Diagrams - Page break protected */
    .mermaid {{
      text-align: center;
      margin: 14pt 0;
      background: #ffffff;
      break-inside: avoid !important;
      page-break-inside: avoid !important;
      display: block;
    }}

    .mermaid svg {{
      max-width: 100% !important;
      max-height: 420pt !important;
      height: auto !important;
      margin: 0 auto;
    }}

    ul, ol {{
      padding-left: 16pt;
      margin-top: 4pt;
      margin-bottom: 8pt;
    }}

    li {{
      margin-bottom: 3pt;
    }}

    @media print {{
      body {{
        padding: 0;
      }}
      h1, h2, h3 {{
        break-after: avoid !important;
        page-break-after: avoid !important;
      }}
      .mermaid, pre, blockquote, table, tr {{
        break-inside: avoid !important;
        page-break-inside: avoid !important;
      }}
    }}
  </style>
</head>
<body>
{html_body}
<script>
  hljs.highlightAll();
  mermaid.initialize({{
    startOnLoad: true,
    theme: "default",
    securityLevel: "loose"
  }});
</script>
</body>
</html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)

async def print_pdf(html_path, pdf_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 900})
        abs_html_uri = f"file://{os.path.abspath(html_path)}"
        await page.goto(abs_html_uri)

        try:
            await page.wait_for_selector(".mermaid svg", timeout=10000)
            await page.wait_for_timeout(1000)
        except Exception as e:
            pass

        footer_template = """
        <div style="font-family: 'Inter', sans-serif; font-size: 8pt; color: #94a3b8; width: 100%; text-align: right; padding-right: 15mm;">
          Page <span class="pageNumber"></span> of <span class="totalPages"></span>
        </div>
        """

        header_template = """
        <div style="font-family: 'Inter', sans-serif; font-size: 8pt; color: #94a3b8; width: 100%; text-align: left; padding-left: 15mm;">
          Backend Engineering Study Notes
        </div>
        """

        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template=header_template,
            footer_template=footer_template,
            margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"}
        )
        await browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    md_to_styled_html(sys.argv[1], sys.argv[2])
    asyncio.run(print_pdf(sys.argv[2], sys.argv[3]))
