my_list = [7, 5, 13, 18, 12, 5, 2, 2, 13, 7, 9, 11]


def count(j):
    res = 0
    for i in my_list:
        if i == j:
            res += 1
    return res


new_list = [i for i in my_list if count(i) == 1]

print(my_list)
print(new_list)


