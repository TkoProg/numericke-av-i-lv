# 1) Napraviti izracun e^x za x iz (-1,1) na 5 tacnih decimala
# 2) Napraviti izracun za sinx, cosx, x iz (-1,1) na 5 tacnih decimala
# 3) Racunanje korijena iz a (sqrt(a))
# Pored toga izracunati ln(2) na 5 tacnih decimala

def faktorijel(n: int) -> int:  # Ocito je sta radi
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


def eksponencijalnaFunkcija(x: float) -> float:  # Bit ce prvih 5 decimala tacno
    suma = 0
    for i in range(0, 9):  # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += x**i/faktorijel(i)
    return suma


def sin(x: float) -> float:  # Bit ce prvih 5 decimala tacno
    suma = 0
    for i in range(0, 9):  # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += (((-1)**i)*(x**((2*i)+1)))/faktorijel((2*i)+1)
    return suma


def cos(x: float) -> float:  # Bit ce prvih 5 decimala tacno
    suma = 0
    for i in range(0, 9):  # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += (((-1)**i)*(x**(2*i)))/faktorijel(2*i)
    return suma


def korijen(x: float, xn=1.0, greska=1e-8) -> float:  # x je broj za koji se trazi korijen, xn je pretpostavljena vrijednost, greska je tolerancija za koliko blizu zelimo da bude stvarne vrijednosti
    if abs(x - xn**2) < greska:
        return xn
    else:
        xn = 1/2*(xn+x/xn)  # Ovo je Newtonova rekurzivna metoda za trazenje korijena broja
        return korijen(x, xn, greska)


def ln(x: float) -> float: # Bit ce prvih 5 decimala tacno. 1/n < 10-5 pa je n < 10^5 koliko puta se petlja mora ponoviti da bi bio tacan rezultat
    suma = 0
    for i in range(0, 100000):  # Ovdje se petlja mora ponoviti najmanje 9 puta da bi 5 decimala bilo tacno (Maklorenov red)
        suma += (((-1)**i)*(x**(i+1)))/(i+1)
    return suma


print(f"{eksponencijalnaFunkcija(-1/2):.5f}")
print(f"{sin(-1/2):.5f}")
print(f"{cos(-1/2):.5f}")
print(f"{ln(1):.5f}")  # Ovo ce izracunati ln(2) jer je Maklorenov red za ln(1+x), ali treba ogroman broj ponavljanja petlje
print(f"{korijen(10):.5f}")
