from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, measure):
        self.name = name
        self.measure = measure

    def __str__(self):
        return f'Расход ткани для пошива {self.name}: {self.fabric_consumption :.2f} метров'

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return f'Суммарный расход ткани: {self.fabric_consumption + other.fabric_consumption :.2f} метров'


class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return self.measure / 6.5 + 0.5


class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return 2 * (self.measure * 0.01) + 0.3


my_coat = Coat("пальто", 44)
print(my_coat)
my_suit = Suit("костюм", 168)
print(my_suit)
print(my_suit + my_coat)
