def my_func(x, y):
    """Функция принимает действительное положительное число x и целое отрицательное число y.
    Функция проверяет корректность аргументов и возводит число x в степень y.
    Вывод не отформатирован, поскольку получаются малые числа.
    """
    while type(x) != float or x <= 0:
        user_input = input('Введите аргумент (действительное положительное число): ')
        x = float(user_input)
    while type(y) != int or y >= 0:
        while True:
            user_input = input('Введите показатель степени (целое отрицательное число): ')
            try:
                y = int(user_input)
            except ValueError:
                print('Вы ввели не целое отрицательное число. Повнимательнее!')
            else:
                break
    result = 1 / x
    for i in range(2,abs(y)+1):
        result = result / x
        i += 1
    print(result)

x = 0
y = 0
while type(x) != float or x <= 0:
    user_input = input('Введите аргумент (действительное положительное число): ')
    x = float(user_input)
while type(y) != int or y >= 0:
    while True:
        user_input = input('Введите показатель степени (целое отрицательное число): ')
        try:
            y = int(user_input)
        except ValueError:
            print('Вы ввели не целое отрицательное число. Повнимательнее!')
        else:
            break
my_func(x,y)