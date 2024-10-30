import numpy as np

def suma_matrices(A, B):
    """
    Suma dos matrices cuadradas A y B
    """
    return np.add(A, B)

def resta_matrices(A, B):
    """
    Resta dos matrices cuadradas A y B
    """
    return np.subtract(A, B)

def multiplicacion_matrices(A, B):
    """
    Multiplica dos matrices cuadradas A y B
    """
    return np.dot(A, B)

def imprimir_matriz(matriz):
    """
    Imprime una matriz de forma legible
    """
    print(matriz)

def main():
    print("Calculadora de matrices cuadradas")
    print("-------------------------------")

    while True:
        print("1. Suma de matrices")
        print("2. Resta de matrices")
        print("3. Multiplicación de matrices")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Suma de matrices")
            A = np.array(eval(input("Ingrese la matriz A: ")))
            B = np.array(eval(input("Ingrese la matriz B: ")))
            resultado = suma_matrices(A, B)
            imprimir_matriz(resultado)

        elif opcion == "2":
            print("Resta de matrices")
            A = np.array(eval(input("Ingrese la matriz A: ")))
            B = np.array(eval(input("Ingrese la matriz B: ")))
            resultado = resta_matrices(A, B)
            imprimir_matriz(resultado)

        elif opcion == "3":
            print("Multiplicación de matrices")
            A = np.array(eval(input("Ingrese la matriz A: ")))
            B = np.array(eval(input("Ingrese la matriz B: ")))
            resultado = multiplicacion_matrices(A, B)
            imprimir_matriz(resultado)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()