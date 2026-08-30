import sys
import os
import re
import asyncio
from playwright.async_api import async_playwright

async def render_mermaid_blocks(md_filepath, output_pdf_path, css_path):
    dir_path = os.path.dirname(os.path.abspath(md_filepath))
    diagrams_dir = os.path.join(dir_path, "diagrams")
    os.makedirs(diagrams_dir, exist_ok=True)

    with open(md_filepath, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)
    matches = list(pattern.finditer(content))

    if not matches:
        print("No Mermaid diagrams found. Compiling directly...")
        cmd = f'pandoc "{md_filepath}" -c "{css_path}" --pdf-engine=weasyprint -o "{output_pdf_path}"'
        os.system(cmd)
        return

    print(f"Found {len(matches)} Mermaid diagrams. Rendering with Playwright...")

    diagram_replacements = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for idx, match in enumerate(matches, 1):
            mermaid_code = match.group(1).strip()
            png_filename = f"diagram_{idx:02d}.png"
            png_filepath = os.path.join(diagrams_dir, png_filename)

            # High-resolution rendering HTML template
            html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <style>
    body {{
      background: white;
      margin: 0;
      padding: 30px;
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}
    .mermaid {{
      display: inline-block;
    }}
    /* Custom CSS to make mindmaps, flowcharts & sequence diagrams large and highly legible */
    .mermaid svg {{
      font-size: 16px !important;
    }}
    .mermaid .node rect, .mermaid .node circle, .mermaid .node polygon {{
      stroke-width: 2px !important;
    }}
    .mermaid .actor {{
      font-size: 16px !important;
      font-weight: bold !important;
    }}
    .mermaid .messageText {{
      font-size: 14px !important;
    }}
    .mermaid text {{
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }}
  </style>
</head>
<body>
  <div class="mermaid">
{mermaid_code}
  </div>
  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'default',
      securityLevel: 'loose',
      flowchart: {{ useMaxWidth: false, htmlLabels: true }},
      mindmap: {{ useMaxWidth: false }},
      sequence: {{ useMaxWidth: false, showSequenceNumbers: true }}
    }});
  </script>
</body>
</html>"""

            page = await browser.new_page(
                viewport={"width": 1400, "height": 1000},
                device_scale_factor=2.5  # High-DPI scaling for ultra crisp text
            )
            await page.set_content(html_content)

            try:
                await page.wait_for_selector(".mermaid svg", timeout=8000)
                element = await page.query_selector(".mermaid svg")
                if element:
                    await element.screenshot(path=png_filepath)
                    print(f"✅ Rendered Diagram {idx}/{len(matches)} -> {png_filepath}")
                    diagram_replacements[match.group(0)] = f'<p style="text-align: center; margin: 18pt 0;"><img src="{png_filepath}" style="width: 98%; height: auto;" /></p>'
                else:
                    print(f"⚠️ Could not find SVG element for diagram {idx}")
            except Exception as e:
                print(f"❌ Error rendering diagram {idx}: {e}")

            await page.close()

        await browser.close()

    # Replace mermaid blocks in markdown
    rendered_md = content
    for original, replacement in diagram_replacements.items():
        rendered_md = rendered_md.replace(original, replacement)

    temp_md_path = os.path.join(dir_path, "render_ready.md")
    with open(temp_md_path, "w", encoding="utf-8") as f:
        f.write(rendered_md)

    print(f"Saved pre-rendered markdown to {temp_md_path}")

    # Run pandoc to produce PDF
    cmd = f'pandoc "{temp_md_path}" -c "{css_path}" --pdf-engine=weasyprint -o "{output_pdf_path}"'
    print(f"Executing: {cmd}")
    status = os.system(cmd)

    if os.path.exists(temp_md_path):
        os.remove(temp_md_path)

    if status == 0:
        print(f"🎉 Successfully generated PDF with crisp diagrams: {output_pdf_path}")
    else:
        print(f"❌ Pandoc execution failed with status {status}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python render_mermaid.py <input.md> <output.pdf> <css_path>")
        sys.exit(1)

    asyncio.run(render_mermaid_blocks(sys.argv[1], sys.argv[2], sys.argv[3]))
