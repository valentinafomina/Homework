from itertools import cycle
from sys import argv

script_name, param_1 = argv

# param_1 для ввода условия завершения цикла
i = 0
for el in cycle([1, 2, 3, 4, 5]):
    if i == int(param_1):
        break
    print(el)
    i += 1
