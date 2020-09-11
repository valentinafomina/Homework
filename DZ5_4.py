russian_numbers = ["один", "два", "три", "четыре"]
old_file = open("numbers eng.txt", encoding="utf-8")
new_file = open("new_file.txt", "a", encoding="utf-8")
content = old_file.readlines()
i = 0
for line in content:
    n = line.split("—")
    new_line = f"{russian_numbers[i]} - {n[1]}"
    new_file.write(new_line)
    i += 1
old_file.close()
