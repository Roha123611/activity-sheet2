#program4
#t.taken 8min
list=[]
b=int(input('Enter the size of list:'))
for i in range(0,b):
    print('Enter the number at location:',i)
    number=int(input())
    list.append(number)
print(list)
def evenAdder(list):
    even=[]
    odd=[]
    for i in list:
        if (i%2==1):
            print('sorry odd number')
            for i in list:
                if(i%2==0):
                    even.append(i)
                    print(even)
                    sumofeven=sum(even)
                    print('the sumof even number in list is:',sumofeven)
    return
evenAdder(list)