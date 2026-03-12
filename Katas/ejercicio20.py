# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

# Creación de la lista de ejemplo
lista_mixta = [10, "hola", 25, "Python", 7, "mundo", 42]

# Obtención de los valores int buscando según el tipo de dato de cada element
soloInt = list(filter(lambda element: type(element)==int, lista_mixta))

# Ejecución
print(soloInt)