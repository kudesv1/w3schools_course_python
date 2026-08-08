age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."

# --- 1. Case Modifications ---

# lower() converts all characters in the string to lowercase
text_lower = "PyThOn".lower()  # Result: 'python'

# upper() converts all characters in the string to uppercase
text_upper = "python".upper()  # Result: 'PYTHON'

# capitalize() capitalizes only the first character of the string
text_cap = "hello world".capitalize()  # Result: 'Hello world'

# title() capitalizes the first character of every word
text_title = "hello world".title()  # Result: 'Hello World'


# --- 2. String Trimming and Cleaning ---

# strip() removes leading and trailing whitespace (or specified characters)
text_strip = "  hello  ".strip()  # Result: 'hello'

# rstrip() removes whitespace (or specified characters) from the right side only
# (lstrip() performs the same operation on the left side)
text_rstrip = "  hello  ".rstrip()  # Result: '  hello'


# --- 3. Searching and Replacing ---

# replace(old, new) replaces all occurrences of a substring with a new substring
text_replace = "banana".replace("a", "o")  # Result: 'bonono'

# find(sub) returns the index of the first occurrence of a substring (-1 if not found)
text_find = "python".find("th")  # Result: 2

# startswith(prefix) checks if the string starts with the specified prefix
is_cat = "cat.jpg".startswith("cat")  # Result: True

# endswith(suffix) checks if the string ends with the specified suffix
is_jpg = "cat.jpg".endswith(".jpg")  # Result: True


# --- 4. Splitting and Joining ---

# split(separator) breaks a string into a list based on a delimiter (defaults to whitespace)
fruits_list = "apple,banana,orange".split(",")  # Result: ['apple', 'banana', 'orange']

# join(iterable) joins elements of an iterable into a single string using a delimiter
date_str = "-".join(["2026", "08", "07"])  # Result: '2026-08-07'


# --- 5. Content Validation Checks (Return True/False) ---

# isdigit() returns True if all characters in the string are digits
check_digits = "12345".isdigit()  # Result: True

# isalpha() returns True if all characters in the string are alphabetic letters
check_alpha = "Hello".isalpha()  # Result: True

# isalnum() returns True if all characters are alphanumeric (letters or numbers)
check_alnum = "Python3".isalnum()  # Result: True

# isspace() returns True if the string contains only whitespace characters (\n, \t, spaces)
check_space = "   \n".isspace()  # Result: True

txt = "Hello, World!"
print(txt[2:5])
print(txt.upper())
name = "Python"
print(f"I love {name}")