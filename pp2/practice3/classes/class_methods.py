# 1
class Person:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1


# 2
class Temperature:
    @classmethod
    def celsius_to_fahrenheit(cls, c):
        return (c * 9/5) + 32


# 3
class Factory:
    @classmethod
    def create_default(cls):
        return cls()


# 4
class Counter:
    total = 0

    @classmethod
    def add(cls, value):
        cls.total += value


# 5
class MathUtils:
    @classmethod
    def square(cls, x):
        return x ** 2


# 6
class Converter:
    @classmethod
    def km_to_m(cls, km):
        return km * 1000


# 7
class Validator:
    @classmethod
    def is_positive(cls, n):
        return n > 0


# 8
class StringTools:
    @classmethod
    def to_upper(cls, text):
        return text.upper()


# 9
class Multiplier:
    factor = 2

    @classmethod
    def multiply(cls, x):
        return x * cls.factor


# 10
class Builder:
    @classmethod
    def create_with_value(cls, value):
        instance = cls()
        instance.value = value
        return instance