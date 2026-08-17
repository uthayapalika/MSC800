try:
    from .database import create_table
    from .student_managent import add_student, delete_student, search_student, view_students
    from .course_management import add_course, delete_course, search_course, view_courses
    from .lecture_managemt import add_lecture, delete_lecture, search_lecture, view_lectures
except ImportError:
    from database import create_table
    from student_managent import add_student, delete_student, search_student, view_students
    from course_management import add_course, delete_course, search_course, view_courses
    from lecture_managemt import add_lecture, delete_lecture, search_lecture, view_lectures

def menu():
    print("\n==== Student Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Delete Student by ID")
    print("5. Add Lecture")
    print("6. View All Lectures")
    print("7. Search Lecture by Name")
    print("8. Delete Lecture by ID")
    print("9. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_student(name, email)
        elif choice == '2':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '3':
            name = input("Enter name to search: ")
            students = search_student(name)
            for student in students:
                print(student)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            name = input("Enter lecture name: ")
            credits = int(input("Enter credits: "))
            add_lecture(name, credits)
        elif choice == '6':
            lectures = view_lectures()
            for lecture in lectures:
                print(lecture)
        elif choice == '7':
            name = input("Enter lecture name to search: ")
            lectures = search_lecture(name)
            for lecture in lectures:
                print(lecture)
        elif choice == '8':
            lecture_id = int(input("Enter lecture ID to delete: "))
            delete_lecture(lecture_id)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
