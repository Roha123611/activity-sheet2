#program13
#t.taken
def count(str):
    count_upper=0
    count_lower=0
    for i in str:
        if(i.islower()):
            count_lower=count_lower+1
        elif(i.isupper()):
            count_upper=count_upper+1
    print('number of lower case:',count_lower)
    print('number of upper case:',count_upper)
    return
str=str(input('enter your str:'))
count(str)

