# Creamos un diccionario vacío para almacenar los nombres de los estudiantes y sus calificaciones
matematicas = {}

# Pedimos al usuario que ingrese los nombres y calificaciones de los 5 estudiantes
for i in range(5):
    nombre = input("Ingrese el nombre del estudiante " + str(i+1) + ": ")
    calificacion = float(input("Ingrese la calificación del estudiante " + nombre + ": "))
    matematicas[nombre] = calificacion

# Buscamos el nombre y calificación de cada estudiante utilizando el método get()
nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
calificacion_buscar = matematicas.get(nombre_buscar)

if calificacion_buscar:
    print(nombre_buscar + " tiene una calificación de " + str(calificacion_buscar))
else:
    print("Estudiante no encontrado")