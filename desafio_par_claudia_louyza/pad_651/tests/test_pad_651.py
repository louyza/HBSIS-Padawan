import unittest
from pad_651.app.pad_651 import Quadrado

class TestPad651(unittest.TestCase):

    def test_quadrado(self):
        a = Quadrado()
        result = a.quadrado()

        self.assertEqual(result, 811181)

    def test_instancia(self):
        a = Quadrado()
        result = a.quadrado()

        self.assertIsInstance(a, Quadrado)


