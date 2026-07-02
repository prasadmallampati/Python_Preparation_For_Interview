# --------------------------------
# Python Data Types
# --------------------------------

# Python is a dynamically typed language.
# We do not need to explicitly declare the data type of a variable.
# Python automatically determines the data type based on the assigned value.

# What is a Data Type?
# A data type specifies the kind of value stored in a variable.
# It also determines what operations can be performed on that value.

# Example

age = 22          # int
price = 99.99     # float
name = "Prasad"   # str

print(type(age))
print(type(price))
print(type(name))


# --------------------------------
# Common Built-in Data Types
# --------------------------------

'''
1. int
   - Stores whole numbers (positive, negative, or zero).
   - Examples: age, marks, quantity.

Example:
age = 22
marks = 95

-----------------------------------

2. float
   - Stores decimal (floating-point) numbers.
   - Examples: price, salary, pi.

Example:
price = 199.99
pi = 3.14159

-----------------------------------

3. bool
   - Represents logical values.
   - Only two values: True and False.
   - Commonly used in conditions, authentication,
     validation, and flags.

Example:
is_logged_in = True
is_admin = False

-----------------------------------

4. NoneType
   - Represents the absence of a value.
   - The value is written as None.

Example:
data = None

-----------------------------------

5. complex
   - Stores complex numbers.
   - Consists of a real part and an imaginary part.

Example:
number = 2 + 3j

-----------------------------------

6. str
   - Stores text (Unicode characters).
   - Can contain letters, numbers, symbols, and spaces.

Examples:
name = "Prasad"
url = "https://python.org"
message = "Hello World"

'''


# --------------------------------
# Python Data Types - Examples
# --------------------------------

# 1. int (Integer)
# Stores whole numbers.

age = 22
marks = 95
temperature = -10

print(age)
print(type(age))


# --------------------------------

# 2. float
# Stores decimal numbers.

price = 199.99
pi = 3.14159
height = 5.8

print(price)
print(type(price))


# --------------------------------

# 3. bool (Boolean)
# Stores only True or False.

is_logged_in = True
is_admin = False

print(is_logged_in)
print(type(is_logged_in))


# --------------------------------

# 4. NoneType
# Represents no value or absence of a value.

data = None

print(data)
print(type(data))


# --------------------------------

# 5. complex
# Stores complex numbers (real + imaginary).

number = 2 + 3j

print(number)
print(type(number))


# --------------------------------

# 6. str (String)
# Stores text.

name = "Prasad"
city = "Hyderabad"
website = "https://python.org"

print(name)
print(type(name))


# --------------------------------

# 7. list
# Ordered, mutable collection.

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(type(fruits))


# --------------------------------

# 8. tuple
# Ordered, immutable collection.

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))


# --------------------------------

# 9. set
# Unordered collection of unique values.

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# --------------------------------

# 10. dict (Dictionary)
# Stores data in key-value pairs.

student = {
    "name": "Prasad",
    "age": 22,
    "course": "Python"
}

print(student)
print(type(student))


# --------------------------------

# 11. range
# Represents a sequence of numbers.

numbers = range(1, 6)

print(list(numbers))
print(type(numbers))


# --------------------------------

# 12. bytes
# Immutable binary data.

binary_data = b"Hello"

print(binary_data)
print(type(binary_data))


# --------------------------------

# 13. bytearray
# Mutable binary data.

data = bytearray([65, 66, 67])

print(data)
print(type(data))


# --------------------------------

# 14. memoryview
# Provides a memory-efficient view of binary data.

data = memoryview(bytes(5))

print(data)
print(type(data))

# -----------------------------------
# Type conversion possibility summary
# ------------------------------------

'''
| From ↓ / To → | int() | float()    | bool()  | complex()   | str()  | None   |
| ------------- | :---: | :-----:    | :----:  | :-------:   | :---:  | :--:   |
| **int**       |   ✅   |    ✅    |    ✅   |     ✅     |   ✅   |   ❌  |
| **float**     |   ✅   |    ✅    |    ✅   |     ✅     |   ✅   |   ❌  |
| **bool**      |   ✅   |    ✅    |    ✅   |     ✅     |   ✅   |   ❌  |
| **complex**   |   ❌   |    ❌    |    ✅   |     ✅     |   ✅   |   ❌  |
| **str**       |   ⚠️   |    ⚠️    |    ✅   |     ⚠️     |   ✅   |   ❌  |
| **None**      |   ❌   |    ❌    |    ✅   |     ❌     |   ✅   |  N/A   |

'''
