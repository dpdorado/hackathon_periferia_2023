from django.test import TestCase
import unittest
from mutants.tests import StatsViewSetTestCase, MutantViewSetTestCase

'''test_suite = unittest.TestSuite()
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(StatsViewSetTestCase))
runner = unittest.TextTestRunner()
runner.run(test_suite)'''

#test_suite = unittest.TestSuite()
#test_suite.addTest(unittest.makeSuite(StatsViewSetTestCase))
##test_suite.addTest(unittest.makeSuite(MutantViewSetTestCase))

#test_runner = unittest.TextTestRunner(verbosity=0)
#test_result = test_runner.run(test_suite)

#num_tests = test_result.testsRun
'''num_failures = len(test_result.failures)
num_errors = len(test_result.errors)

num_successes = num_tests - num_failures - num_errors

print("Resumen de las pruebas:")
print(f"Casos de prueba exitosos: {num_successes}")
print(f"Casos de prueba fallidos: {num_failures}")
print(f"Casos de prueba con errores: {num_errors}")'''