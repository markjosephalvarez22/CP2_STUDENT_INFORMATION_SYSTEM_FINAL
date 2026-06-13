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
            print("\nNo students found.")
            return

        print("\nID | NAME | AGE | COURSE | YEAR")
        print("-" * 40)

        for s in students:
            print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]}")

    @staticmethod
    def display_message(msg):
        print("\n" + msg)
