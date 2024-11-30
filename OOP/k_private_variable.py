class Student:
    def __init__(self, name, id) -> None:
        self.name = name  # instance variable
        self.__id = id  # private instance variable

    def details(self):  # instance method
        print("Name:", self.name, "ID:", self.__id)

    def set_id(self, id):
        if id > 0:
            self.__id = id
        else:
            print("Invalid ID, Enter valid ID.")

    def get_id(self):
        print(self.__id)


s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

s1.set_id(5)
s1.get_id()

s1.details()
s2.details()
