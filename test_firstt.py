import firstt
import unittest
import traceback


class test_first(unittest.TestCase):
    
    def test_crowd_list(self):
        self.assertEqual(firstt.first([11,2,3,4,5,6]),11)
        
    def test_one_item_in_list(self): 
        self.assertEqual(firstt.first([5]),5)
        
    def test_empty_list_with_default(self):
        self.assertEqual(firstt.first([],'boo'),'boo')
        
    def test_empty_list_without_default(self):
        try:
            firstt.first([])
        except ValueError:
            formatted_exception= traceback.format_exc()                 
            self.assertIn('StopIteration' , formatted_exception)        #in line mige jomleye `StopIteration` bayad tooye formatted_Exception vojod dashte bashe
            self.assertIn('The above exception was the direct cause' , formatted_exception)
        else:
            self.fail()    