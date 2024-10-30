edad = int(input("Ingrese su edad: "))
ciudadania = input("¿Es ciudadano registrado de la comunidad? (si/no): ")
restricciones = input("¿Ha sido condenado por algún delito en la comunidad? (si/no): ")

# Verificar condiciones de elegibilidad
def es_elegible_para_votar(edad, ciudadania, restricciones):
    if edad < 18:
        return False
    if ciudadania.lower() != "si":
        return False
    if restricciones.lower() == "si":
        return False
    return True


if es_elegible_para_votar(edad, ciudadania, restricciones):
    print("Usted es elegible para votar.")
else:
    print("Usted no es elegible para votar.")
