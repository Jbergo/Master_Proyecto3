# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# Creación de la función
def buscarEmpleado(nombreCompleto, listaEmpleados):
    """Busca el nombre completo de una persona dentro de una lista de personas, si es correcto muestra su puesto sino salta un mensaje.

    Args:
        nombreCompleto (str): nombre y apellidos a buscar.
        listaEmpleados (list): lista de diccionarios con nombre, apellidos y puesto de cada persona.

    Returns:
        str: texto con el puesto de trabajo en el caso de que se encuentre a la persona, o texto de error si no se encuentra.
    """
    for empleado in listaEmpleados:
        nombreEmpleado = empleado["nombre"].lower() + ' ' + empleado["apellidos"].lower()
        if nombreCompleto == nombreEmpleado:
            return empleado["puesto"]
        else:
            return "La personas que estás buscando no trabaja aquí."
    
# Creación de las variables de ejemplo
empleados = [
    {"nombre": "Ana", "apellidos": "García López", "puesto": "Administrativa"},
    {"nombre": "Luis", "apellidos": "Martínez Pérez", "puesto": "Desarrollador"},
    {"nombre": "Marta", "apellidos": "Sánchez Ruiz", "puesto": "Diseñadora"},
    {"nombre": "Carlos", "apellidos": "Fernández Gómez", "puesto": "Contable"},
    {"nombre": "Elena", "apellidos": "Navarro Díaz", "puesto": "Recursos Humanos"},
    {"nombre": "Javier", "apellidos": "Romero Gil", "puesto": "Analista de Datos"},
    {"nombre": "Sofía", "apellidos": "Torres Molina", "puesto": "Marketing"},
    {"nombre": "Pablo", "apellidos": "Castro Vega", "puesto": "Soporte Técnico"}
]

# Ejecución
print(buscarEmpleado("ana lópez", empleados))