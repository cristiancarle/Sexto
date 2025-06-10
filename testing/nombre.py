def obtener_datos():
    return{"nombre": "Juan", "edad": 25}

def procesar_datos(datos):
    datos=obtener_datos()
    return f"Nombre: {datos['nombre']}, Edad: {datos['edad']}"
