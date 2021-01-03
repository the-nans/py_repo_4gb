"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
from time import sleep



class TrafficLight:
    __sleep_times = {"red": 7, "yellow": 2, "green": 3}
    def __init__(self):
        self.colors_order = {"green" : "yellow", "red" : "green", "yellow" : "red"}
        self.__color = "green"
        self.__prev_color = self.colors_order[self.__color]
        print(f"Default values: {self.__color} and before it there was {self.__prev_color}")
        print("Right sequence is red-yellow-green-red")


    def running(self, next_color):
        if self.colors_order[next_color] == self.__color:
            self.__prev_color = self.__color
            self.__color = next_color
            print(f"Now it's {self.__color}, prev color {self.__prev_color}")
            self.color_sleep()
            return 1
        else:
            print("color order error!")
            return

    def color_sleep(self):

        sleep(self.__sleep_times[self.__color])

t_l = TrafficLight()
try:
    while t_l.running(input("? \n")):
        pass
except KeyError as err:
    print(err)
