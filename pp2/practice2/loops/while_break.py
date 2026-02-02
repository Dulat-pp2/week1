#1
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

#2
i = 0
while True:
    if i == 3:
        break
    print(i)
    i += 1

#3
numbers = [1, 3, 5, 7]
i = 0
while i < len(numbers):
    if numbers[i] == 5:
        break
    print(numbers[i])
    i += 1

#4
password = ""
while True:
    password = input("Enter password: ")
    if password == "1234":
        break
print("Access granted")

#5
nums = [2, 4, -1, 6]
i = 0
while i < len(nums):
    if nums[i] < 0:
        break
    print(nums[i])
    i += 1

#6
i = 5
while i > 0:
    print(i)
    if i == 2:
        break
    i -= 1

#7
word = "Python"
i = 0
while i < len(word):
    if word[i] == "h":
        break
    print(word[i])
    i += 1

#8
while True:
    x = int(input("Enter 0 to stop: "))
    if x == 0:
        break

#9
i = 1
while i < 20:
    if i > 10:
        break
    print(i)
    i += 1

#10
while True:
    text = input()
    if text == "stop":
        break