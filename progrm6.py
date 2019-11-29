#program6
#t.taken
from math import pi
def circle(radius):
    area_cir=pi*(radius**2)
    perimeter=2*pi*radius
    inc_area_cir=(area_cir*0.05)+area_cir
    inc_perimeter=(perimeter*0.05)+perimeter
    print('the area of circle with 5% increment is:',inc_area_cir,'cm\u00b2\nThe perimeter of circle with 5% incriment is:',inc_perimeter,'cm\u00b2')
    return
radius=eval(input('enter the radius of circle:'))
circle(radius)
