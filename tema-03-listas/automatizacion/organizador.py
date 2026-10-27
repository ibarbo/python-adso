# =============================================================
# organizador.py
# Ordena la carpeta Descargas_prueba: cada archivo va a una
# carpeta según su tipo (Imagenes, PDFs, Musica, Documentos...).
#
# Antes de ejecutarlo, crea el desorden con: python crear_desorden.py
# =============================================================

# --- Herramientas que Python ya trae (no hay que instalar nada) ---
import os        # para ver los archivos de una carpeta
import shutil    # para mover archivos de un lugar a otro
import time      # para medir cuánto se demora

inicio = time.time()   # guardamos la hora en que empieza

# --- 1. ¿Qué carpeta vamos a ordenar? ---
carpeta_base = os.path.dirname(os.path.abspath(__file__))
descargas = os.path.join(carpeta_base, "Descargas_prueba")

# --- 2. LISTAS: qué extensiones van en cada carpeta ---
imagenes = [".jpg", ".png", ".gif"]
pdfs = [".pdf"]
musica = [".mp3", ".wav"]
videos = [".mp4"]
documentos = [".docx", ".xlsx", ".txt"]

# --- 3. Una LISTA con todos los archivos de la carpeta ---
archivos = os.listdir(descargas)

movidos = 0   # contador: cuántos archivos movimos

# --- 4. El FOR: recorre la lista, un archivo a la vez ---
for archivo in archivos:
    ruta = os.path.join(descargas, archivo)

    # Si es una carpeta (no un archivo), la saltamos
    if os.path.isdir(ruta):
        continue

    # Sacamos la extensión: "foto_playa.jpg" -> ".jpg"
    extension = os.path.splitext(archivo)[1].lower()

    # --- 5. El IF: decide a qué carpeta va, según la extensión ---
    if extension in imagenes:
        destino = "Imagenes"
    elif extension in pdfs:
        destino = "PDFs"
    elif extension in musica:
        destino = "Musica"
    elif extension in videos:
        destino = "Videos"
    elif extension in documentos:
        destino = "Documentos"
    else:
        destino = "Otros"

    # --- 6. Crear la carpeta destino (si no existe) y mover el archivo ---
    carpeta_destino = os.path.join(descargas, destino)
    os.makedirs(carpeta_destino, exist_ok=True)
    shutil.move(ruta, os.path.join(carpeta_destino, archivo))

    print(f"{archivo:<28} -> {destino}")
    movidos = movidos + 1

# --- 7. El resumen ---
segundos = time.time() - inicio
print()
print(f"LISTO: {movidos} archivos organizados en {segundos:.2f} segundos")
