f = open("task_6.txt", encoding="utf-8")
for line in f:
    new_list = line.split(" ")
    i = 0
    my_dict = dict()
    my_dict[new_list[0]] = 0
    for item in new_list:
        if i > 0:
            sub_item = item.split("(")
            if len(sub_item) > 1:
                my_dict[new_list[0]] += (int(sub_item[0]))
        i += 1
    print(my_dict)
f.close()
