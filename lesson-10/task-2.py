"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


# Абстрактный класс, который определяет обязательность определения метода для получения потребности в ткани
class ClothesABC(ABC):
    @abstractmethod
    def cloth(self):
        pass


# Основной класс, который определяет общие методы и атрибуты одежды. Наследуется от абстрактного класса
class Clothes(ClothesABC):
    def __init__(self, name):
        self._name = name
        self._cloth = 0

    def __add__(self, other):
        clothes = Clothes(f'{self.name}, {other.name}')
        clothes._cloth = self.cloth() + other.cloth()
        return clothes

    def __radd__(self, other):
        if not isinstance(other, Clothes):
            return self
        return self.__add__(other)

    def cloth(self):
        return self._cloth

    @property
    def name(self):
        return self._name


# Класс, определяющий специфику для пальто
class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size
        self._cloth = self._size / 6.5 + 0.5


# Класс, определяющий специфику для костюмов
class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height
        self._cloth = self._height * 2 + 0.3


coat1 = Coat('Пальто 1', 10)
coat2 = Coat('Пальто 2', 20)
suit1 = Suit('Костюм 1', 10)
suit2 = Suit('Костюм 2', 20)

print(f'Ткань для {coat1.name}: {coat1.cloth()}')
print(f'Ткань для {coat2.name}: {coat2.cloth()}')
print(f'Ткань для {suit1.name}: {suit1.cloth()}')
print(f'Ткань для {suit2.name}: {suit2.cloth()}')

clothes_list = [coat1, coat2, suit1, suit2]
full_calc = sum([item.cloth() for item in clothes_list])

print(f'Всего необходимо ткани: {full_calc}')
sum_clothes = coat2 + suit1
print(f'Ткань для {sum_clothes.name}: {sum_clothes.cloth()}')
sum_clothes = sum(clothes_list)
print(f'Ткань для {sum_clothes.name}: {sum_clothes.cloth()}')
