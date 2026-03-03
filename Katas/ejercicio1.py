# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuenciasLetra(cadena):
    """Cuenta el número de repeticiones de cada letra existente.

    Args:
        cadena (str): cadena de texto para comprobar.

    Returns:
        dict: diccionario con clave la letra y valor el número de repeticiones.
    """
    diccionario = {}

    cadena = cadena.strip()
    cadena = cadena.lower()
    for letra in cadena:
        if letra == " ":
            continue
        if letra not in diccionario:
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1

    return diccionario

print(frecuenciasLetra("Esto es una prueba"))