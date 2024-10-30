def puntaje_palabra(palabra):
  """Calcula el puntaje de una palabra según las reglas dadas.

  Argumentos:
    palabra: La palabra a evaluar.

  Retorno:
    El puntaje de la palabra.
  """

  puntaje = 0
  
  # Regla 1: Cantidad impar de letras
  if len(palabra) % 2 != 0:
    puntaje += 5

  # Regla 2: Consonantes y vocales
  for letra in palabra:
    if letra in "aeiou":
      puntaje += 5
    else:
      puntaje += 8

  # Regla 3: Diptongos/Hiatos
  diptongos = ["ai", "au", "ei", "eu", "oi", "iu", "ui"]
  for i in range(len(palabra) - 1):
    if palabra[i:i+2] in diptongos:
      puntaje += 10

  # Regla 4: "fl", "bl", "gr", "dr"
  if "fl" in palabra or "bl" in palabra or "gr" in palabra or "dr" in palabra:
    puntaje += 15

  # Regla 5: Comienza y termina con la misma letra
  if palabra[0] == palabra[-1]:
    puntaje += 30

  return puntaje

# Ejemplo de uso:
palabras = ["GRANDIOSO", "PUEBLERINO", "ANTICUADA", "OJO"]
for palabra in palabras:
  puntaje = puntaje_palabra(palabra)
  print(f"El puntaje de '{palabra}' es: {puntaje}")