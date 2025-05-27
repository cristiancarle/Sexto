
usuarios = {"admin": "1234", "user": "abcd"}   
def autenticar(usuario, clave): 
      return usuarios.get(usuario) == clave

def main():
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if autenticar(usuario, clave):
        print("Autenticación exitosa")
    else:
        print("Autenticación fallida")
