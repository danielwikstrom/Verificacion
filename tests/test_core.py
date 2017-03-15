# -*- coding: utf-8 -*-

from .context import sample

import unittest


class CoreTestSuite(unittest.TestCase):
    """Test cases for Core"""
    def test_countTwoWords(self):
        result = sample.analIce("patta macarron")
        self.assertEqual(len(result),2)
    def test_groupSameWord(self):
        result = sample.analIce("patta patta")
        self.assertEqual(len(result),1)
    def test_countTwoWords(self):
        result = sample.analIce("patta patta")
        self.assertEqual(result[0][1],2)
    def test_question(self):
        result= sample.analIce("¿dónde esta la lista?")
        self.assertEqual(len(result),4)
    def test_simbolNotIncluded(self):
        result = sample.analIce(".:...:.:::.:?¿!perro")
        self.assertEqual(result[0][0],'perro')
        self.assertEqual(len(result),1)
    def test_simbolSeparateWords(self):
        result = sample.analIce("verificar!pudiendo?verificar")
        self.assertEqual(result[0][0],'verificar')
        self.assertEqual(result[0][1],2)
        self.assertEqual(result[1][0], 'pudiendo')
        self.assertEqual(len(result),2)
    def test_onlySimbols(self):
        result = sample.analIce("::::,!¡¿?[]{}();")
        self.assertEqual(len(result),0)
    def test_apostrophe(self):
        result = sample.analIce("y'all wanna kill y'all?")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0],"y'all")
    def test_accentMark(self):
        result = sample.analIce("Quién")
        self.assertEqual(result[0][0], u"quién")
    def test_accentCaps(self):
        result = sample.analIce("QuiÉn")
        self.assertEqual(result[0][0], u"quién")
    def test_email(self):
        result = sample.analIce("juan.gomez@live.u-tad.com")
        self.assertEqual(len(result),6)
    def test_tabulation(self):
        result = sample.analIce("hola   que tal ")
        self.assertEqual(len(result), 3)
    def test_dieresis(self):
        result = sample.analIce("pingüino")
        self.assertEqual(result[0][0],u"pingüino")
    def test_virgulilla(self):
        result = sample.analIce("años")
        self.assertEqual(result[0][0],u"años")



if __name__ == '__main__':
    unittest.main()
