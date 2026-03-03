# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscarPalabra(listaPalabras, palabraObjetivo):
    """A partir de una lista de palabras, busca una palabra específica entre los valores de la lista.

    Args:
        listaPalabras (list): lista de palabras en donde buscar.
        palabraObjetivo (str): palabra a buscar dentro de la lista.

    Returns:
        list: lista de palabras repetidas en la lista original.
    """
    contienePalabra = []

    for element in listaPalabras:
        if not(element == palabraObjetivo):
            continue
        else:
            contienePalabra.append(element)
            
    return contienePalabra

print(buscarPalabra(["casa", "perro", "gato", "mesa", "silla", "ventana", "libro", 'gato', 'gato'], "gato"))