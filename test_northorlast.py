import unittest
import nthorlast

class NthOrLastTest(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(nthorlast.nth_or_last(range(4) , 2) ,2)
        self.assertEqual(nthorlast.nth_or_last(range(2) , 2) ,1)