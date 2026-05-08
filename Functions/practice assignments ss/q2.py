def Check(a):
    L=0
    D=0
    for i in a:
        if i.isalpha():
            L+=1
        elif i.isdigit():
            D+=1
        else:
            pass
    return(L,D)
s=input('Write a Sentence: ')
x,y=Check(s)
print('Letters:',x,'Digits:',y)
