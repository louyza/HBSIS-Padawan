import unittest
from pad_647.app.pad_647 import Accum

class TestPad647(unittest.TestCase):

    def test_acumulador(self):
        a = Accum()
        result = a.acumulador()

        self.assertEqual(result, "A-Bb-Ccc-Dddd-")

    def test_instancia(self):
        a = Accum()
        result = a.acumulador()

        self.assertIsInstance(a, Accum)


