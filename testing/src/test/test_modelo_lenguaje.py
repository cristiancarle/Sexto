from src.models.modelo_lenguaje import ModeloLenguaje

def test_leguajes_no_nada():
    
    """
    Test para el método lenguajes de la clase modelo_lenguaje.
    """
    lenguajes = ModeloLenguaje.lenguajes()
    assert isinstance(lenguajes, list), "El resultado no es una lista"
    assert len(lenguajes) > 0, "La lista de lenguajes está vacía"
    assert all(isinstance(lenguaje, str) for lenguaje in lenguajes), "No todos los elementos son cadenas de texto"