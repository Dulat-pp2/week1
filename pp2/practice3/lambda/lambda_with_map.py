numbers = [1, 2, 3, 4, 5]

# 1
squares = list(map(lambda x: x ** 2, numbers))

# 2
cubes = list(map(lambda x: x ** 3, numbers))

# 3
double = list(map(lambda x: x * 2, numbers))

# 4
plus_five = list(map(lambda x: x + 5, numbers))

# 5
to_string = list(map(lambda x: str(x), numbers))

# 6
absolute_values = list(map(lambda x: abs(x), [-1, -2, 3]))

# 7
lengths = list(map(lambda x: len(x), ["cat", "elephant", "dog"]))

# 8
first_letters = list(map(lambda x: x[0], ["apple", "banana", "cherry"]))

# 9
divide_by_two = list(map(lambda x: x / 2, numbers))

# 10
negatives = list(map(lambda x: -x, numbers))