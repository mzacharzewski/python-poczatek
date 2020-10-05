
import math

a = int(input("Pierwsza przyprostokątna: "))
b = int(input("Druga przyprostokątna: "))
d = pow(a, 2) + pow(b, 2)
c = math.sqrt(d)
print(f"Wynik: {c:.2f}")