'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Поехала")

    def stop(self):
        print("Остановилась")

    def turn(self, direction):
        print(f"Поворот {direction}")

    def show_speed(self):
        print(f"Скорость = {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


print("TOWN **********************************")
town = TownCar(speed=100, color="red", name="TownCar")
town.show_speed()
town.speed = 20
town.show_speed()

print("POLICE **********************************")

police = PoliceCar(speed=100, color="red", name="PoliceCar")
police.show_speed()
print("SPORT **********************************")

sport = SportCar(speed=100, color="red", name="SportCar")
sport.show_speed()
sport.go()
sport.turn("налево")
sport.stop()

print("WORK **********************************")
work = WorkCar(speed=41, color="red", name="WorkCar")
work.show_speed()
work.speed = 39
work.show_speed()
