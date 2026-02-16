# 1
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    pass


# 2
class Vehicle:
    def move(self):
        return "Moving"


class Car(Vehicle):
    def drive(self):
        return "Driving"


# 3
class Person:
    def greet(self):
        return "Hello"


class Student(Person):
    def study(self):
        return "Studying"


# 4
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def rectangle_area(self, w, h):
        return w * h


# 5
class Employee:
    def work(self):
        return "Working"


class Manager(Employee):
    def manage(self):
        return "Managing"


# 6
class Bird:
    def fly(self):
        return "Flying"


class Eagle(Bird):
    pass


# 7
class Device:
    def turn_on(self):
        return "On"


class Phone(Device):
    def call(self):
        return "Calling"


# 8
class Food:
    def taste(self):
        return "Good"


class Fruit(Food):
    pass


# 9
class Computer:
    def compute(self):
        return "Computing"


class Laptop(Computer):
    def portable(self):
        return True


# 10
class Building:
    def open(self):
        return "Open"


class House(Building):
    pass