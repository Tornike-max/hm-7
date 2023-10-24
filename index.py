from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"

class SportCar(Car):
    def start_engine(self):
        self.current_speed = 100
        return f"{super().start_engine()} at current speed {self.current_speed} and max speed {self.max_speed}" ## ეს გამოიყენებს მშობელი კლასის start_engine-ს, ხოლო self.max_speed იქნება ისევ მშობელი ელემენტის max_speed, რადგან სპორტ ქარს max_speed არ აქ.

    def stop_engine(self):
        result = super().stop_engine()
        self.current_speed = 0
        return result


car = SportCar(max_speed=200)
print(car.start_engine())  
print(car.stop_engine()) 
print(car.current_speed)  