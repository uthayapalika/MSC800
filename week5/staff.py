from person import Person

class Staff(Person):
    def __init__(self, name, staff_id, tax_num, rate_of_pay, publications):
        super().__init__(name)
        self.staff_id = staff_id
        self.tax_num = tax_num
        self.rate_of_pay = rate_of_pay
        self.publications = publications

    def calculate_salary(self):
        number_of_hours = 4
        salary = self.rate_of_pay * number_of_hours
        return salary

staff = Staff("John", "S001", "TX123", 10, 5)

salary = staff.calculate_salary()

print("Staff Name:", staff.name)
print("Staff ID:", staff.staff_id)
print("Salary:", salary)
