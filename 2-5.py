my_list = [7, 5, 3, 3, 2]
numinserted = False
print('Имеется рейтинг: ', my_list)
usernum = int(input('Введите новое число для размещения в рейтинге: '))
my_list.append(usernum)
my_list.sort()
my_list.reverse()
print(my_list)