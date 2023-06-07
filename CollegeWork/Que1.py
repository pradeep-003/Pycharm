"""
Write a Program to perform string manipulation operations using set
of pre-defined functions such as :
a) Find()
b) Upper()
c) Len()
d) Max() and Min()
e) Fetching a specific content from the String
"""


# String manipulation using predefined functions

def find_substring(string, substring):
    index = string.find(substring)
    if index != -1:
        print(f"The substring '{substring}' was found at "
              f"index {index} in the string.")
    else:
        print(f"The substring '{substring}' was not found "
              f"in the string.")


def convert_to_uppercase(string):
    return string.upper()


def get_string_length(string):
    return len(string)


def find_max_character(string):
    maxChar = max(string)
    return maxChar


def find_min_character(string):
    minChar = min(string)
    return minChar


def fetch_specific_content(string, start_index, end_index):
    content = string[start_index:end_index]
    return content


# Example usage
input_string = "Hello, World!"

# Find a substring
find_substring(input_string, "World")

# Convert to uppercase
uppercase_string = convert_to_uppercase(input_string)
print("Uppercase:", uppercase_string)

# Calculate string length
length = get_string_length(input_string)
print("Length:", length)

# Find the maximum and minimum characters
max_char = find_max_character(input_string)
min_char = find_min_character(input_string)
print("Maximum character:", max_char)
print("Minimum character:", min_char)

# Fetch specific content
content = fetch_specific_content(input_string, 7, 12)
print("Content:", content)
