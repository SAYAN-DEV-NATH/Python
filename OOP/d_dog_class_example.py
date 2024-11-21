class Dog:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name, "is smilling.")


dog1 = Dog("Rover", "Brown")

dog1.poke()
dog1.update_color("Black")
dog1.poke()
print(dog1.__dict__)  # building attribute
print(
    dir(dog1)
)  # building function, that show me all attribute, variable, method provide with list.
