# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

# Definición de las mascotas prohibidas
prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

# Creación de la función de si es prohibida o no
def esProhibida(mascota):
    """Comprueba si la mascota que se da como argumento está en la lista de prohibida o no.

    Args:
        mascota (str): mascota a comprobar.

    Returns:
        str: devuelve la mascota que no estea dentro de la lista.
    """
    return mascota not in prohibidas

# Creación lista ejemplo
listaMascotas = ["Mapache", "Gato", "Serpiente Pitón", "Perro", "Oso", "León"]

# Función filter para sacar las mascotas que no están prohibidas
mascotaNueva = list(filter(esProhibida, listaMascotas))
print(mascotaNueva)
