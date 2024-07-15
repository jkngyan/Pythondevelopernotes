'''Looping Constructs:

Loops are used to execute a block of code repeatedly as long as a condition is met.
Python provides two main types of loops: while loops and for loops.
'''

'''While Loop:

The while loop repeatedly executes a block of code as long as a given condition is true.
'''

while condition:
    # block of code

count = 0
while count < 5:
    print(count)
    count += 1

'''
For Loop:

The for loop iterates over a sequence (e.g., list, tuple, dictionary, set, string) and 
executes a block of code for each item in the sequence.
'''

for item in sequence:
    # block of code

#for with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#for with Tuple
coordinates = (10, 20, 30)
for coordinate in coordinates:
    print(coordinate)

#for with string
greeting = "hello"
for letter in greeting:
    print(letter)

#for with dictionary
student = {"name": "Alice", "age": 25, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

#for with sets
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)


'''
Range Function:

The range() function generates a sequence of numbers, which is commonly used in for loops.
'''

for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)  # Prints 1, 3, 5, 7, 9

'''
Nested Loops:

Loops can be nested within other loops.
Each iteration of the outer loop triggers the execution of the inner loop from start to finish.
'''

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

'''
Break Statement:

The break statement terminates the loop and transfers control to the statement following the loop.
'''

for i in range(10):
    if i == 5:
        break
    print(i)


'''Continue Statement:

The continue statement skips the current iteration and proceeds to the next iteration of the loop.
'''

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

'''
Pass Statement:

The pass statement is a null operation; 
it is used when a statement is required syntactically but no code needs to be executed.
'''

for i in range(10):
    if i < 5:
        pass
    else:
        print(i)
