"""
Write a Program to perform to test and check the mathematical
functions such as :
a) Ceil()
b) Sqrt()
c) Pow()
d) Factorial()
"""
import math

def test_ceil(number):
    result = math.ceil(number)
    print(f"The ceiling value of {number} is {result}.")

def test_sqrt(number):
    result = math.sqrt(number)
    print(f"The square root of {number} is {result}.")

def test_pow(base, exponent):
    result = math.pow(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}.")

def test_factorial(number):
    result = math.factorial(number)
    print(f"The factorial of {number} is {result}.")

# Example usage
test_ceil(4.3)
test_sqrt(16)
test_pow(2, 3)
test_factorial(5)
