#program1
#t.taken 10min
def fun():
    from math import pi
    import math
    base_tri=int(input('Enter the base of triangle:'))
    radius_circle=float(input('Enter the radius of circle:'))
    area_tri=(math.sqrt(3)/4)*base_tri**2
    area_tri6=area_tri*6
    area_circle=pi*(radius_circle**2)
    shaded_area=area_tri6-area_circle
    print('shaded area of triangle is:',shaded_area,'cm')
fun()