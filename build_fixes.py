import os

html = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth bg-[#070605] text-white">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cotización Casa Tradición - High-End</title>
  
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@800;900&family=Plus+Jakarta+Sans:wght@400;700;900&display=swap" rel="stylesheet">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; background: #070605; }
    .font-cinzel { font-family: 'Cinzel', serif; }
    
    /* Bento Clip Paths */
    .shape-tl { clip-path: polygon(0% 0%, 100% 0%, 100% 65%, 75% 100%, 0% 100%); }
    .shape-tr { clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 25% 100%, 0% 60%); }
    .shape-bl { clip-path: polygon(0% 0%, 75% 0%, 100% 35%, 100% 100%, 0% 100%); }
    .shape-br { clip-path: polygon(30% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 30%); }

    /* Fix text size to prevent cutoffs */
    .huge-text { 
      font-size: clamp(3rem, 12vw, 15rem); 
      line-height: 0.85; 
      font-weight: 900; 
      text-transform: uppercase; 
      letter-spacing: -0.02em; 
      white-space: nowrap; 
    }
    
    /* 3D Flip (Fixed Image Drop Bug) */
    .flip-card-3d { perspective: 1200px; }
    .flip-card-inner { 
      position: relative; 
      width: 100%; 
      height: 100%; 
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1); 
      transform-style: preserve-3d; 
    }
    .flip-card-3d.is-flipped .flip-card-inner { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back { 
      position: absolute; 
      inset: 0; 
      width: 100%; 
      height: 100%; 
      -webkit-backface-visibility: hidden; 
      backface-visibility: hidden; 
      border-radius: 1.25rem; 
      overflow: hidden; 
      background: #000;
    }
    .flip-card-front img, .flip-card-back img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .flip-card-back { transform: rotateY(180deg); }
  </style>
</head>
<body class="antialiased">

  <!-- Pinned Z-Axis Sequence -->
  <div id="z-sequence" class="w-screen h-screen overflow-hidden relative bg-black">
    
    <!-- Layer 4: The Price / Pitch (Black) -->
    <div id="black-section" class="absolute inset-0 flex flex-col justify-center items-center text-white z-10 p-8 opacity-0 scale-50">
      <h2 class="text-[8vw] font-black tracking-tighter leading-none mb-12 text-center text-[#D4AF37] font-cinzel">INVERSIÓN:<br>$2.500.000 COP</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl w-full">
        <div class="bg-white/5 p-8 rounded-2xl border border-white/10">
          <h3 class="text-xl font-bold mb-4">1. El Porqué del Precio</h3>
          <p class="text-sm text-stone-400">Esta no es una plantilla de $500k. Es código nativo, animaciones nivel agencia global y optimización SEO extrema para dominar las búsquedas B2B.</p>
        </div>
        <div class="bg-white/5 p-8 rounded-2xl border border-[#D4AF37]/30">
          <h3 class="text-xl font-bold mb-4 text-[#D4AF37]">2. Soporte 24/7 y Mant.</h3>
          <p class="text-sm text-stone-400">Soporte técnico y mantenimiento continuo por solo $150.000 COP/mes. Además, tu pasarela de WhatsApp no cobra comisiones por venta.</p>
        </div>
        <div class="bg-white/5 p-8 rounded-2xl border border-white/10">
          <h3 class="text-xl font-bold mb-4">3. Herramientas de Cierre</h3>
          <p class="text-sm text-stone-400">Incluye catálogo 3D avanzado y módulos de retención. Tu página web hará el trabajo de venta por ti, sumergiendo al cliente en la marca.</p>
        </div>
      </div>
      <p class="mt-12 text-stone-500 uppercase tracking-widest text-xs font-bold animate-pulse">Sigue haciendo scroll para ver de lo que somos capaces ⬇</p>
    </div>

    <!-- Layer 3: Gold Section -->
    <div id="gold-section" class="absolute inset-0 bg-[#D4AF37] flex flex-col justify-center items-center text-black z-20 origin-center">
      <div class="flex flex-col items-center">
        <h2 class="huge-text font-cinzel gold-text-1">NUESTRO</h2>
        <h2 class="huge-text font-cinzel gold-text-2">CÓDIGO VENDE.</h2>
      </div>
    </div>

    <!-- Layer 2: Red Section -->
    <div id="red-section" class="absolute inset-0 bg-[#A84A2E] flex flex-col justify-center items-center text-white z-30 origin-center">
      <div class="absolute inset-0 opacity-20 mix-blend-multiply"><img src="assets/img/cocina.webp" class="w-full h-full object-cover"></div>
      <div class="flex flex-col items-center z-10">
        <h2 class="huge-text font-cinzel red-text-1">CADA PIXEL</h2>
        <h2 class="huge-text font-cinzel red-text-2 text-black">CUENTA.</h2>
      </div>
    </div>

    <!-- Layer 1: The Jigsaw Bento Hero -->
    <div id="hero-layer" class="absolute inset-0 bg-[#070605] z-40 p-4 pt-12 origin-center">
      <div id="hero-bento" class="w-full h-full max-w-7xl mx-auto relative origin-center">
        
        <!-- Top Left: Title, Thumb, Text, Buttons -->
        <div class="absolute top-0 left-0 w-[46%] h-[58%]">
          <div class="w-full h-full bg-[#120F0D] rounded-[2rem] shape-tl p-8 flex flex-col border border-white/10 shadow-2xl">
            <h1 class="text-4xl lg:text-6xl font-black text-white leading-none tracking-tighter mb-4">
              COTIZACIÓN WEB<br><span class="text-[#D4AF37]">CASA TRADICIÓN.</span>
            </h1>
            <div class="flex gap-4 mt-auto w-[85%] h-32">
              <div class="w-1/3 h-full bg-[#1F4D25] rounded-2xl flex items-center justify-center p-2 border border-white/5"><img src="assets/logo_casa_tradicion.png" class="w-full h-full object-contain"></div>
              <div class="w-2/3 flex flex-col justify-between h-full py-1">
                <div class="bg-black/50 border border-white/5 rounded-xl p-3"><p class="text-[10px] lg:text-xs font-bold text-stone-300">Desarrollo interactivo B2B.<br>Alto rendimiento y diseño inmersivo.</p></div>
                <div class="flex gap-2">
                  <div class="w-1/2 bg-[#A84A2E] rounded-xl flex items-center justify-center font-bold text-[10px] uppercase">Agencia</div>
                  <div class="w-1/2 bg-[#D4AF37] text-black rounded-xl flex items-center justify-center font-bold text-[10px] uppercase">Premium</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Top Right: Image -->
        <div class="absolute top-0 right-0 w-[53%] h-[68%]">
          <div class="w-full h-full bg-black rounded-[2rem] shape-tr relative border border-white/10">
            <img src="assets/img/hero-patacones.webp" class="w-full h-full object-cover opacity-80">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
            <div class="absolute top-6 left-16 text-white font-bold text-xs tracking-widest uppercase bg-black/80 px-4 py-2 rounded-full backdrop-blur-md">Dirección de Arte</div>
          </div>
        </div>

        <!-- Bottom Left: Image -->
        <div class="absolute bottom-0 left-0 w-[64%] h-[41%]">
          <div class="w-full h-full bg-black rounded-[2rem] shape-bl relative border border-white/10">
            <img src="assets/img/finca.webp" class="w-full h-full object-cover opacity-60">
            <div class="absolute bottom-6 left-8 text-[#D4AF37] font-bold text-xs tracking-widest uppercase bg-black/80 px-4 py-2 rounded-full">Animación Nivel Dios</div>
          </div>
        </div>

        <!-- Bottom Right: Product / Price -->
        <div class="absolute bottom-0 right-0 w-[35%] h-[31%]">
          <div class="w-full h-full bg-[#1A1613] rounded-[2rem] shape-br p-6 flex flex-col items-end justify-end relative border border-[#D4AF37]/30">
            <h3 class="text-white font-black text-2xl lg:text-4xl z-10">$2.5M COP</h3>
            <span class="text-[#D4AF37] text-xs font-bold uppercase tracking-widest z-10">Valor del Proyecto</span>
            <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-[#D4AF37]/20 blur-[40px] rounded-full"></div>
          </div>
        </div>

        <!-- Scroll Indicator (Center Gap) -->
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-50 animate-bounce">
          <span class="text-white font-bold text-[10px] uppercase tracking-widest bg-black/80 px-4 py-2 rounded-full border border-white/20">Scrollea</span>
        </div>

      </div>
    </div>
  </div>

  <!-- DEMOS DE CAPACIDAD -->
  <main class="bg-[#070605] relative z-0">
    <section class="py-32 px-4 sm:px-6 max-w-7xl mx-auto">
      <div class="text-center mb-24">
        <h2 class="text-4xl md:text-6xl font-black text-white font-cinzel text-[#D4AF37]">LO QUE SOMOS CAPACES DE HACER.</h2>
        <p class="text-stone-400 mt-4 text-xl">Mira estos módulos técnicos interactivos. Así es como elevaremos Casa Tradición.</p>
      </div>

      <!-- Demo 1: Showroom (Fixed Image bug) -->
      <div class="mb-32">
        <h3 class="text-3xl font-black text-white font-cinzel mb-2">1. Catálogo 3D Inmersivo</h3>
        <p class="text-stone-500 mb-8">No usamos listas aburridas. Mostramos el empaque y el plato servido en la misma interacción. Haz clic en las tarjetas.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" id="showroom-grid">
          <!-- JS Inject -->
        </div>
      </div>

      <!-- Demo 2: Referidos (Replaces Horeca Simulator) -->
      <div>
        <h3 class="text-3xl font-black text-white font-cinzel mb-2">2. Sistema de Referidos Exclusivo</h3>
        <p class="text-stone-500 mb-8">El crecimiento mutuo es clave. Si recomiendas nuestros servicios a otra empresa y cerramos contrato, desbloqueas beneficios permanentes en tu plataforma.</p>
        
        <div class="bg-[#120F0D] rounded-3xl p-8 border border-white/10 flex flex-col md:flex-row items-center gap-12">
          
          <div class="w-full md:w-1/2">
            <div class="flex items-center gap-2 bg-black p-1.5 rounded-full border border-white/5 w-max mb-8 mx-auto md:mx-0 shadow-lg">
              <button id="ref-btn-std" onclick="toggleReferral(false)" class="px-6 py-2 rounded-full text-xs font-bold bg-[#D4AF37] text-black transition-all">Estándar</button>
              <button id="ref-btn-ref" onclick="toggleReferral(true)" class="px-6 py-2 rounded-full text-xs font-bold text-stone-400 hover:text-white transition-all">Con Referido Activo</button>
            </div>

            <div class="space-y-4">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-full bg-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] font-bold">✓</div>
                <span class="text-sm font-bold text-white">Soporte Técnico 24/7</span>
              </div>
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-full bg-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] font-bold">✓</div>
                <span class="text-sm font-bold text-white">Actualizaciones de Seguridad</span>
              </div>
              <div id="ref-extra-feat" class="flex items-center gap-3 opacity-30 grayscale transition-all duration-500">
                <div class="w-8 h-8 rounded-full bg-[#10B981]/20 flex items-center justify-center text-[#10B981] font-bold text-lg leading-none">+</div>
                <span class="text-sm font-bold text-[#10B981]">Módulos Adicionales GRATIS</span>
              </div>
            </div>
          </div>

          <div class="w-full md:w-1/2 bg-black p-8 rounded-2xl text-center border border-[#D4AF37]/30 relative overflow-hidden shadow-2xl">
            <div class="absolute inset-0 bg-gradient-to-t from-[#D4AF37]/5 to-transparent"></div>
            <p class="text-xs text-stone-500 font-bold uppercase mb-4 relative z-10">Inversión Mensual de Mantenimiento</p>
            
            <div class="flex justify-center items-center gap-4 relative z-10 h-16">
              <h4 id="price-old" class="text-3xl font-black text-stone-600 line-through hidden transition-all">$150.000</h4>
              <h4 id="price-current" class="text-5xl lg:text-6xl font-black text-[#D4AF37] transition-all">$150.000</h4>
            </div>
            <p class="text-xs text-stone-400 mt-4 relative z-10 font-bold">COP / MES</p>
            
            <div id="ref-badge" class="absolute top-0 right-0 bg-[#10B981] text-black text-[10px] font-bold uppercase px-4 py-1 rounded-bl-xl hidden">50% DCTO APLICADO</div>
          </div>
          
        </div>
      </div>

    </section>
    
    <footer class="py-12 border-t border-white/10 text-center text-stone-500 text-xs">
      Propuesta de Desarrollo Web B2B para Casa Tradición. <br> $2.500.000 COP.
    </footer>
  </main>

  <script>
    // DEMO DATA (Catalog fixed structure)
    const demoData = [
      { name: 'Plátano Maduro Entero', cant: '3 unds', pack: 'assets/p/img-006.webp', dish: 'assets/p/img-007.webp' },
      { name: 'Tostón Jumbo 28cm', cant: '10 unds', pack: 'assets/p/img-035.webp', dish: 'assets/p/img-036.webp' },
      { name: 'Yuca Astilla', cant: '5kg', pack: 'assets/p/img-008.webp', dish: 'assets/p/img-009.webp' },
      { name: 'Patacón Verde Prelisto', cant: '2.5kg', pack: 'assets/p/img-017.webp', dish: 'assets/p/img-018.webp' }
    ];

    document.getElementById('showroom-grid').innerHTML = demoData.map(p => `
      <div class="bg-black p-4 flex flex-col group rounded-2xl border border-white/5">
        <div class="flip-card-3d rounded-xl aspect-[4/3] mb-4 cursor-pointer" onclick="this.classList.toggle('is-flipped')">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <img src="${p.dish}" loading="lazy">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
              <span class="absolute bottom-2 left-2 text-[10px] font-bold bg-black/80 text-white px-2 py-1 rounded">Plato Servido</span>
            </div>
            <div class="flip-card-back">
              <img src="${p.pack}" loading="lazy">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
              <span class="absolute bottom-2 left-2 text-[10px] font-bold bg-black/80 text-[#D4AF37] px-2 py-1 rounded">Empaque Vacío</span>
            </div>
          </div>
        </div>
        <h4 class="text-sm font-bold text-white mb-1">${p.name}</h4>
      </div>
    `).join('');

    // Referral System Logic
    function toggleReferral(isReferred) {
      const btnRef = document.getElementById('ref-btn-ref');
      const btnStd = document.getElementById('ref-btn-std');
      const oldPrice = document.getElementById('price-old');
      const curPrice = document.getElementById('price-current');
      const extraFeat = document.getElementById('ref-extra-feat');
      const badge = document.getElementById('ref-badge');

      if(isReferred) {
        btnStd.className = 'px-6 py-2 rounded-full text-xs font-bold text-stone-400 hover:text-white transition-all';
        btnRef.className = 'px-6 py-2 rounded-full text-xs font-bold bg-[#D4AF37] text-black transition-all shadow-[0_0_15px_rgba(212,175,55,0.4)]';
        oldPrice.classList.remove('hidden');
        curPrice.textContent = '$75.000';
        curPrice.classList.remove('text-[#D4AF37]');
        curPrice.classList.add('text-[#10B981]');
        extraFeat.classList.remove('opacity-30', 'grayscale');
        badge.classList.remove('hidden');
      } else {
        btnRef.className = 'px-6 py-2 rounded-full text-xs font-bold text-stone-400 hover:text-white transition-all';
        btnStd.className = 'px-6 py-2 rounded-full text-xs font-bold bg-[#D4AF37] text-black transition-all';
        oldPrice.classList.add('hidden');
        curPrice.textContent = '$150.000';
        curPrice.classList.remove('text-[#10B981]');
        curPrice.classList.add('text-[#D4AF37]');
        extraFeat.classList.add('opacity-30', 'grayscale');
        badge.classList.add('hidden');
      }
    }

    // GSAP Z-AXIS ABSORB ANIMATION (BLEACH STYLE)
    document.addEventListener("DOMContentLoaded", () => {
      gsap.registerPlugin(ScrollTrigger);

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: "#z-sequence",
          start: "top top",
          end: "+=400%",
          scrub: 1,
          pin: true
        }
      });

      // 1. HERO ABSORB - SMOOTH TRANSITION
      // Scale hero out. While it scales, we also slowly fade the layer wrapper, creating a smooth dissolve into Red.
      tl.to("#hero-bento", { scale: 35, opacity: 0, duration: 2.5, ease: "power2.inOut" }, 0)
        .to("#hero-layer", { opacity: 0, duration: 1.5, ease: "power2.inOut" }, 0.5);

      // 2. RED SECTION (CADA PIXEL CUENTA)
      // Text flows in smoothly as the hero finishes zooming
      tl.from(".red-text-1", { y: -100, opacity: 0, duration: 1, ease: "power2.out" }, 1)
        .from(".red-text-2", { y: 100, opacity: 0, duration: 1, ease: "power2.out" }, 1);
      // Red section plunges
      tl.to("#red-section", { scale: 25, opacity: 0, duration: 2.5, ease: "power2.inOut" }, "+=0.5");

      // 3. GOLD SECTION (NUESTRO CÓDIGO VENDE)
      tl.from(".gold-text-1", { x: -150, opacity: 0, duration: 1, ease: "power2.out" }, "-=1.5")
        .from(".gold-text-2", { x: 150, opacity: 0, duration: 1, ease: "power2.out" }, "<");
      tl.to("#gold-section", { scale: 25, opacity: 0, duration: 2.5, ease: "power2.inOut" }, "+=0.5");

      // 4. BLACK SECTION (THE PRICE)
      tl.to("#black-section", { opacity: 1, scale: 1, duration: 1.5, ease: "power2.out" }, "-=1.5");
    });
  </script>
</body>
</html>
"""
with open("index.html", "w") as f:
    f.write(html)
