# import unittest
# from pad_653 import growing_plant
#
#
# class TestPad653(unittest.TestCase):
#
#     def test_growing_plant(self):
#         self.assertEqual(growing_plant(100, 10, 910), 10)

import unittest
from pad_653.app.pad_653 import Days

class TestPad653(unittest.TestCase):

    def test_day(self):
        p = Days()
        result = p.grow()

        self.assertEqual(result, 10)

    def test_instancia(self):
        p = Days()
        result = p.grow()

        self.assertIsInstance(p, Days)

