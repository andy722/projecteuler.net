def num_digs(n = 3):
    start = 10 ** (n-1)
    end = 10 ** n
    i = end - 1
    while i > start:
        yield i
        i = i - 1

def is_poly(n):
    return str(n) == str(n)[::-1]

mults = []

for n1 in num_digs():
    for n2 in num_digs():
        n = n1 * n2
        if is_poly(n):
            mults.append(n)

print max(mults)
