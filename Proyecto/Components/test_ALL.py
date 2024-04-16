import unittest
from Test.test_ProductoControl import TestProductoControl
from Test.test_ControlPlagas import TestControlPlagas
from Test.test_ControlFertilizantes import TestControlFertilizantes
from Test.test_Antibiotico import TestAntibiotico
from Test.test_Cliente import TestCliente
from Test.test_Factura import TestFactura
from Test.test_Pedido import TestPedido

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestProductoControl))
    test_suite.addTest(unittest.makeSuite(TestControlPlagas))
    test_suite.addTest(unittest.makeSuite(TestControlFertilizantes))
    test_suite.addTest(unittest.makeSuite(TestAntibiotico))
    test_suite.addTest(unittest.makeSuite(TestCliente))
    test_suite.addTest(unittest.makeSuite(TestFactura))
    test_suite.addTest(unittest.makeSuite(TestPedido))
    return test_suite

if __name__ == '__main__':
    all_tests = suite()
    runner = unittest.TextTestRunner()
    runner.run(all_tests)
