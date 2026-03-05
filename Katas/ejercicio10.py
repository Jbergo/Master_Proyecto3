# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

#Creación de la excepción
class EmptyList(Exception):
    pass

#Creación de la función de cálculo del promedio
def calculoPromedio(listaNum):
    if not listaNum:
        raise EmptyList
    
    promedio = 0
    for element in listaNum:
        promedio += element
       
    promedio /= len(listaNum)
    return promedio

try:
    print(calculoPromedio([]))
except EmptyList as e:
    print("Lista vacía")