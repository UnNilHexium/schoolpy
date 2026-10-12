import random

def roll():
    return random.randint(1,6)
x=0
while True:
    x=int(input('Generate a number? (1=yes, 0=no): '))
    if x == 1: 
        break
print(roll())
