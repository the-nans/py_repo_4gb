"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""
class Road:


    def __init__(self, length, width):
        self._width = width
        self._length = length*1000
        self.pavement_mass = 25

    def pavement_calc(self, pavement_thickness = 1):
        """
        Возвращает количество кг асфальта, необходимое для покрытия данного экземпляра дороги
        :param pavement_thickness:
        :return:
        """
        return self._width * self._length * self.pavement_mass * pavement_thickness

try:
    road_66 = Road(float(input("Ширина дороги в метрах: ")), float(input("Длина дороги в километрах: ")))
    print(road_66.pavement_calc(float(input("Толщина покрытия в см: "))))
except ValueError as err:
    print(err)
