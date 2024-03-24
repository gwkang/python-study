# format string with interpolation
# It's the best way to format strings in Python 3.6 and above

name = "Alice"
age = 30

# name in the second place is converted to repr string.
print(f"Hello, {name}. You are {age} years old. repr: {name!r}")
# Output: Hello, Alice. You are 30 years old. repr: 'Alice'

places = 2
number = 1.23456
print(f"Number: {number:.{places}f}")

