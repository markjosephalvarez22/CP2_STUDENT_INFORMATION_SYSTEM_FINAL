from student_model import StudentModel
from student_view import StudentView

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()
    def add_student(self):

        student = {
            "student_id": input("ID: "),
            "name": input("Name: "),
            "age": int(input("Age: ")),
            "course": input("Course: "),
            "year_level": input("Year Level: ")
        }

