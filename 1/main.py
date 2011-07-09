def trivial():
    sum = 0

    for i in range(1, 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    return sum


def less_trivial():
    return sum([i for i in range(1, 1000) if (i % 3 == 0) or (i % 5 == 0)])


#print trivial()
print less_trivial()