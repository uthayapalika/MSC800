class University:
    def __init__(self, name="Generic University"):
        self.name = name

    def start(self):
        print(f"{self.name} is starting")

    def __repr__(self):
        return f"University(name={self.name!r})"


class Department:
    def __init__(self, university: University):
        self.university = university

    def show_department(self, name):
        self.university.start()
        print(f"{name} Department is starting")


# Usage
uni = University("University of Auckland")
dept = Department(uni)

dept.show_department("Computer Science")
print(dept.university)   