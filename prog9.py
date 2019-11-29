def even_odd(str):
    res=[int(i)for i in str.split() if i.isdigit()]
    even_list=[]
    odd_list=[]
    for i in res:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print('even lst is:',even_list)
    print('odd lst is:',odd_list)
    return
str=input('enter your string:')
even_odd(str)

