# python-adso

Python para construir tu propia aplicación, un tema a la vez.

**SENA · Análisis y Desarrollo de Software · Instructor Víctor**

## Cómo funciona

Cada carpeta es un tema. Cada tema tiene tres archivos:

| Archivo | Para qué |
|---|---|
| `README.md` | Qué vas a aprender y qué entregas |
| `ejemplos.py` | Ejemplos explicados línea por línea. Léelos, ejecútalos y cámbialos |
| `ejercicios.py` | Los ejercicios que entregas. Cada uno dice exactamente qué debe hacer |

Cada tema termina con un ejercicio especial: **"Llévalo a tu app"**. Ahí usas lo que aprendiste en la aplicación de consola que estás construyendo.

## Temas

| # | Tema | Lo que tu app aprende a hacer |
|---|---|---|
| 01 | [Variables, tipos, entrada y salida](tema-01-variables/) | Saludar, preguntar datos y responder |
| 02 | [Condicionales y menú con while](tema-02-condicionales/) | Tomar decisiones y mostrar un menú |
| 03 | [Listas y ciclo for](tema-03-listas/) | Guardar varios registros y recorrerlos |
| 04 | *Próximamente* | |

## Cómo ejecutar un archivo

En la terminal, dentro de la carpeta del tema:

```bash
python ejemplos.py
```

Si `python` no funciona, prueba con `py ejemplos.py` (Windows) o `python3 ejemplos.py` (Mac o Linux).

**¿No tienes Python en tu computador?** Puedes usar un editor en línea, como [programiz.com/python-programming/online-compiler](https://www.programiz.com/python-programming/online-compiler/): copias el código, lo pegas y das clic en *Run*.

## Tus tres carpetas

```
📁 ADSO
   ├── 📁 python-adso         → este material. Solo lees, ejecutas y haces git pull
   ├── 📁 practicas-python    → TU repositorio de ejercicios: tema-01.py, tema-02.py...
   └── 📁 nombre-de-tu-app    → TU app: README, .gitignore, docs/ y src/app.py
```

- Los **ejercicios** van en `practicas-python`.
- El ejercicio **"Llévalo a tu app"** va en el repositorio de tu app.
- Nunca entregas nada en `python-adso`.

## Cómo traer un tema nuevo

```bash
cd python-adso
git branch     # debe mostrar: * main
git pull       # trae lo nuevo que se publicó en GitHub
```

## La regla de la IA

La IA es tu copiloto, no tu piloto. Puedes usarla para entender un error o una línea que no entiendes. Lo que entregas lo tienes que poder explicar línea por línea.
