"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
class Cloth(ABC):
    def __init__(self, fabric_factor):
        self.fabric_factor = fabric_factor

    @property
    @abstractmethod
    def calc_fabric(self):
        pass

class Suit(Cloth):


    @property
    def calc_fabric(self):
        return self.fabric_factor * 2 + 0.3


class Coat(Cloth):

    @property
    def calc_fabric(self):
        return round(self.fabric_factor/6.5,2) + 0.5

if __name__ == "__main__":
    suit1 = Suit(180)
    print(suit1.calc_fabric)

    coat1 = Coat(46)
    print(coat1.calc_fabric)