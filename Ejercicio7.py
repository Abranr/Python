#Calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Ingresa un número: "))
result = factorial(num)
print(f"El factorial de {num} es {result}")