import unittest  # Importa el módulo unittest, que proporciona un marco para escribir y ejecutar pruebas unitarias.
from Model.Control_Fertilizantes import ControlFertilizantes  # Importa la clase ControlFertilizantes del módulo Model.Control_Fertilizantes.

class TestControlFertilizantes(unittest.TestCase):  # Define una clase TestControlFertilizantes que hereda de unittest.TestCase, lo que significa que contiene métodos de prueba.
    def test_fecha_ultima_aplicacion(self):  # Define un método de prueba llamado test_fecha_ultima_aplicacion que verifica la fecha de última aplicación de un fertilizante.
        fertilizante = ControlFertilizantes("789", "Fertilizante Y", "Bimestral", 20.00, "2024-04-01")  # Crea una instancia de la clase ControlFertilizantes con valores específicos.
        self.assertEqual(fertilizante.fecha_ultima_aplicacion, "2024-04-01")  # Comprueba si la fecha de última aplicación del fertilizante es igual a "2024-04-01" usando el método assertEqual.
