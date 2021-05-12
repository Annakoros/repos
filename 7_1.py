class Matrix:
    def __init__(self, matrix):
        columns = []
        for row in matrix:
            new_row = []
            for symb in row:
                new_row.append(symb)
            columns.append(new_row)
        self.matrix = columns

    def __str__(self):
        res_str = ''
        for el in self.matrix:
            print_str = ''
            for symb in el:
                print_str += ' ' * (4 - len(str(symb)))
                print_str += str(symb)
            res_str = res_str + print_str + '\n'
        return res_str

    def __add__(self, other):
        res_matrix = []
        for i in range(len(self.matrix)):
            res_row = []
            for j in range(len(other.matrix[0])):
                self.matrix[i][j] = int(self.matrix[i][j]) + int(other.matrix[i][j])
        res_matrix = self.matrix
        return Matrix(res_matrix)
a = Matrix([[1,2,3],[4,5,6]])
b = Matrix([[2,3,4],[5,6,7]])
print(a + b)