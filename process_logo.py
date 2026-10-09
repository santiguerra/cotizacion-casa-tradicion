from PIL import Image

# Cargar la imagen proporcionada por el usuario
img_path = "/Users/santiagoguerra/.gemini/antigravity/brain/cb889b04-1d29-41de-8c7a-23388fa885e8/.user_uploaded/media_1791519550853.png"
try:
    img = Image.open(img_path)
    img = img.convert("RGBA")

    datas = img.getdata()
    newData = []
    
    # Azul Navy (Hex: #0F172A / RGB: 15, 23, 42) o un Navy clásico (#1E3A8A / RGB: 30, 58, 138)
    # Usaremos el Navy clásico para que contraste bien con el fondo blanco/gris claro del PDF.
    navy_r, navy_g, navy_b = 30, 58, 138

    for item in datas:
        # El logo original es fondo negro (r,g,b < 50) y letras blancas (r,g,b > 200)
        # Vamos a remover el negro (convertir a transparente)
        # Y vamos a colorear el blanco a Azul Navy.
        if item[0] < 50 and item[1] < 50 and item[2] < 50:
            newData.append((255, 255, 255, 0)) # Transparente
        else:
            # Usamos el canal rojo original como el nivel de "blanco" (alpha / antialiasing)
            # Para que los bordes difuminados se vean bien.
            alpha = max(item[0], item[1], item[2])
            newData.append((navy_r, navy_g, navy_b, alpha))

    img.putdata(newData)
    img.save("metalevel_logo_navy.png", "PNG")
    print("Logo procesado correctamente.")
except Exception as e:
    print("Error procesando logo:", e)

