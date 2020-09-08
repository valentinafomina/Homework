from functools import reduce

my_list = [el for el in range(100, 1001, 2)]


def mul (a, b):
    return a * b


print(reduce(mul, my_list))

