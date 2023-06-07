# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicate OK
#   Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicate OK. FASTER

"""  @List  """

fruits = ["apple", "orange", "banana", "coconut"]
"""
# print(fruits)
print(fruits[0:2])
print(fruits[:2])
print(fruits[1:2])
print(fruits[::2])
print(fruits[::3])
print(fruits[::-1])
print(fruits[::-2])
"""

"""
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
"""

# print(dir(fruits))
# help(fruits)
# print(len(fruits))
# print("apple" in fruits)
# print("pineapple" in fruits)

"""
for fruit in fruits:
    print(fruit)
"""

"""
fruits[2] = "pineapple"
for fruit in fruits:
    print(fruit)
"""

# fruits.append("pineapple")
# fruits.remove("orange")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.index("pineapple")) # 'pineapple' is not in list

# print(fruits.count("banana"))
# print(fruits)

"""  @Set  """

fruits = {"apple", "orange", "banana", "coconut", "apple"}