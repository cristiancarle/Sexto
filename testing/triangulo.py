def tipo_triangulo(a, b, c):
    # Primero, validamos si puede formar un triángulo
    if a + b <= c or a + c <= b or b + c <= a:
        return "no es un triángulo"

    if a == b == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "isósceles"
    else:
        return "escaleno"
