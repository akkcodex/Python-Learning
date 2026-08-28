# ============================================
# LISTS
# ============================================

# Lists
# ├── Creating a List
# ├── List Items
# ├── Ordered
# ├── Changeable
# ├── Allow Duplicates
# ├── List Items Can Have Different Data Type
# ├── Type()
# ├── Python Collections (Arrays)
# ├── Access List Items
# ├── Negative Indexing
# ├── Range of Indexes
# ├── Change List Items
# ├── Add List Items
# ├── Remove List Items
# ├── Loop Through a List
# ├── List Length
# ├── List Methods
# ├── List Comprehension
# ├── Copy A List
# ├── Sort A List
# └── Join A List 



# ============================================
# CREATING A LIST
# ============================================

# A list is used to store multiple values
# in a single variable.

# Lists are created using square brackets [].

fruits = ["Apple", "Mango", "Banana"]

print(fruits)       # ['Apple', 'Mango', 'Banana']



# ============================================
# LIST ITEMS
# ============================================

# List items are ordered and have an index.
# The index starts from 0.

fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])    # Apple
print(fruits[1])    # Mango
print(fruits[2])    # Banana



# ============================================
# ORDERED
# ============================================

# Lists are ordered.
# The order of items will remain the same
# unless we change it.

fruits = ["Apple", "Mango", "Banana"]

print(fruits)



# ============================================
# CHANGEABLE
# ============================================

# Lists are changeable.
# We can change the value of an item.

fruits = ["Apple", "Mango", "Banana"]

fruits[1] = "Orange"

print(fruits)

# Output:
# ['Apple', 'Orange', 'Banana']



# ============================================
# ALLOW DUPLICATES
# ============================================

# Lists can contain duplicate values.

fruits = ["Apple", "Mango", "Apple", "Banana"]

print(fruits)       # Output:['Apple', 'Mango', 'Apple', 'Banana']



# ============================================
# LIST ITEMS CAN HAVE DIFFERENT DATA TYPES
# ============================================

# A list can contain items of different data types.

my_list = ["Amit", 25, 5.11, True]

print(my_list)

# String
# Integer
# Float
# Boolean

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [1.50, 2.50, 3.50, 4.50]
list4 = [True, False, False]

# A list can also contain other collections.

my_list = [
    "Amit",
    25,
    [1, 2, 3],
    ("Apple", "Mango"),
    {"name": "Amit"}
]

print(my_list)      # <class 'list'>


# ============================================
# TYPE()
# ============================================

# From Python perspective, lists are defined as objects with the data type 'list':

my_list = ["apple', 'banana', 'cherry"]
print(type(my_list))



# ============================================
# PYTHON COLLECTIONS (ARRAYS)
# ============================================

# There are four collection data types in Python programming language:

# ├── List
# ├── Tuple
# ├── Set
# └── Dictionary



# ============================================
# ACCESS LIST ITEMS
# ============================================

# We can access list items using their index.

fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])
print(fruits[1])
print(fruits[2])



# ============================================
# NEGATIVE INDEXING
# ============================================

# Negative indexing starts from the end of the list.

fruits = ["Apple", "Mango", "Banana"]

print(fruits[-1])   # Banana
print(fruits[-2])   # Mango
print(fruits[-3])   # Apple



# ============================================
# RANGE OF INDEXES
# ============================================

# We can access a range of items using slicing.

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print(fruits[1:4])      # Output:['Mango', 'Banana', 'Orange']

# The first index is included,
# but the last index is not included.



# ============================================
# CHANGE LIST ITEMS
# ============================================

# We can change one or more list items.

fruits = ["Apple", "Mango", "Banana"]

fruits[1] = "Orange"

print(fruits)       # Output:['Apple', 'Orange', 'Banana']

# Changing multiple items:

fruits[0:2] = ["Grapes", "Pineapple"]

print(fruits)



# ============================================
# ADD LIST ITEMS
# ============================================

# We can add items to a list using

# A) Append()
# B) Insert()
# C) Extend()


# A) Append():
# Adds an item to the end of the list.

