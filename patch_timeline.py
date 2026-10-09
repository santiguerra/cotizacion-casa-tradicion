with open("index.html", "r") as f:
    html = f.read()

# Current HTML string to replace:
# I will replace the entire 'seccion-cronograma'

new_cronograma = """
    <!-- CRONOGRAMA Y TECNOLOGIA -->
    <section id="seccion-cronograma" class="py-32 px-4 sm:px-6 relative z-40 bg-[#A84A2E] text-white overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <h2 id="roadmap-title" class="text-[6vw] md:text-[5vw] leading-[0.85] font-black tracking-tighter uppercase mb-16 text-center text-black">ROADMAP DETALLADO Y TECNOLOGÍA.</h2>
        
        <!-- TECNOLOGÍAS USADAS -->
        <div class="mb-16 bg-black/60 p-8 rounded-3xl border border-white/10 tech-card">
          <h3 class="text-[#D4AF37] font-black text-2xl uppercase mb-6 font-cinzel tracking-widest border-b border-white/10 pb-4">Stack Tecnológico (High-End)</h3>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <div>
              <div class="font-bold text-lg">Next.js & React 19</div>
              <div class="text-xs text-stone-400 mt-1">Framework de élite. Ultra rápido y responsivo.</div>
            </div>
            <div>
              <div class="font-bold text-lg text-white">Google Firebase</div>
              <div class="text-xs text-stone-400 mt-1">Base de datos en tiempo real para almacenar usuarios y catálogos.</div>
            </div>
            <div>
              <div class="font-bold text-lg">TypeScript & Zustand</div>
              <div class="text-xs text-stone-400 mt-1">Arquitectura robusta, sin errores técnicos y estado local hiper-optimizado.</div>
            </div>
            <div>
              <div class="font-bold text-lg text-white">Tailwind CSS & Motion</div>
              <div class="text-xs text-stone-400 mt-1">Dirección de arte paramétrica y animaciones nivel cine.</div>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="mes-card bg-black/40 p-8 rounded-[2rem] border border-white/10 relative overflow-hidden group hover:bg-black transition-colors">
            <div class="text-[#D4AF37] font-black text-8xl absolute -top-4 -right-4 opacity-20">01</div>
            <h3 class="text-2xl font-black font-cinzel mb-6 relative z-10 text-white">Mes 1: Frontend & Arte</h3>
            <ul class="text-xs text-stone-300 relative z-10 space-y-3 font-medium">
              <li><span class="text-[#D4AF37] font-bold">Día 01 - 05:</span> Wireframing B2B y Arquitectura de Datos.</li>
              <li><span class="text-[#D4AF37] font-bold">Día 06 - 15:</span> Setup Next.js, React 19 y maquetación Jigsaw.</li>
              <li><span class="text-[#D4AF37] font-bold">Día 16 - 25:</span> Estructuración de Catálogos 3D interactivos con Tailwind.</li>
              <li><span class="text-[#D4AF37] font-bold">Día 26 - 30:</span> Implementación de físicas y GSAP / Motion.</li>
            </ul>
          </div>
          
          <div class="mes-card bg-black/40 p-8 rounded-[2rem] border border-white/10 relative overflow-hidden group hover:bg-black transition-colors">
            <div class="text-[#D4AF37] font-black text-8xl absolute -top-4 -right-4 opacity-20">02</div>
            <h3 class="text-2xl font-black font-cinzel mb-6 relative z-10 text-white">Mes 2: Backend & Base de Datos</h3>
            <ul class="text-xs text-stone-300 relative z-10 space-y-3 font-medium">
              <li><span class="text-[#D4AF37] font-bold">Día 31 - 40:</span> Integración de Google Firebase (Firestore Database y Reglas de Seguridad).</li>
              <li><span class="text-[#D4AF37] font-bold">Día 41 - 50:</span> Desarrollo de Checkout (Recolección de datos y Link a WhatsApp).</li>
              <li><span class="text-[#D4AF37] font-bold">Día 51 - 55:</span> Conexión de estados con Zustand y testing interno.</li>
              <li><span class="text-[#D4AF37] font-bold">Día 56 - 60:</span> <span class="text-white bg-black/50 px-1">Entrega Oficial del Software.</span></li>
            </ul>
          </div>
          
          <div class="mes-card bg-[#120F0D] p-8 rounded-[2rem] border border-[#D4AF37]/50 relative overflow-hidden shadow-2xl scale-105">
            <div class="text-[#D4AF37] font-black text-8xl absolute -top-4 -right-4 opacity-10">03</div>
            <h3 class="text-2xl font-black font-cinzel mb-6 relative z-10 text-[#D4AF37]">Mes 3: Pruebas Beta y Soporte</h3>
            <ul class="text-xs text-stone-300 relative z-10 space-y-3 font-medium">
              <li><span class="text-[#D4AF37] font-bold">Día 61 - 90:</span> Liberación en vivo a clientes HORECA reales.</li>
              <li class="mt-4 border-t border-white/10 pt-4 text-white">Monitoreo activo de servidores en Firebase.</li>
              <li class="text-white">Asistencia a usuarios y corrección ágil de usabilidad.</li>
              <li class="text-white">Preparación de base para futura pasarela de pagos.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
"""

# Find the section to replace
import re
start_str = '<section id="seccion-cronograma"'
end_str = '<!-- METODOS DE PAGO -->'
pattern = re.compile(f"{start_str}.*?(?={end_str})", re.DOTALL)

html = pattern.sub(new_cronograma, html)

# We also need to add GSAP animation for tech-card
if 'gsap.from(".mes-card"' in html:
    gsap_tech = """
      gsap.from(".tech-card", {
        scrollTrigger: { trigger: "#seccion-cronograma", start: "top 75%" },
        scale: 0.8, opacity: 0, duration: 1, ease: "back.out(1.5)"
      });
"""
    html = html.replace('gsap.from(".mes-card"', gsap_tech + '      gsap.from(".mes-card"')


with open("index.html", "w") as f:
    f.write(html)
