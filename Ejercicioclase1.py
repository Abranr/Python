def ProductoEscalar(vector1,vector2):
    u1 =vector1[0]
    u2 = vector1[1]
    u3 = vector1[2]
    
    v1 =vector2[0]
    v2 = vector2[1]
    v3 = vector2[2]
    
    a = u1*v1
    b = u2*v2
    c= u3*v3
    
    return a+b+c

def Vectores ():
    componente1 = float(input("Ingrese la primera componente de su vector\n"))
    componente2 = float(input("Ingrese la segunda componente de su vector\n"))
    componente3 = float(input("Ingrese la tercera componente de su vector\n"))
    
    return [componente1, componente2, componente3]

print('Indique las componentes del primer vector')
vector1 = Vectores()
print('-'*50)

print('Indique las componentes del segundo vector')
vector2 = Vectores()
print('-'*50)

print('El producto escalar entre ',vector1, 'y', vector2, 'es: \n')
print(ProductoEscalar(vector1, vector2))