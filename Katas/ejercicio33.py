# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# Creación de la función
sumatorio = lambda lista1, lista2: list(map(lambda element1, element2: element1 + element2, lista1, lista2))

# Ejecución
print(sumatorio([1, 2, 3],[4, 5, 6]))