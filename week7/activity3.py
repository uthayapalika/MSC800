class Employee:
    """Base class representing a regular employee."""
    
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_details(self):
        print("Employee Details:")
        print(f"  Name    : {self.name}")
        print(f"  Emp ID  : {self.emp_id}")


class Manager(Employee):
    """Derived class representing a manager, which is also an employee."""
    
    def __init__(self, name, emp_id, department):
        # Call the parent class constructor to initialize name and emp_id
        super().__init__(name, emp_id)
        self.department = department
    
    def display_details(self):
        print("Manager Details:")
        print(f"  Name       : {self.name}")
        print(f"  Emp ID     : {self.emp_id}")
        print(f"  Department : {self.department}")


# Create a Manager object and display all details
manager = Manager("Alice Johnson", "M1024", "Human Resources")
manager.display_details()