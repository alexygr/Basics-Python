from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, size):
        Clothes.__init__(self, name="Пальто")
        self.size = size

    @property
    def tissue_consumption(self):
        return self.size/6.5 + 0.5

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Costume(Clothes):
    def __init__(self, height):
        Clothes.__init__(self, name="Костюм")
        self.height = height

    @property
    def tissue_consumption(self):
        return self.height * 2 + 0.3

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


my_coat = Coat(45)
my_costume = Costume(204)
print(f"Расход ткани для {my_coat.name} = {my_coat.tissue_consumption:.02f}")
print(f"Расход ткани для {my_costume.name}а = {my_costume.tissue_consumption:.02f}")
print(f"Общий расход ткани - {my_coat+my_costume:.02f}")
