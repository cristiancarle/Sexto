def sumar(x,y):
    return x + y    

def es_mayor_que(numero1, numero2):
    return numero1 > numero2

def login(usuario, contrasena):
    if usuario == "admin" and contrasena == "admin":
        return True
    else:
        return False