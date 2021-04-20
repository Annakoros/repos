mylist = []
for el in ['somestr', 34, False, 3.4, (4, 'somestr'), {'1': 2, '3': 4}]:
    mylist.append(el)
for el in mylist:
    print(type(el))