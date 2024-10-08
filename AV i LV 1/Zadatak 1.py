from typing import List
# a) Unijeti x, unijeti n (n iz N)
# b) Vratiti x^n (n iz N)
# Svi algoritmi uradjeni imaju zapisani sa vjezbi

def stepenovanje(x: float, n: int) -> float:
    rez = 1.0
    for i in range(1, n+1):
        rez *= x
    return rez


def konverzijaUBinarni(n: int) -> List[int]: # Ovo se koristi u algoritmu A1
    rezultat = []
    while n != 0:
        rezultat.append(n % 2)
        n //= 2
    rezultat.reverse()
    return rezultat


def sLijevaNaDesno(x: float, n: int) -> float: # Algoritam A1
    pocetna_vrijednost = x

    l = konverzijaUBinarni(n)
    l.pop(0)

    for e in l:
        x *= x
        if e == 1:
            x = x * pocetna_vrijednost
    return x


def sDesnaNaLijevo(x: float, n: int) -> float: # Algoritam A2
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
    return Y

x = float(input())
n = int(input())

print(stepenovanje(x, n)) # Uzasno sporo
print(sLijevaNaDesno(x, n)) # Brzo
print(sDesnaNaLijevo(x, n)) # Najbrzi od ova 3 algoritma
