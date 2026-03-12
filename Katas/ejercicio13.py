# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# Creación de la función
def conversionCaracteres(*args):
    """Dada una serie de caracteres, hace tupla de esos caracteres en mayúsculas y minúsculas. Evita duplicados.

    Returns:
        list: lista de tuplas de los caracteres
    """
    
    sinRepetidos = set(map(lambda element: element.lower(), args))
    
    return list(map(lambda element: (element.upper(), element), sinRepetidos))

# Ejecución de la función
print(conversionCaracteres('a','b','c','a','B','d'))