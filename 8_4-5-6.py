#Склад оргтехники
class Warehouse:

    def __init__(self, name):
        self.name = name
    def accept(self, *equipment):
        accept_list = [self.name, '\nПоступило оборудование: \n']
        for eq in equipment:
            accept_list.append(str(eq.make_dict))
            accept_list.append('\n')
        with open ("accepted_equipment.txt", 'w', encoding= 'utf-8') as f:
            f.writelines(accept_list)
        print('Сформирован текстовый файл "accepted_equipment.txt" со списком принятого оборудования')

    def transfer(self, unit, *equipment):
        transfer_list = [unit, '\nПоступило оборудование: \n']
        for eq in equipment:
            transfer_list.append(str(eq.make_dict))
            transfer_list.append('\n')
        with open("transfered_equipment.txt", 'w', encoding='utf-8') as f:
            f.writelines(transfer_list)
        print('Сформирован текстовый файл "transfered_equipment.txt" со списком отправленного оборудования')


class Office_equipment:

    def __init__(self, cls_name):
        self.cls_name = cls_name
        print(f'Ввод данных об оргтехнике.\nНаименование: {self.cls_name}')
        self.name = input('Производитель: ')
        self.release_year = input('Год выпуска: ')
        while int(self.release_year) not in range(1995,2022):
            self.release_year = input('Введен неверный год выпуска. Попробуйте ещё раз: ')
        self.quantity = input("Количество: ")
        while not self.quantity.isdigit():
            try:
                check = int(self.quantity)
            except:
                self.quantity = input('Количество введено неверно. Попробуйте ещё раз: ')

    @property
    def make_dict(self):
        self.eq_dict = {"Наименование": self.cls_name,
                "производитель": self.name,
                "год выпуска": self.release_year,
                "количество": self.quantity
        }
        return self.eq_dict


class Printer(Office_equipment):
    def __init__(self, cls_name = 'Принтер'):
        Office_equipment.__init__(self, cls_name)


class Scanner(Office_equipment):
    def __init__(self, cls_name='Сканер'):
        Office_equipment.__init__(self, cls_name)


class Xerox(Office_equipment):
    def __init__(self, cls_name='Ксерокс'):
        Office_equipment.__init__(self, cls_name)


my_warehouse = Warehouse('Склад № 1')
print('Прием оргтехники на склад')
my_warehouse.accept(Printer(), Scanner(), Xerox())
print('Отправка оргтехники в подразделение')
my_warehouse.transfer('Главный офис', Printer(), Scanner(), Xerox())
