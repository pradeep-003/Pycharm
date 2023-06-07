"""
Write a Program that receive input from the user to calculate the Area
of Square
"""

def calculate_square_area(side_length):
    area = side_length ** 2
    return area

# Input from the user
side_length = float(input("Enter the side length of the square: "))

# Calculate the area of the square
area = calculate_square_area(side_length)

# Output the result
print(f"The area of the square with side length {side_length} is {area}.")
