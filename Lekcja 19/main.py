from Pliki.operacje import create_new_order, orders

def run_shop():
    print("Witaj w sklepie! \n")
    product_name = (input("Jaki towar chcesz kupić? "))
    quantity = int(input("Ile towaru chcesz kupić? "))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(f"Wartość sprzedaży wyniesie", total_price, "zł.")

if __name__ == "__main__":
    run_shop()