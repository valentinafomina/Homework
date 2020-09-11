f = open("task_5.txt", "w", encoding="utf-8")
f.write("1 2 3 4 5 6 7 8 9 10")
f.close()
f1 = open("task_5.txt")
content = f1.readline()
numbers = []
i = 0
line = content.split(" ")
while i < (len(line) - 1):
    for item in line:
        line = content.split(" ")
        numbers.append(int(line[i]))
        i += 1
summa = sum(numbers)
print(summa)
f1.close()
