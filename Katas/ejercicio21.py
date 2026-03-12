# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

# Importación de la librería
import math

# Creación de la función lambda
calculoCubo = lambda num: math.pow(num, 3)

# Ejecución
print(calculoCubo(int(input(f"Introduce el número a calcular: "))))