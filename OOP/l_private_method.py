class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.__id = id

    def details(self):
        print(f"Name: {self.name}, ID: {self.__id}")
        self.__method()

    def __method(self):
        print("Private method executed.")


s1 = Student("Bob", 11)
s2 = Student("Caral", 32)

s1.details()
s2.details()
