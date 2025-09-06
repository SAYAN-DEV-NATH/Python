from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurent import Restaurent
from users import Customer, Admin, Employee

restaurent = Restaurent("Mamar Restaurent")


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"\nWelcome {customer.name}!!")
        print("1. view menu")
        print("2. add item to cart")
        print("3. view cart")
        print("4. pay bill")
        print("5. exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(restaurent)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(restaurent, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid input")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"\nWelcome {admin.name}!!")
        print("1. add new item")
        print("2. add new employee")
        print("3. view employee")
        print("4. view item")
        print("5. delete item")
        print("6. exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(restaurent, item)
        elif choice == 2:
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            phone = int(input("Enter employee phone: "))
            address = input("Enter employee address: ")
            age = input("Enter employee age: ")
            designation = input("Enter employee designation: ")
            salary = int(input("Enter employee salary: "))
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(restaurent, employee)
        elif choice == 3:
            admin.view_employee(restaurent)
        elif choice == 4:
            admin.view_menu(restaurent)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(restaurent, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid input")


while True:
    print("Welcome!!")
    print("1. customer")
    print("2. admin")
    print("3. exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input")
