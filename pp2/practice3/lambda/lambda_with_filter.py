numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 2
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# 3
greater_than_five = list(filter(lambda x: x > 5, numbers))

# 4
less_than_four = list(filter(lambda x: x < 4, numbers))

# 5
positive_numbers = list(filter(lambda x: x > 0, [-5, 3, -2, 7]))

# 6
long_words = list(filter(lambda x: len(x) > 4, ["cat", "elephant", "dog", "giraffe"]))

# 7
starts_with_a = list(filter(lambda x: x.startswith("a"), ["apple", "banana", "avocado"]))

# 8
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))

# 9
non_zero = list(filter(lambda x: x != 0, [0, 1, 2, 0, 3]))

# 10
negative_numbers = list(filter(lambda x: x < 0, [-3, 4, -1, 6]))