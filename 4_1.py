from sys import argv

def salary_func(rate, hours, prize):
    salary = int(rate) * int(hours) + int(prize)
    return salary

script_name, rate, hours, prize = argv
print(salary_func(rate = argv[1], hours = argv[2], prize = argv[3]))