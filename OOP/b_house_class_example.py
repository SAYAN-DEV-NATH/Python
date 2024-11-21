class House:
    def __init__(self) -> None:  # constructor
        self.window = 4  # default instance variable
        self.door = 2  # default instance variable

    def view(self):  # instance method
        print(self.window, "windows", self.door, "doors")


house1 = House()  # instance1
house2 = House()  # instance2

house1.view()
house2.view()

print(house1)
print(house2)
