employees_dict = {}


def thesaurus_adv(*args):
    for employee in args:
        name, surname = employee.split(" ")
        if surname[0] in employees_dict:
            if name[0] not in employees_dict[surname[0]]:
                employees_dict[surname[0]].setdefault(name[0], [employee])
            else:
                employees_dict[surname[0]][name[0]].append(employee)
        else:
            employees_dict.setdefault(surname[0], dict.fromkeys(name[0], [employee]))


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Мария Смирнова",
              "Максим Васильев", "Андрей Костин", "Анатолий Васютин")
print(employees_dict)
