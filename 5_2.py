#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
f = open(r"text_file_5_2.txt", "r", encoding='utf-8')
lines = 0
words = 0
line_list = []
for line in f:
    lines += 1
    line_list = line.split()
    for word in line_list:
        if word != '—' and word != '...':
            words += 1
    print(f'В строке {lines}: {words} слов.')
    words = 0
f.close()