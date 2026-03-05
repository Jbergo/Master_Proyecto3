# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

try:
    num1 = float(input(f"Introduce el primer número: "))
    num2 = float(input(f"Introduce el segundo número: "))

    print(f"El resultado es: {num1/num2}")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Valor no numérico")