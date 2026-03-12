# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# Creación de la función
def elementoDuplicado(lista):
    """Busca el primer elemento duplicado dentro de una lista.

    Args:
        lista (list): lista de palabras a analizar.

    Returns:
        str: elemento duplicado dentro de la lista.
    """
    noDuplicados = []
    
    for element in lista:
        if element in noDuplicados:
            return element
        noDuplicados.append(element)
        
# Ejecución
print(elementoDuplicado(["casa", "perro", "gato", "casa", "árbol", "perro", "sol", "gato", "mesa"]))