import re

with open("index.html", "r") as f:
    html = f.read()

# Replace the entire demoData map logic to ensure it is pristine
new_map = """document.getElementById('showroom-grid').innerHTML = demoData.map((p, idx) => `
      <div class="bg-black p-4 flex flex-col group rounded-2xl border border-white/5 relative" id="card-${idx}">
        <div class="flip-card-3d rounded-xl aspect-[4/3] mb-4 cursor-pointer" onclick="openProductModal(${idx}, this)">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <img src="${p.dish}" loading="lazy">
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
              <span class="absolute bottom-2 left-2 text-[10px] font-bold bg-black/80 text-[#D4AF37] px-2 py-1 rounded">Plato Servido</span>
              <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/40">
                <span class="bg-[#D4AF37] text-black text-[10px] font-black uppercase px-4 py-2 rounded-full shadow-lg flex items-center gap-1">
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/><path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/></svg> Ver Interacción
                </span>
              </div>
            </div>
            <div class="flip-card-back">
              <img src="${p.pack}" loading="lazy">
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
              <span class="absolute bottom-2 left-2 text-[10px] font-bold bg-black/80 text-[#D4AF37] px-2 py-1 rounded">Empaque Vacío</span>
            </div>
          </div>
        </div>
        <h4 class="text-sm font-bold text-white mb-1">${p.name}</h4>
      </div>
    `).join('');"""

# Using regex to replace whatever is there between document.getElementById and .join('');
pattern = re.compile(r"document\.getElementById\('showroom-grid'\)\.innerHTML = demoData\.map.*?\.join\(''\);", re.DOTALL)
html = pattern.sub(new_map, html)

with open("index.html", "w") as f:
    f.write(html)

