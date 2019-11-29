#prog8
#t.taken
def rectangular(length,breath):
    area=length*breath
    perimeter=(2*breath)+(2*breath)
    inc_area=(area*0.08)+area
    inc_perimeter=(perimeter*0.08)+perimeter
    print('the area of rectangle with 8% incriment is:',inc_area,'cm\u00b2\nthe perimeter of')
    return
length=int(input('enter the length:'))
breath=int(input('enter the breath'))
rectangular(length,breath)