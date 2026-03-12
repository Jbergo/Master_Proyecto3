# 36. Crea una función llamada procesar_texto
#     - Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
#     - Código a seguir:
#         1. Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
#         2. Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
#         3. Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
#         4. Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
#     - Caso de uso:
#         - Verificar el funcionamiento completo de procesar_texto.

# Creación de la función contar_palabras
def contar_palabras(listaPalabrasTexto):
    """Cuenta el número de veces que aparece una palabra en el texto.

    Args:
        listaPalabrasTexto (list): lista con todas las palabras que aparecen en el texto.

    Returns:
        dict: diccionario con las palabras y el número de veces que se repite esa palabra.
    """
    numPalabras = {}
    
    for palabra in listaPalabrasTexto:
        if palabra in numPalabras:
            numPalabras[palabra] += 1
        else:
            numPalabras[palabra] = 1
            
    return numPalabras

# Creación de la función reemplazar_palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza una palabra por otra en todo el texto.

    Args:
        texto (str): Texto a modificar.
        palabra_original (str): palabra a reemplazar.
        palabra_nueva (str): palabras por la que se reemplaza.

    Returns:
        str: texto modificado.
    """
    textoModificado = texto.replace(palabra_original, palabra_nueva)
    return textoModificado

# Creación de la función eliminar_palabra
def eliminar_palabra(listaPalabrasTexto, palabra):
    """Elimina todas las ocurrencias de una palabra dentro del texto.

    Args:
        listaPalabrasTexto (list): lista con todas las palabras del texto.
        palabra (str): palabra a eliminar.

    Returns:
        str: texto modificado.
    """
    nueva_lista = []
    for palabra_actual in listaPalabrasTexto:
        if palabra_actual != palabra:
            nueva_lista.append(palabra_actual)
        
    return " ".join(nueva_lista)

# Creación de la función procesar_texto
def procesar_texto(texto, opcion, *args):
    """Ejecuta el resto de funciones según el caso de uso.

    Args:
        texto (str): Texto con el que se va a trabajar.
        opcion (str): Opción para escoger la función que se va a ejecutar.

    Returns:
        dict/str: Dependiendo de la opción que se haya escogido, va a devolver un tipo de variable u otro.
    """
    listaPalabrasTexto = texto.split()
    
    if opcion == "contar":
        return contar_palabras(listaPalabrasTexto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(listaPalabrasTexto, args[0])
    else:
        "Opción no contemplada"
        
# Ejecución
print(procesar_texto("este es un texto este", "contar"))
print(procesar_texto("este es un texto", "reemplazar", "texto", "mensaje"))
print(procesar_texto("este es un texto", "eliminar", "es"))