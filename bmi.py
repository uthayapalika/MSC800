# Validate user input
def getvalid_number(n):
    while True:
        try:
            return float(input(n))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# User input BMI
def calculate_bmi():
    w = getvalid_number("Enter weight in kg: ")
    h = getvalid_number("Enter height in meters: ")
    calculated_bmi = w / (h ** 2)
    return calculated_bmi

print("The calculated BMI is:", calculate_bmi())