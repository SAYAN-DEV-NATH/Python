menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,
}

print("Welcome to PYTHON Restaurant")
for key, value in menu.items():
    print(f"{key}: {value}TK")

order_total = 0
while True:
    item = input("Enter the name of item you want to order = ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Ordered item '{item}' is not avaiable yet")
    another_order = input("Do you want to add another item? (Yes/No) :")
    if another_order == "Yes":
        continue
    else:
        break
print(f"Total amount of items to pay is {order_total}.")
