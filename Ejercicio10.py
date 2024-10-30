def es_par(numero):
        return numero % 2 == 0

# Solicitar al usuario que ingrese un número
numero_usuario = int(input("Ingrese un número: "))

# Verificar si el número es par o impar
if es_par(numero_usuario):
    print(f"El número {numero_usuario} es par.")
else:
    print(f"El número {numero_usuario} es impar.")
