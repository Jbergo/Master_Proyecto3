# 40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe: 
#     1. Solicitar al usuario el precio original de un artículo. 
#     2. Preguntar si tiene un cupón de descuento (respuesta sí o no). 
#     3. Si la respuesta es sí, solicitar el valor del cupón de descuento. 
#     4. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero). 
#     5. Mostrar el precio final de la compra, considerando o no el descuento. 
#     6. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

# Declaración de variables
precioOriginal = float(input(f"Introduce el precio del artículo: "))
cuponDescuento = input(f"Tiene cupón de descuento? (Si/No): ")

# Control de las respuestas del descuento
if cuponDescuento.lower() == 'si':
    valorDescuento = float(input(f"Introduce el valor del descuento (%): "))
    
    # Aplicar descuento y mostrar resultado
    if valorDescuento > 0 and valorDescuento <= 100:
        precioFinal = precioOriginal - ((valorDescuento*precioOriginal)/100)
        print(precioFinal)
    else:
        print("Descuento no válido")
        print(precioOriginal)
    
elif cuponDescuento.lower() == 'no':
    print(precioOriginal)
    
else:
    print("Respueta No Válida")