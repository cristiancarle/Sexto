import pytest
from src.main import sumar, es_mayor_que, login

def test_sumar():
    assert sumar(2, 3) == 5


def test_es_mayor_que():
    assert es_mayor_que(5, 3) == True
    assert es_mayor_que(2, 4) == False


@pytest.mark.parametrize("input_a, input_b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, sumar(0,1), 0),
    (100, 200, 300),
])
def test_sumar_parametros(input_a, input_b, expected):
    assert sumar(input_a, input_b) == expected

def test_login():
    login_pasado = login("admin", "admin")
    assert login_pasado

def test_login_fallado():
    login_fallado = login("admin", "wrong_password")
    assert not login_fallado
    
