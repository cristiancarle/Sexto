
import unittest
from suma import sumar  # Importamos la función desde nuestro archivo

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

if __name__ == '__main__':
    unittest.main()