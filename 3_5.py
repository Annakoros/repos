def sum_func():
    """Функция суммирует числа, вводимые пользователем через пробел.
    За один вызов функции суммируются в одно значение все числа, введенные до символа 'q' (завершение работы функции)
    """
    print('Введите числа через пробел (для завершения вместо числа введите "q"): ')
    myvar = None
    end_input = False
    my_sum = 0
    while end_input != True:
        mystr = input('>')
        mylist = mystr.split()
        mylist.append('q')
        count = 0
        for myvar in mylist:
            if myvar != 'q':
                my_sum = my_sum + int(myvar)
        print(my_sum)
        if mylist.count('q') > 1:
            end_input = True
        else:
            mylist.clear()
sum_func()