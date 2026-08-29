# ============================================
# TUPLES IN PYTHON
# ============================================



# Tuples
# ├── Creating a Tuple
# ├── Tuple Items
# ├── Ordered
# ├── Unchangeable
# ├── Allow Duplicates
# ├── Access Tuple Items
# ├── Negative Indexing
# ├── Range of Indexes
# ├── Check if Item Exists
# ├── Update Tuples
# ├── Add Items
# ├── Remove Items
# ├── Loop Through a Tuple
# ├── Join Two Tuples
# ├── Multiply Tuples
# ├── Tuple Methods
# │   ├── count()
# │   └── index()
# ├── Tuple Unpacking
# └── Nested Tuples



# ============================================
# CREATING A TUPLE
# ============================================

# A tuple is used to store multiple values
# in a single variable.

# Tuples are created using round brackets ().

fruits = ("Apple", "Mango", "Banana")

print(fruits)

# Tuples can also be created without the parentheses:

fruits = "Apple", "Mango", "Banana"
print(fruits)



# ============================================
# TUPLE ITEMS
# ============================================

# Tuple items are ordered and have an index.
# The index starts from 0.

fruits = ("Apple", "Mango", "Banana")

print(fruits[0])    # Apple
print(fruits[1])    # Mango
print(fruits[2])    # Banana



# ============================================
# ORDERED
# ============================================

# Tuples are ordered.
# The order of items will remain the same.

fruits = ("Apple", "Mango", "Banana")

print(fruits)

# To create a tuple with only one item, you have to add 
# a comma after the item:

fruit = ("Apple",)
print(type(fruit))



# ============================================
# UNCHANGEABLE
# ============================================

# Tuples are unchangeable (immutable).
# Once a tuple is created, its items cannot
# be changed.

fruits = ("Apple", "Mango", "Banana")
# This will give an error:
# fruits[1] = "Orange"



# ============================================
# ALLOW DUPLICATES
# ============================================

# Tuples allow duplicate values.

fruits = ("Apple", "Mango", "Apple", "Banana")

print(fruits)



# ============================================
# ACCESS TUPLE ITEMS
# ============================================

# We can access tuple items using their index.

fruits = ("Apple", "Mango", "Banana")

print(fruits[0])
print(fruits[1])
print(fruits[2])



# ============================================
# NEGATIVE INDEXING
# ============================================

# Negative indexing starts from the end
# of the tuple.

fruits = ("Apple", "Mango", "Banana")

print(fruits[-1])   # Banana
print(fruits[-2])   # Mango
print(fruits[-3])   # Apple



# ============================================
# RANGE OF INDEXES
# ============================================

# We can access a range of items using slicing.

fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")

print(fruits[1:4])      # Output: ('Mango', 'Banana', 'Orange')
# The first index is included,
# but the last index is not included.



# ============================================
# CHECK IF ITEM EXISTS
# ============================================

# The 'in' keyword is used to check whether
# an item exists in a tuple.

fruits = ("Apple", "Mango", "Banana")

print("Mango" in fruits)    # Output: True

print("Orange" in fruits)   # Output: False



# ============================================
# UPDATE TUPLES
# ============================================

# Tuples are unchangeable, so we cannot
# directly update their items.

# However, we can convert the tuple into
# a list, make changes, and convert it back.

fruits = ("Apple", "Mango", "Banana")

temp_list = list(fruits)

temp_list[1] = "Orange"

fruits = tuple(temp_list)

print(fruits)       # Output: ('Apple', 'Orange', 'Banana')




# ============================================
# ADD ITEMS
# ============================================

# Tuples do not have an append() or insert()
# method because they are unchangeable.

# We can add items by converting the tuple
# into a list.

fruits = ("Apple", "Mango")

temp_list = list(fruits)

temp_list.append("Banana")

fruits = tuple(temp_list)

print(fruits)       # Output: ('Apple', 'Mango', 'Banana')



# ============================================
# REMOVE ITEMS
# ============================================

# Tuples do not have a remove() method.

# We can remove items by converting the tuple
# into a list.

fruits = ("Apple", "Mango", "Banana")

temp_list = list(fruits)

temp_list.remove("Mango")

fruits = tuple(temp_list)

print(fruits)       # Output: ('Apple', 'Banana')



# ============================================
# LOOP THROUGH A TUPLE
# ============================================

# We can use a for loop to go through
# each item in a tuple.

fruits = ("Apple", "Mango", "Banana")

for fruit in fruits:
    print(fruit)



# ============================================
# JOIN TWO TUPLES
# ============================================

# We can join two tuples using the + operator.

tuple1 = ("Apple", "Mango")
tuple2 = ("Banana", "Orange")

tuple3 = tuple1 + tuple2

print(tuple3)       # Output: ('Apple', 'Mango', 'Banana', 'Orange')



# ============================================
# MULTIPLY TUPLES
# ============================================

# We can multiply a tuple using the * operator.
# This repeats the items in the tuple.

fruits = ("Apple", "Mango")

new_tuple = fruits * 2

print(new_tuple)        # Output: ('Apple', 'Mango', 'Apple', 'Mango')



# ============================================
# TUPLE METHODS
# ============================================

# Tuples have two built-in methods:
#
# count() -> Counts how many times an item appears.
# index() -> Returns the index of an item.


# --------------------------------------------
# count()
# --------------------------------------------

fruits = ("Apple", "Mango", "Apple", "Banana")

print(fruits.count("Apple"))        # Output: 2


# --------------------------------------------
# index()
# --------------------------------------------

fruits = ("Apple", "Mango", "Banana")

print(fruits.index("Mango"))        # Output: 1



# ============================================
# TUPLE UNPACKING
# ============================================

# Tuple unpacking allows us to assign
# tuple values to separate variables.

fruits = ("Apple", "Mango", "Banana")

(fruit1, fruit2, fruit3) = fruits

print(fruit1)       # Apple
print(fruit2)       # Mango
print(fruit3)       # Banana



# ============================================
# NESTED TUPLES
# ============================================

# A tuple can contain another tuple.
# This is called a nested tuple.

fruits = (
    ("Apple", "Mango"),
    ("Banana", "Orange")
)

print(fruits)       # (('Apple', 'Mango'), ('Banana', 'Orange'))

print(fruits[0])    # ('Apple', 'Mango')

print(fruits[0][1]) # Mango



# ============================================
# SUMMARY
# ============================================

# Tuples:
# - Store multiple values.
# - Are ordered.
# - Are unchangeable (immutable).
# - Allow duplicate values.
# - Use index numbers starting from 0.
# - Support negative indexing.
# - Can contain different data types.
# - Are created using round brackets ().
# - Have two main methods: count() and index().



# CHALLENGE:

# Create a tuple called fruits with the values "apple", "banana", "cherry"
# Print the second item in the tuple
# Print the number of items using len()
# Unpack the tuple into three variables a, b, c
# Print the variable b