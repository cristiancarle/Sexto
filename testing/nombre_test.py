import unittest
from nombre import obtener_datos, procesar_datos

class TestIntegracion(unittest.TestCase):
    def test_procesar_datos(self):
        datos = obtener_datos()
        resultado = procesar_datos(datos)
        self.assertEqual(resultado, 10)

if __name__ == "__main__":
    unittest.main()
