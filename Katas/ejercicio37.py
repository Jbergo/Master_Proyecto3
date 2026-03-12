# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

# Importación de la librería
import datetime

# Declaración de las variables
horas = int(input(f"Introduce la hora: "))
minutos = int(input(f"Introduce los minutos: "))
horaUsuario = datetime.time(horas, minutos)

# Detectar si es de noche, de día o de tarde
if horaUsuario >= datetime.time(6,00) and horaUsuario <= datetime.time(11, 59):
    print("Estamos por la mañana")
elif horaUsuario >= datetime.time(12,00) and horaUsuario <= datetime.time(19, 59):
    print("Estamos por la tarde")
elif horaUsuario >= datetime.time(20,00) and horaUsuario <= datetime.time(23, 59):
    print("Estamos por la noche")
elif horaUsuario >= datetime.time(00,00) and horaUsuario <= datetime.time(5, 59):
    print("Estamos por la noche")
else:
    print("Hora no válida")