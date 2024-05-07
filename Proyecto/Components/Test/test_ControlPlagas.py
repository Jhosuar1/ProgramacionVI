import unittest  # Importa el módulo de unittest para realizar pruebas unitarias
from Model.Control_Plagas import ControlPlagas  # Importa la clase ControlPlagas desde el módulo Model.Control_Plagas

class TestControlPlagas(unittest.TestCase):  # Define una clase de pruebas que hereda de unittest.TestCase
    def test_periodo_carencia(self):  # Define un método de prueba llamado test_periodo_carencia
        plagas = ControlPlagas("456", "Plaga X", "Mensual", 15.75, 30)  # Crea una instancia de la clase ControlPlagas con valores específicos para realizar la prueba
        self.assertEqual(plagas.periodo_carencia, 30)  # Comprueba si el atributo periodo_carencia de la instancia plagas es igual a 30
        