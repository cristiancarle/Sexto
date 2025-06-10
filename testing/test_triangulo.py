import pytest
from triangulo import tipo_triangulo

def test_equilatero():
    assert tipo_triangulo(3, 3, 3) == "equilátero"

def test_isosceles():
    assert tipo_triangulo(4, 4, 2) == "isósceles"

def test_escaleno():
    assert tipo_triangulo(3, 4, 5) == "escaleno"

def test_invalido():
    assert tipo_triangulo(1, 2, 10) == "no es un triángulo"

print("Ejecutando pruebas...")
print("Pruebas de triangulo.py")
print("Pruebas de la función tipo_triangulo")
print(test_equilatero())
print(test_isosceles())
print(test_escaleno())
print(test_invalido())
print("Pruebas completadas.")