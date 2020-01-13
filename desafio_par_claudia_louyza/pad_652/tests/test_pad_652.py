# import unittest
# from pad_652 import db_sort
#
#
# class TestPad652(unittest.TestCase):
#
#     def test_db_sort(self):
#         self.assertEqual(db_sort(
#             ["Banana", "Orange", "Apple", "Mango", 0, 2, 2]),
#             [0, 2, 2, "Apple", "Banana", "Mango", "Orange"]
#         )

import unittest
from pad_652.app.pad_652 import Matrizes

class TestPad652(unittest.TestCase):

    def test_matrizes(self):
        m = Matrizes()
        result = m.retornar_organizado()

        self.assertEqual(result, [2, 2, 7, 'Apple', 'Banana', 'Mango', 'Orange'])

    def test_instancia(self):
        m = Matrizes()
        result = m.retornar_organizado()

        self.assertIsInstance(m, Matrizes)

