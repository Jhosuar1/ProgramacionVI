import unittest
from Model.Cliente import Cliente

class TestCliente(unittest.TestCase):
    def test_nombre(self):
        cliente = Cliente("Juan Pérez", "123456789")
        self.assertEqual(cliente.nombre, "Juan Pérez")

    # Agrega más pruebas para otros métodos y casos de uso
