#1
a, b = 10, 5
print(f"{a} > {b}: {a > b}")

#2
a = int(input())
b = int(input())
print(f"{a} < {b}: {a < b}")

#3
a, b = 7, 22
print(f"{a} == {b}: {a == b}")
print(f"{a} >= {b}: {a >= b}")

#4
a, b = 7, 22
print(f"{a == b}")
print(f"{a >= b}")

#5
str1, str2 = "apple", "banana"
print(f"{str1 < str2}")
print(f"{str1 == 'banana'}")

#6
list1, list2 = [1, 2, 3], [1, 2, 4]
print(f"{list1} == {list2}: {list1 == list2}")
print(f"{list1} < {list2}: {list1 < list2}")

#7
list1, list2 = [1, 2, 3], [1, 2, 4]
print(f"{list1 == list2}")
print(f"{list1 < list2}")

#8
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a == b: {a == b}")  # True - same content
print(f"a is b: {a is b}")  # False - different objects
print(f"a is c: {a is c}")  # True - same object

#9
password = input("Enter your password: ")
is_valid_length = 8 <= len(password) <= 20
has_uppercase = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)

print(f"Password length OK: {is_valid_length}")
print(f"There is a capital letter: {has_uppercase}")
print(f"There is a digit: {has_digit}")

#10
a, b = 17, 3
print(f"{a} > {b}: {a > b}")