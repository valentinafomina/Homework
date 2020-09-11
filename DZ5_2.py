f = open("my_file_2.txt", encoding="utf-8")
i = 0
sum_words = 0
for line in f:
    n = line.split()
    sum_words += (len(n))
    i += 1
lines_quantity = i
print(sum_words)
print(lines_quantity)
f.close()

