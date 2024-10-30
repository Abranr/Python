import math

def redondeo_hacia_abajo():
    # Solicitar al usuario que ingrese un número decimal
    numero_decimal = float(input("Por favor, ingrese un número decimal: "))
    
    # Usar math.floor() para redondear hacia abajo
    entero_menor = math.floor(numero_decimal)
    
    # Devolver el resultado
    return entero_menor

# Llamar a la función y mostrar el resultado
resultado = redondeo_hacia_abajo()
print(f"El entero menor más cercano es: {resultado}")
