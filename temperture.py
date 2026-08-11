# Temperature Converter Class
class TemperatureConverter:

    # Convert Fahrenheit to Celsius
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        print("%.2f" % celsius)
        return celsius

    # Convert Celsius to Fahrenheit
    def celsius_to_fahrenheit(celsius):
        fahrenheit = celsius * 9 / 5 + 32
        print("%.2f" % fahrenheit)
        return fahrenheit

    # Validate user input
    def user_validation(user_input):
        # Get first character and rest of the characters
        first_char = user_input[0]
        rest_chars = user_input[1:]

        # Validation checks
        is_first_capital = first_char.isupper()

        # Check rest is a valid number (integer or float)
        try:
            float(rest_chars)
            is_rest_numeric = True
        except ValueError:
            is_rest_numeric = False

        # Final validation
        if is_first_capital and first_char in ['F', 'C'] and is_rest_numeric:
            if first_char == 'F':
                return TemperatureConverter.fahrenheit_to_celsius(float(rest_chars))
            elif first_char == 'C':
                return TemperatureConverter.celsius_to_fahrenheit(float(rest_chars))
        else:
            print("Invalid input: Please enter the temperature with the correct 'F' or 'C' prefix.")
            return False


# User Input
user_input = input("Enter Fahrenheit (e.g., F100) or Celsius (e.g., C0): ")

# Pass the user input to the validation function
uservalidation_result = TemperatureConverter.user_validation(user_input)
