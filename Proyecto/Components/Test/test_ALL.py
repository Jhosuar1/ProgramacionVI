import unittest  # Importa el módulo unittest para realizar pruebas unitarias.

from Test.test_ProductoControl import TestProductoControl  # Importa la clase TestProductoControl desde el módulo test_ProductoControl.
from Test.test_ControlPlagas import TestControlPlagas  # Importa la clase TestControlPlagas desde el módulo test_ControlPlagas.
from Test.test_ControlFertilizantes import TestControlFertilizantes  # Importa la clase TestControlFertilizantes desde el módulo test_ControlFertilizantes.
from Test.test_Antibiotico import TestAntibiotico  # Importa la clase TestAntibiotico desde el módulo test_Antibiotico.
from Test.test_Cliente import TestCliente  # Importa la clase TestCliente desde el módulo test_Cliente.
from Test.test_Factura import TestFactura  # Importa la clase TestFactura desde el módulo test_Factura.

def suite():  # Define una función llamada suite para agrupar las pruebas unitarias.
    test_suite = unittest.TestSuite()  # Crea un objeto TestSuite para almacenar las pruebas.
    test_suite.addTest(unittest.makeSuite(TestProductoControl))  # Agrega todas las pruebas de la clase TestProductoControl al conjunto de pruebas.
    test_suite.addTest(unittest.makeSuite(TestControlPlagas))  # Agrega todas las pruebas de la clase TestControlPlagas al conjunto de pruebas.
    test_suite.addTest(unittest.makeSuite(TestControlFertilizantes))  # Agrega todas las pruebas de la clase TestControlFertilizantes al conjunto de pruebas.
    test_suite.addTest(unittest.makeSuite(TestAntibiotico))  # Agrega todas las pruebas de la clase TestAntibiotico al conjunto de pruebas.
    test_suite.addTest(unittest.makeSuite(TestCliente))  # Agrega todas las pruebas de la clase TestCliente al conjunto de pruebas.
    test_suite.addTest(unittest.makeSuite(TestFactura))  # Agrega todas las pruebas de la clase TestFactura al conjunto de pruebas.
    return test_suite  # Devuelve el conjunto de pruebas.

if __name__ == '__main__':  # Comprueba si el script se ejecuta directamente.
    all_tests = suite()  # Obtiene todas las pruebas definidas en la función suite.
    runner = unittest.TextTestRunner()  # Crea un corredor de pruebas que muestra los resultados en la consola.
    runner.run(all_tests)  # Ejecuta todas las pruebas y muestra los resultados en la consola.

