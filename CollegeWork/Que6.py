"""
Write a Program that receive input from the user to calculate the Area
of Rectangle
"""
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = calculate_rectangle_area(length, width)

# Output the result
print(f"The area of the rectangle with length {length} and width {width} is {area}.")
