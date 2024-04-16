import unittest
from Test.test_ProductoControl import TestProductoControl
from Test.test_ControlPlagas import TestControlPlagas
from Test.test_ControlFertilizantes import TestControlFertilizantes
from Test.test_Antibiotico import TestAntibiotico
from Test.test_Cliente import TestCliente
from Test.test_Factura import TestFactura

class VerboseTestResult(unittest.TextTestResult):
    def startTest(self, test):
        super().startTest(test)
        print(f"Running test: {test.__class__.__name__}.{test._testMethodName}")

    def addSuccess(self, test):
        super().addSuccess(test)
        print("  - Result: OK")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"  - Result: ERROR\n    - {err[1]}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"  - Result: FAILURE\n    - {err[1]}")

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestProductoControl))
    test_suite.addTest(unittest.makeSuite(TestControlPlagas))
    test_suite.addTest(unittest.makeSuite(TestControlFertilizantes))
    test_suite.addTest(unittest.makeSuite(TestAntibiotico))
    test_suite.addTest(unittest.makeSuite(TestCliente))
    test_suite.addTest(unittest.makeSuite(TestFactura))
    return test_suite

if __name__ == '__main__':
    all_tests = suite()
    runner = unittest.TextTestRunner(resultclass=VerboseTestResult)
    runner.run(all_tests)
