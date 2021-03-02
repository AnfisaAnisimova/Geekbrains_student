employees_dict = {}


def thesaurus(*args):
    for name in args:
        if name[0] in employees_dict:
            employees_dict[name[0]].append(name)
        else:
            employees_dict.setdefault(name[0], [name])


thesaurus("Иван", "Мария", "Петр", "Илья", "Максим", "Анна", "Андрей")
print(employees_dict)
