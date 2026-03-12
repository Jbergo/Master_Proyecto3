# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def calculoDiferencia(lista1, lista2):
    """Calcula la diferencia entre los valores de dos listas.

    Args:
        lista1 (list): lista a analizar.
        lista2 (list): lista a analizar.

    Returns:
        list: cada valor es la diferencia entre los valores de las dos listas.
    """
    return list(map(lambda element1, element2:element1-element2, lista1, lista2))

lista1 = [5, 7, 9]
lista2 = [1, 2, 3]

print(calculoDiferencia(lista1, lista2))