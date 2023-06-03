# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")
# result = len(name)
# result = name.find("o")
# result = name.rfind("o")
# print(result)
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", "")
# print(result)

# print(help(str))

"""
Exercise - 1
       * Valid username input exercise
              1. username is no mare than 12 character
              2. username must not contain spaces
              3. username must not contain digits
"""

username = input("Enter your name: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.find(" ") != -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("username can't contain digits")
else:
    print(f"Welcome {username}!!")
