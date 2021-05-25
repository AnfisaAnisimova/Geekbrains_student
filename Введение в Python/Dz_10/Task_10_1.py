class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for item in self.matrix:
            for i in range(len(item)):
                if i < len(item) - 1:
                    result += f'{item[i]}\t{item[i + 1]}\n'

        return result

    def __add__(self, other):
        matrix_sum = Matrix([
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ])
        return matrix_sum


matrix_1 = Matrix([[2, 6], [7, 11], [56, 6]])
matrix_2 = Matrix([[42, 4], [33, 8], [97, 3]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