fruits = ["Apple", "Mango"]

fruits.append("Banana")

print(fruits)


# B) Insert():
# Adds an item at a specific position.

fruits.insert(1, "Orange")

print(fruits)


# C) Extend():
# Adds multiple items to the end of the list.

fruits.extend(["Grapes", "Pineapple"])

print(fruits)



# ============================================
# REMOVE LIST ITEMS
# ============================================

# We can remove items using
# A) Remove()
# B) Pop()
# C) Del.


# A) Remove():
# Removes a specific value.

fruits = ["Apple", "Mango", "Banana"]

fruits.remove("Mango")

print(fruits)


# B) Pop():
# Removes an item using its index.
# If no index is given, it removes the last item.

fruits = ["Apple", "Mango", "Banana"]

fruits.pop(1)

print(fruits)


# C) Del:
# Deletes an item using its index.

fruits = ["Apple", "Mango", "Banana"]

del fruits[0]

print(fruits)


# Clear()
# Removes all items from the list.

fruits = ["Apple", "Mango", "Banana"]

fruits.clear()

print(fruits)

# Output:
# []



# ============================================
# LOOP THROUGH A LIST
# ============================================

# We can use a for loop to go through
# each item in a list.

fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)



# ============================================
# LIST LENGTH
# ============================================

# The len() function is used to find
# the number of items in a list.

fruits = ["Apple", "Mango", "Banana"]

print(len(fruits))

# Output:
# 3



# ============================================
# LIST METHODS
# ============================================

# List methods are built-in functions
# used to perform different operations on lists.

# Common List Methods:

# append()   -> Adds an item to the end
# insert()   -> Adds an item at a specific position
# extend()   -> Adds multiple items
# remove()   -> Removes a specific item
# pop()      -> Removes an item by index
# clear()    -> Removes all items
# sort()     -> Sorts the list
# reverse()  -> Reverses the list
# copy()     -> Creates a copy of the list
# count()    -> Counts how many times an item appears
# index()    -> Returns the index of an item


# Example:

numbers = [30, 10, 20, 40]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]



# ============================================
# LIST COMPREHENSION
# ============================================

# List comprehension provides a shorter way
# to create a new list.

# Example:

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)      # Output: 1, 4, 9, 16, 25]


# List comprehension with a condition:

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)     # Output: [2, 4, 6]



# ============================================
# COPY A LIST
# ============================================

# The copy() method is used to create a copy
# of an existing list.

fruits = ["Apple", "Mango", "Banana"]

new_fruits = fruits.copy()

print(new_fruits)       # Output: ['Apple', 'Mango', 'Banana']

# By copying, we get a seperate list:

fruits = ["Apple", "Mango", "Banana"]

new_fruits = fruits.copy()

new_fruits.append("Orange")

print(fruits)       # ['Apple', 'Mango', 'Banana']
print(new_fruits)   # ['Apple', 'Mango', 'Banana', 'Orange']



# ============================================
# SORT A LIST
# ============================================

# The sort() method is used to arrange
# the items of a list in order.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)      # Output:[10, 20, 30, 40]

# in descending order:

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)      # Output:[40, 30, 20, 10]

# We can also sort strings:

fruits = ["Mango", "Apple", "Banana"]

fruits.sort()

print(fruits)       # Output: ['Apple', 'Banana', 'Mango']

 

# ============================================
# JOIN LIST ITEMS
# ============================================

# The join() method is used to combine
# string items into a single string.

fruits = ["Apple", "Mango", "Banana"]

result = ", ".join(fruits)

print(result)       # Output: Apple, Mango, Banana



# ============================================
# SUMMARY
# ============================================

# Lists:
# - Store multiple values
# - Are ordered
# - Are changeable
# - Allow duplicate values
# - Use index numbers starting from 0
# - Can contain different data types



# CHALLENGE:

# Create a list called colors with the value "red", "green", "blue"
# Print the first item
# Change the second item to "yellow"
# Add "purple" to the end of the list using append()
# Remove "red" from the list using remove()
# Print the list
