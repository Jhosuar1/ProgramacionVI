import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from Model.ProductoControl import ProductoControl  # Importa la clase ProductoControl desde el módulo Model.

class TestProductoControl(unittest.TestCase):  # Define una clase de prueba que hereda de unittest.TestCase.
    def test_registro_ICA(self):  # Define un método de prueba llamado test_registro_ICA.
        producto = ProductoControl("123", "Producto A", "Quincenal", 10.50)  # Crea una instancia de ProductoControl con valores específicos.
        self.assertEqual(producto.registro_ICA, "123")  # Comprueba si el atributo registro_ICA del producto es igual a "123" y reporta el resultado.