class Student:
    university_name = "BGCTUB"  # class variable

    def __init__(self, name, id) -> None:  # instance or object constructor
        self.name = name  # instance or object variable
        self.__id = id

    def details(self):  # instance or object method
        print(f"Name: {self.name}, ID: {self.__id}, {Student.university_name}.")

    @classmethod  # decorator
    def update_university_name(cls, name):  # class method
        cls.university_name = name
        # Student.university_name = name

    @classmethod
    def from_string(cls, info):
        name, id = info.split("-")
        obj = cls(name, id)
        return obj

    @staticmethod
    def check_department(id):
        if id[2:4] == "02":
            print("CSE")
        elif id[2:4] == "41":
            print("CS")


student1 = Student("Nayan", 11)  # instance or object
student2 = Student.from_string("Sayan-22")

student1.details()
student2.details()

Student.update_university_name("BGC Trust University Bangladesh")  # classmethod call
Student.check_department("230240104")  # staticmethod call

student1.details()
student2.details()
