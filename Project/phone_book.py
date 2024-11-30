phone_book = {}

print("Welcome to the PYTHON phone book\n")
print("New Contact for enter 1")
print("Search Contact for enter 2")
print("Delete Contact for enter 3")
print("Contact List for enter 4")
print("Exit for enter 5")

while True:
    option = int(input())
    if option == 1:
        name = input("Enter your name ")
        number = int(input("Enter your number "))
        phone_book[name] = number
        print("Added Successfully.")

    elif option == 2:
        name = input("Enter name of the number ")
        if name in phone_book:
            print(f"{name} - {phone_book[name]}")
        else:
            print("Not found")

    elif option == 3:
        name = input("Enter name of number that you want to delete ")
        if name in phone_book:
            del phone_book[name]
            print("Delete Successfully")
        else:
            print("Not found")

    elif option == 4:
        for key, value in phone_book.items():
            print(f"{key} - {value}")

    else:
        break

print(phone_book)
