seasons = [[3, 4, 5], [6, 7, 8], [9, 10, 11],[1, 2, 12]]
month = int(input('Введите номер месяца (число от 1 до 12): '))
ind = 4
count = 0
for season in seasons:
    for monthnum in season:
        if month == monthnum:
                ind = count
    count = count + 1
result = ['Весна!', 'Лето!', 'Осень!', 'Зима', 'Для вашего месяца нет времени года...']
print(result[ind])