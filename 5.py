revenue = int(input('Какова выручка Вашей фирмы? - '))
cost = int(input('Каковы Ваши издержки? - '))
if revenue > cost:
    print('Ваш финансовый результат - прибыль')
    profitability = (revenue - cost)/revenue
    print(f"Рентабельность: {round(profitability,2)}")
    workers = int(input('Какова численность вашего персонала? - '))
    print(f'Прибыль в расчете на одного сотрудника: {round(((revenue - cost) / workers), 2)}')
elif revenue < cost:
    print('Ваш финансовый результат - убыток')
else:
    print('Ваш финансовый результат - самоокупаемость без прибыли')

