# There are three types of numeric types in Python:
#    int
#    float
#    complex

# integer (int) is used for whole numbers, float is used for numbers with decimal points, and complex
# is used for complex numbers.

# int: int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 6372683787
z = -762378613

print(type(x))
print(type(y))
print(type(z))


# float: float, or floating point number, is a number, positive or negative, containing one or more decimals.

a = 1.0
b = 3.14159
c = -87.75

print(type(a))
print(type(b))
print(type(c))

# float can also be scientific numbers with an "e" to indicate the power of 10.
d = 35e4
e = 12E10
f = -87.75E100

print(type(d))
print(type(e))
print(type(f))

# complex: complex, or complex number, is a number, positive or negative, containing one or more decimals.

g = 3+5j
h = 5j
i = -5j

print(type(g))
print(type(h))
print(type(i))

# you can convert from one type to another with the int(), float(), and complex() methods: 

x = 1    # int
y = 5.68  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x) 

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# ---------------------------------------------

# CASTING:

# casting in python is therefore done using constructor functions:

# integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)   # z will be '3.0'

# ----------------------------------------------

# STRINGS:

# strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello")
print('Hello')

# you can use single quotes inside a string with double quotes, or double quotes inside a string with single quotes:

print("It's a beautiful day")


# assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Cat"
print(a)


# You can assign a multiline string to a variable by using three quotes:

a = """Where there is a will, there is a way.""" # you can use three double quotes
print(a)

a = '''Where there is a will, there is a way.''' # you can use three single quotes
print(a)


# a string is a sequence of characters, and each character can be accessed using its index number, which starts at 0.
# you can also use negative indexing to access characters from the end of the string, starting at -1.

a = " Good Morning"
print(a[3]) # prints the character at index 3, which is 'o'
print(a[-3]) # prints the character at index -3, which is 'i'


# since strings are arrays, you can loop through the characters in a string using a for loop:

for x in "Apricot":
 print(x)


# to get the length of a string, use the built-in len() function:
  
a = "Good Morning"
print(len(a)) # prints 12


# to check if a certain phrase or character is present in a string, use the keyword in:

txt = "The best things in life are free!"
print("free" in txt) # prints True


# use it in an if statement:   

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# to check if a certain phrase or character is NOT present in a string, use the keyword not in:

txt = "The best things in life are free!"
print("expensive" not in txt) # prints True


# use it in an if statement:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")