# --------------------------------
# Python Input and Output
# --------------------------------

# What is Input?
# Input is the process of receiving data from the user during program execution.
# In Python, the built-in input() function is used to take input from the keyboard.
# By default, input() always returns the entered value as a string.

# Syntax
value = input("Enter a value: ")

# Example
name = input("Enter your name: ")
print(name)


# --------------------------------
# What is Output?
# --------------------------------

# Output is the process of displaying information to the user.
# In Python, the built-in print() function is used to display output
# on the console or terminal.

# Syntax
print(object)

# Example
print("Hello, Python!")


# --------------------------------
# Input Example
# --------------------------------

name = input("Enter your name: ")

print("Your name is:", name)


# Output
'''
Enter your name: Prasad
Your name is: Prasad
'''


# --------------------------------
# Numeric Input
# --------------------------------

# Since input() returns a string,
# convert it to int or float when needed.

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

print(age)
print(salary)


# --------------------------------
# Multiple Inputs
# --------------------------------

name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

print(name)
print(age)
print(city)


# --------------------------------
# Output Examples
# --------------------------------

name = "Prasad"
age = 22

print(name)
print(age)
print(name, age)


# --------------------------------
# f-string Output
# --------------------------------

name = "Prasad"
age = 22

print(f"My name is {name} and I am {age} years old.")


# --------------------------------
# print() Parameters
# --------------------------------

print("Python", "Java", "C++")
# Python Java C++

print("Python", "Java", sep="-")
# Python-Java

print("Hello", end=" ")
print("World")
# Hello World


# --------------------------------
# Type of input()
# --------------------------------

number = input("Enter a number: ")

print(number)
print(type(number))

# Output
'''
Enter a number: 100
100
<class 'str'>
'''


# --------------------------------
# Type Conversion
# --------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)