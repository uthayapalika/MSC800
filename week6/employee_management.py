def check_login(func):

    def wrapper(employee, *args, **kwargs):

        if employee.logged_in:
            return func(employee, *args, **kwargs)

        print("Access denied!")
        print(f"{employee.name} is not logged in.")

    return wrapper


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"{self.name} logged in.")

    def logout(self):
        self.logged_in = False
        print(f"{self.name} logged out.")

    @check_login
    def view_salary(self):
        print(f"{self.name}'s salary is ${self.salary}")


# Two employees
employee1 = Employee("John", 60000)
employee2 = Employee("Sarah", 70000)


# John tries before login
print("\n--- John tries to view salary ---")
employee1.view_salary()


# John logs in
print("\n--- John logs in ---")
employee1.login()


# John tries again
print("\n--- John tries again ---")
employee1.view_salary()


# John logs out
print("\n--- John logs out ---")
employee1.logout()


# John tries again
print("\n--- John tries after logout ---")
employee1.view_salary()