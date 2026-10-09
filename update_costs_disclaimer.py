with open("COTIZACION_CASA_TRADICION.md", "r") as f:
    md = f.read()

old_pdf = "*   **Infraestructura Cloud:** Pago de servidores en Google Firebase y consumo de base de datos."
new_pdf = "*   **Gestión de Infraestructura:** Administración técnica, monitoreo y asesoría/acompañamiento para la configuración de pagos directos de dominios y servidores (Google Firebase)."
md = md.replace(old_pdf, new_pdf)

with open("COTIZACION_CASA_TRADICION.md", "w") as f:
    f.write(md)

with open("index.html", "r") as f:
    html = f.read()

old_html_1 = '<span class="text-sm font-bold text-white">Servidores Cloud & Base de Datos Firebase</span>'
new_html_1 = '<span class="text-sm font-bold text-white">Gestión de Servidores & Base de Datos</span>'
html = html.replace(old_html_1, new_html_1)

old_html_2 = 'Costos de servidor Firebase y soporte por $150.000 COP/mes. (Requisito Obligatorio para operar).'
new_html_2 = 'Gestión de infraestructura y soporte 24/7 por $150.000 COP/mes. (Requisito Obligatorio para operar).'
html = html.replace(old_html_2, new_html_2)

with open("index.html", "w") as f:
    f.write(html)
