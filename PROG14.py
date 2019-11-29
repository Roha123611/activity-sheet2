#PROGRAM14
#T.TAKEN
def area(l1,l2,b1,b2):
    area1=l1*b1
    print('area of 1st rectangle is:',area1,'cm\u00b2')
    area2=l2*b2
    print('area of 2nd rectangle is:',area2,'cm\u00b2')
    if l1>l2 or b1>b2:
        q=area1-area2
        print('the remaining area is:',q,'cm\u00b2')
    else:
        q=area2-area1
        print('the remainig area is:',q,'cm\u00b2')
        return
l1=eval(input('enter the 1st lenght:'))
l2=eval(input('enter the 2nd lenght:'))
b1=eval(input('enter the 1st breath:'))
b2=eval(input('enter the 2nd breath:'))
area(l1,l2,b1,b2)
