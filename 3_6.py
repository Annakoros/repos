#$ pip install langdetect
#Не хочет понимать такую строку, почему-то(( поэтому не могу сделать проверку языка ввода...
def int_func(mystr):
    """Функция принимает строку и переводит первый символ в заглавный регистр.
    """
    mynewstr = mystr[0].upper() + mystr[1:]
    return(mynewstr)

input_str = input('Напишите несколько слов маленькими буквами (латинскими буквами): ')
correct_input = False
while correct_input != True:
    new_input_done = False
    for input_letter in input_str:
        if input_letter.isupper():
            if new_input_done == True:
                pass
            else:
                print('Нужны только маленькие буквы...')
                input_str = input('Напишите несколько слов маленькими буквами (латинскими буквами): ')
                correct_input = False
                new_input_done = True
        else:
            correct_input = True
words_list = input_str.split()
output_str = ''
for input_word in words_list:
    output_str = output_str + int_func(input_word) + ' '
print(output_str)
