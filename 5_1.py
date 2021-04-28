#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
new_f = open("new_file_5_1.txt", "w", encoding='utf-8')
input_text = []
inpstr = '1'
while inpstr != '':
    inpstr = input('Введите строку (для завершения сразу нажмите "enter"): ')
    if inpstr != '':
        input_text.extend([inpstr, '\n'])
    else:
        break
new_f.writelines(input_text)
new_f.close()