import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Agregar IDs y Clases a las secciones HTML
# Alcance
content = content.replace(
    '<section class="py-32 px-4 sm:px-6 relative z-40 bg-[#D4AF37] text-black border-t border-black">',
    '<section id="seccion-alcance" class="py-32 px-4 sm:px-6 relative z-40 bg-[#D4AF37] text-black border-t border-black overflow-hidden">'
)
content = content.replace('NUESTRO<br>ALCANCE.', '<span id="alcance-title" class="block origin-left">NUESTRO<br>ALCANCE.</span>')
content = content.replace('class="bg-black text-white p-8 rounded-2xl"', 'class="alcance-card bg-black text-white p-8 rounded-2xl"')
content = content.replace('class="bg-white/20 p-8 rounded-2xl border border-black/10"', 'class="alcance-card bg-white/20 p-8 rounded-2xl border border-black/10"')

# Cronograma
content = content.replace(
    '<section class="py-32 px-4 sm:px-6 relative z-40 bg-[#A84A2E] text-white">',
    '<section id="seccion-cronograma" class="py-32 px-4 sm:px-6 relative z-40 bg-[#A84A2E] text-white overflow-hidden">'
)
content = content.replace('ROADMAP: 3 MESES.', '<span id="roadmap-title" class="block">ROADMAP: 3 MESES.</span>')
content = content.replace('class="bg-black/40 p-8 rounded-[2rem]', 'class="mes-card bg-black/40 p-8 rounded-[2rem]')
content = content.replace('class="bg-[#120F0D] p-8 rounded-[2rem]', 'class="mes-card bg-[#120F0D] p-8 rounded-[2rem]')

# Pagos
content = content.replace(
    '<section class="py-32 px-4 sm:px-6 relative z-40 bg-[#070605] text-white border-t border-white/10">',
    '<section id="seccion-pagos" class="py-32 px-4 sm:px-6 relative z-40 bg-[#070605] text-white border-t border-white/10 overflow-hidden">'
)
content = content.replace('FLEXIBILIDAD FINANCIERA', '<span id="pagos-title" class="block">FLEXIBILIDAD FINANCIERA</span>')
content = content.replace('class="bg-[#120F0D] p-8 rounded-2xl border', 'class="pago-card bg-[#120F0D] p-8 rounded-2xl border')
content = content.replace('class="bg-[#1A1613] p-8 rounded-2xl border', 'class="pago-card bg-[#1A1613] p-8 rounded-2xl border')

# CTA
content = content.replace(
    '<section class="py-24 text-center px-4 relative z-40 bg-gradient-to-t from-[#120F0D] to-[#070605] border-t border-white/10">',
    '<section id="seccion-cta" class="py-24 text-center px-4 relative z-40 bg-gradient-to-t from-[#120F0D] to-[#070605] border-t border-white/10 overflow-hidden">'
)
content = content.replace('¿LISTO PARA ESCALAR<br><span class="text-[#D4AF37]">CASA TRADICIÓN?</span>', '<div id="cta-title">¿LISTO PARA ESCALAR<br><span class="text-[#D4AF37]">CASA TRADICIÓN?</span></div>')

# 2. Inyectar Animaciones GSAP
gsap_logic = """
      // --- ANIMACIONES SECCIONES COMERCIALES ---
      
      // Alcance
      gsap.from("#alcance-title", {
        scrollTrigger: { trigger: "#seccion-alcance", start: "top 70%" },
        scale: 4, opacity: 0, duration: 1.2, ease: "power4.out"
      });
      gsap.from(".alcance-card", {
        scrollTrigger: { trigger: "#seccion-alcance", start: "top 60%" },
        x: 200, opacity: 0, duration: 1, stagger: 0.2, ease: "back.out(1.5)"
      });

      // Cronograma (Roadmap)
      gsap.from("#roadmap-title", {
        scrollTrigger: { trigger: "#seccion-cronograma", start: "top 75%" },
        y: 100, opacity: 0, duration: 1, ease: "power4.out"
      });
      gsap.from(".mes-card", {
        scrollTrigger: { trigger: "#seccion-cronograma", start: "top 60%" },
        y: 150, opacity: 0, rotationY: 45, duration: 1, stagger: 0.2, ease: "back.out(1.2)"
      });

      // Pagos
      gsap.from("#pagos-title", {
        scrollTrigger: { trigger: "#seccion-pagos", start: "top 80%" },
        scale: 0.5, opacity: 0, duration: 1, ease: "back.out(2)"
      });
      gsap.from(".pago-card", {
        scrollTrigger: { trigger: "#seccion-pagos", start: "top 65%" },
        scale: 0, opacity: 0, duration: 0.8, stagger: 0.2, ease: "back.out(1.5)"
      });

      // CTA Final
      gsap.from("#cta-title", {
        scrollTrigger: { trigger: "#seccion-cta", start: "top 85%" },
        scale: 1.5, opacity: 0, duration: 1.5, ease: "power3.out"
      });
"""

# Insert the logic right before the closing brace of DOMContentLoaded
content = content.replace(
    'tl.to("#black-section", { opacity: 1, scale: 1, duration: 1.5, ease: "power2.out" }, "-=1.5");\n    });',
    'tl.to("#black-section", { opacity: 1, scale: 1, duration: 1.5, ease: "power2.out" }, "-=1.5");\n' + gsap_logic + '\n    });'
)

with open("index.html", "w") as f:
    f.write(content)

