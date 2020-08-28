user_seconds = int(input('Введите количество секунд: '))
hours = user_seconds // 3600
minutes = int((user_seconds % 3600) / 60)
second = int((user_seconds%3600) %60)
print(f'{hours} : {minutes} : {second}')




























