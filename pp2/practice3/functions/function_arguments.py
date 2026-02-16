# 1. Function with two required arguments
def greet(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# 2. Function with one argument
def square(number):
    return number ** 2


# 3. Function with default argument
def power(base, exponent=2):
    return base ** exponent


# 4. Function with multiple arguments
def add_three(a, b, c):
    return a + b + c


# 5. Function with arbitrary number of arguments (*args)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


# 6. Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    return kwargs


# 7. Function with positional and default arguments
def introduce(name, country="Kazakhstan"):
    return f"{name} is from {country}."


# 8. Function with mixed arguments
def calculate(a, b=10):
    return a + b


# 9. Function returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)


# 10. Function with boolean argument
def is_adult(age):
    return age >= 18