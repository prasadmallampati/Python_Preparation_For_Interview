# --------------------------------
# Python Type Conversion
# --------------------------------

'''
What is Type Conversion?

Type conversion is the process of converting one data type into another
data type.

Python provides built-in functions to convert values from one type to
another.

Example:
int → float
float → int
str → int
int → str

There are two types of type conversion:

1. Implicit Type Conversion
2. Explicit Type Conversion
'''

# --------------------------------
# 1. Implicit Type Conversion
# --------------------------------

'''
Python automatically converts one data type into another
without programmer intervention.

Usually, Python converts a smaller data type into a larger
compatible data type to avoid data loss.
'''

# Example

a = 10          # int
b = 2.5         # float

result = a + b

print(result)
print(type(result))

# Output
# 12.5
# <class 'float'>


# --------------------------------
# More Examples
# --------------------------------

print(10 + 5.5)         # 15.5
print(type(10 + 5.5))   # float

print(True + 5)         # 6
print(type(True + 5))   # int


# --------------------------------
# 2. Explicit Type Conversion
# --------------------------------

'''
Explicit type conversion is performed manually by the programmer
using Python's built-in conversion functions.
'''

# --------------------------------
# Built-in Type Conversion Functions
# --------------------------------

'''
int()
float()
str()
bool()
complex()
list()
tuple()
set()
dict()
bytes()
bytearray()
frozenset()
'''

# --------------------------------
# int()
# --------------------------------

num = 10.99

print(int(num))

# Output
# 10


# String to int

num = "100"

print(int(num))

# Output
# 100


# --------------------------------
# float()
# --------------------------------

num = 25

print(float(num))

# Output
# 25.0


text = "45.67"

print(float(text))

# Output
# 45.67


# --------------------------------
# str()
# --------------------------------

num = 100

print(str(num))
print(type(str(num)))

# Output
# "100"


# --------------------------------
# bool()
# --------------------------------

print(bool(1))          # True
print(bool(0))          # False

print(bool(""))         # False
print(bool("Python"))   # True

print(bool([]))         # False
print(bool([1]))        # True

print(bool(None))       # False


# --------------------------------
# complex()
# --------------------------------

print(complex(10))

# Output
# (10+0j)

print(complex(10, 5))

# Output
# (10+5j)


# --------------------------------
# list()
# --------------------------------

text = "Python"

print(list(text))

# Output
# ['P', 'y', 't', 'h', 'o', 'n']


# --------------------------------
# tuple()
# --------------------------------

numbers = [1, 2, 3]

print(tuple(numbers))

# Output
# (1, 2, 3)


# --------------------------------
# set()
# --------------------------------

numbers = [1, 2, 2, 3, 4]

print(set(numbers))

# Output
# {1, 2, 3, 4}


# --------------------------------
# dict()
# --------------------------------

data = [
    ("name", "Prasad"),
    ("age", 22)
]

print(dict(data))

# Output
# {'name': 'Prasad', 'age': 22}


# --------------------------------
# bytes()
# --------------------------------

print(bytes([65, 66, 67]))

# Output
# b'ABC'


# --------------------------------
# bytearray()
# --------------------------------

print(bytearray([65, 66, 67]))

# Output
# bytearray(b'ABC')


# --------------------------------
# frozenset()
# --------------------------------

numbers = [1, 2, 2, 3]

print(frozenset(numbers))

# Output
# frozenset({1, 2, 3})


# --------------------------------
# Valid Type Conversions
# --------------------------------

'''
int      -> float ✔
int      -> bool ✔
int      -> str ✔
int      -> complex ✔

float    -> int ✔
float    -> bool ✔
float    -> str ✔
float    -> complex ✔

bool     -> int ✔
bool     -> float ✔
bool     -> str ✔
bool     -> complex ✔

str      -> int ✔ (only numeric strings)
str      -> float ✔ (only numeric strings)
str      -> bool ✔
str      -> complex ✔ (only valid numeric strings)
str      -> list ✔
str      -> tuple ✔
str      -> set ✔

list     -> tuple ✔
list     -> set ✔
list     -> frozenset ✔

tuple    -> list ✔
tuple    -> set ✔
tuple    -> frozenset ✔

set      -> list ✔
set      -> tuple ✔
set      -> frozenset ✔
'''

# --------------------------------
# Invalid Type Conversions
# --------------------------------

'''
int(complex)        ❌ TypeError
float(complex)      ❌ TypeError

int("Python")       ❌ ValueError
float("Hello")      ❌ ValueError

dict([1,2,3])       ❌ TypeError

int(None)           ❌ TypeError
float(None)         ❌ TypeError
complex(None)       ❌ TypeError
'''

# --------------------------------
# Common Interview Questions
# --------------------------------

'''
Q1. Does input() return int?
Answer:
No. input() always returns a string.

--------------------------------

Q2. What is implicit type conversion?
Answer:
Python automatically converts compatible data types.

--------------------------------

Q3. What is explicit type conversion?
Answer:
The programmer manually converts one data type into another
using built-in conversion functions.

--------------------------------

Q4. Difference between implicit and explicit conversion?

Implicit:
Automatic conversion by Python.

Explicit:
Manual conversion using int(), float(), str(), etc.

--------------------------------

Q5. Can int() convert float?

Yes.

Example:
int(10.99)

Output:
10

--------------------------------

Q6. Can int() convert "Python"?

No.

Raises ValueError.

--------------------------------

Q7. Which conversion functions are used most in Python?

int()
float()
str()
bool()
list()
tuple()
set()
dict()
complex()
'''

# --------------------------------
# Summary
# --------------------------------

'''
✔ Type conversion converts one data type into another.

✔ Two types:
   - Implicit Conversion
   - Explicit Conversion

✔ Most commonly used conversion functions:
   int()
   float()
   str()
   bool()
   complex()
   list()
   tuple()
   set()
   dict()

✔ input() always returns a string.

✔ Some conversions are valid, while others raise
   TypeError or ValueError.
'''