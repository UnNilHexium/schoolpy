import random as r

def rand_gen_v2(a):
    for i in range(a):
        x=r.randint(0,9)
        print(x,end="")
a = int(input("Please enter no. of digit in random no needed :"))
rand_gen_v2(a)