with open("COTIZACION_CASA_TRADICION.md", "r") as f:
    md = f.read()

# Add frontmatter to remove hardcoded puppeteer margins
frontmatter = """---
pdf_options:
  format: A4
  margin:
    top: 0
    right: 0
    bottom: 0
    left: 0
---
"""

# Add @page CSS
css_page = """
  @page {
    margin: 20mm;
  }
  @page :first {
    margin: 0;
  }
"""

if not md.startswith("---"):
    md = frontmatter + md

if "@page" not in md:
    md = md.replace("<style>", "<style>\n" + css_page)

with open("COTIZACION_CASA_TRADICION.md", "w") as f:
    f.write(md)
