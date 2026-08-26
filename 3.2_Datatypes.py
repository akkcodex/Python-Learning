# SLICING

# you can return a range of characters by using the slice syntax.
# specify the start index and the end index, separated by a colon, to return a part of the string.

a = "Hello, World!"
print(a[2:5]) # returns the characters from position 2 to 5 (not included)


# by leaving out the start index, the range will start at the first character:

a = "Hello, World!"
print(a[:5]) # returns the characters from the start to position 5 (not included)


# by leaving out the end index, the range will go to the end:

a = "Hello, World!"
print(a[2:]) # returns the characters from position 2 to the end


# by using negative indexes, you can start the slice from the end of the string:

a = "Hello, World!"
print(a[-5:-2]) # returns the characters from position -5 to -2


# MODIFYING STRINGS:

# python has a set of built-in methods that you can use on strings.

# Upper Case:

a = "Hello, World!"
print(a.upper()) # returns "HELLO, WORLD!"


# Lower Case:

a = "Hello, World!"
print(a.lower()) # returns "hello, world!"


# Remove Whitespace:

# white space is the empty space between characters, words, or lines. It includes spaces, tabs, and newlines.

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String:

a = "Hello, World!"
print(a.replace("H", "J")) # returns "Jello, World!"


# Split String:

# the split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']



#_____________________________________________________________________


# STRING CONCATENATION:

# to concatenate, or combine, two strings you can use the + operator.


# merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# to add space between the two strings, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#______________________________________________________________________

# FORMAT STRINGS:

# An f-string is a formatted string that allows us to insert variables and expressions directly inside a string using {}.

age = 30
txt = f"My name is John, and I am {age} years old."
print(txt) # returns "My name is John, and I am 30 years old."



#_______________________________________________________________________

# PLACEHOLDERS AND MODIFIERS:

# # placeholder can contain variables, operations, and modifiers to format the value.

price = 49
txt = f"The price is {price} dollars."
print(txt) # returns "The price is 49 dollars."

# a placeholder can include a modifier to format the value.
# a modifier is included by adding a colon: followed by a legal formatting type, like .2f which means fixed point number with 2 decimals.

price = 49
txt = f"The price is {price:.2f} dollars."
print(txt) # returns "The price is 49.00 dollars."

# a placeholder can contain Python code, like a mathematical operation:

txt = f"The price is {price * 2} dollars."
print(txt) # returns "The price is 98 dollars."


#_______________________________________________________________________

# CHALLENGE

# # Create a variable txt with the Create a variable txt with the value "Hello, World!"
# Print the characters from index 2 to 5 (slicing)
# Print txt converted to upper case
# Create a variable name with the value "Python"
# Use an f-string to print "I love Python" using the name variable

txt = "Hello, World!"
print(txt[2:5]) # returns "llo"
print(txt.upper()) # returns "HELLO, WORLD!"
name = "Python"
print(f"I love {name}") # returns "I love Python"


#______________________________________________________________________

# BOOLEAN VALUES:

# Boolean is a data type that has only two values:
# True or False.

is_python_easy = True
is_python_hard = False

print(is_python_easy)
print(is_python_hard)

# Boolean values are commonly used with conditions
# and comparisons.

print(10 > 5)    # True
print(10 == 5)   # False

# the bool() function allows you to evaluate any value, and give you True or False in return.

print(bool("Hello"))  # True
print(bool(15))     # True

# Evauate two variables:

x = "Hello"
y = 15
print(bool(x))  # True
print(bool(y))  # True

# Some values are evaluated to False, like empty values, such as:
print(bool(""))     # False
print(bool(0))      # False
print(bool([]))     # False


# Functions can return a Boolean value:
# You can create functions that return a Boolean value:

def myFunction() :
  return True

print(myFunction())  # True

# You can execute code based on the Boolean value of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#_______________________________________________________________________

# CHALLENGE

# # Print the result of 10 > 9
# Print the result of 10 == 9
# Print the result of bool("Hello")
# Print the result of bool(0)
