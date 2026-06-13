from student_controller import StudentController


controller = StudentController()

while True:

    controller.view.display_menu()

    choice = input("Choice: ")
