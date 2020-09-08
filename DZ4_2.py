import random

i = 0
list = []
while i < 10:
    list.append(random.randint(0, 200))
    i += 1

new_list = []
x = 1
while x < len(list):
    if list[x] > list[x-1]:
        new_list.append(list[x])
    x += 1

print(list)
print(new_list)
