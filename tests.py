import unittest

from solutions.list import *

def testDay(self, solution):
    solution[INIT]()
    self.assertEqual(solution[FIRST](), solution[RES_FIRST])
    self.assertEqual(solution[SECOND](), solution[RES_SECOND])

class TestSolutions(unittest.TestCase):
    def testDay01(self):
        testDay(self, solution01)

    def testDay02(self):
        testDay(self, solution02)

    def testDay03(self):
        testDay(self, solution03)

    def testDay04(self):
        testDay(self, solution04)

    def testDay05(self):
        testDay(self, solution05)

    def testDay06(self):
        testDay(self, solution06)

    def testDay07(self):
        testDay(self, solution07)

    def testDay08(self):
        testDay(self, solution08)

    def testDay09(self):
        testDay(self, solution09)

    def testDay10(self):
        testDay(self, solution10)
