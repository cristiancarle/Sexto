import math

def zetadieta(C, P, G):
   
    bananas = math.ceil(C / 27)
   
    atun = math.ceil(P / 30)
   
    aceite_oliva = G
    
   
    calorias_bananas = bananas * 105
   
    calorias_atun = atun * 120
    
    calorias_aceite_oliva = aceite_oliva * 9
    
    
    calorias_totales = calorias_bananas + calorias_atun + calorias_aceite_oliva
    
    return calorias_totales


#C, P, G = 60, 55, 10
C=int(input(Ingrese los carbohidratos, proteinas y Grasas))
print(zetadieta(C, P, G)) 