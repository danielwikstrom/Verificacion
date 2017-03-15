# -*- coding: utf-8 -*-

from .context import sample

import unittest


class CoreTestSuite(unittest.TestCase):
    """Test cases for Core"""
    def test_countTwoWords(self):
        result = sample.analIce("patta macarron")
        self.assertEqual(len(result),2)

    def test_countSameWord(self):
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

if __name__ == '__main__':
    unittest.main()
