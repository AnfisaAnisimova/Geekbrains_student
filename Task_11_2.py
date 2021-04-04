class MyOwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input("Введите делимое: ")
b = input("Введите делитель: ")
try:
    dividend = int(a)
    divisor = int(b)
    if divisor == 0:
        raise MyOwnException("Деление на ноль!")
except (ValueError, MyOwnException) as err:
    print(err)
else:
    print(dividend / divisor)


