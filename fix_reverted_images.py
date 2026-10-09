with open("index.html", "r") as f:
    html = f.read()

# Fix the bug where both front and back had p.pack
old_grid_code = """<div class="flip-card-front">
              <img src="${p.pack}" loading="lazy">
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
              <span class="absolute bottom-2 left-2 text-[10px] font-bold bg-black/80 text-[#D4AF37] px-2 py-1 rounded">Empaque Vacío</span>
              <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/40">
                <span class="bg-[#D4AF37] text-black text-[10px] font-black uppercase px-4 py-2 rounded-full shadow-lg flex items-center gap-1">
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/><path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/></svg> Ver Interacción
                </span>
              </div>
            </div>
            <div class="flip-card-back">
              <img src="${p.pack}" loading="lazy">"""

new_grid_code = """<div class="flip-card-front">
              <img src="${p.dish}" loading="lazy">
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
              <span class="absolute bottom-2 left-2 text-[10px] font-bold bg-[#D4AF37] text-black px-2 py-1 rounded shadow-lg">Plato Servido</span>
              <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/40">
                <span class="bg-[#D4AF37] text-black text-[10px] font-black uppercase px-4 py-2 rounded-full shadow-lg flex items-center gap-1">
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/><path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/></svg> Ver Interacción
                </span>
              </div>
            </div>
            <div class="flip-card-back">
              <img src="${p.pack}" loading="lazy">"""

if old_grid_code in html:
    html = html.replace(old_grid_code, new_grid_code)
else:
    print("WARNING: Could not find exact string to replace. Trying regex...")
    import re
    # Just replace the image logic generically in JS
    html = re.sub(r'<div class="flip-card-front">\s*<img src="\$\{p\.pack\}"', r'<div class="flip-card-front">\n              <img src="${p.dish}"', html)
    html = re.sub(r'Empaque Vacío</span>', r'Plato Servido</span>', html, count=1)

with open("index.html", "w") as f:
    f.write(html)
