def faktorijel(n: int) -> int: # Ovako profa deklarise funkcije, zanimljivo tbh. Nismo ovako radili kod Elvedina
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
# Ova funkcija fore je beskorisna jer Aco ne da (tugy plaky)

def mojaE(x: float) -> float:
    rez = 0
    fakt = 1
    temp = x
    for i in range(0, 10):
        if i == 0:
            rez += 1
        elif i == 1:
            rez += x
        else:
            temp = temp * x
            fakt *= i
            rez += temp / fakt
    return rez


def mojaBoljaE(x: float, eps: float) -> float:
    rez = .0
    i = 0
    fakt = 1
    temp = x
    while(True):
        if i == 0:
            rez += 1
        elif i == 1:
            rez += x
        else:
            temp = temp * x
            fakt *= i
            rez += temp / fakt
        i += 1
        rn = (2.72*temp * x) / fakt * i
        if rn < eps:
            break
    return rez


def zaSveE(x: float) -> float:
    eNaCioX = mojaBoljaE(int(x), 1e-6)
    nekoMaloX = x - int(x)
    if x - int(x) < 0:
        nekoMaloX *= 1
    eNaMaloX = mojaBoljaE(nekoMaloX, 1e-6)
    return eNaCioX * eNaMaloX


print(mojaE(2))
print(mojaBoljaE(0, 1e-6))
print(zaSveE(3))
