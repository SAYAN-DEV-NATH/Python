from abc import ABC, abstractmethod
from orders import *
from restaurent import Restaurent
from food_item import FoodItem
from menu import Menu


class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if item.quantity >= quantity:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
            else:
                print("Item quantity exceeded!!")
        else:
            print("Item not found")

    def view_cart(self):
        print("\n*****View Cart*****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price()}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price()} paid successfully")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
