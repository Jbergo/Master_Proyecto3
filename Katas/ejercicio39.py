# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

# Importación de la libería
import math

# Creación de la función
def areaFigura(figura, datos):
    """Dependiendo de los argumentos que se le pasen a la función, calcula el área de una figura teniendo en cuenta los datos.

    Args:
        figura (str): Establecer qué área se van a calcular.
        datos (tuple): Tupla con los datos de la figura.

    Returns:
        int/float/str: Dependiendo del resultado del cálculo, o sino no ha sido posible calcularlo.
    """
    if figura.lower() == 'rectangulo':
        return datos[0]*datos[1]
    elif figura.lower() == 'circulo':
        return math.pi*datos[0]**2
    elif figura.lower() == 'triangulo':
        return (datos[0]*datos[1])/2
    else:
        return 'Opción no válida'
    
# Ejecución
print(areaFigura("rectangulo", (5,3)))
print(areaFigura("circulo", (5,)))
print(areaFigura("triangulo", (6,3)))