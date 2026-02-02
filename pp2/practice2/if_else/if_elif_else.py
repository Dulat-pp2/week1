#1
a = int(input())
if a > 0:
    print("Positive")
elif a == 0:
    print("Zero")
else:
    print("Negative")

#2
a = 2
b = 5
if b > a:
  print("b is greater")
elif a == b:
  print("equal")
elif a > b:
  print("a is greater")

#3
a = 200
b = 33
if b > a:
  print("b is greater")
elif a == b:
  print("equal")
else:
  print("a is greater")

#4
age = 15
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

#5
score = 85
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")

#6
temp = 10
if temp > 25:
    print("Hot")
elif temp >= 15:
    print("Warm")
else:
    print("Cold")

#7
day = "Saturday"
if day == "Sunday":
    print("Sunday")
elif day == "Saturday":
    print("Saturday")
else:
    print("Weekday")

#8
a = 15
if a > 0:
  print("The a is positive")

#9
a = input()
if a.isalpha():
   print("Yes")
else:
   print("No")

#10
password = "admin"
if password == "admin":
    print("Admin access")
elif password == "user":
    print("User access")
else:
    print("Access denied")