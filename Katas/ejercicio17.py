# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

# Importar reduce
from functools import reduce

# Creación de la función
def numeroFinal(listaDigitos):
    """Convierte una lista de dígitos en un número.

    Args:
        listaDigitos (list): lista a convertir.

    Returns:
        int: número final
    """
    return reduce(lambda acum,num: acum*10+num, listaDigitos)

# Ejecución
print(numeroFinal([5,4,1,5]))