def faktorijel(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(f"f(5) = {faktorijel(5)}")
print(f"{1/3:.20f}") # format za ispis sa 20 decimala, vidimo da sve poslije 16. decimale nije tacno
print(f"1.1 + 2.2:20f") # ovdje se isto desi, nakon 16. decimale nije tacan ispis
