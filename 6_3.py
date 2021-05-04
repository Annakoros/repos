class Worker:
    def __init__(self):
        name = 'name'
        surname = 'surname'
        position = 'position'
        wage = 0
        bonus = 0
        _income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self, position):
        self.name = input('Введите имя сотрудника: ')
        self.surname = input('Введите фамилию сотрудника: ')
        self.position = position
    def get_total_income(self):
        wage = int(input("Зарплата сотрудника: "))
        bonus = int(input("Премия сотрудника: "))
        self._income = {'wage': wage, 'bonus': bonus}
        print(f'{self.name} {self.surname}, {self.position}\nДоход с учётом премии: {self._income.get("wage") + self._income.get("bonus")}')

engineer = Position()
engineer.get_full_name("инженер")
engineer.get_total_income()
director = Position()
director.get_full_name("директор")
director.get_total_income()