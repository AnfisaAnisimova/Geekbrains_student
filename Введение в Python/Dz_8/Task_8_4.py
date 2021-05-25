def val_checker(inner_func):
    def _val_checker(func):
        def wrapper(number):
            if inner_func(number):
                print(func(number))
            else:
                raise ValueError(f'wrong val {number}')

        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == "__main__":
    try:
        calc_cube(-8)
    except ValueError as error:
        print(error)

# пробовала с инпутом но не пойму как доделать проверку для ввода такого вида: ghh6 ???

    # number = input("Введите положительное число: ")
    # if number.isalpha():
    #     print("Необходимо было ввести число")
    # elif number.find(".") >= 0:
    #     number = float(number)
    #     try:
    #         calc_cube(number)
    #     except ValueError as error:
    #         print(error)
    # elif int(number):
    #     number = int(number)
    #     try:
    #         calc_cube(number)
    #     except ValueError as error:
    #         print(error)


