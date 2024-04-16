import unittest
from Model import Antibiotico

class TestAntibiotico(unittest.TestCase):
    def test_nombre(self):
        antibiotico = Antibiotico("Antibiótico Z", 500, "Bovinos", 30.50)
        self.assertEqual(antibiotico.nombre, "Antibiótico Z")

    # Agrega más pruebas para otros métodos y casos de uso
