# login.py

# Diccionario simulando una base de datos
USERS = {
    "admin": "1234",
    "user": "pass",
    "profesor": "clase2025"
}

def check_login(username: str, password: str) -> bool:
    """
    Verifica si el usuario y la contraseña son válidos.
    """
    if not username or not password:
        return False
    return USERS.get(username) == password
