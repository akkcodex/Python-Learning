# ============================================
# DICTIONARIES IN PYTHON
# ============================================



# Dictionaries
# ├── Creating a Dictionary
# ├── Dictionary Items
# ├── Ordered
# ├── Changeable
# ├── Do Not Allow Duplicate Keys
# ├── Access Dictionary Items
# ├── Get Keys
# ├── Get Values
# ├── Get Items
# ├── Check if Key Exists
# ├── Change Dictionary Items
# ├── Add Dictionary Items
# ├── Remove Dictionary Items
# ├── Loop Through a Dictionary
# ├── Dictionary Length
# ├── Copy a Dictionary
# ├── Nested Dictionaries
# └── Dictionary Methods



# ============================================
# CREATING A DICTIONARY
# ============================================

# A dictionary is used to store data in
# key-value pairs.

# Dictionaries are created using curly brackets {}.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

print(person)



# ============================================
# DICTIONARY ITEMS
# ============================================

# Dictionary items are stored as key-value pairs.

person = {
    "name": "Alex",
    "age": 25
}

# "name" and "age" are keys.
# "Alex" and 25 are values.

print(person)



# ============================================
# ORDERED
# ============================================

# Dictionaries are ordered.
# They maintain the order in which items
# are added.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

print(person)



# ============================================
# CHANGEABLE
# ============================================

# Dictionaries are changeable.
# We can change, add, or remove items.

person = {
    "name": "Alex",
    "age": 25
}

person["age"] = 26

print(person)



# ============================================
# DO NOT ALLOW DUPLICATE KEYS
# ============================================

# Dictionary keys cannot have duplicate values.
# If a key is repeated, the latest value
# will replace the previous value.

person = {
    "name": "Alex",
    "age": 25,
    "name": "Rob"
}

print(person)

# Output:
# {'name': 'Rob', 'age': 25}



# ============================================
# ACCESS DICTIONARY ITEMS
# ============================================

# We can access dictionary values by using
# their keys.

person = {
    "name": "Alex",
    "age": 25
}

print(person["name"])       # Alex
print(person["age"])        # 25



# ============================================
# GET KEYS
# ============================================

# The keys() method returns all the keys
# in a dictionary.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

print(person.keys())



# ============================================
# GET VALUES
# ============================================

# The values() method returns all the values
# in a dictionary.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

print(person.values())



# ============================================
# GET ITEMS
# ============================================

# The items() method returns all key-value pairs.

person = {
    "name": "Alex",
    "age": 25
}

print(person.items())



# ============================================
# CHECK IF KEY EXISTS
# ============================================

# The 'in' keyword checks whether a key
# exists in a dictionary.

person = {
    "name": "Alex",
    "age": 25
}

print("name" in person)
print("city" in person)

# Output:
# True
# False



# ============================================
# CHANGE DICTIONARY ITEMS
# ============================================

# We can change the value of a key
# by using its key.

person = {
    "name": "Alex",
    "age": 25
}

person["name"] = "Rob"

print(person)


# We can also use update().

person.update({"age": 26})

print(person)



# ============================================
# ADD DICTIONARY ITEMS
# ============================================

# We can add a new key-value pair
# by using a new key.

person = {
    "name": "Alex",
    "age": 25
}

person["city"] = "New York"

print(person)


# We can also use update().

person.update({"country": "USA"})

print(person)



# ============================================
# REMOVE DICTIONARY ITEMS
# ============================================

# pop() removes an item using its key.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

person.pop("age")

print(person)


# popitem() removes the last added item.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

person.popitem()

print(person)


# del removes an item using its key.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

del person["age"]

print(person)


# clear() removes all items.

person = {
    "name": "Alex",
    "age": 25
}

person.clear()

print(person)

# Output:
# {}



# ============================================
# LOOP THROUGH A DICTIONARY
# ============================================

# We can loop through the keys of a dictionary.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

for key in person:
    print(key)


# Loop through values:

for value in person.values():
    print(value)


# Loop through keys and values:

for key, value in person.items():
    print(key, value)



# ============================================
# DICTIONARY LENGTH
# ============================================

# The len() function returns the number
# of key-value pairs.

person = {
    "name": "Alex",
    "age": 25,
    "city": "New York"
}

print(len(person))      # Output: 3



# ============================================
# COPY A DICTIONARY
# ============================================

# The copy() method creates a copy
# of an existing dictionary.

person = {
    "name": "Alex",
    "age": 25
}

new_person = person.copy()

print(new_person)



# ============================================
# NESTED DICTIONARIES
# ============================================

# A dictionary can contain another dictionary.
# This is called a nested dictionary.

students = {
    "student1": {
        "name": "Alex",
        "age": 25
    },
    "student2": {
        "name": "Rob",
        "age": 26
    }
}

print(students)


# Accessing nested dictionary values:

print(students["student1"]["name"])
print(students["student2"]["age"])



# ============================================
# DICTIONARY METHODS
# ============================================

# Common Dictionary Methods:

# keys()       -> Returns all keys
# values()     -> Returns all values
# items()      -> Returns all key-value pairs
# get()        -> Returns the value of a key
# update()     -> Adds or changes items
# pop()        -> Removes an item
# popitem()    -> Removes the last added item
# clear()      -> Removes all items
# copy()       -> Creates a copy



# ============================================
# GET() METHOD
# ============================================

# The get() method is used to access
# a value using its key.

person = {
    "name": "Alex",
    "age": 25
}

print(person.get("name"))       # Output: Amit


# get() can also return a default value
# if the key does not exist.

print(person.get("city", "Not Found"))      # Output: Not Found



# ============================================
# SUMMARY
# ============================================

# Dictionaries:
# - Store data in key-value pairs.
# - Are ordered.
# - Are changeable.
# - Do not allow duplicate keys.
# - Use curly brackets {}.
# - Values are accessed using keys.
# - Can contain different data types.
# - Can contain nested dictionaries.



# CHALLENGE:

# Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
# Print the value of the "model" key
# Add a new key "color" with the value "red"
# Remove the "brand" key using pop()
# Print the dictionary