userstr = input('Введите строку (слова, разделенные пробелами): ')
userwords = userstr.split()
newstr = []
for userword in userwords:
    newword = userword[:10]
    newstr.append(newword)
for ind, newword in enumerate(newstr):
    print(ind, newword)