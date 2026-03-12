# 27. Crea una función que calcule el promedio de una lista de números.

# Creación de la función
def promedio(listaNum):
    """Calcula el promedio de una lista de números.

    Args:
        listaNum (list): lista de números para calcular su promedio.

    Returns:
        int/float: promedio de la lista de números.
    """
    promedio=0
    for element in listaNum:
        promedio+=element
    return promedio/len(listaNum)

# Ejecución
print(promedio([4,3,2,1,9]))