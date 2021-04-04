"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + i*{self.b + other.b}'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - self.b * other.b} + i*{self.a * other.b + other.a * self.b}'


z_1 = ComplexNumber(3, 7)
z_2 = ComplexNumber(-5, 4)
print(z_1 + z_2)
print(z_1 * z_2)
