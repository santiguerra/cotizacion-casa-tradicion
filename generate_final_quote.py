html = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth bg-[#070605] text-[#EDE8E1]">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Propuesta Comercial Casa Tradición</title>
  
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800;900&family=Playfair+Display:ital,wght@0,600;0,800&family=Plus+Jakarta+Sans:wght@400;600;800;900&display=swap" rel="stylesheet">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>

  <style>
    :root { --gold: #D4AF37; --bg-dark: #070605; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; background: var(--bg-dark); }
    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-editorial { font-family: 'Playfair Display', serif; }
    
    /* Jigsaw Bento Clip Paths - Gaps are handled by exact percentage layouts */
    .shape-tl { clip-path: polygon(0% 0%, 100% 0%, 100% 65%, 75% 100%, 0% 100%); }
    .shape-tr { clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 25% 100%, 0% 60%); }
    .shape-bl { clip-path: polygon(0% 0%, 75% 0%, 100% 35%, 100% 100%, 0% 100%); }
    .shape-br { clip-path: polygon(30% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 30%); }

    .huge-text { font-size: 11vw; line-height: 0.85; font-weight: 900; text-transform: uppercase; letter-spacing: -0.04em; }
    
    /* UI Overrides */
    .bezel-chassis {
      background: linear-gradient(145deg, rgba(24,21,18,0.9) 0%, rgba(14,12,10,0.95) 100%);
      border: 1px solid rgba(212,175,55,0.2);
    }
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #070605; }
    ::-webkit-scrollbar-thumb { background: #D4AF37; border-radius: 4px; }

    /* 3D Flip */
    .flip-card-3d { perspective: 1200px; }
    .flip-card-inner { position: relative; width: 100%; height: 100%; transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1); transform-style: preserve-3d; }
    .flip-card-3d.is-flipped .flip-card-inner { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; border-radius: 1.25rem; overflow: hidden; }
    .flip-card-back { transform: rotateY(180deg); }
  </style>
</head>
<body class="antialiased">

  <div class="fixed inset-0 w-full h-full pointer-events-none z-50 opacity-[0.03] mix-blend-overlay" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noise%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.8%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noise)%22/%3E%3C/svg%3E');"></div>

  <!-- HEADER AGENCIA -->
  <header class="fixed top-0 left-0 w-full z-50 px-6 py-5 flex justify-between items-center mix-blend-difference pointer-events-none">
    <div class="flex items-center gap-3">
      <div class="w-2 h-2 rounded-full bg-[#D4AF37] animate-pulse"></div>
      <span class="font-cinzel font-bold text-sm tracking-widest text-white uppercase">Propuesta Comercial</span>
    </div>
    <div class="pointer-events-auto flex items-center gap-4">
      <a href="#precio" class="bg-white text-black px-6 py-2.5 rounded-full text-[10px] font-black tracking-widest uppercase hover:scale-105 transition-transform">
        Inversión: $2.5M
      </a>
    </div>
  </header>

  <main id="smooth-wrapper" class="bg-[#070605]">
    <div id="smooth-content">

      <!-- 1. HERO BENTO (El Rompecabezas / The Pitch) -->
      <section class="h-[100vh] min-h-[700px] w-full p-4 pt-24 pb-8 flex flex-col items-center justify-center relative origin-center" id="hero-wrapper">
        <div class="relative w-full max-w-7xl h-full mx-auto rounded-[2.5rem] bg-[#070605]">
          
          <!-- Top Left (Pitch) -->
          <div class="absolute top-0 left-0 w-[47%] h-[60%]">
            <div class="w-full h-full bg-gradient-to-br from-[#1A1613] to-[#0A0807] shape-tl p-8 lg:p-12 flex flex-col border border-white/5 relative shadow-2xl">
              <h1 class="text-4xl xl:text-6xl font-black text-white leading-[0.95] tracking-tighter relative z-10">
                PROYECTO WEB<br>
                <span class="text-[#D4AF37] font-cinzel italic pr-2 font-light">CASA TRADICIÓN</span>
              </h1>
              <div class="mt-auto relative z-10 w-[85%] pr-8">
                <p class="text-xs font-bold text-stone-300 leading-relaxed mb-6 border-l-2 border-[#D4AF37] pl-4">
                  Esta no es una página web básica. Es una plataforma B2B interactiva diseñada para dominar el canal HORECA, justificar tus precios y automatizar tus ventas por WhatsApp.
                </p>
                <a href="#precio" class="inline-block bg-[#D4AF37] text-black px-8 py-3 rounded-xl font-black text-[10px] uppercase tracking-wider hover:bg-white transition-colors cursor-pointer">
                  Ver Presupuesto y Entregables
                </a>
              </div>
            </div>
          </div>

          <!-- Top Right (Visual Capability Demo) -->
          <div class="absolute top-0 right-0 w-[52%] h-[68%]">
            <div class="w-full h-full bg-[#120F0D] shape-tr overflow-hidden relative group">
              <img src="assets/img/hero-patacones.webp" class="w-full h-full object-cover opacity-60 group-hover:opacity-90 group-hover:scale-105 transition-all duration-[1.5s] ease-out">
              <div class="absolute inset-0 bg-gradient-to-t from-[#070605] via-transparent to-transparent"></div>
              <div class="absolute top-8 left-16 text-white font-bold text-xs tracking-[0.2em] uppercase font-cinzel">Dirección de Arte Real</div>
            </div>
          </div>

          <!-- Bottom Left (Visual Capability Demo) -->
          <div class="absolute bottom-0 left-0 w-[65%] h-[39%]">
            <div class="w-full h-full bg-[#120F0D] shape-bl overflow-hidden relative group">
              <img src="assets/img/finca.webp" class="w-full h-full object-cover opacity-40 group-hover:opacity-80 group-hover:scale-105 transition-all duration-[1.5s] ease-out grayscale-[20%]">
              <div class="absolute inset-0 bg-gradient-to-r from-[#070605] via-[#070605]/50 to-transparent"></div>
              <div class="absolute bottom-8 left-10 text-white flex flex-col">
                <span class="text-[#D4AF37] font-bold text-[10px] tracking-[0.2em] uppercase mb-1">Identidad de Marca</span>
                <span class="font-editorial text-2xl italic">Proyectamos tu esencia.</span>
              </div>
            </div>
          </div>

          <!-- Bottom Right (Tech capability) -->
          <div class="absolute bottom-0 right-0 w-[34%] h-[31%]">
            <div class="w-full h-full bg-[#D4AF37] shape-br p-8 flex flex-col items-end justify-end relative overflow-hidden group">
              <h3 class="text-black font-black text-3xl tracking-tighter text-right leading-none z-10 relative">ALTA<br>INGENIERÍA</h3>
              <p class="text-black/70 text-[10px] uppercase font-bold tracking-widest mt-2 z-10 relative text-right">0% Plantillas. 100% Código Libre.</p>
              <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-white/20 blur-[30px] rounded-full group-hover:bg-white/40 transition-colors"></div>
            </div>
          </div>

        </div>
      </section>

      <!-- 2. "ABSORB" SCROLL ANIMATION & STARK PITCH PANELS -->
      <!-- Contenedor general donde ocurrirá el pinning y el wipe -->
      <section id="pitch-sequence" class="relative w-full bg-[#070605]">
        
        <!-- Stark Panel 1: RED IMPACT (Capabilities) -->
        <div class="stark-panel w-full h-screen bg-[#A84A2E] sticky top-0 flex items-center justify-center overflow-hidden z-10 origin-center panel-1-wrap" style="clip-path: circle(0% at center);">
          <div class="absolute inset-0 opacity-10 mix-blend-multiply"><img src="assets/img/cocina.webp" class="w-full h-full object-cover"></div>
          <div class="z-20 text-center w-full px-4 flex flex-col items-center">
            <h2 class="huge-text font-cinzel text-[#FBF0B9] p1-text translate-y-20 opacity-0">NO HACEMOS</h2>
            <img src="assets/p/img-014.webp" class="w-[50vw] max-w-[600px] drop-shadow-[0_40px_80px_rgba(0,0,0,0.8)] z-30 my-[-10vh] scale-[0.2] opacity-0 p1-img origin-center">
            <h2 class="huge-text font-cinzel text-white p1-text translate-y-20 opacity-0 relative z-40">FOLLETOS ABURRIDOS.</h2>
          </div>
        </div>

        <!-- Stark Panel 2: GOLD IMPACT (Why buy it) -->
        <div class="stark-panel w-full h-screen bg-[#D4AF37] sticky top-0 flex items-center justify-center overflow-hidden z-20 panel-2-wrap" style="clip-path: inset(100% 0 0 0);">
          <div class="z-20 flex flex-col md:flex-row items-center justify-center w-full max-w-7xl px-8 gap-12">
            <div class="md:w-1/2 text-left">
              <h2 class="text-[9vw] leading-[0.8] font-black tracking-tighter uppercase text-black p2-text -translate-x-20 opacity-0">CREAMOS<br>VENTAS.</h2>
              <p class="text-xl md:text-2xl font-bold mt-8 text-black/80 max-w-md border-l-4 border-black pl-4 p2-desc translate-y-10 opacity-0">Construimos motores interactivos que le demuestran a los chefs por qué tu producto es superior. Cero comisiones a pasarelas, pedidos directo a tu WhatsApp.</p>
            </div>
            <div class="md:w-1/2 flex justify-center p2-img translate-x-20 opacity-0">
              <img src="assets/p/img-012.webp" class="w-full max-w-[500px] drop-shadow-2xl">
            </div>
          </div>
        </div>

        <!-- Stark Panel 3: BLACK IMPACT (Price Justification) -->
        <div id="precio" class="stark-panel w-full min-h-screen bg-[#070605] sticky top-0 flex flex-col justify-center items-center overflow-hidden z-30 px-6 py-24 panel-3-wrap" style="clip-path: inset(100% 0 0 0);">
          <span class="text-[#D4AF37] font-bold text-xs uppercase tracking-[0.3em] mb-4 p3-text scale-50 opacity-0">Inversión Transparente y Única</span>
          <h2 class="text-[12vw] leading-[0.8] font-black tracking-tighter uppercase text-white p3-text scale-50 opacity-0 text-center">$2.500.000 <span class="text-3xl text-[#D4AF37] align-top block mt-2">COP</span></h2>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl w-full mt-16 p3-boxes opacity-0 translate-y-20">
            <div class="bezel-chassis p-8 rounded-3xl text-left border-t border-[#D4AF37]">
              <h4 class="text-white font-bold mb-2">Desarrollo B2B Custom</h4>
              <p class="text-xs text-stone-400">Sin plantillas mediocres. Código escrito desde cero para cargar en milisegundos y aplastar a tu competencia.</p>
            </div>
            <div class="bezel-chassis p-8 rounded-3xl text-left border-t border-[#D4AF37]">
              <h4 class="text-white font-bold mb-2">0% Comisiones (QR + WP)</h4>
              <p class="text-xs text-stone-400">Toda la orden se compila automatizada a WhatsApp y el pago es directo por QR. 100% del dinero es tuyo.</p>
            </div>
            <div class="bezel-chassis p-8 rounded-3xl text-left border-t border-[#D4AF37]">
              <h4 class="text-white font-bold mb-2">Dominio, Cloud & SEO</h4>
              <p class="text-xs text-stone-400">Montaje en servidores seguros (HTTPS), configuración de correos corporativos y optimización para Google.</p>
            </div>
          </div>
        </div>

      </section>

      <!-- 3. DEMOSTRACIÓN DE CAPACIDADES TÉCNICAS -->
      <section class="py-32 px-4 sm:px-6 max-w-7xl mx-auto border-t border-white/10 relative z-40 bg-[#070605]">
        <div class="text-center max-w-3xl mx-auto mb-20 space-y-4">
          <h2 class="text-4xl md:text-6xl font-black text-white">ESTO ES LO QUE<br>SOMOS CAPACES DE HACER.</h2>
          <p class="text-stone-400 font-semibold text-lg">Prueba en vivo los módulos interactivos que desarrollaremos para el portal final de Casa Tradición.</p>
        </div>

        <!-- Demo 1: Showroom -->
        <div class="mb-32">
          <div class="flex flex-col md:flex-row justify-between items-end border-b border-white/10 pb-6 mb-8 gap-4">
            <div>
              <h3 class="text-3xl font-black text-white font-cinzel">Módulo 1: Catálogo 3D</h3>
              <p class="text-sm text-stone-500 mt-2 max-w-xl">Un portafolio vivo. El cliente puede girar la tarjeta para ver el producto en empaque al vacío y servido gourmet. Haz clic en las tarjetas de abajo para probarlo.</p>
            </div>
          </div>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" id="showroom-grid">
            <!-- Inyectado por JS (Solo mostraremos 4 como demo técnica de la agencia) -->
          </div>
        </div>

        <!-- Demo 2: Simulador -->
        <div>
          <div class="flex flex-col md:flex-row justify-between items-end border-b border-white/10 pb-6 mb-8 gap-4">
            <div>
              <h3 class="text-3xl font-black text-white font-cinzel">Módulo 2: Motor Financiero</h3>
              <p class="text-sm text-stone-500 mt-2 max-w-xl">Una calculadora reactiva que convence al Chef de comprarte demostrando cuánto ahorra. Mueve los deslizadores y mira cómo cambia el dinero.</p>
            </div>
          </div>

          <div class="bezel-chassis rounded-[2rem] p-8 grid grid-cols-1 lg:grid-cols-2 gap-12 bg-gradient-to-br from-[#120F0D] to-[#0A0807]">
            <div class="space-y-8">
              <div class="space-y-4">
                <div class="flex justify-between text-sm font-semibold">
                  <span class="text-stone-300">Porciones servidas por día:</span>
                  <span class="text-xl font-black text-[#D4AF37] font-cinzel" id="disp-dishes">140</span>
                </div>
                <input type="range" id="sim-dishes" min="30" max="600" step="10" value="140" oninput="runHorecaCalc()" class="w-full accent-[#D4AF37] cursor-pointer">
              </div>
            </div>
            <div class="flex flex-col justify-center items-center text-center">
              <span class="text-xs uppercase tracking-widest text-stone-500 font-bold mb-2">Ahorro Mensual que demuestras al Chef</span>
              <div class="text-5xl md:text-7xl font-black text-[#D4AF37] font-cinzel" id="out-money">$4.730.000</div>
              <p class="text-xs text-[#10B981] mt-4 font-bold bg-[#10B981]/10 px-4 py-2 rounded-full border border-[#10B981]/20">Tus ventas se justifican matemáticamente.</p>
            </div>
          </div>
        </div>

      </section>

      <!-- Footer Agency -->
      <footer class="py-12 border-t border-white/10 text-center bg-[#070605] relative z-40 text-stone-500 text-xs">
        Cotización interactiva desarrollada con Alta Ingeniería Web.<br>
        2026 © Diseño e Implementación por Santiago Guerra.
      </footer>

    </div>
  </main>

  <script>
    // DATOS DE DEMO
    const demoData = [
      { id: 1, name: 'Plátano Maduro Entero', cant: '3 unds', pack: 'assets/p/img-006.webp', dish: 'assets/p/img-007.webp' },
      { id: 2, name: 'Tostón Jumbo 28cm', cant: '10 unds', pack: 'assets/p/img-035.webp', dish: 'assets/p/img-036.webp' },
      { id: 3, name: 'Yuca Astilla', cant: '5kg', pack: 'assets/p/img-008.webp', dish: 'assets/p/img-009.webp' },
      { id: 4, name: 'Aborrajado Valluno', cant: '9 unds', pack: 'assets/p/img-041.webp', dish: 'assets/p/img-042.webp' }
    ];

    function renderShowroomDemo() {
      const container = document.getElementById('showroom-grid');
      container.innerHTML = demoData.map(p => `
        <div class="bezel-chassis p-4 flex flex-col group rounded-2xl bg-[#120F0D]">
          <div class="flip-card-3d rounded-xl aspect-[4/3] mb-4 cursor-pointer" onclick="this.classList.toggle('is-flipped')">
            <div class="flip-card-inner">
              <div class="flip-card-front relative">
                <img src="${p.dish}" class="w-full h-full object-cover rounded-xl" loading="lazy">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent rounded-xl"></div>
                <span class="absolute bottom-2 left-2 text-[10px] bg-black/80 text-white px-2 py-1 rounded border border-white/10 flex items-center gap-1">
                  <svg class="w-3 h-3 text-[#D4AF37]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/></svg> Haz Clic
                </span>
              </div>
              <div class="flip-card-back relative">
                <img src="${p.pack}" class="w-full h-full object-cover rounded-xl" loading="lazy">
                <div class="absolute inset-0 bg-gradient-to-t from-[#1F4D25]/90 to-transparent rounded-xl"></div>
                <span class="absolute bottom-2 left-2 text-[10px] bg-black/80 text-[#10B981] px-2 py-1 rounded border border-[#10B981]/30">Empaque Real</span>
              </div>
            </div>
          </div>
          <h4 class="text-sm font-bold text-white leading-tight mb-1">${p.name}</h4>
          <span class="text-[10px] font-mono text-[#D4AF37]">${p.cant}</span>
        </div>
      `).join('');
    }

    function runHorecaCalc() {
      const d = parseInt(document.getElementById('sim-dishes').value);
      const days = 26; // Fijo para el demo
      document.getElementById('disp-dishes').textContent = d;
      const w = Math.round((d * days * 0.22) * 0.38);
      document.getElementById('out-money').textContent = `$${Math.round((w * 3400) + (w/26 * 9800)).toLocaleString('es-CO')}`;
    }

    // GSAP ABSORB & PITCH ANIMATIONS
    document.addEventListener("DOMContentLoaded", () => {
      renderShowroomDemo(); runHorecaCalc();
      gsap.registerPlugin(ScrollTrigger);

      const absorbTl = gsap.timeline({
        scrollTrigger: {
          trigger: "#hero-wrapper",
          start: "top top",
          end: "+=120%",
          scrub: 1,
          pin: true,
          pinSpacing: true
        }
      });

      // 1. EL ABSORB: El rompecabezas se succiona hacia el centro y desaparece.
      absorbTl.to("#hero-wrapper > div", {
        scale: 0.05,
        rotationZ: 10,
        opacity: 0,
        filter: "blur(20px)",
        ease: "power2.in",
        duration: 1
      });

      // 2. PANEL ROJO ("NO HACEMOS FOLLETOS") irrumpe desde el centro (wipe circular)
      const p1Tl = gsap.timeline({
        scrollTrigger: {
          trigger: ".panel-1-wrap",
          start: "top top",
          end: "+=150%",
          scrub: 1,
          pin: true,
          pinSpacing: true
        }
      });
      p1Tl.to(".panel-1-wrap", { clipPath: "circle(150% at center)", duration: 1, ease: "power2.out" })
          .to(".p1-img", { scale: 1.1, opacity: 1, duration: 1, ease: "back.out(1.5)" }, "<0.2")
          .to(".p1-text", { y: 0, opacity: 1, duration: 1, stagger: 0.2 }, "<0.2");

      // 3. PANEL DORADO ("CREAMOS VENTAS") hace wipe desde abajo
      const p2Tl = gsap.timeline({
        scrollTrigger: {
          trigger: ".panel-2-wrap",
          start: "top top",
          end: "+=150%",
          scrub: 1,
          pin: true,
          pinSpacing: true
        }
      });
      p2Tl.to(".panel-2-wrap", { clipPath: "inset(0% 0 0 0)", duration: 1, ease: "power2.out" })
          .to(".p2-text", { x: 0, opacity: 1, duration: 1, ease: "power3.out" }, "<0.3")
          .to(".p2-desc", { y: 0, opacity: 1, duration: 0.8 }, "<0.2")
          .to(".p2-img", { x: 0, opacity: 1, duration: 1, ease: "power3.out" }, "<0");

      // 4. PANEL NEGRO (PRECIO)
      const p3Tl = gsap.timeline({
        scrollTrigger: {
          trigger: ".panel-3-wrap",
          start: "top top",
          end: "+=100%",
          scrub: 1,
          pin: true,
          pinSpacing: true
        }
      });
      p3Tl.to(".panel-3-wrap", { clipPath: "inset(0% 0 0 0)", duration: 1, ease: "power2.out" })
          .to(".p3-text", { scale: 1, opacity: 1, duration: 1, stagger: 0.3, ease: "back.out(1.5)" }, "<0.3")
          .to(".p3-boxes", { y: 0, opacity: 1, duration: 1, ease: "power2.out" }, "<0.5");
    });
  </script>
</body>
</html>
"""
with open("index.html", "w") as f:
    f.write(html)
