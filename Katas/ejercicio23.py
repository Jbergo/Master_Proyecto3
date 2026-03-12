# 23. Concatena una lista de palabras. Usa la función reduce().

# Importar reduce
from functools import reduce

# Crear la lista de palabras de ejemplo
listaPalabras = ['Hola', 'que', 'tal']

# Crear la función
concatenacion = reduce(lambda acum, palabra: acum+' '+palabra, listaPalabras)

# Ejecución
print(concatenacion)
