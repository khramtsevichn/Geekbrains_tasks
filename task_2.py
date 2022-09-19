'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def count_of_material(self):
        pass


class Suit(Clothes):

    def __init__(self, h):
        self.__h = h

    @property
    def h(self):
        return self.__h

    def count_of_material(self):
        return 2 * self.__h + 0.3


class Coat(Clothes):

    def __init__(self, v):
        self.__v = v

    @property
    def v(self):
        return self.__v

    def count_of_material(self):
        return self.__v / 6.5 + 0.5


suit = Suit(100)
print(suit.h)
print(suit.count_of_material())

print("********************")
coat = Coat(100)
print(coat.v)
print(coat.count_of_material())

