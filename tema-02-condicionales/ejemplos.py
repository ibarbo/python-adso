# =============================================================
# Tema 02 · Condicionales y menú con while · EJEMPLOS
# python-adso · SENA ADSO
#
# Cómo usar este archivo:
#   1. Léelo de arriba a abajo. Cada línea con # es una explicación.
#   2. Ejecútalo:  python ejemplos.py
#   3. Cambia algo en cada ejemplo y vuelve a ejecutarlo.
# =============================================================


# -------------------------------------------------------------
# EJEMPLO 1 · if: hacer algo solo si se cumple una condición
# -------------------------------------------------------------
# if significa "si". Después va una condición y dos puntos :
# Lo que está debajo, con sangría (4 espacios), solo se ejecuta
# si la condición es verdadera (True).

print("=== EJEMPLO 1: if ===")
saldo = 50000
precio = 32000

if saldo >= precio:
    print("Compra aprobada")
    print(f"Te quedan ${saldo - precio:,.0f}")

print("Esta línea siempre se ejecuta: no tiene sangría")
print()


# -------------------------------------------------------------
# EJEMPLO 2 · if / else: uno de dos caminos
# -------------------------------------------------------------
# else significa "si no". Se ejecuta cuando la condición es falsa.

print("=== EJEMPLO 2: if / else ===")
edad = 16

if edad >= 18:
    print("Puedes registrarte solo")
else:
    print("Necesitas la autorización de un adulto")
print()


# -------------------------------------------------------------
# EJEMPLO 3 · Las comparaciones
# -------------------------------------------------------------
#   ==   igual a              !=   distinto de
#   >    mayor que            <    menor que
#   >=   mayor o igual        <=   menor o igual
#
# OJO: un solo = guarda un valor; dos == comparan.

print("=== EJEMPLO 3: comparaciones ===")
clave_guardada = "sena2026"
clave_escrita = "sena2026"

print(clave_escrita == clave_guardada)   # True
print(5 > 8)                             # False
print("Ana" != "Ana")                    # False
print()


# -------------------------------------------------------------
# EJEMPLO 4 · elif: más de dos caminos
# -------------------------------------------------------------
# elif significa "si no, si...". Python revisa de arriba a abajo
# y entra SOLO en el primer caso que se cumple.

print("=== EJEMPLO 4: elif ===")
total_compra = 120000

if total_compra >= 200000:
    envio = 0
elif total_compra >= 100000:
    envio = 5000
else:
    envio = 12000

print(f"Compra: ${total_compra:,.0f}  ·  Envío: ${envio:,.0f}")
print()


# -------------------------------------------------------------
# EJEMPLO 5 · and / or: unir condiciones
# -------------------------------------------------------------
#   and → se deben cumplir LAS DOS
#   or  → basta con que se cumpla UNA

print("=== EJEMPLO 5: and / or ===")
hora = 14
dia = "domingo"

if hora >= 8 and hora < 18:
    print("La barbería está en horario de atención")

if dia == "sábado" or dia == "domingo":
    print("Hoy es fin de semana: el corte tiene recargo")
print()


# -------------------------------------------------------------
# EJEMPLO 6 · while: un menú que se repite
# -------------------------------------------------------------
# while significa "mientras". Repite lo que tiene debajo mientras
# la condición sea verdadera. Así funcionan los menús de las apps:
# se muestran una y otra vez hasta que el usuario elige "Salir".
#
# Este ejemplo junta todo: input(), if, elif, else y while.
# Es el préstamo del tema 01, ahora con menú y validaciones.

print("=== EJEMPLO 6: menú con while ===")
continuar = True

while continuar:
    print()
    print("--- PRÉSTAMOS ENTRE AMIGOS ---")
    print("1. Calcular un préstamo")
    print("2. Ver las reglas")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("¿Cuánto vas a prestar? "))
        cuotas = int(input("¿En cuántas cuotas? "))

        if monto <= 0 or cuotas <= 0:
            print("El monto y las cuotas deben ser mayores que cero.")
        elif cuotas > 12:
            print("Máximo 12 cuotas entre amigos.")
        else:
            print(f"Valor de cada cuota: ${monto / cuotas:,.0f}")

    elif opcion == "2":
        print("Reglas: monto mayor que cero y máximo 12 cuotas.")

    elif opcion == "3":
        print("¡Hasta luego!")
        continuar = False   # al ser False, el while se detiene

    else:
        print("Opción no válida. Escribe 1, 2 o 3.")


# =============================================================
# RETO RÁPIDO (no se entrega)
# Agrega al ejemplo 6 una opción "4. Préstamo con interés" que
# pregunte el interés en % y muestre el total a pagar.
# Pista: lo hiciste en el reto del tema 01.
# =============================================================
