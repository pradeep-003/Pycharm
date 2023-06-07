""" Write a Program to check if the input string is Palindrome or not
"""

def is_palindrome(string):
    reversed_string = string[::-1]
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False

# Input from the user
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
