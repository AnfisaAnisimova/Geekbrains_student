from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [arg for arg in [*args, *kwargs.values()]]
        arg_type = [f'{func.__name__}({arg}: {type(arg)})' for arg in args_list]
        print(*arg_type, sep=",\n")

    return wrapper


@type_logger
def calc_cube(*x, **y):
    args_list = [arg for arg in [*x, *y.values()] if type(arg) == int or type(arg) == float]
    print([number ** 3 for number in args_list])


calc_cube(5, 6, 6.7, num=45)
