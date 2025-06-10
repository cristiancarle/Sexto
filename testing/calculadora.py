# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(x):
    if x < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return x ** 0.5
