# ===============================
# Variables in Python
# ===============================

# What is a variable?
# A variable is a name (identifier) that refers to a value (object) in memory.
# It is used to store data so it can be accessed and modified later.

# Examples
name = "Prasad"
age = 22
salary = 50000.50

print(name)
print(age)
print(salary)


# ===============================
# Rules for Naming Variables
# ===============================

# 1. A variable name must start with a letter (A-Z or a-z) or an underscore (_).

name = "Prasad"
_name = "Python"

# 2. A variable name cannot start with a number.

# Invalid
# 1name = "Mallampati"

# Valid
name1 = "Mallampati"

# 3. A variable name can contain:
#    - Letters (A-Z, a-z)
#    - Numbers (0-9)
#    - Underscore (_)

student_name = "Prasad"
roll_no = 101
user1 = "Admin"

# 4. Special characters are not allowed.

# Invalid
# user-name = "Python"
# user@name = "Python"
# user$name = "Python"

# 5. Variable names are case-sensitive.

name = "Prasad"
Name = "Mallampati"

print(name)   # Prasad
print(Name)   # Mallampati

# 'name' and 'Name' are different variables.

# 6. Python keywords cannot be used as variable names.

# Invalid
# if = 10
# class = "Python"
# for = 5

# 7. Variable names should be meaningful.

student_name = "Prasad"   # Good
total_marks = 95          # Good

x = "Prasad"              # Allowed, but not descriptive