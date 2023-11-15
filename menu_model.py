from minimarket_module import *


def input_products():
    name = input("Product name>>>")
    price = float(input("Enter price>>>"))
    code = int(input("Enter code>>>"))
    unit = input("Enter unit>>>")
    amount = int(input("Enter amount>>>"))
    add_product(name, price, code, unit, amount)


def input_remove_product():
    code = int(input("Enter code>>>"))
    amount = int(input("Enter amount>>>"))
    remove_product(code, amount)


while True:
    print("choose option:")
    print("1. add product")
    print("2. print products")
    print("3. remove product")
    print("4. change price")
    print("5. exit")
    answer = input(">>>")
    if answer == "5":
        break
    elif answer == 2:
        print_products()
    elif answer == "1":
        input_products()
    elif answer == "3":
        input_remove_product()

