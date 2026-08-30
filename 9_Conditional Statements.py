# ============================================
# CONDITIONAL STATEMENTS IN PYTHON
# ============================================

# Conditional Statements
# ├── if Statement
# ├── elif Statement
# ├── else Statement
# ├── Short Hand if
# ├── Short Hand if...else
# ├── Multiple Conditions
# ├── Nested if
# ├── pass Statement
# └── Match Statement



# ============================================
# CONDITIONAL STATEMENTS IN PYTHON
# ============================================

# Conditional statements are used to make
# decisions based on conditions.

# Python mainly uses:
# A) if
# B) elif
# C) else


# ============================================
# A. IF STATEMENT
# ============================================
# The if statement runs a block of code
# when a condition is True.

age = 20

if age >= 18:
    print("You are an adult.")      # Output: You are an adult.


# ============================================
# B. ELIF STATEMENT
# ============================================
# elif means "else if".
# It is used to check another condition
# when the previous condition is False.

age = 15

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")        # Output: You are a teenager.


# ============================================
# C. ELSE STATEMENT
# ============================================
# The else statement runs when all previous
# conditions are False.

age = 10

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")      # Output: You are not an adult.


# ============================================
# IF, ELIF AND ELSE TOGETHER
# ============================================

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")        # Output: Grade B



# ============================================
# SHORT HAND IF
# ============================================

# A short-hand if can be written on one line
# when there is only one statement.

age = 20

if age >= 18: print("Adult")


# ============================================
# SHORT HAND IF...ELSE
# ============================================

# A short-hand if...else can be written
# using one line.

age = 20

print("Adult") if age >= 18 else print("Not Adult")

# Output: Adult


# ============================================
# MULTIPLE CONDITIONS
# ============================================

# We can use logical operators such as
# and, or, and not with conditions.

age = 25

if age >= 18 and age <= 30:
    print("Age is between 18 and 30.")

# Output: Age is between 18 and 30.


# ============================================
# NESTED IF
# ============================================

# An if statement inside another if statement
# is called a nested if.

age = 20

if age >= 18:
    print("You are an adult.")

    if age >= 21:
        print("You are 21 or older.")

# Output:
# You are an adult.
# You are 21 or older.


# ============================================
# PASS STATEMENT
# ============================================

# The pass statement does nothing.
# It is used when a statement is required
# but we do not want to execute any code yet.

age = 20

if age >= 18:
    pass

# The program continues without doing anything.


# ============================================
# MATCH STATEMENT
# ============================================

# The match statement is used to compare
# a value against different patterns.

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

# Output:
# Tuesday


# ============================================
# SUMMARY
# ============================================

# if      -> Runs code when a condition is True.
# elif    -> Checks another condition.
# else    -> Runs when all conditions are False.
# pass    -> Does nothing.
# match   -> Matches a value against different cases.



# CHALLENGE:

# Create a variable age with the value 20
# Write an if statement that prints "Child" if age is less than 13
# Add an elif that prints "Teenager" if age is less than 18
# Add an else that prints "Adult"