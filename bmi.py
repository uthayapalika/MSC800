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

    # Call the function
bmi = calculate_bmi()

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You have a normal weight.")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

print("The calculated BMI is:", bmi)