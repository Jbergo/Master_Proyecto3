# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

#Creación de la función
def filtradoLetra(listaPalabras, letra):
    """Filtra las palabras que contienen una letra en específico

    Args:
        listaPalabras (lsit): lista a analizar
        letra (str): letra para filtrar

    Returns:
        list: lista que contiene las palabras con la letra específica.
    """
    return list(filter(lambda element: element[0].lower() == letra.lower(), listaPalabras))

# Creación de las variables de ejemplo
listaPalabras = ['Gato', 'Vaca', 'Perro', 'Dinosaurio', 'Gusano']
letra = 'd'

# Ejecución
print(filtradoLetra(listaPalabras, letra))