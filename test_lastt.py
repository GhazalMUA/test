import unittest
import lastt



class test_last(unittest.TestCase):
    def test_basic(self):
        casses=[
            (range (4) , 3) ,
            (iter(range(4)), 3) ,                  #tamame halathai k momkene pish biad ro neveshtim 
            ((range(1)),0) , 
            (iter(range(1)),0) ,                             
            ({n:str(n) for n in range(5)} , 4)     #in male vaghtie ke vorodimon string bashe, masalan 'ghazal' bashe
         ]
    
        for iterable , expected in casses:         #chonke casses y list hast k toosh tuple darim va tooye tuple ha 2ta arguman hast bayad intori vasash halghe bnevisim. tooye tuple ha item aval chizie k mikhaymm bjaye parametre iterable befrestim b last()  va excepted on chizie k entezar darim khorojie function last() bashe.
            
            with self.subTest(iterable=iterable):    #in line ro mitonid nanevisid vali bhtare benevisid. age benevisidesh, vaghti b error barkhord kardin, bhton mige daghiighan  beyne on casses ha koja irad hastesh.
                self.assertEqual(lastt.last(iterable), expected)
                
            
    def test_default(self):
        for iterable,default,expected in [ 
            (range(2) , None , 1) ,
            ([] ,None , None) , 
            ({} , None, None) ,
            (iter([]), None , None)            
        ]:
            with self.subTest(argse=(iterable,default)):       #swubTest hamishe bayad ba with ejra bshe chon context manager hastesh
                self.assertEqual(lastt.last(iterable,default) , expected)        
                
                

if __name__ == "__main__":
    unittest.main()