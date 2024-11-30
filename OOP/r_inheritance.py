class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking.")


a1 = Animal("Jack")
d1 = Dog("Rover")

d1.eat()
d1.bark()
