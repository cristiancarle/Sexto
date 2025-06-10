import sqlite3

def crear_base_datos():
    # Crear/conectar a la base de datos
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    # Crear tabla de usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        usuario TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )''')

    # Insertar algunos usuarios de prueba
    usuarios_prueba = [
        ('admin', '1234'),
        ('juan', '5678'),
        ('maria', 'abc123')
    ]

    cursor.executemany('INSERT OR IGNORE INTO usuarios (usuario, contraseña) VALUES (?, ?)', 
                      usuarios_prueba)
    
    conn.commit()
    conn.close()

def login_vulnerable():
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    print("\n=== Sistema de Login Vulnerable (SQLite real) ===")
    print("Usuarios válidos:")
    print("usuario: admin, contraseña: 1234")
    print("usuario: juan, contraseña: 5678")
    print("\nPrueba SQL Injection:")
    print("usuario: ' OR '1'='1")
    print("contraseña: cualquiera")

    usuario = input("\nUsuario: ")
    contraseña = input("Contraseña: ")

    # Consulta SQL vulnerable
    query = f"SELECT * FROM usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}'"
    print("\nConsulta SQL ejecutada:")
    print(query)

    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
        print(resultado)
        if resultado:
            print("\n⚠️ Login exitoso!")
            print("Usuarios encontrados:")
            for fila in resultado:
                print(f"ID: {fila[0]}, Usuario: {fila[1]}, Contraseña: {fila[2]}")
        else:
            print("\n❌ Usuario o contraseña incorrectos")

    except sqlite3.Error as error:
        print("\n❌ Error en la consulta SQL:", error)

    conn.close()

def menu_principal():
    while True:
        print("\n=== MENÚ ===")
        print("1. Crear/Resetear base de datos")
        print("2. Intentar login")
        print("3. Salir")

        opcion = input("\nElije una opción: ")

        if opcion == "1":
            crear_base_datos()
            print("Base de datos creada/reseteada exitosamente")
        elif opcion == "2":
            login_vulnerable()
        elif opcion == "3":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_principal()