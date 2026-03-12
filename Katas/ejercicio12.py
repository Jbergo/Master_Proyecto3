# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

#Creación de la función y del input
frase = input("Introduce una frase: ")
def longitudFrase(frase):
    """Función que calcula la longitud de una frase, dependiendo la longitud de cada palabra

    Args:
        frase (str): frase a analizar.

    Returns:
        list: lista con la longitud de cada palabra de la frase.
    """
    listaPalabras = frase.split()
    return list(map(lambda element: len(element), listaPalabras))

# Ejecución
print(longitudFrase(frase))