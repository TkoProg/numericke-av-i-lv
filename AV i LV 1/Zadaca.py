def faktorijel(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

def eksponencijalna(x):
    suma = 0.0
    for i in range(0, 15):
        suma = x**i/faktorijel(x) + suma
    return suma


print(eksponencijalna(1.0))
