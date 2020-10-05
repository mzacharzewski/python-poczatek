from .produkty import products, sprzedaz

orders = [
    {"towar": "jabłka",
    "ilość": 5,
    "total_price": 25}
]

def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    dostepna_ilosc = products[product_name]["quantity"]

    if dostepna_ilosc < quantity:
        print('Nie ma tyle towaru.')
        return None

    total_price = price * quantity
    new_order = {"towar": product_name,
                 "ilość": quantity,
                 "total_price": total_price
                 }

    orders.append(new_order)
    sprzedaz(product_name, quantity) # aktualizuje ilość towarów

    return new_order