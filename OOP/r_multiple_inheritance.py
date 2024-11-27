class A:
    def __init__(self) -> None:
        print("__init__ of class A")

    def method(self):
        print("Method of class A")


class B:
    def __init__(self) -> None:
        print("__init__ of class B")

    def method(self):
        print("method of class B")


class C(A, B):

    def __init__(self) -> None:
        super().__init__()
        B.__init__(self)


s1 = C()
B.method(s1)
A.method(s1)
