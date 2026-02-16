students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

numbers = [5, 2, 9, 1, 7]

# 1
sorted_numbers = sorted(numbers, key=lambda x: x)

# 2
sorted_desc = sorted(numbers, key=lambda x: x, reverse=True)

# 3
sorted_by_grade = sorted(students, key=lambda x: x["grade"])

# 4
sorted_by_grade_desc = sorted(students, key=lambda x: x["grade"], reverse=True)

# 5
sorted_by_name = sorted(students, key=lambda x: x["name"])

# 6
words = ["cat", "elephant", "dog", "giraffe"]
sorted_by_length = sorted(words, key=lambda x: len(x))

# 7
sorted_by_last_letter = sorted(words, key=lambda x: x[-1])

# 8
numbers2 = [-10, 5, -3, 2]
sorted_by_abs = sorted(numbers2, key=lambda x: abs(x))

# 9
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_by_second = sorted(pairs, key=lambda x: x[1])

# 10
names = ["alice", "Bob", "charlie"]
sorted_ignore_case = sorted(names, key=lambda x: x.lower())