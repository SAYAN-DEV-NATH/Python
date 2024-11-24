class Car:
    def __init__(self, name, model) -> None:
        self.name = name
        self.model = model
        self.wheel = 4

    def view(self):
        print(
            f"The model of this {self.name}, is {self.model} with {self.wheel} wheels."
        )


car1 = Car("BMW", 2016)
car1.view()
