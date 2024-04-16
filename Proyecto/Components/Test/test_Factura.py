import unittest
from Model.Factura import Factura

class TestFactura(unittest.TestCase):
    def test_fecha(self):
        factura = Factura("2024-04-10", 100.00)
        self.assertEqual(factura.fecha, "2024-04-10")

    # Agrega más pruebas para otros métodos y casos de uso
