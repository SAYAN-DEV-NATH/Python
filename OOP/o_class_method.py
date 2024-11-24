class Employee:
    org_name = "Google"

    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def info(cls):
        return cls.org_name


print(Employee.info())
