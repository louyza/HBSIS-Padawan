import unittest
from pad_650.app.pad_650 import PAD_650
from pad_650.app.bootstrap import StartUp


class TestPad650(unittest.TestCase):

    def test_descending_order(self):
        execicio = PAD_650()
        resultado = execicio.descending_order()

        self.assertEqual(resultado, 9876543210)

    def test_instancia_Exercicio01(self):
        execicio = PAD_650()
        execicio.descending_order()

        self.assertIsInstance(execicio, PAD_650)


    def test_instancia_startup(self):
        startup = StartUp()
        startup.execute()

        self.assertIsInstance(startup, StartUp)

    def test_bootstrap(self):
        startup = StartUp()
        startup.execute()

        execicio = PAD_650()
        execicio.descending_order()

        self.assertEqual(execicio.descending_order(), 9876543210)
