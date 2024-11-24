class Employee:
    org_name = "Facebook"

    def __init__(self, name) -> None:
        self.name = name

    @staticmethod
    def details():
        print("This is an Employee class")


Employee.details()
