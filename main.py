class BMIcalculator:
  def getdata(this):
    """
    Get weight in kgs and height in cms.
    Height is entered in cetimetres and stored in metres
    """

    this.w = float(input("Please enter your weight in kilograms:"))
    this.h = float(input("Please enter your height in centimetres:"))/100

  def calculate(this):
    """
    Calculate and return bmi
    """

    return round(this.w/(this.h*this.h),2)


def main():
  print("\n","="*42,"\n")
  print("Hello, let's calculate your BMI.");
  
  calc = BMIcalculator()
  print()
  calc.getdata()
  bmi=calc.calculate()
  print(f"Your BMI is {bmi}")
  print("\n","="*42,"\n")

if __name__ == "__main__":
    main()