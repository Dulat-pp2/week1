#1
is_active = True
is_completed = False
print(f"is_active: {is_active}, is_completed: {is_completed}")
print(f"Тип is_active: {type(is_active)}")

#2
result = 10 > 5
print(f"10 > 5: {result}")


#3
number = 7
is_even = number % 2 == 0
print(f"Число {number} четное: {is_even}")


#4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#5
print(13 > 99)

#6
print(bool("Hello"))
print(bool(15))

#7
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#8
print(bool(""))
print(bool(0))

#9
print(10 > 9)
print(10 == 9)
print(10 < 9)

#10
print(10 != 9)