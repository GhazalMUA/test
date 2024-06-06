import unittest
import nthorlast

class NthOrLastTest(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(nthorlast.nth_or_last(range(4) , 2) ,2)
        self.assertEqual(nthorlast.nth_or_last(range(2) , 2) ,1)
        
        
    def test_default_value(self):
        default=60
        self.assertEqual(nthorlast.nth_or_last(range(2) , 1 , default), 1)
        self.assertEqual(nthorlast.nth_or_last([] ,1 , default), default)
        
    def test_empty_iterable_no_default(self):
        self.assertRaises(ValueError, lambda:nthorlast.nth_or_last([],0))    



if __name__ == "__main__":
    unittest.main()