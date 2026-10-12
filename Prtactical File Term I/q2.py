import random
number=''
n=int(input("Enter number of digits in random number: "))
for i in range(n):
    if i == 0:
        x=str(random.randint(1,9))
    else:
        x=str(random.randint(0,9))
    number+=x
print(number)