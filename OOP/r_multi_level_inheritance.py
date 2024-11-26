class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def details(self):
        print(f"Name: {self.name}, ID: {self.id}")


class CSE(Student):
    def __init__(self, name, id, labs) -> None:
        super().__init__(name, id)
        self.labs = labs

    def cry(self, labs):
        print(f"{self.name} is crying because of {self.labs} labs")


class CSE_RRESHER(CSE):
    def enroll(self):
        print("Enrolled in CSE110")


s1 = CSE("Bob", 11, 3)
s2 = CSE_RRESHER("Carol", 55, 1)

s2.details()
