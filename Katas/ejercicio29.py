# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

# Creación de la función
def enmascararCaracteres(var):
    """Enmascara todos los caracteres de una cadena de texto, salvo las 4 últimas posiciones.

    Args:
        var (str): texto a enmascarar.

    Returns:
        str: texto enmascarado.
    """
    cadTexto = str(var)
    
    return '#' * (len(cadTexto) - 4) + cadTexto[-4:]
    
# Ejecución
print(enmascararCaracteres('prueba'))