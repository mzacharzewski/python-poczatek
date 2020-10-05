
import math

def calculate_c_len(a_len, b_len):
    d = pow(a_len, 2) + pow(b_len, 2)
    c = math.sqrt(d)
    return c

a = int(input("Pierwsza przyprostokątna: "))
b = int(input("Druga przyprostokątna: "))
print(f"Wynik: {calculate_c_len(a, b):.2f}")