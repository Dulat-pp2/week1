# n = int(input())
# power = 1

# while power <= n:
#     print(power, end=' ')
#     power *= 2

a = int(input())
b = int(input())
c = int(input())

s = list(map(int, input().split()))

g = s[:b-1]
f = s[b-1]
d = s[b:c-1]
e = s[c-1:]
    
print(*g, f, *d, *e)
