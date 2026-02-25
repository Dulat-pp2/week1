#401
# def sq(n):
#     for i in range(1, n + 1):
#         yield i**2
# a = sq(int(input()))
# for i in a:
#     print(i)


#402
# def even(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

# a = even(int(input()))

# first = True
# for i in a:
#     if not first:
#         print(",", end="")
#     print(i, end="")
#     first = False


#403
# def div(n):
#     for i in range(n + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# a = div(int(input()))
# for i in a:
#     print(i, end=" ")


# 404
# def squares(a, b):
#     for i in range(a, b + 1):
#         yield i ** 2

# a, b = map(int, input().split())

# n = squares(a, b)
# for i in n:
#     print(i)


#405
# def countdown(n):
#     for i in range(n, -1, -1):
#         yield i

# for i in countdown(int(input())):
#     print(i)


#406
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# first = True
# for i in fibonacci(int(input())):
#     if not first:
#         print(",", end="")
#     print(i, end="")
#     first = False


#407
# def reverse(s):
#     for i in reversed(s):
#         yield i

# for i in reverse(input()):
#     print(i, end="")


#408
def primes(n):
    for num in range(2, n + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

# n = int(input())
print(*primes(int(input())))


#409
# def pow2(n):
#     for i in range(n + 1):
#         yield 2 ** i

# for i in pow2(int(input())):
#     print(i, end = " ")


#410
# def limit(arr):
#     m = int(input())
#     for i in range(m):
#         yield arr

# for i in limit(list(map(str, input().split()))):
#     print(*i, end = " ")

#411
# import json

# def patch(s, p):
#     if isinstance(s, dict) and isinstance(p, dict):
#         for k, v in p.items():
#             if v is None:
#                 s.pop(k, None)
#             elif k in s and isinstance(s[k], dict) and isinstance(v, dict):
#                 s[k] = patch(s[k], v)
#             else:
#                 s[k] = v
#     else:
#         return p
#     return s

# source = json.loads(input())
# patch_obj = json.loads(input())

# print(json.dumps(patch(source, patch_obj), separators=(",", ":"), sort_keys=True))


#412
