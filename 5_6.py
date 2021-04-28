#6.Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
disciplines_d = {}
data_list = []
with open('data_5_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        hours = 0
        data_list = line.split()
        discip = data_list[0][:-1]
        data_list.pop(0)
        for hour in data_list:
            if len(hour)>1:
                hours += int(hour[:hour.index('(')])
        disciplines_d.update({discip: hours})
print(disciplines_d)