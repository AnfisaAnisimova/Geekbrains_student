class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} is moving!')

    def stop(self):
        print(f'The car {self.name} has stopped.')

    def turn(self, direction):
        print(f'The car {self.name} turned in the {direction} direction.')

    def show_speed(self):
        print(f'Speed of the car is {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("You have exceeded the speed limit!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("You have exceeded the speed limit!")


class PoliceCar(Car):
    pass


car_1 = TownCar(50, "red", "Kia Rio")
car_1.go()
car_1.stop()
car_1.turn("left")
car_1.show_speed()

car_2 = WorkCar(70, "silver", "Toyota Yaris")
car_2.go()
car_2.stop()
car_2.turn("right")
car_2.show_speed()

car_3 = SportCar(120, "black", "Jaguar F Type SVR")
car_3.go()
car_3.stop()
car_3.turn("right")
car_3.show_speed()

car_4 = PoliceCar(80, "blue", "Ford Focus")
car_4.go()
car_4.stop()
car_4.turn("right")
car_4.show_speed()
