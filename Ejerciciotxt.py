# Crear un nuevo archivo "ejercicio.txt" con el texto especificado
with open("ejercicio.txt", "w") as file:
    file.write("Hola mundo, estamos aprendiendo a usar Java\n")
    file.write("escribir y guardar informacion\n")
    file.write("en archivos en Java.\n")

# Sustituir todas las instancias de "Java" por "Python" en el archivo
with open("ejercicio.txt", "r+") as file:
    content = file.read()
    file.seek(0)
    file.write(content.replace("Java", "Python"))
    file.truncate()

# Buscar si la palabra "aprendiendo" existe en el archivo
with open("ejercicio.txt", "r") as file:
    content = file.read()
    if "aprendiendo" in content:
        print("La palabra 'aprendiendo' existe en el archivo.")
    else:
        print("La palabra 'aprendiendo' no existe en el archivo.")
