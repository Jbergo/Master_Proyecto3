# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# Creación de la lista
infoEstudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 22, "calificacion": 78},
    {"nombre": "Marta", "edad": 19, "calificacion": 92},
    {"nombre": "Carlos", "edad": 21, "calificacion": 69}
]

# Creación del filter
compararCalificacion = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, infoEstudiantes))

# Ejecución
print(compararCalificacion)