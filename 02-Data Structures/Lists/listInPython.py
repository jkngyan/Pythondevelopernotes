'''
Lists are ordered collections of items.
Lists can contain items of different types.
Lists are mutable, meaning their elements can be changed after they are created.
Lists are defined using square brackets [].
'''

numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]


'''
You can create lists by enclosing the items in square brackets and separating them with commas.
'''
fruits = ["apple", "banana", "cherry"]

'''
You can access elements by their index. Indexing starts at 0.
'''
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Outputs: apple
print(fruits[2])  # Outputs: cherry

'''
You can modify elements by assigning a new value to a specific index.
'''

fruits[1] = "blueberry"
print(fruits)  # Outputs: ['apple', 'blueberry', 'cherry']

'''
List Functions
Adding Elements:
append(): Adds an element to the end of the list.
'''

fruits.append("orange")
print(fruits)  # Outputs: ['apple', 'blueberry', 'cherry', 'orange']

'''
insert(): Adds an element at a specified index.
'''
fruits.insert(1, "grape")
print(fruits)  # Outputs: ['apple', 'grape', 'blueberry', 'cherry', 'orange']

'''Removing Elements:
remove(): Removes the first occurrence of a specified value.
'''
fruits.remove("blueberry")
print(fruits)  # Outputs: ['apple', 'grape', 'cherry', 'orange']

'''
extend(): Adds elements from another list (or any iterable) to the end of the list
'''
fruits.extend(["kiwi", "melon"])
print(fruits)  # Outputs: ['apple', 'grape', 'blueberry', 'cherry', 'orange', 'kiwi', 'melon']


'''
pop(): Removes and returns an element at a specified index (default is the last element).
'''
fruits.pop()
print(fruits)  # Outputs: ['apple', 'grape', 'cherry']

'''
clear(): Removes all elements from the list.
'''

fruits.clear()
print(fruits)  # Outputs: []

'''
len(): Returns the number of elements in the list.
'''

print(len(fruits))  # Outputs: 5

'''
sort(): Sorts the list in ascending order.
'''

fruits.sort()
print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'date', 'fig']

'''
reverse(): Reverses the order of the list.
'''

fruits.reverse()
print(fruits)  # Outputs: ['fig', 'date', 'cherry', 'banana', 'apple']


'''
index(): Returns the index of the first occurrence of a specified value.
'''
print(fruits.index("cherry"))  # Outputs: 2

'''
Returns the number of occurrences of a specified value.
'''
print(fruits.count("apple"))  # Outputs: 1

'''
copy(): Returns a shallow copy of the list
'''

fruits_copy = fruits.copy()
print(fruits_copy)  # Outputs: ['fig', 'date', 'cherry', 'banana', 'apple']


'''
List Slicing:
Slicing allows you to access a subset of the list.
'''

fruits = ["apple", "banana", "cherry", "date", "fig"]
print(fruits[1:4])  # Outputs: ['banana', 'cherry', 'date']
print(fruits[:3])   # Outputs: ['apple', 'banana', 'cherry']
print(fruits[2:])   # Outputs: ['cherry', 'date', 'fig']
print(fruits[-3:])  # Outputs: ['cherry', 'date', 'fig']


'''
List Comprehensions:
List comprehensions provide a concise way to create lists.
They consist of brackets containing an expression followed by a for clause, and optionally an if clause.
List comprehensions can include conditional logic.
'''

squares = [x**2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]



'''Nested Lists:

Lists can contain other lists as elements, creating nested lists.
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
Accessing elements in nested lists:
'''

print(matrix[0][1])  # Outputs: 2


