lst = []
primes = [2]

for i in range(2,100000):
    prime = None
    for j in range(2,i):
        if i%j != 0:
            prime = i
        else:
            prime = None
            break
    if prime != None:
        print(prime)
        primes.append(prime)

print(primes)
