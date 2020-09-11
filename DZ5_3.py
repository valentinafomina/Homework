f = open("salaries.txt", encoding="utf-8")
content = f.readlines()
low_salary = []
salary_list = []
for line in content:
    n = line.split(": ")
    salary_list.append(int(n[1]))
    if int(n[1]) < 20000:
        low_salary.append(n[0])
avg_salary = sum(salary_list) / len(salary_list)
print(f"Сотрудники с зарплатой ниже 20.000 руб: {low_salary}")
print(f"Средняя зарплата: {avg_salary}")
f.close()
