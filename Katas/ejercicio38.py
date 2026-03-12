# 38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
#     - Reglas:
#         - 0 - 69: insuficiente
#         - 70 - 79: bien
#         - 80 - 89: muy bien
#         - 90 - 100: excelente

# Declaración de variables
notaNumerica = int(input(f"Introduce la nota numérica obtenida: "))

# Control de la relación entre notas
if notaNumerica >= 90 and notaNumerica <= 100:
    print("Excelente")
elif notaNumerica >= 80 and notaNumerica <= 89:
    print("Muy Bien")
elif notaNumerica >= 70 and notaNumerica <= 79:
    print("Bien")
elif notaNumerica >= 0 and notaNumerica <= 69:
    print("Insuficiente")
else:
    print("Nota No Válida")