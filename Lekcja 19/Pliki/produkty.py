products = {"jabłka": {"quantity": 20, "price": 5},
            "buraki": {"quantity": 50, "price": 3},
            "ziemniaki": {"quantity": 100, "price": 2},
            "banany": {"quantity": 10, "price": 8}}

def sprzedaz(produkt, ilosc):
    products[produkt]["quantity"] -= ilosc

