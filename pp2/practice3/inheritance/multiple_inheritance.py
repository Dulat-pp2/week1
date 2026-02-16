# 1
class Fly:
    def fly(self):
        return "Flying"


class Swim:
    def swim(self):
        return "Swimming"


class Duck(Fly, Swim):
    pass


# 2
class Writer:
    def write(self):
        return "Writing"


class Speaker:
    def speak(self):
        return "Speaking"


class Author(Writer, Speaker):
    pass


# 3
class A:
    def method_a(self):
        return "A"


class B:
    def method_b(self):
        return "B"


class C(A, B):
    pass


# 4
class Scanner:
    def scan(self):
        return "Scanning"


class Printer:
    def print_doc(self):
        return "Printing"


class AllInOne(Scanner, Printer):
    pass


# 5
class Musician:
    def play(self):
        return "Playing music"


class Teacher:
    def teach(self):
        return "Teaching"


class MusicTeacher(Musician, Teacher):
    pass


# 6
class Camera:
    def capture(self):
        return "Capturing"


class Phone:
    def call(self):
        return "Calling"


class SmartPhone(Camera, Phone):
    pass


# 7
class Run:
    def run(self):
        return "Running"


class Jump:
    def jump(self):
        return "Jumping"


class Athlete(Run, Jump):
    pass


# 8
class Read:
    def read(self):
        return "Reading"


class Write:
    def write(self):
        return "Writing"


class Student(Read, Write):
    pass


# 9
class Cook:
    def cook(self):
        return "Cooking"


class Drive:
    def drive(self):
        return "Driving"


class Chef(Cook, Drive):
    pass


# 10
class Work:
    def work(self):
        return "Working"


class Study:
    def study(self):
        return "Studying"


class Intern(Work, Study):
    pass