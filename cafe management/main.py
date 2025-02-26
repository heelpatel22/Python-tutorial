menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':30,
    'Coffe':80,
}

print("Welcome to Pycode Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs30\nCoffe: Rs80")

order_total = 0
item_1 = input("Enter the name of an item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order.")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items is {order_total}.")