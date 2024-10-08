# 1) Napraviti izracun e^x za x iz (-1,1) na 5 tacnih decimala
# 2) Napraviti izracun za sinx, cosx, x iz (-1,1) na 5 tacnih decimala
# 3) Racunanje korijena iz a (sqrt(a))
# Pored toga izracunati ln(2) na 5 tacnih decimala

def faktorijel(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


def eksponencijalnaFunkcija(x: float) -> float: # Bit ce prvih 5 decimala tacno
    suma = 0
    for i in range(0, 9): # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += x**i/faktorijel(i)
    return suma


def sin(x: float) -> float: # Bit ce prvih 5 decimala tacno
    suma = 0
    for i in range(0, 9): # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += (((-1)**i)*(x**((2*i)+1)))/faktorijel((2*i)+1)
    return suma


def cos(x: float) -> float: # Bit ce prvih 5 decimala tacno
    suma = 0
    for i in range(0, 9): # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += (((-1)**i)*(x**(2*i)))/faktorijel(2*i)
    return suma


print(f"{eksponencijalnaFunkcija(-1/2):.5f}")
print(f"{sin(-1/2):.5f}")
print(f"{cos(-1/2):.5f}")
