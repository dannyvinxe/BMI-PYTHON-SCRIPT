def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) given weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi


def interpret_bmi(bmi, age, gender):
    """
    Interpret BMI value and provide corresponding category based on age and gender.
    """
    if gender == "male":
        if age < 18:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 25:
                return "Normal weight"
            elif 25 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
        else:
            if bmi < 20:
                return "Underweight"
            elif 20 <= bmi < 25:
                return "Normal weight"
            elif 25 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
    elif gender == "female":
        if age < 18:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 24:
                return "Normal weight"
            elif 24 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
        else:
            if bmi < 19:
                return "Underweight"
            elif 19 <= bmi < 24:
                return "Normal weight"
            elif 24 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
    else:
        return "Invalid gender input"


def main():
    # Get user input for weight in pounds
    weight_lbs = float(input("Enter your weight in pounds: "))

    # Get user input for height in feet and inches
    height_ft = int(input("Enter your height in feet: "))
    height_in = int(input("Enter your height in inches: "))

    # Get user input for age and gender
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()

    # Convert weight to kilograms and height to meters
    weight_kg = weight_lbs * 0.453592
    height_m = (height_ft * 12 + height_in) * 0.0254

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # Interpret BMI and display category
    bmi_category = interpret_bmi(bmi, age, gender)
    print("Your BMI is: {:.2f}".format(bmi))
    print("BMI Category: {}".format(bmi_category))


if __name__ == "__main__":
    main()
