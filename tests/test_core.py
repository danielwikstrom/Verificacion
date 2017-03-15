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
    def test_countTwoWords(self):
        result = sample.analIce("patta patta")
        self.assertEqual(result[0][1],2)
if __name__ == '__main__':
    unittest.main()
