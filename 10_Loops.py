# ============================================
# LOOPS IN PYTHON
# ============================================

# Roadmap:
# ├── While Loop
# ├── For Loop
# ├── Loop Through a List
# ├── Loop Through a Tuple
# ├── Loop Through a Set
# ├── Loop Through a Dictionary
# ├── range()
# ├── Break
# ├── Continue
# ├── Nested Loops
# └── Pass



# ============================================
# 1. WHILE LOOP
# ============================================

# A while loop runs as long as the condition is True.

i = 1

while i <= 5:
    print(i)
    i = i + 1


# BREAK STATEMENT:

# With break statement, we can stop the loop even if
# the while condition is true:

# Exiting the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# CONTINUE STATEMENT:

# With the continue statement we can stop the current iteration
# and continue with the next:

# Continue to the next iteration if i = 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)


# THE ELSE STATEMENT:

# With the else statement we can run a block
# of code once when the condition no longer is true:

# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")



# ============================================
# 2. FOR LOOP
# ============================================

# A for loop is used to iterate through a sequence
# such as a list, tuple, set, string, or range.

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# BREAK STATEMENT:

# With the break statement we can stop the loop
# before it has looped through all the items:

# Exit the loop when x is "banana":
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)
    if fruit == "Banana":
        break

# Exit the loop when fruit is "Banana", but this
# time the break comes before the print:
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    if fruit == "Banana":
        break
    print(fruit)


# CONTINUE STATEMENT:

# With the continue statement we can stop the current
# iteration of the loop, and continue with the next:

# Do not print Banana:
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    if fruit == "Banana":
        continue
    print(fruit)


# ELSE IN FOR LOOP:

# The else keyword in a for loop specifies
# a block of code to be executed when the loop is finished:

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for i in range (6):
    print(i)
else:
    print("Finally finished!")




# ============================================
# 3. LOOP THROUGH A LIST
# ============================================

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)



# ============================================
# 4. LOOP THROUGH A TUPLE
# ============================================

colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)



# ============================================
# 5. LOOP THROUGH A SET
# ============================================

cities = {"Delhi", "Mumbai", "Chennai"}

for city in cities:
    print(city)



# ============================================
# 6. LOOP THROUGH A DICTIONARY
# ============================================

person = {
    "name": "Amit",
    "age": 25,
    "city": "Delhi"
}

# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through keys and values
for key, value in person.items():
    print(key, value)



# ============================================
# 7. RANGE()
# ============================================

# range() generates a sequence of numbers.

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# range(start, stop)

for i in range(2, 6):
    print(i)


# range(start, stop, step)

for i in range(2, 11, 2):
    print(i)





# ============================================
# 8. BREAK
# ============================================

# break stops the loop immediately.

for i in range(1, 6):
    if i == 3:
        break
    print(i)



# ============================================
# 9. CONTINUE
# ============================================

# continue skips the current iteration
# and moves to the next iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)



# ============================================
# 10. NESTED LOOPS
# ============================================

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Print each adjective for every fruit:
adj = ["Red", "Big", "Tasty"]
fruits = ["Apple", "Banana", "Mango"]

for a in adj:
    for fruit in fruits:
        print(a, fruit)



# ============================================
# 11. PASS
# ============================================

# pass does nothing.
# It is used when a statement is required
# but we do not want to execute any code yet.

for i in range(5):
    pass
