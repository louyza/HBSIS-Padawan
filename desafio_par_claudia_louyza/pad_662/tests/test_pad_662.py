# import unittest
# from pad_662 import iq_test
#
#
# class TestPad662(unittest.TestCase):
#
#     def test_iq_test(self):
#         self.assertEqual(iq_test("2 4 7 8 10"), 3)

import unittest
from pad_662.app.pad_662 import VerificarDiferente

class TestPad662(unittest.TestCase):

    def test_verifica_if(self):
        d = VerificarDiferente()
        lista=[2, 4, 7, 8, 10]
        result = d.verifica(lista)

        self.assertEqual(result, 3)

    def test_verifica_else(self):
        d = VerificarDiferente()
        lista=[1, 2, 1, 1]
        result = d.verifica(lista)

        self.assertEqual(result, 2)

    def test_instancia(self):
        d = VerificarDiferente()
        lista = [1, 2, 1, 1]
        result = d.verifica(lista)

        self.assertIsInstance(d, VerificarDiferente)


