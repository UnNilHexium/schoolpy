import random

def roll():
    return random.randint(1,6)
x=0
whle True:
    x=int(input('Generatte a number? (1=yes, 0=no): '))    
while x:
    print(roll())