# a. Crear la lista de tuplas con al menos tres estudiantes
estudiantes = [
    ("Juan", 20),
    ("María", 22),
    ("Pedro", 21),
    ("Ana", 19)
]

# b. Imprimir la lista de estudiantes
print("Lista de estudiantes:")
print(estudiantes)

# Imprimir el nombre y la edad de cada estudiante
print("\nInformación de cada estudiante:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante[0]}, Edad: {estudiante[1]}")