import unittest
from Model.Pedido import Pedido

class TestPedido(unittest.TestCase):
    def test_fecha_entrega(self):
        pedido = Pedido("2024-04-12", 150.00)
        self.assertEqual(pedido.fecha_entrega, "2024-04-12")

    # Agrega más pruebas para otros métodos y casos de uso
