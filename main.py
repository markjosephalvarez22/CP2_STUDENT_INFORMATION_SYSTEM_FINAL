from student_controller import StudentController


controller = StudentController()

while True:

    controller.view.display_menu()

    choice = input("Choice: ")

    if choice == "1":
        controller.add_student()

    elif choice == "2":
        controller.view_students()

    elif choice == "3":
        controller.search_student()

    elif choice == "4":
        controller.update_student()

    elif choice == "5":
        controller.delete_student()

    elif choice == "6":
        controller.count_students()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid input")
