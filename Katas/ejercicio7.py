# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def conversionLista(listaTuplas):
    """Convierte una lista de tuplas en una lista de strings.

    Args:
        listaTuplas (tuple): lista a convertir

    Returns:
        list: lista de strings.
    """
    return list(map(lambda element: str(element), listaTuplas))

listaTuplas = (1,2,3)
print(conversionLista(listaTuplas))