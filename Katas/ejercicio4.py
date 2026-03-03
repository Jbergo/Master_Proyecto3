# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

newList = list(map(lambda element1, element2:element1-element2, [5, 7, 9], [1, 2, 3]))
print(newList)