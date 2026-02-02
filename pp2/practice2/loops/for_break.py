#1
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#2
num = [1, 3, 5, 7, 9]
for n in num:
    if n == 5:
        break
    print(n)

#3
nums = [2, 4, 6, -1, 8]
for x in nums:
    if x < 0:
        break
    print(x)

#4
passwords = ["123", "admin", "qwerty"]
for p in passwords:
    if p == "admin":
        print("Found admin")
        break

#5
word = "Python"
for letter in word:
    if letter == "h":
        break
    print(letter)

#6
for i in range(1, 20):
    if i > 7:
        break
    print(i)

#7
for i in range(1, 10):
    if i % 2 != 0:
        break
    print(i)

#8
values = [10, 20, 30, 40]
for v in values:
    if v == 30:
        break
    print(v)

#9
words = ["hello", "stop", "world"]
for w in words:
    if w == "stop":
        break
    print(w)

#10
for i in range(100):
    if i == 3:
        break
    print("Hello")