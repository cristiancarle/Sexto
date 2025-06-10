usuarios = {"admin": "1234", "user": "abcd"}

def autenticar(usuario, clave):
    return usuarios.get(usuario) == clave

