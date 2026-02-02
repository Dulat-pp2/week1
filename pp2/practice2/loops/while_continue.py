#1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#2
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

#3
i = 0
while i < 10:
    i += 1
    if i % 2 != 1:
        continue
    print(i)

#4
numbers = [2, -1, 4, -3, 6]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

#5
numbers = [2, -1, 4, -3, 6]
i = 0
while i < len(numbers):
    if numbers[i] > 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

#6
words = ["hello", "skip", "world"]
i = 0
while i < len(words):
    if words[i] == "skip":
        i += 1
        continue
    print(words[i])
    i += 1

#7
word = "Python"
i = 0
while i < len(word):
    if word[i] == "h":
        i += 1
        continue
    print(word[i])
    i += 1

#8
nums = [1, 0, 2, 0, 3]
i = 0
while i < len(nums):
    if nums[i] == 0:
        i += 1
        continue
    print(nums[i])
    i += 1

#9
i = 0
while i < 10:
    i += 1
    if i > 5:
        continue
    print(i)

#10
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print("Number:", i)