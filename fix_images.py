with open("index.html", "r") as f:
    html = f.read()

# Fix the bug where both front and back had p.pack
old_grid_code = """<div class="flip-card-front"><img src="${p.pack}"><div class="absolute inset-0 bg-black/40"></div><span class="absolute bottom-2 left-2 text-[10px] font-bold bg-[#D4AF37] text-black px-2 py-1 rounded shadow-lg">Click para 3D</span></div>
            <div class="flip-card-back"><img src="${p.pack}"></div>"""

new_grid_code = """<div class="flip-card-front"><img src="${p.dish}"><div class="absolute inset-0 bg-black/40"></div><span class="absolute bottom-2 left-2 text-[10px] font-bold bg-[#D4AF37] text-black px-2 py-1 rounded shadow-lg">Click para 3D (Ver Empaque)</span></div>
            <div class="flip-card-back"><img src="${p.pack}"></div>"""

html = html.replace(old_grid_code, new_grid_code)

with open("index.html", "w") as f:
    f.write(html)
