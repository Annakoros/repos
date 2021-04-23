def division_func(s_1, s_2):
    """Выводит на печать выражение деления с ответом.
    Именованные параметры:
    number - делимое
    divider - делитель
    Параметры запрашиваются у пользователя.
    Делитель запрашивается до тех пор, пока не будет введен не 0.
    """
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'ZeroDivisionError HAHAHAHA'
    return round(div_num, 4)

print(division_func(input('Введите первое число: '), input('Введите второе число: ')))