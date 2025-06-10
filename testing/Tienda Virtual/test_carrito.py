import unittest
from productos import Producto

class TestCarrito(unittest.TestCase):
    #------------------------------------------------------
    # Test de la clase Producto
    #------------------------------------------------------

    #Se ejecuta antes de las pruebas para inicializar los objetos


    
    def setUp(self):
        self.producto1 = Producto("Producto 1", 10.0, 5)
        self.producto2 = Producto("Producto 2", 20.0, 3)
        self.carrito = []

    #------------------------------------------------------
    # Se ejecuta después de cada prueba para limpiar los objetos

    def tearDown(self):
        self.nombre = ""
        self.precio = 0.0


    #------------------------------------------------------
    # Método de la clases setup y tearDown
    #------------------------------------------------------
    @classmethod
    def setUpClass(cls):
        print("Configurando la clase de prueba...")
    
    @classmethod
    def tearDownClass(cls):
        print("Limpiando la clase de prueba...")

    #------------------------------------------------------

    def test_producto(self):
        # Crear un producto de prueba
        producto = Producto("Camiseta", 20.0, 10)
        
        # Verificar que el nombre del producto sea correcto
        self.assertEqual(producto.nombre, "Camiseta")
        
        # Verificar que el precio del producto sea correcto
        self.assertEqual(producto.precio, 20.0)
        
        # Verificar que el stock del producto sea correcto
        self.assertEqual(producto.stock, 10)

        nombre = "Camiseta"
        precio = 20.0
        stock = 10

        self.assertEqual(producto.nombre, nombre, "Error en el item Nombre")
        self.assertEqual(producto.precio, precio, "Error en el item Precio")
        self.assertEqual(producto.stock, stock, "Error en el item Stock")

if __name__ == '__main__':
    unittest.main()