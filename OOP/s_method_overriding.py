class A:
    def __init__(self) -> None:
        print("__init__ of class A")

    def method1(self):
        print("Always study")

    def method2(self):
        print("You will get all of my property and methods")


class B(A):
    def __init__(self) -> None:
        pass

    def method1(self):
        print("Always party")


b1 = B()
b1.method1()
