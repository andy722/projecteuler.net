"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys

divisors = range(20, 1, -1)

def is_divisible(n):
    for i in divisors:
        if n % i:
            return False
    return True

n = 20
while True:
    #print 'n = ', n
    if is_divisible(n):
        print n
        break
    n = n + 20

#
#
#from fractions import gcd
#
#def lcm(a, b): 
#    return a * b / gcd(a, b)
#
#print reduce(lcm, range(1, 21))
#
