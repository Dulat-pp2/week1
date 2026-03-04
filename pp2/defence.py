#507
# import re

# s = input()
# r = input()
# p = input()
# print(re.sub(r, p, s))

#508
# import re

# s = input()
# p = input()
# print(",".join(re.split(p, s)))

#509
# import re

# s = input()
# words = re.findall(r"\b[A-Za-z]{3}\b", s)
# print(len(words))

#510
# import re

# s = input()
# if re.findall(r"(cat|dog)", s):
#     print("Yes")
# else:
#     print("No")

#511
# import re

# s = input()
# print(len(re.findall(r"[A-Z]", s)))

#512
# import re

# s = input()
# print(*re.findall(r"[0-9]{2,}", s))

#512
# import re

# s = input()
# count = 0
# print(len(re.findall(r"\w+", s)))

#513
import re

s = input()
p = re.compile(r"^\d+$")
if p.match(s):
    print("Match")
else:
    print("No match")