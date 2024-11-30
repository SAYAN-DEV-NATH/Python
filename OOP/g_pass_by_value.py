class Cat:
    def __init__(self, color, action) -> None:
        self.color = color
        self.action = action

    def view(self, num, clr):
        num = num + 5
        clr1 = clr
        clr1[0] = "Green"
        print("Method inside:", num)
        print("Method inside:", clr)


colors = ["Black", "Red", "Yellow", "Blue"]
cat1 = Cat("White", "jumping")

x = 55
cat1.view(x, colors)  # x passbyvalue and colors passbyreference
print("Method outside:", x)
print("Method outside:", colors)
