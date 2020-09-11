with open("task_7.txt", encoding="utf-8") as f:
    i = 0
    my_dict = dict()
    for line in f:
        split_list = line.split(" ")
        my_dict[split_list[0]] = (int(split_list[2]) - int(split_list[3]))
        i += 1
    avg_profit = dict()
    avg_profit["average profit"] = sum(my_dict.values())/len(my_dict.values())
    complete_list = [my_dict, avg_profit]
    print(complete_list)

import json
with open("task_7.json", "w", encoding="utf-8") as j:
    json.dump(complete_list, j)

