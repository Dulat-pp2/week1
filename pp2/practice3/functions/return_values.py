# 1. Function that returns a single value
def add(a, b):
    return a + b


# 2. Function that returns a string
def greet(name):
    return f"Hello, {name}!"


# 3. Function that returns a boolean value
def is_even(n):
    return n % 2 == 0


# 4. Function that returns multiple values (tuple)
def min_max(numbers):
    return min(numbers), max(numbers)


# 5. Function that returns None
def print_message(message):
    print(message)
    return None


# 6. Function that returns a list
def get_squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result


# 7. Function that returns a dictionary
def create_person(name, age):
    return {"name": name, "age": age}


# 8. Function with conditional return
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# 9. Function that returns early
def check_positive(n):
    if n < 0:
        return "Negative number"
    return "Positive number"


# 10. Function that returns a set
def unique_elements(numbers):
    return set(numbers)