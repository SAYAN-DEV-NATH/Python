class Car:
    def __init__(self, name, model) -> None:
        self.name = name
        self.model = model
        self.wheel = 4

    def view(self):
        print("The model of this", self.name, "is", self.model, "with", self.wheel)


car1 = Car("BMW", 2016)
car1.view()
