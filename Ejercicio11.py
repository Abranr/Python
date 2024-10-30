# Pedir al usuario que ingrese sus 3 películas favoritas y almacenarlas en una lista.
peliculas_favoritas = []

for i in range(3):
    pelicula = input("Escribe tu película favorita: ")
    peliculas_favoritas.append(pelicula)

# Imprimir la lista de películas favoritas.
print("Tus películas favoritas son:")
for pelicula in peliculas_favoritas:
    print(pelicula)
