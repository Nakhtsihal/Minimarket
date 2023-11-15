products = dict()


def add_product(name: str, price: float, code: int, unit: str, amount: int):
    key = (name, price, code, unit)
    if key in products:
        value = products.get(key)
        value += amount
        products.update({key: value})
    else:
        products.update({key: amount})







def print_products():
    print("===================================================")
    print("\tProducts")
    for key in products.keys():
        print("name: ", key[0], ",price:", key[1], ",unit:", key[3], ",code: ", key[2])
        print("amount: ", products.get(key))
    else:
        print("===================================================")


def remove_product(code: int, amount: int):
    for key in products:
        if int(key[2]) == code:
            value = products.get(key)
            if amount > value:
                print(f"ERROR: only {value} have in stock")
                return
            value -= amount
            products.update({key: value})
            return
    print("ERROR: wrong code")


def change_product_price(code: int, new_price: float):
    for key in products:
        if int(key[2]) == code:
            new_key = (key[0], new_price, key[2], key[3])
            value = products.get(key)
            products.pop(key)
            products.update({new_key: value})
            return

