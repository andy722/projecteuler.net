MAX = 4000000

def fib():
    i = 0
    j = 1

    while True:
        yield i
        i, j = j, i + j


def fibl(nmax):
    i = 0
    j = 1

    while i < nmax:
        yield i
        i, j = j, i + j


def trivial():
    return sum([i for i in fibl(MAX) if (i % 2 == 0)])


print trivial()
        
