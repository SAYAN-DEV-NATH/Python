class Book:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print(
            "Book Name:",
            self.name,
            "\nAuthor Name:",
            self.author,
            "\nPrice:",
            self.price,
            "Taka.",
        )


book1 = Book("Opekkha", "Humayun Ahmed")
book1.details()
book1.set_price(250)
book1.details()
