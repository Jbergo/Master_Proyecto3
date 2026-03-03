# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def calculoFactorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * calculoFactorial(num-1)
    
print(calculoFactorial(5))