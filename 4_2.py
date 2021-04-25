from random import randint
orig_list = []
for i in range (1, 11):
    orig_list.append(randint(-100, 100))
    i =+1
print(f'Случайная последовательность целых чисел: {orig_list}')
res_list = [orig_list[i] for i in range(1, len(orig_list)) if orig_list[i] > orig_list[i-1]]
print(f'Числа, являющиеся в последовательности больше предыдущих: {res_list}')