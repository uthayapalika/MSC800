class Bmi:
    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

bmi_calculator = Bmi()   

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = bmi_calculator.calculate_bmi(weight, height)
print("The calculated BMI is:", bmi)