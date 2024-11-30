class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.color = "White"

    def eat(self):
        print(f"{self.color} {self.name} is eating")


class Dog(Animal):
    def __init__(self, name, color) -> None:
        super().__init__(name)
        self.color = color

    def bark(self):
        print(f"{self.color} {self.name} is barking")


d1 = Dog("Mike", "Brown")
d1.bark()
d1.eat()
print(d1.__dict__)
