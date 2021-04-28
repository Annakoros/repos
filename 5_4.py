#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
f_read = open(r"read_file_5_4.txt","r", encoding='utf-8')
f_write = open(r"write_file_5_4.txt","w", encoding="utf-8")
str_list = []
new_str = ''
digits = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
for line in f_read:
    if line[:line.find(' ')] in digits.keys():
        new_str = digits.get(line[:line.find(' ')]) +  line[line.find(' '):]
    str_list.append(new_str)
    new_str = ''
f_write.writelines(str_list)
f_read.close()
f_write.close()