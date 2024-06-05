import unittest
import more

class TakeTests(unittest.TestCase):
    
    def test_simple_take(self):
        self.assertEqual(more.take(range(8) , 2), [0,1])
        
    def test_take_ngreater(self):
        self.assertEqual(more.take(range(3),8) , [0,1,2] )    
        
    def test_take_none(self):
        self.assertEqual(more.take([] , 4) , [])
        
    def test_take_negative(self):
        self.assertRaises(ValueError,more.take,range(10), -2)  
        
        
        
class ChunksTests(unittest.TestCase):
    
    
    def test_even(self):
        self.assertEqual(list(more.chunked(range(4),2)), [[0,1], [2,3]])
        
        
    def test_odd(self):
        self.assertEqual(list(more.chunked(range(5),2)),[[0,1],[2,3],[4]])    
    
    
    def test_n_none(self):
        self.assertEqual(list(more.chunked(range(3), None)), [[0,1,2]])
        
        
    def test_strict_false(self):
        self.assertEqual(list(more.chunked(range(3),2)), [[0,1],[2]])    
        
        
    def test_strict_true(self):          #chonke chandta moredo mikhaym barresi konim aval ye function misazim base mon ro toosh gharraar midim
        def f():
            return list(more.chunked(range(5),2, strict=True))
        self.assertRaisesRegex(ValueError,'iterator is not divisible by n' , f)
        self.assertEqual(list(more.chunked(range(4),2,strict=True)), [[0,1],[2,3]])
        
        
    def test_strict_true_size_none(self):    
        def f():
            return list(more.chunked( range(4), None, strict=True ))
        self.assertRaisesRegex(ValueError,'n can`t be None while strict is true',f)
                           
        
if __name__ == '__main__':
    unittest.main()        