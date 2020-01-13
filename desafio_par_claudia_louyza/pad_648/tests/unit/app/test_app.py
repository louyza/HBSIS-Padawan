import unittest
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pad_648.app.app import Vogais

class Teste_Exercicio_2(TestCase):

    def test_pegar_vogais(self):
        vog = Vogais()
        resultado = vog.pegar_vogais()
        self.assertEqual(resultado, 12)

    def test_instancia(self):
        vog = Vogais()
        self.assertIsInstance(vog, Vogais)

