import unittest
from Components.Model.ProductoControl import ProductoControl

class TestProductoControl(unittest.TestCase):
    def test_constructor(self):
        producto = ProductoControl("123ABC", "Fertilizante A", "cada 15 días", 10)
        self.assertEqual(producto.registro_ICA, "123ABC")
        self.assertEqual(producto.nombre, "Fertilizante A")
        self.assertEqual(producto.frecuencia_aplicacion, "cada 15 días")
        self.assertEqual(producto.valor, 10)

if __name__ == "__main__":
    unittest.main()
