#1
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#2
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#3
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

#4
num = [2, -1, 4, -3, 6]
for n in num:
    if n < 0:
        continue
    print(n)

#5
words = ["hello", "skip", "world"]
for w in words:
    if w == "skip":
        continue
    print(w)

#6
word = "Python"
for letter in word:
    if letter == "h":
        continue
    print(letter)

#7
nums = [1, 0, 2, 0, 3]
for x in nums:
    if x == 0:
        continue
    print(x)

#8
for i in range(1, 8):
    if i > 5:
        continue
    print(i)

#9
days = ["Mon", "Tue", "Sun", "Wed"]
for day in days:
    if day == "Sun":
        continue
    print(day)

#10
for i in range(1, 10):
    if i == 5:
        continue
    print("Number:", i)