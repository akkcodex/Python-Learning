# ============================================
# SETS IN PYTHON
# ============================================



# Sets
# ├── Creating a Set
# ├── Set Items
# ├── Unordered
# ├── Unchangeable
# ├── Do Not Allow Duplicates
# ├── Access Set Items
# ├── Check if Item Exists
# ├── Add Items
# ├── Remove Items
# ├── Loop Through a Set
# ├── Set Length
# ├── Join Two Sets
# ├── Set Intersection
# ├── Set Difference
# ├── Symmetric Difference
# ├── Set Methods
# └── Frozenset



# ============================================
# SETS IN PYTHON
# ============================================

# What is a Set?

# A set is a collection used to store
# multiple values in a single variable.

# Sets are created using curly brackets {}.

fruits = {"Apple", "Mango", "Banana"}

print(fruits)



# ============================================
# SET ITEMS
# ============================================

# Set items are unordered.
# Set items do not have an index.
# Set items are unchangeable.
# Sets do not allow duplicate values.

fruits = {"Apple", "Mango", "Banana"}

print(fruits)



# ============================================
# UNORDERED
# ============================================

# Sets are unordered.
# The items do not have a defined order.

fruits = {"Apple", "Mango", "Banana"}

print(fruits)

# The order of items may change when displayed.



# ============================================
# UNCHANGEABLE
# ============================================

# Set items cannot be changed directly
# after the set is created.

fruits = {"Apple", "Mango", "Banana"}

# This will give an error:
# fruits[0] = "Orange"



# ============================================
# DO NOT ALLOW DUPLICATES
# ============================================

# Sets do not allow duplicate values.

fruits = {"Apple", "Mango", "Apple", "Banana"}

print(fruits)

# Output will contain "Apple" only once.



# ============================================
# DIFFERENT DATA TYPES
# ============================================

# A set can contain different data types.

my_set = {"Amit", 25, 5.11, True}

print(my_set)



# ============================================
# ACCESS SET ITEMS
# ============================================

# Sets do not have indexes.
# Therefore, we cannot access items using an index.

fruits = {"Apple", "Mango", "Banana"}

# This will give an error:
# print(fruits[0])


# We can use a for loop to access
# each item in a set.

for fruit in fruits:
    print(fruit)



# ============================================
# CHECK IF ITEM EXISTS
# ============================================

# The 'in' keyword is used to check
# whether an item exists in a set.

fruits = {"Apple", "Mango", "Banana"}

print("Mango" in fruits)        # True

print("Orange" in fruits)       # False



# ============================================
# ADD ITEMS
# ============================================

# The add() method is used to add
# one item to a set.

fruits = {"Apple", "Mango"}

fruits.add("Banana")

print(fruits)



# ============================================
# ADD MULTIPLE ITEMS
# ============================================

# The update() method is used to add
# multiple items to a set.

fruits = {"Apple", "Mango"}

fruits.update(["Banana", "Orange"])

print(fruits)



# ============================================
# REMOVE ITEMS
# ============================================

# The remove() method removes a specific item.

fruits = {"Apple", "Mango", "Banana"}

fruits.remove("Mango")

print(fruits)



# ============================================
# DISCARD ITEMS
# ============================================

# The discard() method also removes an item.
# Unlike remove(), discard() does not give
# an error if the item does not exist.

fruits = {"Apple", "Mango", "Banana"}

fruits.discard("Orange")

print(fruits)



# ============================================
# POP ITEMS
# ============================================

# The pop() method removes one item from a set.
# Since sets are unordered, we do not know
# which item will be removed.

fruits = {"Apple", "Mango", "Banana"}

fruits.pop()

print(fruits)



# ============================================
# CLEAR A SET
# ============================================

# The clear() method removes all items
# from a set.

fruits = {"Apple", "Mango", "Banana"}

fruits.clear()

print(fruits)       # set()



# ============================================
# DELETE A SET
# ============================================

# The del keyword completely deletes the set.

fruits = {"Apple", "Mango", "Banana"}

del fruits

# print(fruits)  # This will give an error.



# ============================================
# SET LENGTH
# ============================================

# The len() function returns the number
# of items in a set.

fruits = {"Apple", "Mango", "Banana"}

print(len(fruits))      # 3



# ============================================
# JOIN TWO SETS
# ============================================

# We can combine two sets using union()
# or the | operator.

set1 = {"Apple", "Mango"}
set2 = {"Banana", "Orange"}

set3 = set1.union(set2)

print(set3)


# Using | operator:

set3 = set1 | set2

print(set3)



# ============================================
# SET INTERSECTION
# ============================================

# intersection() returns items that are
# present in both sets.

set1 = {"Apple", "Mango", "Banana"}
set2 = {"Mango", "Banana", "Orange"}

result = set1.intersection(set2)

print(result)       # {'Mango', 'Banana'}


# Using & operator:

result = set1 & set2

print(result)



# ============================================
# SET DIFFERENCE
# ============================================

# difference() returns items that exist
# in the first set but not in the second set.

set1 = {"Apple", "Mango", "Banana"}
set2 = {"Mango", "Banana", "Orange"}

result = set1.difference(set2)

print(result)       # {'Apple'}


# Using - operator:

result = set1 - set2

print(result)



# ============================================
# SET SYMMETRIC DIFFERENCE
# ============================================

# symmetric_difference() returns items
# that are present in either set,
# but not in both sets.

set1 = {"Apple", "Mango", "Banana"}
set2 = {"Mango", "Banana", "Orange"}

result = set1.symmetric_difference(set2)

print(result)       # {'Apple', 'Orange'}


# Using ^ operator:

result = set1 ^ set2

print(result)



# ============================================
# SET METHODS
# ============================================

# Common Set Methods:

# add()                    -> Adds one item
# update()                 -> Adds multiple items
# remove()                 -> Removes an item
# discard()                -> Removes an item safely
# pop()                    -> Removes one item
# clear()                  -> Removes all items
# union()                  -> Combines sets
# intersection()           -> Finds common items
# difference()             -> Finds different items
# symmetric_difference()   -> Finds items in either set,
#                              but not both



# ============================================
# FROZENSET
# ============================================

# A frozenset is an immutable version of a set.
# Its items cannot be changed after creation.

fruits = frozenset(["Apple", "Mango", "Banana"])

print(fruits)

# We cannot add or remove items from a frozenset.



# ============================================
# SUMMARY
# ============================================

# Sets:
# - Store multiple values.
# - Are unordered.
# - Do not have indexes.
# - Do not allow duplicate values.
# - Are changeable as a collection.
# - Can contain different data types.
# - Use curly brackets {}.
# - Support set operations like union,
#   intersection, and difference.



# CHALLENGE:

# Create a set called colors with the values "red", "green", "blue"
# Print the set
# Add "yellow" to the set using add()
# Remove "green" from the set using discard()
# Print the number of items using len()