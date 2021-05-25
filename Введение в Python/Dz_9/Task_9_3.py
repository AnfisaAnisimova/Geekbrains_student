class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(total_income)


pos_1 = Position('Anfisa', 'Anisimova', 'cabin crew', 6000, 500)
pos_1.get_full_name()
pos_1.get_total_income()
