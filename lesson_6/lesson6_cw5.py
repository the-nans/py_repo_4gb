"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Тонкая чёрная линия")


class Pencil(Stationery):
    def draw(self):
        print("Графитовый след на поверхности")


class Handle(Stationery):
    def draw(self):
        print("Жирная полоса пигмента")

pen = Pen("Parker")
pencil = Pencil("Koh-i-noor")
handle = Handle("Komus")

pen.draw()
pencil.draw()
handle.draw()