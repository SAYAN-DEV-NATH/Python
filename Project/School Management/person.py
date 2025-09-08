from school import School
import random


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass

    def evaluate_exam(self):
        return random.randint(50, 100)


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
        self.__id = None

    def calculate_final_grade(self):
        if not self.subject_grade:
            self.grade = None
            return None

        total = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            total += point

        gpa = total / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)
        return self.grade

    @property
    def id(self):
        return self.__id

    def id(self, value):
        self.__id = value
