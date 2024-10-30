def es_elegible_para_votar(edad, ciudadania, condenas):
    if edad >= 18 and ciudadania and not condenas:
        return True
    else:
        return False

def calcular_años_faltantes(edad):
    años_faltantes = 18 - edad
    return años_faltantes

def main():
    edad_tim = 14
    ciudadania_tim = True
    condenas_tim = False

    if es_elegible_para_votar(edad_tim, ciudadania_tim, condenas_tim):
        print("Tim ya es elegible para votar.")
    else:
        años_faltantes = calcular_años_faltantes(edad_tim)
        print(f"Tim le faltan {años_faltantes} años para poder votar.")

if __name__ == "__main__":
    main()