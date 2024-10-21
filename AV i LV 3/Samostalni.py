def ln(x: float) -> float:
    suma = 0
    temp = x
    for i in range(0, 25):
        suma += (((-1)**i)*(temp))/(i+1)
        temp *= x
    return suma


def lnbolji(x: float) -> float:
    suma = 0
    temp = x
    for i in range(1, 25):
        suma += 2*(temp)/((2*i)-1)
        temp *= x
        temp *= x
    return suma


def lnlistabolje(x: float) -> float:
    suma = 0
    temp = x
    lista = []
    for i in range(1, 25):
        clan = (temp)/((2*i)-1)
        temp *= x
        temp *= x
        lista.append(clan)
    lista.reverse()
    for i in range(1, 24):
        suma += 2*lista[i]
    return suma

print(ln(1))
print(lnbolji(1/3))
print(lnlistabolje(1/3))
