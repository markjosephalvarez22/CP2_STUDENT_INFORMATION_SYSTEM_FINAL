from student_model import StudentModel
from student_view import StudentView

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()
