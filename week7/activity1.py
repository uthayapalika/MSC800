class Person:
    def show_person(self):
        print("This is a person")

class Student(Person):
    def study(self):
        print("Student is studying")

class Employee:
    def work(self):
        print("Employee is working")

class Teacher(Person, Employee):
    def teach(self):
        print("Teacher is teaching")

class UndergraduateStudent(Student):
    def attend_class(self):
        print("Undergraduate student is attending class")

class PostgraduateStudent(Student):
    def conduct_research(self):
        print("Postgraduate student is conducting research")

# Undergraduate student
student1 = UndergraduateStudent()

student1.show_person()
student1.study()
student1.attend_class()

# Postgraduate student
student2 = PostgraduateStudent()
student2.show_person()
student2.study()
student2.conduct_research()

# Teacher
teacher = Teacher()
teacher.show_person()
teacher.work()
teacher.teach()