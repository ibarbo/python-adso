# =============================================================
# rutina_manana.py
# Abre de golpe las páginas que usas todos los días.
# Cámbialas por las tuyas.
# =============================================================

import webbrowser   # la herramienta de Python que abre el navegador

# Una LISTA con las páginas
paginas = [
    "https://classroom.google.com",
    "https://github.com",
    "https://mail.google.com",
    "https://www.youtube.com",
]

# El FOR abre cada página en una pestaña nueva
for pagina in paginas:
    webbrowser.open(pagina)

print(f"Abrí {len(paginas)} páginas. ¡Buen día!")
