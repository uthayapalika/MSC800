class Bmi:
    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

bmi_calculator = Bmi()   

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = bmi_calculator.calculate_bmi(weight, height)
#print("The calculated BMI is:", bmi)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")