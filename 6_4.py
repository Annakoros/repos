from random import randint, choice
from time import sleep
class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = False
    def go(self):
        print('Начало движения')
        self.speed = randint(0,120)
        sleep(1)
        print(f'Скорость {self.speed}')
    def stop(self):
        sleep(1)
        print('Конец движения')
        self.speed = 0
        sleep(1)
        print(f'Скорость {self.speed}')
        print('-' * 50)
    def turn(self):
        self.direction = choice(['Направо', 'Налево'])
        sleep(1)
        print(self.direction)
    def show_speed(self):
        self.speed = randint(0, 180)
        sleep(1)
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(color, name, speed, is_police)

    def go(self):
        print('Начало движения')
        self.speed = randint(0,120)
        sleep(1)
        print(f'Скорость {self.speed}')
        if self.speed > 60:
            print('Превышение!!!')

    def show_speed(self):
        self.speed = randint(0, 120)
        sleep(1)
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 60:
            print('Превышение!!!')

class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(color, name, speed, is_police)

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(color, name, speed, is_police)

    def go(self):
        print('Начало движения')
        self.speed = randint(0,80)
        sleep(1)
        print(f'Скорость {self.speed}')
        if self.speed > 40:
            print('Превышение!!!')

    def show_speed(self):
        self.speed = randint(0, 80)
        sleep(1)
        print(f'Текущая скорость: {self.speed}')
        if self.speed > 40:
            print('Превышение!!!')

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(color, name, speed, is_police)
        self.is_police = True

ferrari = SportCar('ferrari spider', 'white', 0, False)
hyindai = TownCar('hyindai starex', 'black', 0, False)
bobcat = WorkCar('bobcat snow cleaner', 'orange', 0, False)
ford = PoliceCar('ford focus', 'white-blue', 0, True)

for auto in [ferrari, hyindai, bobcat, ford]:
    print(f'{auto.name}, {auto.color}')
    print(f'Является ли авто полицейским: {auto.is_police}')
    auto.go()
    for i in range(0, 3):
        auto.turn()
        auto.show_speed()
        i += 1
    auto.stop()