# 1
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# 2
class Person:
    def greet(self):
        return "Hello"


class Student(Person):
    def greet(self):
        parent_message = super().greet()
        return parent_message + ", I am a student"


# 3
class Vehicle:
    def move(self):
        return "Moving"


class Car(Vehicle):
    def move(self):
        return super().move() + " by car"


# 4
class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius


# 5
class Employee:
    def work(self):
        return "Working"


class Developer(Employee):
    def work(self):
        return super().work() + " on code"


# 6
class Device:
    def turn_on(self):
        return "Device on"


class Phone(Device):
    def turn_on(self):
        return super().turn_on() + " with screen"


# 7
class Book:
    def __init__(self, title):
        self.title = title


class EBook(Book):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size


# 8
class Teacher:
    def introduce(self):
        return "I teach"


class MathTeacher(Teacher):
    def introduce(self):
        return super().introduce() + " math"


# 9
class Animal:
    def sound(self):
        return "Sound"


class Cat(Animal):
    def sound(self):
        return super().sound() + " meow"


# 10
class Worker:
    def task(self):
        return "Task"


class Cleaner(Worker):
    def task(self):
        return super().task() + " cleaning"