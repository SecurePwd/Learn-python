# Week 7: OOP Principles

# 1. Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Outputs: Woof!

# 2. Encapsulation (Private Attributes)
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed  # Private attribute
    
    def accelerate(self):
        self.__speed += 10
        return f"Speed is now {self.__speed}"

car = Car("Toyota", 60)
print(car.accelerate())
