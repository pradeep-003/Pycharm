# python Calc
"""
operator = input("Enter the operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == '+':
    result = num1 + num2
    print(round(result, 3))
elif operator == '-':
    result = num1 - num2
    print(round(result, 3))
elif operator == '*':
    result = num1 * num2
    print(round(result, 3))
elif operator == '/':
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
"""

# python weight converter

"""
weight = float(input("Enter your weight: "))
unit = input("Kilogram or pound? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 3)}{unit}")
elif unit == 'L':
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 3)}{unit}")
else:
    print(f"{unit} was not valid unit")
"""

# python temperature converter

unit = input("Is this temperature in celsius or fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp)/5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in celsius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")
    

