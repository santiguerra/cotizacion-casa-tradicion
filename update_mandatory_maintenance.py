import re

# 1. Update PDF
with open("COTIZACION_CASA_TRADICION.md", "r") as f:
    md = f.read()

old_md_maint = "**Mantenimiento Mensual (Opcional post-lanzamiento):** $150.000 COP\n*Incluye soporte técnico 24/7 y actualizaciones de seguridad. Aplica sistema de referidos: si nos refieren un cliente que cierre contrato, el mantenimiento baja al 50% ($75.000 COP) y se añaden módulos gratis.*"

new_md_maint = """**Mantenimiento Operativo Mensual (Requisito Obligatorio):** $150.000 COP
Al ser un software vivo y no una plantilla estática, este rubro es indispensable para mantener el sistema en el aire. Incluye:
*   **Infraestructura Cloud:** Pago de servidores en Google Firebase y consumo de base de datos.
*   **Blindaje de Seguridad:** Certificados SSL, encriptación de datos de clientes HORECA y copias de seguridad.
*   **Soporte Técnico 24/7:** Monitoreo activo para un 99.9% de uptime (la página nunca se cae) y resolución de bugs.
*Aplica sistema de referidos: si nos refieren un cliente que cierre contrato con la agencia, este costo operativo baja al 50% ($75.000 COP) y desbloquean módulos de código gratis.*"""

if old_md_maint in md:
    md = md.replace(old_md_maint, new_md_maint)
else:
    # Use Regex just in case
    md = re.sub(
        r'\*\*Mantenimiento Mensual \(Opcional post-lanzamiento\):\*\* \$150\.000 COP.*?\n.*?(?=\n### Planes de Pago Flexibles:)',
        new_md_maint,
        md,
        flags=re.DOTALL
    )

with open("COTIZACION_CASA_TRADICION.md", "w") as f:
    f.write(md)

# 2. Update HTML
with open("index.html", "r") as f:
    html = f.read()

old_html_list = """<div class="space-y-4">
              <div class="flex items-center gap-3"><div class="w-8 h-8 rounded-full bg-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] font-bold">✓</div><span class="text-sm font-bold text-white">Soporte Técnico 24/7</span></div>
              <div class="flex items-center gap-3"><div class="w-8 h-8 rounded-full bg-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] font-bold">✓</div><span class="text-sm font-bold text-white">Actualizaciones Seguridad</span></div>
              <div id="ref-extra-feat" class="flex items-center gap-3 opacity-30 grayscale transition-all duration-500"><div class="w-8 h-8 rounded-full bg-[#10B981]/20 flex items-center justify-center text-[#10B981] font-bold text-lg leading-none">+</div><span class="text-sm font-bold text-[#10B981]">Módulos Adicionales GRATIS</span></div>
            </div>"""

new_html_list = """<div class="space-y-4">
              <div class="flex items-center gap-3"><div class="w-8 h-8 rounded-full bg-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] font-bold">✓</div><span class="text-sm font-bold text-white">Servidores Cloud & Firebase</span></div>
              <div class="flex items-center gap-3"><div class="w-8 h-8 rounded-full bg-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] font-bold">✓</div><span class="text-sm font-bold text-white">Blindaje SSL y Soporte 24/7</span></div>
              <div id="ref-extra-feat" class="flex items-center gap-3 opacity-30 grayscale transition-all duration-500"><div class="w-8 h-8 rounded-full bg-[#10B981]/20 flex items-center justify-center text-[#10B981] font-bold text-lg leading-none">+</div><span class="text-sm font-bold text-[#10B981]">Módulos Adicionales GRATIS</span></div>
            </div>"""

html = html.replace(old_html_list, new_html_list)

old_html_label = '<p class="text-xs text-stone-500 font-bold uppercase mb-4 relative z-10">Mantenimiento Mensual</p>'
new_html_label = '<p class="text-xs text-stone-500 font-bold uppercase mb-4 relative z-10">Mantenimiento (Obligatorio)</p>'
html = html.replace(old_html_label, new_html_label)

# Also update the Z-Axis text if it's there
html = html.replace(
    '<h3 class="text-xl font-bold mb-4 text-[#D4AF37]">2. Mantenimiento</h3>\n            <p class="text-sm text-stone-400">Soporte 24/7 continuo por $150.000 COP/mes. Tu plataforma siempre en línea, blindada y veloz.</p>',
    '<h3 class="text-xl font-bold mb-4 text-[#D4AF37]">2. Mantenimiento</h3>\n            <p class="text-sm text-stone-400">Servidores, DB y soporte 24/7 por $150.000 COP/mes. Costo obligatorio para mantener el software vivo y blindado.</p>'
)

with open("index.html", "w") as f:
    f.write(html)

