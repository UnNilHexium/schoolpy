import random as r

def rend_gen(n):
    x=10**(n-1) #so for x=2. range is 10-99
    y=(10**n)-1 #       x=3. range is 100-999
    z=r.randint(x,y) #incluive of both x and y
    print(z)
    return

a = int(input("Please enter no. of digit in random no needed :"))
rand_gen(a)