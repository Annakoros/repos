mylist=[]
newel=None
while newel != 'q':
    newel = (input("Введите значение элемента массива\n(для завершения нахмите 'q'): "))
    if newel == 'q':
        break
    else:
        mylist.append(newel)
print('Было: ', mylist)
mynewlist = []
while mylist != []:
    var_1, *var_2 = mylist
    if var_2 != []:
        mynewlist.extend([var_2[0], var_1])
        mylist.pop(0)
    else:
        mynewlist.append(var_1)
    mylist.pop(0)
print('Стало: ', mynewlist)