#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce()
from functools import reduce

def multipl_func(prev_el, el):
    return prev_el * el
many_even_numbers = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(multipl_func, many_even_numbers))
print(f'Длина числа - {len(str(reduce(multipl_func,many_even_numbers)))} символов XD')

