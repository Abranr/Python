precios = {
    "leche": 1.19,
    "galletas": 1.45,
    "mantequilla": 1.90,
    "queso": 2.59,
    "pan": 4.99,
    "jalea": 3.65,
    "yogurt": 3.15,
    "manzanas": 2.15,
    "naranjas": 0.99,
    "bananos": 1.29
}

existencias = {
    "leche": 20,
    "galletas": 32,
    "mantequilla": 15,
    "queso": 15,
    "pan": 20,
    "jalea": 18,
    "yogurt": 35,
    "manzanas": 40,
    "naranjas": 23,
    "bananos": 35
}

print("¡Hola! Yo seré tu asistente virtual para generar tu lista de compras el día de hoy.")
nombre = input("Por favor, ingresa tu nombre: ")
nombre_completo = f"{nombre}"
print(f"¡Excelente {nombre}! A continuación, se mostrarán los artículos con sus respectivos precios.")

# Mostrar los artículos y sus precios
for articulo, precio in precios.items():
    print(f"{articulo}: ${precio:.2f}")

# Función para solicitar la cantidad de un artículo y verificar inventario
def solicitar_cantidad(articulo):
    while True:
        cantidad = int(input(f"Ingrese cuántos {articulo} quiere (si no desea alguno, por favor coloque 0): "))
        if cantidad <= existencias[articulo]:
            return cantidad
        print(f"No hay inventario disponible, escoja una cantidad menor o igual a {existencias[articulo]}")

# Solicitar la cantidad de cada artículo
compras_usuario = {}
for articulo in precios.keys():
    compras_usuario[articulo] = solicitar_cantidad(articulo)

# Generar recibo de compra
print("\n--------------------------------------------------")
print("                 RECIBO DE COMPRA                  ")
print(f"Recibo a nombre de: {nombre_completo}")
print("--------------------------------------------------")
print("Cantidad Artículo    Precio Unitario    Precio Final")
total = 0
for articulo, cantidad in compras_usuario.items():
    if cantidad > 0:
        precio_unitario = precios[articulo]
        precio_final = round(cantidad * precio_unitario, 2)
        total += precio_final
        print(f"{cantidad:<9} {articulo:<13} ${precio_unitario:<14} ${precio_final}")

total_final = round(total, 2)
print("--------------------------------------------------")

print(f"EL TOTAL ES DE                       ${total_final}")
print("--------------------------------------------------")

# Actualizar inventario
for articulo, cantidad in compras_usuario.items():
    existencias[articulo] -= cantidad

# Mostrar inventario restante
print("                 INVENTARIO                         ")
print("--------------------------------------------------")
print("Artículo                           Cantidad restante")
for articulo, cantidad in existencias.items():
    print(f"{articulo:<11} {cantidad}")
