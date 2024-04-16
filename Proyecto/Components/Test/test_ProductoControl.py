import unittest
from Model.ProductoControl import ProductoControl

class TestProductoControl(unittest.TestCase):
    def test_registro_ICA(self):
        producto = ProductoControl("123", "Producto A", "Quincenal", 10.50)
        self.assertEqual(producto.registro_ICA, "123")

    # Agrega más pruebas para otros métodos y casos de uso
