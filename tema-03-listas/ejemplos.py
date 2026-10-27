# =============================================================
# Tema 03 · Listas y ciclo for · EJEMPLOS
# python-adso · SENA ADSO
#
# Cómo usar este archivo:
#   1. Léelo de arriba a abajo. Cada línea con # es una explicación.
#   2. Ejecútalo:  python ejemplos.py
#   3. Cambia algo en cada ejemplo y vuelve a ejecutarlo.
# =============================================================


# -------------------------------------------------------------
# EJEMPLO 1 · Una lista: varias cosas en una sola variable
# -------------------------------------------------------------
# Una lista va entre corchetes [ ] y sus elementos se separan
# con comas. Es como una fila de cajitas numeradas.
# OJO: la primera cajita es la 0, no la 1.

print("=== EJEMPLO 1: listas y posiciones ===")
frutas = ["mango", "banano", "fresa", "lulo"]
#  posición:   0         1        2       3

print(frutas)        # toda la lista
print(frutas[0])     # mango   -> la primera
print(frutas[2])     # fresa
print(frutas[-1])    # lulo    -> -1 es la última
print()


# -------------------------------------------------------------
# EJEMPLO 2 · len y append: contar y agregar
# -------------------------------------------------------------
# len(lista)          dice cuántos elementos tiene
# lista.append(algo)  agrega algo al final

print("=== EJEMPLO 2: len y append ===")
compras = ["arroz", "huevos"]
print(f"Tengo {len(compras)} cosas en la lista")

compras.append("leche")
compras.append("café")
print(compras)
print(f"Ahora tengo {len(compras)}")
print()


# -------------------------------------------------------------
# EJEMPLO 3 · for: recorrer la lista, una cosa a la vez
# -------------------------------------------------------------
# Se lee: "por cada fruta en la lista frutas, haz esto".
# La variable fruta toma un valor distinto en cada vuelta.
# Lo que se repite va con sangría (4 espacios), como en el if.

print("=== EJEMPLO 3: for ===")
for fruta in frutas:
    print(f"Hoy compro {fruta}")

print("Esta línea va una sola vez: no tiene sangría")
print()


# -------------------------------------------------------------
# EJEMPLO 4 · for con acumulador: sumar todo
# -------------------------------------------------------------
# Creamos total = 0 ANTES del for, y en cada vuelta le sumamos.

print("=== EJEMPLO 4: sumar con for ===")
precios = [4500, 2000, 12000, 3500]
total = 0

for precio in precios:
    total = total + precio
    print(f"Sumo ${precio:,} -> llevo ${total:,}")

print(f"Total: ${total:,}")
print(f"Con sum() da lo mismo: ${sum(precios):,}")
print()


# -------------------------------------------------------------
# EJEMPLO 5 · range: repetir un número de veces
# -------------------------------------------------------------
# range(5)      -> 0, 1, 2, 3, 4   (empieza en 0, el 5 NO entra)
# range(1, 6)   -> 1, 2, 3, 4, 5

print("=== EJEMPLO 5: range ===")
for i in range(5):
    print(f"Vuelta {i}")

for numero in range(1, 4):
    print(f"Turno número {numero}")
print()


# -------------------------------------------------------------
# EJEMPLO 6 · in: ¿está en la lista?
# -------------------------------------------------------------
# algo in lista  ->  True si está, False si no.

print("=== EJEMPLO 6: in ===")
inscritos = ["ana", "luis", "sara"]
nombre = "luis"

if nombre in inscritos:
    print(f"{nombre} sí está en la lista")
else:
    print(f"{nombre} no está en la lista")
print()


# -------------------------------------------------------------
# EJEMPLO 7 · for + if: filtrar
# -------------------------------------------------------------
# Recorremos la lista y solo mostramos lo que cumple la condición.

print("=== EJEMPLO 7: for + if ===")
notas = [4.5, 2.8, 3.9, 2.1, 5.0]
aprobadas = 0

for nota in notas:
    if nota >= 3.0:
        print(f"{nota} -> aprobó")
        aprobadas = aprobadas + 1
    else:
        print(f"{nota} -> no aprobó")

print(f"Aprobaron {aprobadas} de {len(notas)}")
print()


# -------------------------------------------------------------
# EJEMPLO 8 · BONUS: list comprehension, un for en una línea
# -------------------------------------------------------------
# [lo_que_quiero for elemento in lista]
# Crea una lista nueva a partir de otra.

print("=== EJEMPLO 8: list comprehension ===")
precios = [1000, 2000, 3000]

# Con for normal (4 líneas):
con_iva = []
for p in precios:
    con_iva.append(p * 1.19)
print(con_iva)

# Con comprehension (1 línea, mismo resultado):
con_iva = [p * 1.19 for p in precios]
print(con_iva)

# También puede filtrar con if:
altas = [n for n in notas if n >= 4.0]
print(f"Notas de 4 o más: {altas}")
