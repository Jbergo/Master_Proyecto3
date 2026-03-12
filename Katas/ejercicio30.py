# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# Creación de la función
def sonAnagramas(palabra1, palabra2):
    """Comprueba si dos palabras son anagramas, ordenando las letras de cada palabra.

    Args:
        palabra1 (str): palabra a comprobar.
        palabra2 (str): palabra a comprobar.

    Returns:
        bool: 'True' si son anagramas y 'False' si no lo son.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


# Ejecución
print(sonAnagramas("Roma", "Amor"))