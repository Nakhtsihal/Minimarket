from minimarket_module import *

add_product("milk", 6.80, 1234, "1L", 12)
add_product("yogurt", 4.90, 4321, "200ml", 6)
add_product("bread", 10.80, 5454, "0.5kg", 15)
add_product("yogurt", 4.90, 4321, "200ml", 2)

print_products()
remove_product(4321, 5)
print_products()

change_product_price(5454, 8.5)
print_products()