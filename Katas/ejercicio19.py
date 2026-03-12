# 19. Crea una función lambda que filtre los números impares de una lista dada.

# Creación de la función lambda
filtradoImpar = lambda lista: list(filter(lambda element: element%2!=0, lista))

# Ejecución
print(filtradoImpar([3,12,4,5,29,386,51,23,5123,51,23,46,23,323]))