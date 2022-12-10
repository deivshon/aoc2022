import unittest

from solutions.list import *

class TestSolutions(unittest.TestCase):
    def testAll(self):
        for s in solutionTests:
            s[INIT]()
            self.assertEqual(s[FIRST](), s[RES_FIRST])
            self.assertEqual(s[SECOND](), s[RES_SECOND])
