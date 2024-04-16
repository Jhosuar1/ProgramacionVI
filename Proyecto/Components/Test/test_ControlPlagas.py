import unittest
from Model.Control_Plagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):
    def test_periodo_carencia(self):
        plagas = ControlPlagas("456", "Plaga X", "Mensual", 15.75, 30)
        self.assertEqual(plagas.periodo_carencia, 30)

    # Agrega más pruebas para otros métodos y casos de uso
