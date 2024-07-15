'''
Conditional Statements:

Conditional statements allow the execution of certain pieces of code based on whether a condition is true or false.
The primary conditional statements in Python are
if, if-else, and if-elif-else.

If Statement:

The if statement evaluates a condition. If the condition is true, the block of code within the if statement is executed.
'''

if condition:
    # block of code

age = 18
if age >= 18:
    print("You are an adult.")

'''
If-Else Statement:

The if-else statement evaluates a condition. If the condition is true, the block of code within the if statement is executed; 
otherwise, the block of code within the else statement is executed.
'''

if condition:
    # block of code if condition is true
else:
    # block of code if condition is false

age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


'''
If-Elif-Else Statement:

The if-elif-else statement allows checking multiple conditions. The first true condition will execute its corresponding block of code. 
If none of the conditions are true, the else block is executed.
'''

if condition1:
    # block of code if condition1 is true
elif condition2:
    # block of code if condition2 is true
elif condition3:
    # block of code if condition3 is true
else:
    # block of code if none of the conditions are true

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")


'''
Nested Conditionals:

Conditionals can be nested within other conditionals, allowing for more complex decision-making processes.
'''
if condition1:
    if condition2:
        # block of code if both condition1 and condition2 are true
    else:
        # block of code if condition1 is true and condition2 is false
else:
    # block of code if condition1 is false

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")



######################examples of if,if-else,if-elif-else############################
# Example of if statement
temperature = 30
if temperature > 25:
    print("It's hot outside!")

# Example of if-else statement
temperature = 20
if temperature > 25:
    print("It's hot outside!")
else:
    print("It's not hot outside.")

# Example of if-elif-else statement
temperature = 15
if temperature > 25:
    print("It's hot outside!")
elif temperature > 15:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# Example of nested conditionals
number = 10
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

