def area_triangulo(base, altura):

    # Calcula el área usando la fórmula del triángulo
    area = 0.5 * base * altura

    # Imprime el resultado del área calculada
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

    # Devuelve el área calculada
    return area

# Solicitar al usuario que ingrese los valores de la base y la altura
try:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    # Llamar a la función con los valores ingresados por el usuario
    area_triangulo(base, altura)
except ValueError:
    print("Por favor, ingrese valores numéricos válidos para la base y la altura.")
