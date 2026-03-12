# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

# Importar reduce
from functools import reduce

# Creación de la lista de ejemplo
listaNum = [3,2,5,10]

# Creación de la función
productoTotal = reduce(lambda acum, element:acum*element, listaNum)

# Ejecución
print(productoTotal)