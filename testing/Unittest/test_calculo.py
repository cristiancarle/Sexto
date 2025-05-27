import unittest
class TestCalculo(unittest.TestCase):
    def test_sumatoria(self)-> int:
        valorA = 10
        valorB = 20
        valorC = 30
        suma = valorA + valorB + valorC
        self.assertEqual(suma, 50, "La suma no es correcta")
        return suma

    def test_resta(self)-> int:
        valorA = 10
        valorB = 5
        valorC = 2
        resta = valorA - valorB - valorC
        self.assertEqual(resta, 3, "La resta no es correcta")
        return resta
    