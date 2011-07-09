N = 600851475143

primes = [2]

maxp = 1

def trydiv():
    global N, maxp
    for p in primes:
        if N % p == 0:
            N = N/p
            maxp = max(maxp, p)
            return True
    return False


def prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True


def next():
    n = primes[len(primes)-1] + 1
    while not prime(n):
        n += 1

    primes.append(n)
    

while True:

    if N == 1:
        break
    
    while trydiv():
        pass

    next()
    
    
print maxp