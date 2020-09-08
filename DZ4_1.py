from sys import argv
script_name, rate, hours, bonus = argv
salary = (int(rate) * int(hours)) + int(bonus)
print(f"Зарплата составит {salary}")

