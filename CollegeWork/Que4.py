"""
Write a Program that receive input from the user to calculate the Area
of Triangle
"""
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Input from the user
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = calculate_triangle_area(base, height)

# Output the result
print(f"The area of the triangle with base {base} and height {height} is {area}.")
