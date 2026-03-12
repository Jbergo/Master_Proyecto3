# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

# Creación de la función
def palabrasLargas(cadTexto, n):
    """Compara qué palabras son más largas que n.

    Args:
        cadTexto (str): texto a analizar
        n (int): número para comparar

    Returns:
        list: lista con las palabras más largas que n.
    """
    listaTexto = cadTexto.split()
    return list(filter(lambda palabra: len(palabra)>n, listaTexto))

#Ejecución
print(palabrasLargas("Hola que tal", 3))