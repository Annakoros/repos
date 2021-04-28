#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
f = open(r"text_file_5_3.txt", "r", encoding="utf-8")
worker_data = []
poor_workers = []
all_salaries = 0
counter = 0
for line in f:
    worker_data = line.split()
    if int(worker_data[1]) < 20000:
        poor_workers.append(worker_data[0])
    all_salaries += int(worker_data[1])
    counter +=1
print(f'Оклад менее 20 тыс. имеют сотрудники: {poor_workers}')
print(f'Средняя величина дохода сотрудников равняется {all_salaries/counter} руб.')
f.close()