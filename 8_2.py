#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class Zero_division_processing:

    def try_division(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor
        try:
            print(round(int(divisible)/int(divisor), 2))
        except ZeroDivisionError:
            print('Деление на 0 недопустимо))')
        except ValueError:
            print('Вы ввели не число...')

a = input('Введите делимое: ')
b = input('Введите делитель: ')
zd = Zero_division_processing()
zd.try_division(a,b)