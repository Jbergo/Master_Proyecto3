# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

# Importar reduce
from functools import reduce

# Creación de la lista de ejemplo
lista = [15, 4, 6, 2]

# Creación de la función
diferencia = reduce(lambda acum, num: acum-num, lista)

# Ejecución
print(diferencia)