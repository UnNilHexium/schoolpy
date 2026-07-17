import random

n=int(input("Enter number of digits in random number: "))
for i in range(n):
    if i == 0:
        x=str(random.randint(1,9))
    else:
        x=str(random.randing(0,9))