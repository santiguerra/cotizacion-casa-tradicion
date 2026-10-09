with open("index.html", "r") as f:
    html = f.read()

# Fix bullet 1
html = html.replace(
    '<span class="text-sm font-bold text-white">Soporte Técnico 24/7</span>',
    '<span class="text-sm font-bold text-white">Servidores Cloud & Base de Datos Firebase</span>'
)

# Fix bullet 2
html = html.replace(
    '<span class="text-sm font-bold text-white">Actualizaciones de Seguridad</span>',
    '<span class="text-sm font-bold text-white">Blindaje SSL y Soporte 24/7 (Obligatorio)</span>'
)

# Fix Z-Axis text
html = html.replace(
    'Soporte 24/7 continuo por $150.000 COP/mes. Tu plataforma siempre en línea, blindada y veloz.',
    'Costos de servidor Firebase y soporte por $150.000 COP/mes. (Requisito Obligatorio para operar).'
)

with open("index.html", "w") as f:
    f.write(html)
