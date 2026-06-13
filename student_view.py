class StudentView:

    @staticmethod
    def display_menu():

        print("\n==============================")
        print(" STUDENT INFORMATION SYSTEM")
        print("==============================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Count Students")
        print("7. Exit")

    @staticmethod
    def display_students(students):

        if not students:
            print("No students found.")
            return

        for s in students:
            print(s)
