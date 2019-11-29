#prog12
#t.taken
from math import pi
def area(rad1,rad2):
    area1=pi*rad1**2
    area2=pi*rad2**2
    print('area of circle is:',area1,'cm\u00b2')
    print('area of circle is:',area2,'cm\u00b2')
    if rad1>rad2:
        r=area1-area2
        print('the remaining area is:',r,'cm\u00b2')
    else:
        r=area2-area1
        print('the remaining area is:',r,'cm\u00b2')
    return
rad1=eval(input('enter the radius 1 in cm:'))
rad2=eval(input('enter the radius 2 in cm:'))
area(rad1,rad2)

