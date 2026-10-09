with open("COTIZACION_CASA_TRADICION.md", "r") as f:
    md_content = f.read()

old_md = "*   **Opción A (De Contado):** Pago único de $2.500.000 COP al iniciar el proyecto. Prioridad máxima en la cola de desarrollo de la agencia."
new_md = "*   **Opción A (De Contado - Fast-Track):** Pago único de $2.500.000 COP al iniciar. Prioridad máxima y equipo dedicado: <strong style='color: #1E3A8A;'>Reduce el tiempo de desarrollo de 2 meses a solo 40 días</strong> para entrega acelerada."
md_content = md_content.replace(old_md, new_md)

with open("COTIZACION_CASA_TRADICION.md", "w") as f:
    f.write(md_content)

with open("index.html", "r") as f:
    html_content = f.read()

# Since we reverted to the GSAP standard, let's look for what Option 1 currently says in index.html
old_html = """<h4 class="text-3xl font-black mb-4">De Contado</h4>
              <p class="text-sm text-stone-400 mb-8">Pago único al iniciar el proyecto. Prioridad máxima en la cola de desarrollo.</p>"""

new_html = """<h4 class="text-3xl font-black mb-4">De Contado</h4>
              <p class="text-sm text-stone-400 mb-8">Pago único al iniciar. <span class="text-[#D4AF37] font-bold">Fast-Track: Reduce el tiempo de desarrollo de 2 meses a solo 40 días.</span></p>"""

if old_html in html_content:
    html_content = html_content.replace(old_html, new_html)
else:
    # Try regex fallback if spacing is different
    import re
    html_content = re.sub(
        r'<h4 class="text-3xl font-black mb-4">De Contado</h4>\s*<p class="text-sm text-stone-400 mb-8">.*?</p>',
        r'<h4 class="text-3xl font-black mb-4">De Contado</h4>\n              <p class="text-sm text-stone-400 mb-8">Pago único al iniciar. <span class="text-[#D4AF37] font-bold">Fast-Track: Reduce el tiempo de desarrollo de 2 meses a solo 40 días.</span></p>',
        html_content
    )

with open("index.html", "w") as f:
    f.write(html_content)

