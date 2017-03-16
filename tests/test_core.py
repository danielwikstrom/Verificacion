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

    def test_countSameWordTwoTimes(self):
        result = sample.analIce("patta patta")
        self.assertEqual(result[0][1],2)

    def test_emptyInputString(self):
        self.assertEqual(len(sample.analIce("")),0)

    def test_longInputString(self):
        numberOfMayors = 10000
        longString = ""
        for i in range(0,numberOfMayors):
            longString = longString + "Es el alcalde el que quiere que sean los vecinos el alcalde "
        self.assertEqual(sample.analIce(longString)[1][0],'alcalde')
        self.assertEqual(sample.analIce(longString)[1][1],numberOfMayors*2)

    def test_resultSortingCount(self):
        result = sample.analIce("tres tres tres dos dos uno")
        self.assertEqual(result[0][1],3)
        self.assertEqual(result[1][1],2)
        self.assertEqual(result[2][1],1)

    def test_resultSortingValues(self):
        result = sample.analIce("tres tres tres dos dos uno")
        self.assertEqual(result[0][0],'tres')
        self.assertEqual(result[1][0],'dos')
        self.assertEqual(result[2][0],'uno')

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

    def test_countStopword(self):
        result = sample.analIce("about all")
        self.assertEqual(len(result), 0)

    def test_countStopwordTogether(self):
        result = sample.analIce("aboutall the")
        self.assertEqual(len(result), 1)

    def test_countStopwordTogetherPoint(self):
        result = sample.analIce("about.all/the")
        self.assertEqual(len(result), 0)

    def test_countStopwordWithword(self):
        result = sample.analIce("Let me go in the")
        self.assertEqual(len(result), 2)

    def test_countStopwordWith(self):
        result = sample.analIce("a a all machine-gunball all machine")
        self.assertEqual(result[0][0], "machine")
        self.assertEqual(result[1][1], 1)

    def test_countStopwordWithCaps(self):
        result = sample.analIce("a an About how HoW about An a")
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
