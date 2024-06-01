#inja mikham vaseye file two.py k 4ta amale riazi ro anjam mide test benevisam k ba pytest ejrashon konam. barkhalafe unittest k majbor bodim
#ye seri chizaro import konim va hatman az assertequal o khanevadash estefade konim o hataman class base bashan o on class az (unittest.TestCase) ers bari kone o ....
#dg vase pytest majbor nistim onkararo bokonim kheili sade test minevissim va faghat az kalameye kilidie assert estefade mikonim


import two

def test_add():
    assert two.add(33,5) == 38
    assert two.add(0,12) == 12    
    
def test_sub():
    assert two.sub(30,6) == 24
    assert two.sub(0,12) == -12

def test_mul():
    assert two.mul(3,5) == 15
    assert two.mul(0,12) == 0

def test_div():
    assert two.div(30,5) == 6
    assert two.div(11,1) == 11

                