from autenti import autenticar

def test_autenticacion_exitosa_admin():
    assert autenticar("admin", "1234") == True

def test_autenticacion_exitosa_user():
    assert autenticar("user", "abcd") == True

def test_autenticacion_fallida_clave_incorrecta():
    assert autenticar("admin", "wrongpass") == False

def test_autenticacion_fallida_usuario_incorrecto():
    assert autenticar("wronguser", "1234") == False

def test_autenticacion_fallida_ambos_incorrectos():
    assert autenticar("noexiste", "nopass") == False
