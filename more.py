from itertools import islice
from functools import partial

def take(iterable,n):
    return list(islice(iterable,n))


def chunked(iterable,n,strict=False):
    iterator= iter ( partial (take , iter(iterable),n) , [] )             #method partial be onvane arguman aval y function migire arguman hay baadi parametr hay on function ro migire k betone on function ro ejra bokone. dar vaghe mishe in:     'partial(take,iterable,n)'  vali miaym az function 'iter' estefade mikonim ke betone tike tike bokone on paarametre iterable moon ro. ba iter y hamchin chizi darim:  ' iterator=partial(take , iter(iterable),n)  '    khode function iter ag berim tooye source codesh mibinim k be do sorat mishe azash estefade kard yeki inke ye object iterable behshe bedim va on vaasamon tike ash bokone. ye halaate dg ham dare k object iterable migire azamon va ye parametr be esme 'sentinel' ke mige onghadr becharkh ta be on shekli k man mikham dar biay. hala inja ma mikham inghadr becharkhe ta y list khali behem,on bede. dar nahayat kole in partial ro mizarim tooye y iter va behesh ye sentinel midim.
    if strict:                                                #vase bakhshe strict=true mikhaym begim age tedade item hay avalie bar on n bakhsh pazir nabod behemon error bede nemikhyam list e tike dashte bashim
        if n is None:
            raise ValueError('n can`t be None while strict is true')
        def ret():
            for chunk in iterator:
                if len(chunk) != n:
                    raise ValueError('iterator is not divisible by n')
                yield(chunk)
        return iter(ret())        
    return iterator










