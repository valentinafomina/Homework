from itertools import count
from sys import argv

script_name, param_1 = argv

my_list_count = []
for el in count(int(param_1)):
    if el % 2 == 0:
        my_list_count.append(el)
    elif el > 10:
        break

print(my_list_count)


