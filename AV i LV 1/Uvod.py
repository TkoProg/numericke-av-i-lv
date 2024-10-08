def faktorijel(n: int) -> int: # Ovako profa deklarise funkcije, zanimljivo tbh. Nismo ovako radili kod Elvedina
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


print(f"f(5) = {faktorijel(5)}")
print(f"{1/3:.20f}") # Format za ispis sa 20 decimala, Vidimo da sve poslije 16. decimale nije tacno
print(f"1.1 + 2.2:20f") # Ovdje se isto desi, nakon 16. Decimale nije tacan ispis
