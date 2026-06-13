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

        self.model.add_student(student)
        self.view.display_message("Student added!")

    def view_students(self):

        students = self.model.get_all_students()
        self.view.display_students(students)

    def search_student(self):

        sid = input("ID: ")
        result = self.model.search_student(sid)

        print(result if result else "Not found")

    def update_student(self):

        sid = input("ID: ")

        student = self.model.search_student(sid)

        if not student:
            print("Not found")
            return

        self.model.update_student(
            sid,
            input("New Name: "),
            int(input("New Age: ")),
            input("New Course: "),
            input("New Year Level: ")
        )

        print("Updated!")

    def delete_student(self):

        sid = input("ID: ")

        self.model.delete_student(sid)

        print("Deleted!")

    def count_students(self):
        total = self.model.count_students()
        print("Total:", total)
