# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# Crear excepción "fuera de rango"
class FueraRango(Exception):
    pass

# Función
def numero():
    """Pide la edad al usuario y maneja error

    Raises:
        FueraRango: error lanzado cuando la edad está fuera del rango del condicional.
    """
    edad = int(input(f"Introduce tu edad: "))
    
    if edad<0 or edad>120:
        raise FueraRango
    
    print(f"Tu edad es {edad}")
    
# Ejecución de la función y manejo de errores
try:
    numero()
except ValueError:
    print("Valor no numérico")
except FueraRango:
    print("Edad fuera del rango válido")