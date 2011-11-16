"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

top = 1000

def is_triplet(a, b, c):
    return a**2 + b**2 == c**2

def triplets(top):
    for a in range(1, top):
        for b in range(1, top - a):
            c = top - a - b
            if c >= 0 and is_triplet(a, b, c):
                yield (a, b, c)

mul = lambda i: reduce(lambda x, y : x*y, i)

print set(map(mul, triplets(top)))