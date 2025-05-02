# Week 6: Object-Oriented Programming

# 1. Creating a Class
class Dog:
    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to describe the dog
    def describe(self):
        return f"{self.name} is {self.age} years old."

# Create an object of the class
dog1 = Dog("Buddy", 3)
print(dog1.describe())
