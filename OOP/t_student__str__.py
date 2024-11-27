class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def __str__(self) -> str:  # overriding
        return f"This is {self.name}"


s1 = Student("Bob", 11)
s2 = Student("Carol", 11)

# print(s1.__str__())
# print(s1)
print(s1, s2)
