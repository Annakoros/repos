seasons = {
    'Весна!': [3, 4, 5],
    'Лето!': [6, 7, 8],
    'Осень!': [9, 10, 11],
    'Зима!': [1, 2, 12]
}
result = 'Для Вашего месяца времени года не найдено...'
month = int(input('Введите номер месяца (число от 1 до 12): '))
for season, months in seasons.items():
    for mon in months:
        if mon == month:
            result = season
print(result)

