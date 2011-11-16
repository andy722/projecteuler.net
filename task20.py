"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

n = 100

def sum_of_digits(n):
    return reduce(lambda x, y: int(x) + int(y),
                  str(n))

def fact(n):
    return reduce(lambda x, y: int(x) * int(y), range(1, n))

print sum_of_digits(fact(100))