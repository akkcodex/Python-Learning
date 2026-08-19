# ============================================
# DATA TYPES IN PYTHON
# ============================================

# What is a Data Type?

# A data type tells us what type of value
# a variable contains.

# Python has several built-in data types.

# Main Data Types in Python:



# 1) Numeric Types

# Values of numeric types are created when you assign a value to them.

# ============================================
# 1. INTEGER (int)
# ============================================

# Used for whole numbers.

age = 31
birth_year = 1995

print(age)
print(type(age))
print(birth_year)
print(type(birth_year))


# ============================================
# 2. FLOAT (float)
# ============================================

# Used for numbers with decimal points.

price = 99.99
height = 5.11

print(price)
print(type(price))


# ============================================
# 3. COMPLEX (complex)
# ============================================

# Used for complex numbers.

number = 3 + 4j

print(number)
print(type(number))


# To verify the type of any object in Pyton, you can use the built-in type() function.



# 2) Boolean Type
#    bool

# Boolean has only two values:
# True or False

is_student = True
is_married = False

print(is_student)
print(type(is_student))


# 3) Text Type
#    str

# Used for text and can be surrounded by single or double quotes.

name = "Jonathan"
city = 'New York'

print(name)
print(type(name))

# 4) Sequence Types

# ============================================
# 1. LIST (list)
# ============================================

# Used to store multiple values.
# Lists are ordered and changeable.

fruits = ["Apple", "Mango", "Banana"]

print(fruits)
print(type(fruits))


# ============================================
# 2. TUPLE (tuple)
# ============================================

# Used to store multiple values.
# Tuples are ordered but cannot be changed.

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))

# ============================================
# 3. RANGE (range)
# ============================================

# Used to generate a sequence of numbers.

numbers = range(5)

print(numbers)
print(type(numbers))

# 5) Set Types

# ============================================
# 1. SET (set)
# ============================================

# Used to store multiple unique values.
# Sets are unordered.

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# ============================================
# 2. FROZENSET (frozenset)
# ============================================

# A frozenset is an unchangeable set.

numbers = frozenset({10, 20, 30})

print(numbers)
print(type(numbers))

# 6) Mapping Type

# ============================================
# 1. DICTIONARY (dict)
# ============================================

# Used to store data in key-value pairs.

student = {
    "name": "Amit",
    "age": 31
}

print(student)
print(type(student))

# 7) Binary Types

# ============================================
# 1. BYTES (bytes)
# ============================================

# Used to store binary data.

data = "Python"

print(data)
print(type(data))


# ============================================
# 2. BYTEARRAY (bytearray)
# ============================================

# Similar to bytes, but it can be changed.

data = bytearray(5)

print(data)
print(type(data))


# ============================================
# 3. MEMORYVIEW (memoryview)
# ============================================

# Used to access the memory of binary objects.

data = memoryview(bytes(5))

print(data)
print(type(data))

# 8) None Type

# ============================================
# 15. NONE (NoneType)
# ============================================

# None represents the absence of a value.

result = None

print(result)
print(type(result))
