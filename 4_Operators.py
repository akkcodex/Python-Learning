# ============================================
# OPERATORS IN PYTHON
# ============================================

# What is an Operator?

# An operator is a symbol or keyword used to perform
# an operation on values or variables.

# Example:

from sre_constants import IN


a = 10
b = 5

print(a + b)

# Python divides the operators in the following groups:

# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators



# ============================================
# ARITHMETIC OPERATORS
# ============================================

# Arithmetic operators are used with numeric values to perform common mathematical operations:

a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation
print(a // b)   # Floor Division


# DIVISON IN PYTHON:
# In Python, the division operator (/) always returns a float value, even if the result is a whole number.

x = 15
y = 4
print(x / y)  # Output: 3.75

# The floor division operator (//) returns the largest integer less than or equal to the result of the division.

print(x // y) # Output: 3
    


# ============================================
# ASSIGNMENT OPERATORS
# ============================================

# Assignment operators are used to assign values to variables:

# =	    Assignment        x = 5       # x = 5
# +=	Addition          x += 5      # x = x + 5     add and assign
# -=	Subtraction       x -= 5      # x = x - 5     subtract and assign
# *=	Multiplication    x *= 5      # x = x * 5     multiply and assign
# /=	Division          x /= 5      # x = x / 5     divide and assign
# %=	Modulus           x %= 5      # x = x % 5     modulus and assign
# **=	Exponentiation    x **= 5     # x = x ** 5    exponentiation and assign
# //=	Floor Division    x //= 5     # x = x // 5    floor division and assign



# ============================================
# COMPARISON OPERATORS
# ============================================

# Comparison operators are used to compare two values:

a = 10
b = 5

print(a == b)    # False        == Equlas to
print(a != b)    # True         != Not equals to
print(a > b)     # True         > Greater than
print(a < b)     # False        < Less than
print(a >= b)    # True         >= Gretaer than or equal to
print(a <= b)    # False        <= Less than or equal to


# Chaining comparison operators
# Python allows you to chain comparison operators

x = 5
print(1 < x < 10)
print(1 < x and x < 10)



# ============================================
# LOGICAL OPERATORS
# ============================================


# Logical operators are used to combine multiple
# conditions and return True or False.

# Python has three logical operators:
# A) and
# B) or
# C) not

# ============================================
# A. AND OPERATOR
# ============================================
# 'and' returns True only when both conditions are True.

age = 25

print(age > 18 and age < 30)

# age > 18  -> True
# age < 30  -> True
# True and True -> True


# If any one condition is False, the result is False.

print(age > 18 and age > 30)

# age > 18  -> True
# age > 30  -> False
# True and False -> False

# ============================================
# B. OR OPERATOR
# ============================================
# 'or' returns True when at least one condition is True.

age = 25

print(age < 18 or age > 20)

# age < 18  -> False
# age > 20  -> True
# False or True -> True


# If both conditions are False, the result is False.

print(age < 18 or age > 30)

# False or False -> False

# ============================================
# C. NOT OPERATOR
# ============================================
# 'not' reverses the result.
# True becomes False.
# False becomes True.

age = 25

print(not(age > 18))

# age > 18 -> True
# not True -> False


print(not(age < 18))

# age < 18 -> False
# not False -> True

# ============================================
# SUMMARY
# ============================================

# and -> True when both conditions are True.
# or  -> True when at least one condition is True.
# not -> Reverses the result.



# ============================================
# IDENTITY OPERATORS
# ============================================

# Identity operators are used to check whether
# two variables refer to the same object or not.

# Python has two identity operators:
# A) is
# B) is not

# ============================================
# A. IS OPERATOR
# ============================================
# 'is' returns True when two variables refer
# to the same object.

a = [1, 2, 3]
b = a

print(a is b)

# a and b refer to the same object.
# Output:
# True

# ============================================
# B. IS NOT OPERATOR
# ============================================
# 'is not' returns True when two variables
# do not refer to the same object.

a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)

# a and b have the same values,
# but they are different objects.
# Output:
# True

# ============================================
# IS vs ==
# ============================================

# '==' checks whether two values are equal.
# 'is' checks whether two variables refer
# to the same object.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True
print(a is b)   # False


# ============================================
# SUMMARY
# ============================================

# is      -> Checks if two variables are the same object.
# is not  -> Checks if two variables are different objects.
# ==      -> Checks if two values are equal.



# ============================================
# MEMBERSHIP OPERATORS
# ============================================

# Membership operators are used to check whether
# a value exists in a sequence or collection.

# Python has two membership operators:
# A) in
# B) not in

# ============================================
# A. IN OPERATOR
# ============================================
# 'in' returns True if a value exists
# in the sequence or collection.

fruits = ["Apple", "Mango", "Banana"]

print("Mango" in fruits)

# "Mango" exists in the list.
# Output:
# True


print("Orange" in fruits)

# "Orange" does not exist in the list.
# Output:
# False

# ============================================
# B. NOT IN OPERATOR
# ============================================
# 'not in' returns True if a value does not
# exist in the sequence or collection.

fruits = ["Apple", "Mango", "Banana"]

print("Orange" not in fruits)

# "Orange" does not exist in the list.
# Output:
# True


print("Mango" not in fruits)

# "Mango" exists in the list.
# Output:
# False


# ============================================
# MEMBERSHIP OPERATORS WITH STRINGS
# ============================================

# Membership operators can also be used
# to check characters or words in a string.

name = "Python"

print("P" in name)
print("z" in name)

print("Py" in name)
print("Java" not in name)


# ============================================
# SUMMARY
# ============================================

# in      -> Checks if a value exists.
# not in  -> Checks if a value does not exist.



# ============================================
# BITWISE OPERATORS
# ============================================

# Bitwise operators perform operations on
# the binary representation of numbers.

# Python has six bitwise operators:
# A) &
# B) |
# C) ^
# D) ~
# E) <<
# F) >>

# ============================================
# A. BITWISE AND (&)
# ============================================
# Returns 1 only when both bits are 1.

a = 5           # 5 = 101
b = 3           # 3 = 011
#                 --------
#                     001 
print(a & b)    # output: 1

# ============================================
# B. BITWISE OR (|)
# ============================================
# Returns 1 when at least one bit is 1.

a = 5           # 5 = 101
b = 3           # 3 = 011
#                --------
#               #     111
print(a | b)    # output: 7

# ============================================
# C. BITWISE XOR (^)
# ============================================
# Returns 1 when the two bits are different.

a = 5           # 5 = 101
b = 3           # 3 = 011
#                 -------- 
#                     110
print(a ^ b)    # output: 6

# ============================================
# D. BITWISE NOT (~)
# ============================================
# Reverses the bits of a number.

a = 5           # ~a = -(n + 1)
print(~a)       # output: -6

# ============================================
# E. LEFT SHIFT (<<)
# ============================================
# Shifts the bits to the left.

a = 5           
print(a << 1)   # 5 = 101 (we have to shift 1 position left)
#                   = 1010 (Binary number of 10)
#                   output: 10


a = 5            
print(a << 3)   # 5 = 101 (we have to shift 3 position left)
#                   = 101000 (Binary number of 40)
#                   output: 40

# ============================================
# F. RIGHT SHIFT (>>)
# ============================================
# Shifts the bits to the right.

a = 5           
print(a >> 1)   # 5 = 101 (we have to shift 1 position right)
#                   = 010 (Binary number of 2)
#                   output: 2


a = 7
print(a >> 2)   # 7 = 111 (we have to shift 2 position right)
#                   = 001 (Binary number of 1)
#                   output: 1


# ============================================
# SUMMARY
# ============================================

# &   -> Bitwise AND
# |   -> Bitwise OR
# ^   -> Bitwise XOR
# ~   -> Bitwise NOT
# <<  -> Left Shift
# >>  -> Right Shift



# ============================================
# OPERATOR PRECEDENCE
# ============================================

# What is Operator Precedence?

# Operator precedence tells Python which operation
# should be performed first when an expression
# contains multiple operators.

# Example:

print(10 + 5 * 2)

# Multiplication (*) has higher precedence than
# addition (+).

# First: 5 * 2 = 10
# Then: 10 + 10 = 20

# Output:
# 20

# ============================================
# PARENTHESES
# ============================================
# Parentheses () have the highest priority
# and are performed first.

print((10 + 5) * 2)

# First: 10 + 5 = 15
# Then: 15 * 2 = 30

# Output:
# 30

# ============================================
# PRECEDENCE ORDER
# ============================================
# From highest to lowest:

# 1) ()       Parentheses
# 2) **       Exponentiation
# 3) +x, -x   Unary Plus, Unary Minus
# 4) *, /, //, %   Multiplication, Division,
#                  Floor Division, Modulus
# 5) +, -     Addition, Subtraction
# 6) <, <=, >, >=, ==, !=   Comparison
# 7) not      Logical NOT
# 8) and      Logical AND
# 9) or       Logical OR

# ============================================
# EXAMPLES
# ============================================
print(2 + 3 * 4)

# First: 3 * 4 = 12
# Then: 2 + 12 = 14

# Output:
# 14


print((2 + 3) * 4)

# First: 2 + 3 = 5
# Then: 5 * 4 = 20

# Output:
# 20


print(2 ** 3 + 4)

# First: 2 ** 3 = 8
# Then: 8 + 4 = 12

# Output:
# 12

# ============================================
# SAME PRECEDENCE
# ============================================
# If operators have the same precedence,
# Python usually evaluates them from left to right.

print(10 - 5 + 2)

# First: 10 - 5 = 5
# Then: 5 + 2 = 7

# Output:
# 7