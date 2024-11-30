class Student:
    # def __init__(self, name, id) -> None:
    #     self.name = name
    #     self.id = id

    # def __init__(self, name, id, cgpa) -> None:
    #     self.name = name
    #     self.id = id
    #     self.cgpa = cgpa

    # def __init__(self, *info) -> None:
    #     if len(info) == 3:
    #         self.name = info[0]
    #         self.id = info[1]
    #         self.cgpa = info[2]
    #     elif len(info) == 2:
    #         self.name = info[0]
    #         self.id = info[1]
    #     elif len(info) == 1:
    #         self.name = info[0]
    #     print("A student object created.")

    def __init__(self, **info) -> None:  # unknown key, value arguments
        print(info)
        if len(info) == 3:
            self.name = info["name"]
            self.id = info["id"]
            self.cgpa = info["cgpa"]
        elif len(info) == 2:
            self.name = info["name"]
            self.id = info["id"]
        elif len(info) == 1:
            self.name = info["name"]

        print("A student object created\n")


# s1 = Student("Bob", 33)
# s2 = Student("Ali", 11, 4.0)

s1 = Student(name="Ali", id=33, cgpa=4.0)
s2 = Student(name="Bob", id=55)
s3 = Student(name="Manik")
s4 = Student()
