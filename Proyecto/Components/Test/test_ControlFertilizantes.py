import unittest
from Model.Control_Fertilizantes import ControlFertilizantes

class TestControlFertilizantes(unittest.TestCase):
    def test_fecha_ultima_aplicacion(self):
        fertilizante = ControlFertilizantes("789", "Fertilizante Y", "Bimestral", 20.00, "2024-04-01")
        self.assertEqual(fertilizante.fecha_ultima_aplicacion, "2024-04-01")

    # Agrega más pruebas para otros métodos y casos de uso
