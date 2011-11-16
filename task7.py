"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime0(n, primes):
    for p in primes:
        if n % p == 0:
            return False
    return True

# TODO: start with 3 and step with 2
# TODO: nice snippet:
#N,T = 1,3
#while N < 10001:
#	if IsPrime(T):
#		N+=1
#	T+=2

# TODO: testing for being prime:
#range = int( math.sqrt(n) ) + 1
#	while( i < range ):

def gen_primes():
    is_prime = lambda n, primes: len([p for p in primes if (n % p) == 0]) == 0

    primes = [2]
    count = len(primes)
    while True:
        n = primes[-1] + 1
        while not is_prime0(n, primes):
            n = n + 1
        primes.append(n)
        yield (len(primes), n)

nmax = 10001

for (n, p) in gen_primes():
    print "> num = %d, value = %d" % (n, p)
    if n == nmax:
        break
