class MyOwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


some_list = []
while True:
    try:
        some_input = input("Введите число: ")
        if some_input == "quit":
            break
        elif some_input.replace("-", "").isdigit():
            some_list.append(some_input)
        else:
            raise MyOwnException("Вы ввели не число")

    except MyOwnException as err:
        print(err)

print(some_list)

