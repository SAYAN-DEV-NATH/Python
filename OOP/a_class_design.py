class Employee:
    # parameterized constructor
    def __init__(self, name, no) -> None:
        self.name = name  # instance variable
        self.no = no  # instance variable

    # instance method
    def display(self):
        print(self.name, self.no)


emp1 = Employee("John", 11)  # instance 1
emp2 = Employee("David", 12)  # instance 2

emp1.display()
emp2.display()
