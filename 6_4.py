class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.show_speed(speed)

    def stop(self):
        self.speed = 0
        print(f"Машина '{self.name}' остановилась")

    def turn(self, direction):
        return print(f"Машина '{self.name}' повернула {direction}")

    def show_speed(self, speed):
        self.speed = speed
        print(f"{self.name} движется со скоростью {self.speed}.")


class TownCar(Car):
    def __init__(self, color, name, ):
        super().__init__(color, name, )

    def show_speed(self, speed=None):
        if not speed:
            print(f"Машина '{self.name}' движется со скорстью {self.speed}")
        if speed > 60:
            print("Это городская машина, её скорость ограничена 60 км.")
        else:
            super().speed = speed
            print(f"Машина '{self.name}' движется со скорстью {self.speed}")


class SportCar(Car):
    def __init__(self, color, name, ):
        super().__init__(color, name, )


class WorkCar(Car):
    def __init__(self, color, name, ):
        super().__init__(color, name)

    def show_speed(self, speed=None):
        if not speed:
            print(f"Машина '{self.name}' движется со скорстью {self.speed}")
        elif speed > 40:
            print("Эта рабочая калымага и так еле ездит, 40 километров её предел.")
        else:
            self.speed = speed
            print(f"Машина '{self.name}' движется со скорстью {self.speed}")


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


work_car = WorkCar("Белая", "грузовик")
work_car.go(50)
work_car.go(35)
work_car.show_speed()
print(f"Имя машины '{work_car.name}', цвет {work_car.color}.")
work_car.turn("на право")
work_car.stop()
work_car.show_speed()
if work_car.is_police:
    print("Это полиция")
else:
    print("Это не полицейская машина")
