#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.
class Complex_digit:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = complex(x, y)

    def __add__(self, other):
        return f'Сумма комплексных чисел: {self.x + other.x} + {self.y + other.y} * j'

    def __mul__(self, other):
        return f'Произведение комплексных чисел: {(self.x * other.x) - (self.y * other.y)} + {(self.x * other.y) + (self.y * other.x)} * j'

    def __str__(self):
        return f'Комплексное число {self.z}'
#        return f'z = {self.x} + {self.y} * i'

z1 = Complex_digit(-3, 5)
z2 = Complex_digit(2,4)
print(z1)
print(z2)
print(z1+z2)
print(z1*z2)