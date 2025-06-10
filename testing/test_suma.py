import pytest
from suma import sumar

def test_suma():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

print("Ejecutando pruebas...")
print("Pruebas de suma.py")
print("Pruebas de la función sumar")
print(test_suma())
print("Pruebas completadas.") 