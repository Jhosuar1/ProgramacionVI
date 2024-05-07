import unittest  # Importa el módulo unittest para realizar pruebas unitarias.
from Model.Cliente import Cliente  # Importa la clase Cliente del módulo Model.

class TestCliente(unittest.TestCase):  # Define una clase de pruebas que hereda de unittest.TestCase.
    def test_nombre(self):  # Define un método de prueba llamado test_nombre.
        cliente = Cliente("Juan Pérez", "123456789")  # Crea una instancia de la clase Cliente con el nombre "Juan Pérez" y el número de identificación "123456789".
        self.assertEqual(cliente.nombre, "Juan Pérez")  # Comprueba si el nombre del cliente es igual a "Juan Pérez".
