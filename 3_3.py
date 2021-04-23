def my_func(var1, var2, var3):
    """Функция принимает три числа и возвращает сумму двух наибольших"""
    my_list = [var1, var2, var3]
    return sum(sorted(my_list)[1:])

print(my_func(2, 11, -30))

# my_newfunc = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)