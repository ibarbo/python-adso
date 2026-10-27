# =============================================================
# crear_desorden.py
# Crea la carpeta Descargas_prueba llena de archivos revueltos,
# como la carpeta de Descargas de cualquier persona.
#
# Ejecútalo cada vez que quieras volver a desordenar la carpeta
# para probar organizador.py otra vez.
# =============================================================

import os
import shutil

# La carpeta se crea al lado de este archivo
carpeta_base = os.path.dirname(os.path.abspath(__file__))
descargas = os.path.join(carpeta_base, "Descargas_prueba")

# Si ya existe, la borramos para empezar desde cero
if os.path.exists(descargas):
    shutil.rmtree(descargas)
os.mkdir(descargas)

# La lista de archivos "descargados"
archivos = [
    "foto_playa.jpg", "selfie_cumple.png", "meme_gato.jpg", "fondo_pantalla.png",
    "foto_carnet.jpg", "captura_whatsapp.png", "paisaje_guatape.jpg", "logo_app.png",
    "cedula_escaneada.pdf", "certificado_sena.pdf", "factura_epm.pdf", "extracto_banco.pdf",
    "guia_python.pdf", "recibo_arriendo.pdf", "pasaje_bus.pdf", "manual_celular.pdf",
    "cancion_favorita.mp3", "podcast_tecnologia.mp3", "nota_de_voz.mp3", "salsa_clasica.mp3",
    "reggaeton_2026.mp3", "audio_clase.mp3",
    "hoja_de_vida.docx", "carta_presentacion.docx", "trabajo_final.docx", "acta_reunion.docx",
    "presupuesto_mes.xlsx", "notas_trimestre.xlsx", "inventario_tienda.xlsx", "lista_mercado.txt",
    "apuntes_clase.txt", "contrasenas_NO_ABRIR.txt",
    "video_graduacion.mp4", "tutorial_git.mp4", "baile_tiktok.mp4", "clase_grabada.mp4",
    "instalador_python.exe", "juego_viejo.exe", "proyecto_comprimido.zip", "fotos_viaje.zip",
]

for nombre in archivos:
    ruta = os.path.join(descargas, nombre)
    with open(ruta, "w") as archivo:
        archivo.write("Archivo de prueba")

print(f"Listo: {len(archivos)} archivos revueltos en Descargas_prueba")
