'''

Python syntax refers to the set of rules that define how a Python program is written and interpreted.
Python semantics involve the meaning of the syntactical elements and how they behave in the program.
'''

'''
1> Indentation: Unlike many other programming languages, Python uses indentation to define blocks of code.
Indentation is crucial in Python as it defines the structure and flow of control in the code. 
Proper indentation is necessary for defining blocks of code for loops, functions, classes, etc.
'''

def greet(name):
    if name:
        print(f"Hello, {name}!")  # This line is indented to show it's inside the if block
    else:
        print("Hello, world!")  # This line is also indented to show it's inside the else block


'''
2> Statements: A statement is an instruction that the Python interpreter can execute.
Examples include assignment statements and print statements.
'''

# Assignment statement
x = 10

# Conditional statement
if x > 5:
    print("x is greater than 5")

# Loop statement
for i in range(5):
    print(i)

# Function definition statement
def add(a, b):
    return a + b



'''
3> Expressions: An expression is a combination of values, variables, operators,
and function calls that are interpreted to produce another value.
'''
# Arithmetic expression
y = x + 5  # Here, x + 5 is an expression

# Function call expression
result = add(3, 4)  # Here, add(3, 4) is an expression

# Boolean expression
is_greater = x > 5  # Here, x > 5 is an expression

# String expression
greeting = "Hello" + " " + "world!"  # Here, "Hello" + " " + "world!" is an expression


'''
4> Comments: Comments are used to explain code and are ignored by the interpreter. They start with a # symbol.
'''


x = 10  # This is an inline comment

'''
This is a
multi-line comment
'''

"""
This is also a
multi-line comment
"""
