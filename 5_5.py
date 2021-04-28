#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
digits = [randint(0, 100) for el in range(20)]
f_digits = ''
for digit in digits:
    f_digits += str(digit) + ' '
with open("rw_file_5_5.txt", 'w') as f:
    f.write(f_digits)
with open("rw_file_5_5.txt", 'r') as f:
    content = f.read()
    print(f'Набор случайных чисел: {content}')
    sum_digits = sum(int(el) for el in content.split())
    print(f'Сумма чисел: {sum_digits}')
