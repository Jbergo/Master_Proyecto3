# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

# Creación de la excepción
class NoSeEncuentra(Exception):
    pass

# Creación de la función
def buscarNombre(listaNombres, nombre):
    """Comprueba si un nombre se encuentra dentro de una lista de nombres, las dos variables dadas por el usuario.

    Args:
        listaNombres (list): lista de nombres para buscar el nombre.
        nombre (str): nombre a buscar dentro de la lista.

    Raises:
        NoSeEncuentra: excepción que se lanza cuando no se encuentra el nombre dentro de la lista.

    Returns:
        str: mensaje indicando que se ha encontrado el nombre correctamente.
    """
    if nombre.lower() in listaNombres.lower():
        return "Nombre encontrado"
    else:
        raise NoSeEncuentra
    
# Ejecución
try:
    print(buscarNombre(input(f"Introduce la lista de nombres: "), input(f"Introduce el nombre a buscar: ")))
except NoSeEncuentra:
    print("Nombre no encontrado en la lista")