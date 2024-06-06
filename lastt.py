
from collections import deque
from collections.abc import Sequence

_marker=object()                  # object()  yani khali. yani vaghti meghdare default empty hast va karbar defaulti vasamon vared nakardee
 
def last(iterable,default=_marker):
    
    try:
        if isinstance(iterable,Sequence):                   #inja check mikonim k aya on objecte iterable yek sequence ya hamon donbale hastesh ya naa. `Sequence` ke az module collection import esh kardim karesh check kardane hamine ke bbine ye objecti donbale hast ya na                                  
            return iterable[-1]                             #[-1] yani akharin item e ye list ya tuple ya dictionary (kolan sequence)
        
        elif hasattr(iterable,'__reversed__'):               #inja ba hasattr mitonim check konim felan object ya felan class ya felan function, tooye delesh felan method ro dare yaaa na.
            return next(reversed(iterable))                 # reversed(iterable) yani on object eto barax kon va `next` ham hamontor k az ghabl midonim yani az liste jadid (ke hala barax shodan item hash) morede aval ro biar
        
        else:
            return deque(iterable, maxlen=1)[-1]                #deque ham function az module collection hastesh k mesle list amal mikone ag source codesho negah koni ye iterable migire ba yedone maxlen
                                                               
                                                                #ta inja ye if neveshtim ba y elif ba y else ke hamaeye ina ye seri exception momkenen dashte bashan vase hamin hamashono mizaarim tooye try
                                                                
    except (IndexError,StopIteration,TypeError):                #3 noe exception momkene k pish biad yeli indexerror k marboot b `isinstance` hast va male vaghtie ke index akhar ro peyda nakone.  `StopIteration` male vaghtie ke dari az `next` estefade mikoni va be stopiteration barbokhore. `TypeError` male deque
        if default is _marker:
            raise ValueError('you called last() with empty iterable with no default')
        else:
            return default
       
       
l=[]        
print(last(l , 'manobebin'))