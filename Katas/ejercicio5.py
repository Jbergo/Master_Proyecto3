# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def calcularMedia(listaNum, nota_aprobado = 5):
    """Recorre la lista de números, calcula la media y evalúa el valor de dicha media.

    Args:
        listaNum (list): lista de número para analizar
        nota_aprobado (int, optional): nota para evaluar la media. Defaults to 5.

    Returns:
        tuple: contiene la nota media y el estado de dicha nota.
    """
    media = 0
    for element in listaNum:
        media += element
    
    media = media/len(listaNum)

    if media >= nota_aprobado:
        estado = 'Aprobado'
    else:
        estado = 'Suspenso'

    return (media, estado)

print(calcularMedia([5, 7, 9]))