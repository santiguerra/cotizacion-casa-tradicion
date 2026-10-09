with open("index.html", "r") as f:
    content = f.read()

# Replace WhatsApp link
content = content.replace(
    'href="https://wa.me/?text=Hola%20equipo%20Meta%20Level,%20estoy%20preparado,%20vamos%20a%20empezar%20con%20el%20proyecto."',
    'href="https://wa.me/573017505981?text=Hola%20equipo%20Meta%20Level,%20estoy%20preparado,%20vamos%20a%20empezar%20con%20el%20proyecto."'
)

# New sections HTML (Bleach Aesthetic: Huge text, stark contrasts)
new_sections = """
    <!-- NUEVAS SECCIONES COMERCIALES (ALCANCE, CRONOGRAMA Y PAGOS) -->
    
    <!-- ALCANCE (Scope) -->
    <section class="py-32 px-4 sm:px-6 relative z-40 bg-[#D4AF37] text-black border-t border-black">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-16">
        <div class="w-full md:w-1/2">
          <h2 class="text-[8vw] md:text-[6vw] leading-[0.85] font-black tracking-tighter uppercase mb-8">NUESTRO<br>ALCANCE.</h2>
          <p class="text-xl font-bold border-l-4 border-black pl-4">No es solo una web. Es una identidad visual inmersiva cruzada con un motor de ventas B2B.</p>
        </div>
        <div class="w-full md:w-1/2 space-y-6">
          <div class="bg-black text-white p-8 rounded-2xl">
            <h4 class="text-xl font-black uppercase text-[#D4AF37] mb-2">1. Identidad Interactiva</h4>
            <p class="text-sm">Animaciones GSAP, diseño editorial y catálogos 3D que proyectan el estatus premium de Casa Tradición.</p>
          </div>
          <div class="bg-white/20 p-8 rounded-2xl border border-black/10">
            <h4 class="text-xl font-black uppercase mb-2">2. Pasarela B2B WhatsApp</h4>
            <p class="text-sm">Sistema de Checkout donde el usuario llena su info. Envía la orden directa al chat ("Adjunto pago de X..."). Listo para escalar a pasarela bancaria real en el futuro comprando la licencia.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CRONOGRAMA (Horizontal Scroll or Stark Grid) -->
    <section class="py-32 px-4 sm:px-6 relative z-40 bg-[#A84A2E] text-white">
      <div class="max-w-7xl mx-auto">
        <h2 class="text-[8vw] md:text-[5vw] leading-[0.85] font-black tracking-tighter uppercase mb-16 text-center text-black">ROADMAP: 3 MESES.</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-black/40 p-8 rounded-[2rem] border border-white/10 relative overflow-hidden group hover:bg-black transition-colors">
            <div class="text-[#D4AF37] font-black text-8xl absolute -top-4 -right-4 opacity-20">01</div>
            <h3 class="text-2xl font-black font-cinzel mb-4 relative z-10">MES 1: Fundamentos</h3>
            <p class="text-sm text-stone-300 relative z-10">Diseño UI/UX, arquitectura de la información, maquetación del Jigsaw Bento y configuración de las animaciones GSAP base.</p>
          </div>
          
          <div class="bg-black/40 p-8 rounded-[2rem] border border-white/10 relative overflow-hidden group hover:bg-black transition-colors">
            <div class="text-[#D4AF37] font-black text-8xl absolute -top-4 -right-4 opacity-20">02</div>
            <h3 class="text-2xl font-black font-cinzel mb-4 relative z-10">MES 2: Motor B2B</h3>
            <p class="text-sm text-stone-300 relative z-10">Programación del catálogo 3D, desarrollo del Checkout a WhatsApp (recolección de datos). <strong>Entrega oficial del proyecto al finalizar.</strong></p>
          </div>
          
          <div class="bg-[#120F0D] p-8 rounded-[2rem] border border-[#D4AF37]/50 relative overflow-hidden shadow-2xl scale-105">
            <div class="text-[#D4AF37] font-black text-8xl absolute -top-4 -right-4 opacity-10">03</div>
            <h3 class="text-2xl font-black font-cinzel mb-4 relative z-10 text-[#D4AF37]">MES 3: Pruebas Beta</h3>
            <p class="text-sm text-stone-300 relative z-10">Lanzamiento en entorno real. Clientes reales pueden usarla para comprar. Hacemos monitoreo, soporte técnico y corrección de bugs en vivo.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- METODOS DE PAGO -->
    <section class="py-32 px-4 sm:px-6 relative z-40 bg-[#070605] text-white border-t border-white/10">
      <div class="max-w-7xl mx-auto text-center">
        <h2 class="text-[6vw] md:text-[4vw] leading-[0.85] font-black tracking-tighter uppercase mb-4 text-white">FLEXIBILIDAD FINANCIERA</h2>
        <p class="text-stone-400 mb-16 max-w-2xl mx-auto">Tú eliges cómo apalancar este proyecto. Tres modalidades de pago disponibles para los $2.500.000 COP.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
          <div class="bg-[#120F0D] p-8 rounded-2xl border border-white/10 flex flex-col">
            <span class="text-[#10B981] font-bold text-xs tracking-widest uppercase mb-4">Opción 1</span>
            <h4 class="text-3xl font-black mb-4">De Contado</h4>
            <p class="text-sm text-stone-400 mb-8">Pago único del 100% al iniciar el proyecto. Prioridad máxima en cola de desarrollo.</p>
            <div class="mt-auto text-2xl font-black text-[#D4AF37]">1x $2.500.000</div>
          </div>
          
          <div class="bg-[#120F0D] p-8 rounded-2xl border border-white/10 flex flex-col">
            <span class="text-[#10B981] font-bold text-xs tracking-widest uppercase mb-4">Opción 2</span>
            <h4 class="text-3xl font-black mb-4">3 Cuotas</h4>
            <p class="text-sm text-stone-400 mb-8">Una cuota por mes de desarrollo. Mes 1, Mes 2, y la última al finalizar el Mes 3 (Fase de Pruebas).</p>
            <div class="mt-auto text-2xl font-black text-[#D4AF37]">3x $833.333</div>
          </div>
          
          <div class="bg-[#1A1613] p-8 rounded-2xl border border-[#D4AF37] flex flex-col relative overflow-hidden shadow-[0_0_30px_rgba(212,175,55,0.15)]">
            <div class="absolute top-0 right-0 bg-[#D4AF37] text-black text-[10px] font-bold px-3 py-1 rounded-bl-lg">Recomendado</div>
            <span class="text-[#D4AF37] font-bold text-xs tracking-widest uppercase mb-4">Opción 3</span>
            <h4 class="text-3xl font-black mb-4">40% / 60%</h4>
            <p class="text-sm text-stone-400 mb-8">40% inicial para arrancar diseño. 60% al finalizar el Mes 2 (Entrega del proyecto, antes de entrar a Beta).</p>
            <div class="mt-auto">
              <div class="text-lg font-bold text-stone-300">Inicia: $1.000.000</div>
              <div class="text-lg font-bold text-stone-300">Entrega: $1.500.000</div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

# Insert new sections before CTA
cta_marker = "<!-- CTA WHATSAPP META LEVEL -->"
content = content.replace(cta_marker, new_sections + "\n    " + cta_marker)

with open("index.html", "w") as f:
    f.write(content)

