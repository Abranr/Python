import random

# Definimos la baraja de cartas
baraja = [
    f"{palo} de {numero}"
    for palo in ["Corazones", "Diamantes", "Tréboles", "Espadas"]
    for numero in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
]

def repartir_cartas():
    # Creamos una copia de la baraja para no modificar la original
    baraja_copia = baraja.copy()
    
    # Seleccionamos 4 cartas aleatorias de la baraja
    cartas_usuario = random.sample(baraja_copia, 4)
    
    # Eliminamos las cartas seleccionadas de la baraja
    for carta in cartas_usuario:
        baraja_copia.remove(carta)
    
    return cartas_usuario

# Ejemplo de uso
cartas_usuario = repartir_cartas()
print("Cartas repartidas:", cartas_usuario)