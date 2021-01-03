"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""
class Car:

    def __init__(self, name, color, speed, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # print(f"Our car is {name} colored {color}")

    def __enter__(self):
        print(f"{self.name} colored {self.color} is starting the engine!")
        print("This car is police!" if self.is_police else "--")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} colored {self.color} leaves traffic")

    def go(self):
        print(f"{self.color} car {self.name} goes forward")

    def stop(self):
        print(f"{self.color} car {self.name} stops")

    def turn(self, direction):
        print(f"{self.color} car {self.name} turns {direction}")

    def show_speed(self):
        print(f"{self.color} car {self.name} goes {self.speed} mph")

class TownCar(Car):

    def show_speed(self):
        print(f"{self.color} car {self.name} goes {self.speed} mph")
        if int(self.speed) > 60:
            print("Overspeed! Let's call the police!")
            return 1
        return

class WorkCar(Car):

    def show_speed(self):
        print(f"{self.color} car {self.name} goes {self.speed} mph")
        if self.speed > 40:
            print("Overspeed! Let's call the police!")
            return 1
        return

class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)
        self._police_sound = "WeeeoowwWwwreeeooWWWwwoeeooOWW!"

    def _make_sound(self):
        print(self._police_sound)

    def __call__(self, *args, **kwargs):
        self._make_sound()

    def catch_trespassor(self, trespassor_speed):
        if trespassor_speed < self.speed:
            print("Police catches the trespassor")
            return 1
        else:
            print(f"{self.speed} mph is miserably slow to catch the trespassor")
            return


def road_chase(trespassor, policecar):
    with trespassor as car:
        car.go()
        if car.show_speed():
            policecar()
            with policecar as police:
                police.go()
                trespassor.turn("right-left-right")
                police.turn("right-left-right")
                if police.catch_trespassor(trespassor.speed) is None:
                    police.stop()
                    trespassor.turn("To hell")
                    return "A glorious race!"
            return "A shameful attempt of trespassing"
        car.turn("to destination")
        car.stop()
        return "A smooth ride"

print("\n")
print(road_chase(TownCar("Mazda", "white", 50), PoliceCar("Renault Logan", "white", 100)))
print("\n")
print(road_chase(WorkCar("Caterpillar Bulldozer", "red", 45), PoliceCar("Renault Logan", "white", 50)))
print("\n")
print(road_chase(SportCar("Dodge Viper", "blue", 140), PoliceCar("Renault Logan", "white", 120)))