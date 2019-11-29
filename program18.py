#prog18
#t.taken
from math import pi
def area(l,r):
    areasqr=l**2
    print('area of sqr is:',areasqr,'cm\u00b2')
    area_circle=pi*r**2
    print('area of circle is:',area_circle,'cm\u00b2')
    if areasqr>area_circle:
        x=areasqr-area_circle
        print('the remaing area is:',x,'cm\u00b2')
    else:
        x=area_circle-areasqr
        print('the remaining area is:',x,'cm\u00b2')
    return
l=eval(input('enter lenght square:'))
r=eval(input('enter radius of circle:'))
area(l,r)
