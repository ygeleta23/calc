import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
    
    def test_div(self):
      self.assertEqual(self.calc.div(20, 5), 4)

    def test_pow(self):
      self.assertEqual(self.calc.pow(2, 3), 8)

    def test_sqrt(self):
      self.assertEqual(self.calc.sqrt(81), 9)