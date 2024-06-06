from lastt import last
from itertools import islice

'''
    in function gharare y list begire ba y index bad b ma value e on index ro neshoon bede 
    va age on index az tedade aazaye listemon bishtar bood, be naachaar adade akhar ro bargardoone
'''



_marker= object()

def nth_or_last(iterable,n , default=_marker):
    return last(islice(iterable , n+1)   , default=default)      # aval ino minevisim   `return islice(iterable , n)`     in manteghe slice e ta shomarei k beehesh midi tiike mikone . vali inja function nth_or_last ()  mikhad tebghe index kar kone pas code ro intori mikonim. ` return islice(iterable , n+1) `      hala k slice vasamon listemono ta indexee morede nsazaremon tike karde, nobate ine k akhario return konim. k miaym az function `last` k ghblan khodemon hminja sakhtim estefade mikonim. aval importesh mikonim vaa badesh kole dastanaro midim bhsh


