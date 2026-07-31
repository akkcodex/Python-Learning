# ============================================
# COMMON SYMBOLS USED IN PYTHON VARIABLES
# ============================================

# ""  Double Quotes
# Used to create a string.
name = "John"

# ''  Single Quotes
# Also used to create a string.
city = 'New York'

# =  Assignment Operator
# Used to assign a value to a variable.
age = 31

# () Parentheses
# Used with functions and expressions.
print(name)

# , Comma
# Used to separate values.
x, y, z = 10, 20, 30

# . Dot Operator
# Used to access methods and attributes.
name.upper()

# # Hash
# Used to write single-line comments.
# This is a comment

# ''' ''' or """ """
# Used for multi-line comments or docstrings.

"""
This is a
multi-line string.
"""

# _ Underscore
# Used in variable names.
student_name = "Jack"



# ============================================
# VARIABLES IN PYTHON
# ============================================

# What is a Variable?
# A variable is a name used to store data in memory.
# Or a variable are containers for storing data values.
# The value of a variable can be changed during program execution.

# Example:
x = 31
y = "Rocky"
print(x)
print(y)

# Python automatically detects the data type of a variable. You do not need to mention it.
# A variable can also change its data type at any time.

# Example:
x = 20        # x is a type int
y = "Adam"    # x is now of type str



# ============================================
# TYPE CASTING IN PYTHON
# ============================================

# Type casting is the process of converting one data type into another data type.
# If you want to specify the data type of varaibles, this can be done with casting.

# Example:
x = str(10)     # x will be '10'
y = int(10)     # y will be 10
z = float(10)       # z will be 10.0



# ============================================
# GET THE TYPE OF A VARIABLE
# ============================================

# type() tells you what type of data a variable contains.

# Example:
x = 41
y = "Martin"
print(type(x))
print(type(y))



# ============================================
# SINGLE AND DOUBLE QUOTES IN PYTHON
# ============================================

# Single quotes (' ') and double quotes (" ") are used to create strings in Python.
# Both work the same way. You can use either one based on your needs.

# Example:
x = 'Henry'
# will be same as
x = "Henry"



# ============================================
# CASE SENSITIVE IN PYTHON
# ============================================

# Python is a case-sensitive language. It treats uppercase and lowercase letters as different.

# Example_1:
# name ≠ Name
# age ≠ Age
# python ≠ Python
# true ≠ True (True is a valid Boolean value, true is not)

# Example_2:

a = 25
A = "Victor"
# A will not overwrite a