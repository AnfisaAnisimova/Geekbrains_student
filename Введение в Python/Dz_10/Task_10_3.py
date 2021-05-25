class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        pass

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        if self.cell > other.cell:
            return self.cell / other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def __floordiv__(self, other):
        if self.cell > other.cell:
            return self.cell // other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def make_order(self, rows):
        result = ''
        for i in range(self.cell // rows):
            result += f'{"*" * rows}\n'
        result += f'{"*" * (self.cell % rows)}\n'
        return result


cell_1 = Cell(40)
cell_2 = Cell(11)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(5))
