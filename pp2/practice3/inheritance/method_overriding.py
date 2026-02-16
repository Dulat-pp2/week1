# 1
class Animal:
    def speak(self):
        return "Sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


# 2
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        return 10


# 3
class Employee:
    def work(self):
        return "Working"


class Manager(Employee):
    def work(self):
        return "Managing"


# 4
class Bird:
    def fly(self):
        return "Flying"


class Penguin(Bird):
    def fly(self):
        return "Cannot fly"


# 5
class Vehicle:
    def move(self):
        return "Moving"


class Bike(Vehicle):
    def move(self):
        return "Riding"


# 6
class Person:
    def role(self):
        return "Person"


class Student(Person):
    def role(self):
        return "Student"


# 7
class Food:
    def taste(self):
        return "Normal"


class Cake(Food):
    def taste(self):
        return "Sweet"


# 8
class Device:
    def status(self):
        return "Off"


class Laptop(Device):
    def status(self):
        return "On"


# 9
class Animal:
    def type(self):
        return "Unknown"


class Tiger(Animal):
    def type(self):
        return "Wild"


# 10
class Building:
    def open(self):
        return "Closed"


class Shop(Building):
    def open(self):
        return "Open"