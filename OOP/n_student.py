class Student:
    count = 0  # static or class variable

    def __init__(self, name, id) -> None:  # instance method
        self.name = name  # instance variable
        self.id = id
        Student.count += 1

    def details(self):
        print(f"Name: {self.name}, ID: {self.id}")


s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s3 = Student("Mike", 33)

s1.details()
print("Student Count:", Student.count)
