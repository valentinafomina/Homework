revenue = float(input('Введите размер выручки вашей компании в рублях: '))
expense = float(input('А теперь размер издержек: '))
company_return = revenue - expense
if company_return > 0:
    print(f'Поздравляем! Ваша компания приносит прибыль в размере {company_return} рублей.')
    print(f'Рентабельность вашей компании составляет {company_return/revenue*100}%')
    personnel = int(input('Сколько в вашей компании сотрудников? '))
    print(f'Прибыль вашей компании на 1 сотрудника составляет {company_return/personnel} рублей')
else:
    print('Похоже, ваша компания пока убыточная.')












































