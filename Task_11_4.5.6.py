class WareHouse:
    def __init__(self):
        self.storage = {}
        self.other_storages = {}

    def __str__(self):
        items_in_storage = str()
        for key, value in self.storage.items():
            items_in_storage += f'{key}: '
            for item in value:
                items_in_storage += f'{item}; '
            items_in_storage += f'\n'
        print(f'На складе находятся следующие единицы оргтехники: ')
        return items_in_storage

    def eq_acceptance(self, item):
        eq_type = item.__class__.__name__
        if self.storage.get(eq_type):
            self.storage[eq_type].append(item)
        else:
            self.storage[eq_type] = [item]

    def eq_moving(self, item, department):
        eq_type = item.__class__.__name__
        if self.storage.get(eq_type):
            for ind, val in enumerate(self.storage.get(eq_type)[:]):
                if item == val:
                    result = val - item
                    if result.get_quantity() == 0:
                        self.storage.get(eq_type).pop(ind)
                    else:
                        self.storage.get(eq_type)[ind] = result
                    if self.other_storages.get(department):
                        self.other_storages[department] += f'; '
                        self.other_storages[department] += f'{eq_type}: {item.__str__()}'
                    else:
                        self.other_storages.setdefault(department, f'{eq_type}: {item.__str__()}')
        print(f'{eq_type}: {item.__str__()} перемещён в подразделение: {department}\n')
        return f'Единицы оргтехники в других подразделениях: {self.other_storages}\n'


class OfficeEquipment:
    count = int()

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_quantity(self, count):
        if isinstance(count, int):
            self.count = count
        else:
            raise ValueError(f'Необходимо было ввести число')

    def get_quantity(self):
        return self.count

    def __sub__(self, other):
        remainder = self.get_quantity() - other.get_quantity()
        if remainder > 0:
            self.set_quantity(remainder)
        else:
            self.set_quantity(0)

        return self


class Printer(OfficeEquipment):
    def __init__(self, name, price, output_type):
        super().__init__(name, price)
        self.output_type = output_type

    def __str__(self):
        return f'{self.name} {self.price} {self.output_type} {self.count}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.output_type == other.output_type


class Scanner(OfficeEquipment):
    def __init__(self, name, price, photo_scan=True):
        super().__init__(name, price)
        self.photo_scan = photo_scan

    def __str__(self):
        return f'{self.name} {self.price} {self.photo_scan} {self.count}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.photo_scan == other.photo_scan


class Copier(OfficeEquipment):
    def __init__(self, name, price, two_sided_print=True):
        super().__init__(name, price)
        self.two_sided_print = two_sided_print

    def __str__(self):
        return f'{self.name} {self.price} {self.two_sided_print} {self.count}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.two_sided_print == other.two_sided_print


item_1 = Printer("HP", 3000, "color")
item_1.set_quantity(7)
item_2 = Scanner("EPSON", 7000, False)
item_2.set_quantity(2)
item_3 = Copier("CANON", 10000, True)
item_3.set_quantity(1)
my_wh = WareHouse()
for i in [item_1, item_2, item_3]:
    my_wh.eq_acceptance(i)
print(my_wh)

item_4 = Printer("HP", 3000, "color")
item_4.set_quantity(2)

print(my_wh.eq_moving(item_4, "Бухгалтерия"))
print(my_wh)

item_5 = Scanner("EPSON", 7000, False)
item_5.set_quantity(1)
print(my_wh.eq_moving(item_5, "Отдел продаж"))
print(my_wh)

item_6 = Printer("HP", 3000, "color")
item_6.set_quantity(4)
print(my_wh.eq_moving(item_6, "Отдел продаж"))
print(my_wh)

