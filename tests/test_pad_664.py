import unittest
from pad_664.app.pad_664 import Carinhas

class TestPad664(unittest.TestCase):

    def test_day(self):
        p = Carinhas()
        lista = [';]', ':[', ';*', ':$', ';-D']
        result = p.valida_carinhas(lista)

        self.assertEqual(result, 1)

    def test_instancia(self):
        p = Carinhas()
        lista = [';]', ':[', ';*', ':$', ';-D']
        result = p.valida_carinhas(lista)

        self.assertIsInstance(p, Carinhas)

