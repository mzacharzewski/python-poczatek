import Calculations.lokatawbanku1

print("Kalkulator wartości lokaty z roczną kapitalizacją")
wartosc = float(input("Wartość lokaty: "))
rate = float(input("Oprocentowanie: "))
years = int(input("Na jaki okres: "))
print(f"Wartość lokaty po {years} latach wynosi {Calculations.lokatawbanku1.lokata_wartosc(wartosc, rate, years):.2f}.")