# Tema 03 · Listas y ciclo for

**Lo que tu app aprende hoy:** guardar varios registros y recorrerlos uno por uno.

## Lo que vas a aprender

| Concepto | Para qué sirve | Ejemplo |
|---|---|---|
| Lista | Guardar varias cosas en una sola variable | `frutas = ["mango", "lulo"]` |
| Posición | Sacar un elemento. **La primera es la 0** | `frutas[0]` |
| `len()` | Contar cuántos elementos hay | `len(frutas)` |
| `.append()` | Agregar al final | `frutas.append("fresa")` |
| `for` | Recorrer la lista, uno a la vez | `for fruta in frutas:` |
| `range()` | Repetir un número de veces | `for i in range(5):` |
| `in` | Preguntar si algo está en la lista | `if "lulo" in frutas:` |
| `sum()` | Sumar una lista de números | `sum(precios)` |
| **Bonus:** list comprehension | Un `for` en una sola línea | `[p * 1.19 for p in precios]` |

## Cómo trabajar

1. **Abre `ejemplos.py`.** Lee los comentarios y ejecuta el archivo.
2. **Cambia algo en cada ejemplo** y vuelve a ejecutarlo.
3. **Abre `ejercicios.py`.** Cópialo a tu repositorio `practicas-python` como `tema-03.py`. Van de fácil a difícil: 🥉 bronce, 🥈 plata y 🥇 oro.
4. **Haz el ejercicio "Llévalo a tu app"** en el `src/app.py` de tu app.

## La automatización de la clase

En la carpeta `automatizacion/` está el programa que ordenó la carpeta de Descargas. Pruébalo en tu computador:

```bash
cd automatizacion
python crear_desorden.py     # crea la carpeta Descargas_prueba con 40 archivos revueltos
python organizador.py        # los ordena en carpetas según su tipo
```

Abre `organizador.py`: cada línea está explicada. Vas a reconocer la **lista**, el **for** y el **if**.

**Bonus:** `rutina_manana.py` abre de golpe las páginas que usas todos los días. Cámbialas por las tuyas.

## Qué entregas

| Repositorio | Archivo | Commit |
|---|---|---|
| `practicas-python` | `tema-03.py` con los ejercicios 1 a 6 | `feat: ejercicios del tema 03` |
| Tu app | `src/app.py` con la lista de registros (ejercicio 7) | `feat: guarda registros en una lista` |

En Classroom: el enlace de los **dos commits**.

## Cómo se califica

| Criterio | Puntos |
|---|---|
| Bronce y plata (ejercicios 1 a 5) funcionan | 4 |
| Oro: la mini tienda funciona | 2 |
| Tu app guarda y muestra registros con una lista | 2 |
| Los dos commits están en GitHub con mensajes claros | 2 |
| **Total** | **10** |

## Errores comunes

| Error | Qué pasó | Cómo se arregla |
|---|---|---|
| `IndexError: list index out of range` | Pediste una posición que no existe. En una lista de 3, la última es la `2` | Empieza a contar desde 0, o usa `lista[-1]` para la última |
| `SyntaxError: expected ':'` | Falta el `:` al final del `for` | Agrega los dos puntos |
| `IndentationError` | Lo que se repite no tiene sangría | Lo de adentro del `for` va 4 espacios más a la derecha |
| El total siempre da el último número | Pusiste `total = 0` **dentro** del `for` y se reinicia en cada vuelta | Ponlo **antes** del `for` |
| `range(10)` no llega al 10 | `range` no incluye el número final | Para llegar al 10 usa `range(1, 11)` |
| `TypeError` al sumar | La lista tiene textos, no números (por ejemplo, de un `input()`) | Convierte antes de agregar: `precios.append(int(precio))` |
