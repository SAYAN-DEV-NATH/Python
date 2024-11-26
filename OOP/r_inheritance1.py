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

    def cry(self):
        print(f"CSE student is crying because of {self.labs} labs")


class BBA(Student):
    def party(self):
        print("All day party")


s1 = CSE("Nayan", 11, 3)
s2 = BBA("Abrar", 22)

s1.details()
s2.details()
s1.cry()
s2.party()
