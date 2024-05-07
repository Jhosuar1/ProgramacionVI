import unittest  # Importa el módulo de pruebas unitarias de Python.
from Model.Factura import Factura  # Importa la clase Factura desde el módulo Model.Factura.

class TestFactura(unittest.TestCase):  # Define una clase de pruebas que hereda de unittest.TestCase.
    def test_fecha(self):  # Define un método de prueba llamado test_fecha.
        factura = Factura("2024-04-10", 100.00)  # Crea una instancia de la clase Factura con la fecha "2024-04-10" y el monto 100.00.
        self.assertEqual(factura.fecha, "2024-04-10")  # Verifica que el atributo fecha de la factura sea "2024-04-10".