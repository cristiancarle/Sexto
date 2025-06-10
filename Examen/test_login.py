# test_login.py

import pytest
from login import check_login

# Casos exitosos
def test_login_admin():
    assert check_login("admin", "1234") is True

def test_login_user():
    assert check_login("user", "pass") is True

def test_login_profesor():
    assert check_login("profesor", "clase2025") is True

# Casos fallidos
def test_wrong_username():
    assert check_login("usuario", "1234") is False

def test_wrong_password():
    assert check_login("admin", "0000") is False

def test_wrong_username_and_password():
    assert check_login("fakeuser", "wrongpass") is False

# Campos vacíos
def test_empty_username():
    assert check_login("", "1234") is False

def test_empty_password():
    assert check_login("admin", "") is False

def test_both_empty():
    assert check_login("", "") is False
