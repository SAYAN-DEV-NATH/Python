from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print("I am eating")

class Dog(Animal):
    