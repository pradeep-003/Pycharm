"""
name = input("Enter your name: ")
age = float(input("Enter your age: "))
age = age + 1
print(f"Hello {name}")
print(f"You are {age} years old")
"""

"""
adjective1 = input("Enter an adjective: ")
noun = input(" Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")
"""

# Calculate volume
"""
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
height = float(input("Enter the height of rectangle: "))

volume = length * width * height
print(f"The volume is: {volume}cm^3")
"""

# Shopping cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"you have bought {quantity} x {item}/s")
print(f"Your total is : ${round(total, 2)}")
