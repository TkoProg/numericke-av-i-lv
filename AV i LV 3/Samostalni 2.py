def horner(lista, x: float) -> float:  # Hornerova shema
    bn = lista[-1]
    for i in range(len(lista) - 2, -1, -1):
        bn = lista[i] + (bn * x)
    return bn


def horner_rekuzrzija(lista, x, n=None):
    # Ako n nije zadato, koristi dužinu liste koeficijenata - 1
    if n is None:
        n = len(lista) - 1

    # Baza rekurzije: ako je n nula, vrati konstantni koeficijent
    if n == 0:
        return lista[0]

    # Rekurzivno pozivanje funkcije
    return lista[n] + x * horner_rekuzrzija(lista, x, n - 1)


print(horner([4, 2, 6], 2))  # Ovdje je oblika 4+2x+6x^2
print(horner_rekuzrzija([6, 2, 4], 2))  # Ovdje je oblika 6+2x+4x^2
