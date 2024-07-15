'''Exception Handling:

Exception handling in Python is used to manage and respond to runtime errors or exceptional conditions in a program.
It ensures the program can handle errors gracefully without crashing.
Introduction to Exceptions:

An exception is an error that occurs during the execution of a program.
Common built-in exceptions include ZeroDivisionError, TypeError, ValueError, IndexError, KeyError, etc.
When an exception occurs, the normal flow of the program is interrupted, and Python looks for an exception handler.
'''

try:
    # code that may raise an exception
except ExceptionType:
    # code that runs if the exception occurs


'''
Try, Except, Finally Blocks:

Try Block:
The try block contains the code that might throw an exception.
Except Block:
The except block contains the code that executes if an exception occurs.
You can specify the type of exception to catch.
'''

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

'''
Finally Block:
The finally block contains the code that always executes, regardless of whether an exception occurred or not.
It is typically used for cleanup actions (e.g., closing files, releasing resources).
'''

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()


'''Raising Exceptions:

You can raise exceptions manually using the raise keyword.
This is useful for generating errors in specific conditions.
'''

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-1)
except ValueError as e:
    print(e)

'''
Custom Exceptions:

You can define your own exception classes by inheriting from the built-in Exception class.
Custom exceptions provide more specific error handling tailored to the application.
'''

class CustomError(Exception):
    pass

def cause_error():
    raise CustomError("This is a custom error")

try:
    cause_error()
except CustomError as e:
    print(e)
