import unittest
from Components.Model.ProductoControl import TestProductoControl
from Components.Model.Control_Plagas import TestControlPlagas
from Components.Model.Control_Fertilizantes import TestControlFertilizantes
from Components.Model.Antibiotico import TestAntibiotico
from Components.Model.Cliente import TestCliente
from Components.Model.Factura import TestFactura
from Components.Model.Pedido import TestPedido

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestProductoControl))
    suite.addTest(unittest.makeSuite(TestControlPlagas))
    suite.addTest(unittest.makeSuite(TestControlFertilizantes))
    suite.addTest(unittest.makeSuite(TestAntibiotico))
    suite.addTest(unittest.makeSuite(TestCliente))
    suite.addTest(unittest.makeSuite(TestFactura))
    suite.addTest(unittest.makeSuite(TestPedido))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    print("\nAnalizando pruebas:")
    for test_result in result.failures:
        print("\nPrueba fallida:", test_result[0])
        print(test_result[1])
    if result.wasSuccessful():
        print("\nTodas las pruebas se ejecutaron correctamente.")
    else:
        print("\nAl menos una prueba falló. Revisa los detalles.")
