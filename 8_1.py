class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def transforme_date(cls, date_str):
        date_spl = date_str.split('-')
        try:
            date_int = f'Число - {int(date_spl[0])}, месяц - {int(date_spl[1])}, год - {int(date_spl[2])}'
            return date_int
        except:
            print('Некорректный ввод!')

    @staticmethod
    def validate_input(date_str):
        date_spl = date_str.split('-')
        if int(date_spl[0]) not in range(1,32) or not date_spl[0].isdigit():
            print("Число введено неверно!")
        if int(date_spl[1]) not in range(1,13) or not date_spl[1].isdigit():
            print("Месяц введен неверно!")
        if not date_spl[2].isdigit():
            print("Год введен неверно!")

input_date = input('Введите дату через "-" (например: "1-4-2018"): ')
my_date = Date(input_date)
print(my_date.transforme_date(input_date))
my_date.validate_input(input_date)