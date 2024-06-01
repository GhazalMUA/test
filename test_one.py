import unittest
from one import Person


class PersonTest(unittest.TestCase):
    """
    in yest baraye class person hastesh k tooye file one.py hastesh. baraye test function hay email va fullname bayad az class person instance besazim va chon inja mikhaym 2ta method ro test konim nhatman bayad jologiri konim az code tekrari(mazoor hamon instance hast)
    pas tooye class PersonTest , az method haye setup va teardown estefade mikonim setup ghabl az hameye methodha va teardown badaz hameye methodha ejra mishe
    
    """    
    
    def setUp(self):
        self.p1=Person('ghazal' , 'hafezi')
        self.p2=Person('amir' , 'hatami')
    
    def test_fullname(self):
        self.assertEqual(self.p1.fullname() , 'ghazal hafezi')
        self.assertEqual(self.p2.fullname() , 'amir hatami')

    def test_email(self):
        self.assertEqual(self.p1.email() , 'ghazalhafezi@gmail.com')
        self.assertEqual(self.p2.email() , 'amirhatami@gmail.com')


if __name__ == '__main__':
        unittest.main()