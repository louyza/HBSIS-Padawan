# import unittest
# from pad_649 import find_short
#
#
# class TestPad649(unittest.TestCase):
#
#     def test_find_short(self):
#         self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)

import unittest
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from pad_649.app.app import PalavraMenor

class test_palavra_menor (TestCase):

    def test_palavra_menor(self):
        mp = PalavraMenor()
        resultado = mp.menor()
        self.assertEqual(resultado, 3)

    def test_instancia(self):
        mp = PalavraMenor()
        self.assertIsInstance(mp, PalavraMenor)

