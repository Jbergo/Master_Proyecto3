# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

conversion = list(map(lambda element: str(element), (1,2,3)))
print(conversion)