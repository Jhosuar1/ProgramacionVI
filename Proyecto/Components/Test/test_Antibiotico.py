import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from Model.Antibiotico import Antibiotico  # Importa la clase Antibiotico del módulo Model.

class TestAntibiotico(unittest.TestCase):  # Define una clase de prueba llamada TestAntibiotico que hereda de unittest.TestCase.
    def test_nombre(self):  # Define un método de prueba llamado test_nombre.
        antibiotico = Antibiotico("Antibiótico Z", 500, "Bovinos", 30.50) # Crea una instancia de la clase Antibiotico con los argumentos proporcionados.
        self.assertEqual(antibiotico.nombre, "Antibiótico Z")# Verifica si el atributo nombre de la instancia antibiotico es igual a "Antibiótico Z".
        
