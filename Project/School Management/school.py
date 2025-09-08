class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # subject -> teacher
        self.classrooms = {}  # classname -> classroom

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        if classname in self.classrooms:
            self.classrooms[classname].add_student(student)
        else:
            raise ValueError(f"Classroom {classname} does not exist in {self.name}")

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return "A+"
        elif 70 <= marks < 80:
            return "A"
        elif 60 <= marks < 70:
            return "A-"
        elif 50 <= marks < 60:
            return "B"
        elif 40 <= marks < 50:
            return "C"
        elif 33 <= marks < 40:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00,
        }
        return grade_map.get(grade, 0.00)

    @staticmethod
    def value_to_grade(value):
        if value == 5.00:
            return "A+"
        elif 4.00 <= value < 5.00:
            return "A"
        elif 3.50 <= value < 4.00:
            return "A-"
        elif 3.00 <= value < 3.50:
            return "B"
        elif 2.00 <= value < 3.00:
            return "C"
        elif 1.00 <= value < 2.00:
            return "D"
        else:
            return "F"

    def evaluate_students(self):
        """
        Assign random marks and grades to all students in all classrooms.
        """
        for classname, classroom in self.classrooms.items():
            for student in classroom.students:
                for subject in classroom.subjects:
                    teacher = self.teachers.get(subject.name)
                    if teacher:
                        marks = teacher.evaluate_exam()
                        grade = School.calculate_grade(marks)
                        student.marks[subject.name] = marks
                        student.subject_grade[subject.name] = grade

    def __repr__(self):
        output = f"School: {self.name}, Address: {self.address}\n"
        output += "============================\n"

        # Show all classrooms
        for classname, classroom in self.classrooms.items():
            output += f"\n--- {classname.upper()} CLASSROOM STUDENTS ---\n"
            for student in classroom.students:
                output += f"Student: {student.name}\n"

        # Show all subjects
        for classname, classroom in self.classrooms.items():
            output += f"\n--- {classname.upper()} CLASSROOM SUBJECTS ---\n"
            for sub in classroom.subjects:
                output += f"{sub.name}\n"

        # Show results
        output += "\n--- STUDENTS RESULTS ---\n"
        for classname, classroom in self.classrooms.items():
            for student in classroom.students:
                output += f"\nResult for {student.name}:\n"
                for subject, marks in student.marks.items():
                    grade = student.subject_grade.get(subject, "N/A")
                    output += f"  {subject}: {marks} ({grade})\n"
                final_grade = student.calculate_final_grade()
                output += f"  Final Grade: {final_grade}\n"

        return output
