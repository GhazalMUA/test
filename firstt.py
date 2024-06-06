'''
    mikhaym function first besazim k y object iterable mesle list migire va item aval esh ro barmigardoone. age ham beehesh y default bedim, vaghti ke liste khalli bhsh midim on default ro barmigardoone
'''

_marker=object()
def first(iterable,default=_marker):     # defaul
    try:
        return next(iter(iterable))           #itaratable hamon listie k bbhesh midim. iter(iterable) yani oon liste ro tike kon. next(harchi) yani avalisho bede
    except StopIteration as e:                     #inja mige check kon bbin stopiteration etefagh oftde ya na age etefagh oftade bod bbin karbar default ferestadae vassat ya na age feerestade bod behehsh hamon default ro bargardon ag ham na beehesh on error ro neshoon bede
            if default is _marker:
                raise ValueError ('first() was called with no iterable and no  default value was provided') from e
            return default    


