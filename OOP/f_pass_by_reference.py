class Cat:
    def __init__(self, color, action) -> None:
        self.color = color
        self.action = action

    def view(self):
        print(self.color, "cat is", self.action)

    def compare(self, cat):  # pass by reference
        if self.action == cat.action:
            print("Both cats are", self.action)
        else:
            print("They are different.")


cat1 = Cat("White", "jumping")
cat2 = Cat("Brown", "sitting")

cat1.view()
cat2.view()

cat1.compare(cat2)
