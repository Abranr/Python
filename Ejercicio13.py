# Lista original
lista = [3, 7, 5, 8, 1, 6, 1, 6, 2, 5]

# Eliminar valores duplicados utilizando conjuntos
conjunto = set(lista)
print("Conjunto sin duplicados:", conjunto)

# Crear un conjunto con números del 1 al 5
conjunto_nuevo = {1, 2, 3, 4, 5}
print("Conjunto con números del 1 al 5:", conjunto_nuevo)

# Realizar la intersección entre ambos conjuntos
interseccion = conjunto & conjunto_nuevo
print("Intersección entre ambos conjuntos:", interseccion)