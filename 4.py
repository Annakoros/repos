number = int(input('Введите целое положительное число: '))
maxn = 0
while number !=0:
    numb = number % 10
    if numb > maxn:
        maxn = numb
    number = number // 10
print(f'{maxn} - самая большая цифра Вашего числа')