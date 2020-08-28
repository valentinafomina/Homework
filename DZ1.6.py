speed1 = int(input('Введите начальную скорость спортсмена в км/ч: '))
speed2 = int(input('Какой скорости должен достичь спортсмен в результате тренировок? '))
days = 1
while speed1+(speed1*0.1) <= speed2:
    speed1 = speed1+(speed1*0.1)
    days = days + 1
print(days)

















































