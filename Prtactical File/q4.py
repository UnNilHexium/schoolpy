def gen(n):
    if n == 1:
        fib=[0]
    elif n >= 2:
        fib=[0,1]
        for i in range(2,n):
            x=fib[i-2]+fib[i-1]
            fib.append(x)
    return fib
n=int(input("Please enter no. of terms"))
fib=gen(n)
print(fib)
for i in fib:
    print(i," ","*"*i)