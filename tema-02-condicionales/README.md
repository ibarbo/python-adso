# Tema 02 · Condicionales y menú con while

**Lo que tu app aprende hoy:** tomar decisiones y mostrar un menú que se repite, como una app de verdad.

## Lo que vas a aprender

| Concepto | Para qué sirve | Ejemplo |
|---|---|---|
| `if` | Hacer algo solo si se cumple una condición | `if saldo >= precio:` |
| `else` | El otro camino, si no se cumple | `else:` |
| `elif` | Más de dos caminos | `elif total >= 100000:` |
| Comparaciones | Comparar valores | `==` `!=` `>` `<` `>=` `<=` |
| `and` / `or` | Unir condiciones | `if hora >= 8 and hora < 19:` |
| `while` | Repetir mientras se cumpla algo: el menú | `while continuar:` |

**La sangría importa.** Lo que va "dentro" de un `if` o de un `while` se escribe 4 espacios más adentro. VS Code lo hace solo al presionar Enter después de los dos puntos `:`.

## Cómo trabajar

1. **Abre `ejemplos.py`.** Lee los comentarios y ejecuta el archivo. El ejemplo 6 es un menú completo: juega con él.
2. **Cambia algo en cada ejemplo** y vuelve a ejecutarlo.
3. **Abre `ejercicios.py`.** Cópialo a tu repositorio `practicas-python` como `tema-02.py` y resuelve los ejercicios ahí.
4. **Haz el ejercicio "Llévalo a tu app"** en el `src/app.py` de tu app.

## Qué entregas

| Repositorio | Archivo | Commit |
|---|---|---|
| `practicas-python` | `tema-02.py` con los ejercicios 1 a 5 | `feat: ejercicios del tema 02` |
| Tu app | `src/app.py` con el menú (ejercicio 6) | `feat: agrega menú principal` |

En Classroom: el enlace de los **dos commits**.

## Cómo se califica

| Criterio | Puntos |
|---|---|
| Los ejercicios 1 a 5 funcionan | 5 |
| El menú de tu app funciona: 3 opciones, "Salir", una validación con `if` | 3 |
| Los dos commits están en GitHub con mensajes claros | 2 |
| **Total** | **10** |

## Errores comunes

| Error | Qué pasó | Cómo se arregla |
|---|---|---|
| `SyntaxError: expected ':'` | Falta el `:` al final del `if`, `elif`, `else` o `while` | Agrega los dos puntos |
| `IndentationError` | La sangría está mal: falta, sobra o mezclaste espacios y tabulaciones | Lo de adentro va 4 espacios más a la derecha, siempre igual |
| `SyntaxError` en `if x = 5` | Usaste un `=` para comparar | Para comparar se usan dos: `==` |
| El menú nunca termina | La variable del `while` nunca cambia a `False` | En la opción "Salir", pon `continuar = False` |
| La opción `1` nunca entra | Comparaste con un número: `opcion == 1` | `input()` devuelve texto: compara con `"1"` |
