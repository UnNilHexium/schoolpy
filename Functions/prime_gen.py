def prime_gen(a=50):
    primes=list()
    i=2
    flag=0
    while i<=a:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
        if flag == 0:
            primes.append(i)
        i+=1
    print(primes)

n=input("Enter no of primes to find (Default = 50): ")
if n=='': 
    prime_gen()
else:
    n=int(n)
    prime_gen(n)