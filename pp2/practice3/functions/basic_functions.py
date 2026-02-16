# 1. Function that returns the sum of two numbers
def add(a, b):
    return a + b


# 2. Function that returns the difference of two numbers
def subtract(a, b):
    return a - b


# 3. Function that returns the product of two numbers
def multiply(a, b):
    return a * b


# 4. Function that divides two numbers
# It checks division by zero
def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero is not allowed"


# 5. Function that checks if a number is even
def is_even(n):
    return n % 2 == 0


# 6. Function that checks if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 7. Function that finds the maximum value in a list
def find_max(arr):
    return max(arr)


# 8. Function that returns the length of a string
def string_length(s):
    return len(s)


# 9. Function that converts a string to uppercase
def to_uppercase(s):
    return s.upper()


# 10. Function that raises a number to a power
def power(a, b):
    return a ** b