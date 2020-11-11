import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_5_10_returns_5_is_less_than_10(self):
        self.assertEqual("5 is less than 10", compare(5,10))
    
    # I picked these numbers for the test before looking at the solution weirdly
    def test_compare_4_4_returns_4_is_equal_to_4(self):
        self.assertEqual("4 is equal to 4", compare(4, 4))