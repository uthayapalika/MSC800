class Student:
    def getdetails(self, fullname, age, address, studentId):
        self.name = fullname
        self.age = age
        self.address = address
        self.studentId = studentId


  

# Initialize an empty list
students_details = []

# get user input frome students
for i in range(70):
    print(f"\nEnter details for student {i+1}:")
    name = input("Full Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    studentId = input("Student ID: ")

    # Create a new Student object and get details
    student = Student()
    student.getdetails(name, age, address, studentId)
    students_details.append(student)
    print(f"Student {i+1} details added successfully.")