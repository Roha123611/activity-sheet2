#prog15
#t.taken
from fractions import Fraction
def addfraction(st_value,it_value):
    sum=0
    for i in range(st_value,it_value):
        sum=sum+Fraction(1,i)
    print('the sum of fractions is:',sum)
    return
st_value=int(input('input starting value of series:'))
it_value=int(input('enter ending value of series'))
addfraction(st_value,it_value)
