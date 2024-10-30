def es_vocal(letra):
    return letra in 'aeiouáéíóuu'

def es_consonante(letra):
    return letra. isalpha() and not es_vocal(letra)

def es_diptongo(palabra):
    vocales = "aeiouáéíóúü"
    for i in range(len(palabra)-1):
        if palabra[i] in vocales and palabra[i+1] in vocales:
            return True
        return False

def contiene_secuencia(palabra):
    secuencias = ["fl", "bl", "gr", "dr"]
    for secuencia in secuencias:
        if secuencia in palabra:
            return True
        return False

def calcular_puntuacion(palabra):
    puntuacion = 0

# Regla 1: Cantidad impar de letras
    if len(palabra) % 2 != 0:
        puntuacion += 5

# Regla 2: Consonantes y vocales
    for letra in palabra:
        if es_consonante(letra):
            puntuacion += 8
        elif es_vocal(letra):
            puntuacion += 5

# Regla 3: Diptongos/Hiatos
    if es_diptongo(palabra):
        puntuacion += 10

# Regla 4: Secuencias específicas
    if contiene_secuencia(palabra):
        puntuacion += 15

# Regla 5: Misma letra al inicio y fin
    if palabra[0] == palabra[-1]:
     puntuacion += 30
     
     return puntuacion

# Ejemplo de uso
palabra = "anticuada"
puntuacion = calcular_puntuacion(palabra)
print(f"La puntuacion de la palabra '{palabra}' es: {puntuacion}")