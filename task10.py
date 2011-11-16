"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import itertools

from math import sqrt

def is_prime0(n, primes):
    """Checks if a value is a prime number.

    The number is considered prime if it's not divisible by any 
    of already discovered primes.

    Args:
        n: A number to be checked.
        primes: All known prime numbers.
    
    """
    return all(n % p for p in primes)

def is_prime(n):
    return all(n % p for p in range(2, int(sqrt(n)) + 1))

def gen_primes():
    """Prime number generator.

    Yields:
        Prime numbers, i.e. 2, 3, 5 ...

    """

    n = 2
    while True:
        yield n

        n += 1
        while not is_prime(n):
            n += 1

top = 2000000

print sum(itertools.takewhile(lambda num : num < top, gen_primes()))
