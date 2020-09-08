from math import factorial


def fact(n):
    i = 0
    while i < n + 1:
        el = factorial(i)
        i += 1
        yield el


f = fact(4)
for el in f:
    print(el)
