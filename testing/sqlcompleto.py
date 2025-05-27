# Ejemplo educativo de SQL Injection
def simulador_login_inseguro():
    print("=== Sistema de Login Inseguro (Ejemplo Educativo) ===")
    print("Base de datos simulada de usuarios:")
    print("Usuario: admin, Contraseña: 1234")
    print("Usuario: estudiante, Contraseña: 5678\n")

    # Simular una base de datos simple
    base_datos = [
        {"usuario": "admin", "contraseña": "1234"},
        {"usuario": "estudiante", "contraseña": "5678"}
    ]

    # Versión insegura de consulta
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")

    # Simulación de consulta SQL vulnerable
    query = f"SELECT * FROM usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}'"
    print("\nConsulta SQL generada:")
    print(query)

    # Simular verificación
    if "' OR '1'='1" in usuario or "' OR '1'='1" in contraseña:
        print("\n¡ALERTA! Se detectó un intento de SQL Injection!")
        print("Este es un ejemplo de cómo NO debe programarse un sistema de login")
        return False

    # Verificación normal
    for user in base_datos:
        if user["usuario"] == usuario and user["contraseña"] == contraseña:
            return True
    return False

# Versión segura para comparar
def simulador_login_seguro():
    print("\n=== Sistema de Login Seguro ===")
    
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")

    # Simular consulta parametrizada
    query = "SELECT * FROM usuarios WHERE usuario=? AND contraseña=?"
    print("\nConsulta SQL segura:")
    print(query)
    print("Parámetros:", [usuario, contraseña])

# Programa principal
def main():
    print("Bienvenidos a la clase de Seguridad Informática\n")
    
    while True:
        print("\n=== MENÚ ===")
        print("1. Probar login inseguro")
        print("2. Probar login seguro")
        print("3. Salir")
        
        opcion = input("\nElija una opción: ")
        
        if opcion == "1":
            resultado = simulador_login_inseguro()
            if resultado:
                print("\n✅ Login exitoso")
            else:
                print("\n❌ Login fallido")
        
        elif opcion == "2":
            simulador_login_seguro()
            print("\nEste es un ejemplo de cómo SÍ debe programarse un sistema de login")
        
        elif opcion == "3":
            print("\n¡Gracias por aprender sobre seguridad!")
            break

if __name__ == "__main__":
    main()