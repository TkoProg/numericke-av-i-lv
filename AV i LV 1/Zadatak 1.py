# from typing import List
# a) Unijeti x, unijeti n (n iz N)
# b) Vratiti x^n (n iz N)

# def stepenovanje(x: float, n: int) -> float:
#     rez = 1.0
#     for i in range(1, n+1):
#         rez *= x
#     return rez

# def konverzija(n: int) -> List[int]:
#     rezultat = []
#     while n != 0:
#         rezultat.append(n % 2)
#         n //= 2
#     rezultat.reverse()
#     return rezultat
#
#
# x = float(input())
# izv = x
# n = int(input())
#
# l = konverzija(n)
# l.pop(0)
#
# for e in l:
#     if e == 0:
#         x *= x
#     if e == 1:
#         x *= x
#         x = x * izv
#
# print(x)

x = float(input())
n = int(input())

Y = 1
N = n
Z = x

while N != 0:
    F = N % 2
    N = N // 2
    if F != 0:
        Y = Z * Y
        if N == 0:
            break
    Z *= Z

print(Y)

# Uradi sve zadatke fino po funkcijama organizovano.