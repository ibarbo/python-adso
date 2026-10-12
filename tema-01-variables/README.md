# Tema 01 · Variables, tipos, entrada y salida

**Lo que tu app aprende hoy:** saludar, preguntar datos y responder con ellos.

## Lo que vas a aprender

| Concepto | Para qué sirve | Ejemplo |
|---|---|---|
| `print()` | Mostrar algo en pantalla | `print("Hola")` |
| Variable | Guardar un dato con un nombre | `nombre = "Ana"` |
| Tipos de dato | Saber si es texto, número entero o decimal | `"Ana"`, `25`, `3.5` |
| `input()` | Preguntarle algo al usuario | `nombre = input("¿Cómo te llamas? ")` |
| `int()` y `float()` | Convertir texto en número para hacer cuentas | `edad = int(input("Edad: "))` |
| f-strings | Mezclar texto y variables al mostrar | `print(f"Hola, {nombre}")` |

## Cómo trabajar

1. **Abre `ejemplos.py`.** Lee los comentarios y ejecuta el archivo. Son 6 ejemplos cortos, cada uno sobre un caso real.
2. **Cambia algo en cada ejemplo** y vuelve a ejecutarlo. Así se aprende: experimentando.
3. **Abre `ejercicios.py`.** Copia el archivo a tu repositorio como `ejercicios/tema-01.py` y resuelve los ejercicios ahí.
4. **Haz el ejercicio "Llévalo a tu app"** en el `app.py` de tu proyecto.

## Qué entregas

En el repositorio de tu app:
- `ejercicios/tema-01.py` con los ejercicios 1 a 5 resueltos.
- `app.py` con la pantalla de bienvenida de tu app (ejercicio 6).
- Subido a GitHub con un commit: `feat: tema 01 y bienvenida de la app`.

En Classroom: el enlace de ese commit.

## Cómo se califica

| Criterio | Puntos |
|---|---|
| Los ejercicios 1 a 5 funcionan | 5 |
| La bienvenida de tu app funciona y usa `input()`, variables y f-strings | 3 |
| Todo está en GitHub con un commit claro | 2 |
| **Total** | **10** |

## Errores comunes

| Error | Qué pasó | Cómo se arregla |
|---|---|---|
| `TypeError: can only concatenate str (not "int") to str` | Intentaste sumar texto con un número | Usa f-strings: `f"Tienes {edad} años"` |
| `ValueError: invalid literal for int()` | Escribiste letras donde el programa esperaba un número | Escribe solo números, o revisa que usaste `int()` en el `input()` correcto |
| `NameError: name 'nombre' is not defined` | Usaste una variable antes de crearla, o la escribiste distinto | Revisa que el nombre sea exactamente igual, con mayúsculas y minúsculas |
| La suma da `"55"` en vez de `10` | `input()` siempre devuelve texto | Convierte con `int()` o `float()` antes de sumar |
