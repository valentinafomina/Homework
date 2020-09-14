class Car:
    speed = ()
    color = ()
    name = ()
    is_police = bool

    def go(self):
        print("Старт")

    def stop(self):
        print("Стоп")

    def turn(self, direction):
        print(f"Повернуть {direction}")

    def show_speed(self):
        speed = int()
        print(f"{speed} км/ч")


class SportCar(Car):
    pass


class PoliceCar (Car):
    pass


class TownCar (Car):
    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")
        if self.speed > 40:
            print("Превышение скорости")


class WorkCar (Car):
    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")
        if self.speed > 60:
            print("Превышение скорости")


vaz2110 = WorkCar()
vaz2110.speed = 30
vaz2110.color = "зелёный"
vaz2110.name = "Десятка"
vaz2110.is_police = False
print(vaz2110.name, vaz2110.color, vaz2110.is_police, vaz2110.turn("направо"))
vaz2110.show_speed()

vaz2107 = TownCar()
vaz2107.speed = 70
vaz2107.color = "синий"
vaz2107.name = "Семёрка"
vaz2107.is_police = False
print(vaz2107.name, vaz2107.color, vaz2107.is_police, vaz2110.turn("налево"))
vaz2107.show_speed()
