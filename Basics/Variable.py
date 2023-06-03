# variable = a reusable container for storing a value
#            a variable behaves as if it were the value it contains

age = 21

print("You are " + str(age) + " years old")
print("You are", age, "Years old")
print(f"You are {age} years old")

# INTEGER

age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# FLOAT

gpa = 8.3
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"you ran {distance}Km")
print(f"The price of book is {price}$")

# STRING

name = "Bro"
food = "pizza"
email = "Bro123@gmail.com"

print(f"Your name is {name}")
print(f"you like {food}")
print(f"Your emailId is: {email}")

# BOOLEAN

online = False
for_sale = True
running = True

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running?: {running}")

if running:
    print("The game is running")
else:
    print("The game is over")

# Tips & Tricks

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)
