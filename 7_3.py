class Cell:
    def __init__(self,cellule):
        self.cellule = int(cellule)

    def __add__(self, other):
        return f'Сумма: {self.cellule + other.cellule}'

    def __sub__(self, other):
        return f'Разность: {self.cellule - other.cellule}' if self.cellule > other.cellule else 'Разность отрицательна'

    def __mul__(self, other):
        return f'Произведение: {self.cellule * other.cellule}'

    def __truediv__(self, other):
        return f'Частное: {self.cellule // other.cellule}'

    def make_order(self,str_len):
        return (('*' * str_len) + '\n') * (self.cellule // str_len) + '*' * (self.cellule % str_len)

one_cell = Cell(15)
other_cell = Cell(12)
result = one_cell + other_cell
print(result)
print(one_cell - other_cell)
print(other_cell - one_cell)
print(one_cell * other_cell)
print(one_cell / other_cell)
print(one_cell.make_order(4))