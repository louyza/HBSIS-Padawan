import unittest
from pad_646.app.pad_646 import PalavraMeio


class TestPad646(unittest.TestCase):

    def test_achar_meio_par(self):
        p = PalavraMeio()
        result = p.achar_meio('batata')

        self.assertEqual(result, "ta")
        self.assertEqual(p.achar_meio("self"), "el")
        self.assertEqual(p.achar_meio("selfing"), "f")
        self.assertEqual(p.achar_meio("middle"), "dd")
        self.assertEqual(p.achar_meio("A"), "A")
        self.assertEqual(p.achar_meio("of"), "of")

    def test_achar_meio_impar(self):
        p = PalavraMeio()
        result = p.achar_meio('uva')

        self.assertEqual(result, "v")

    def test_instancia(self):
        p = PalavraMeio()
        result = p.achar_meio('uva')

        self.assertIsInstance(p, PalavraMeio)


