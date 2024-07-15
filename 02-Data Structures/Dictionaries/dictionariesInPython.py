'''
Dictionary notes for kabu and kwame
Dictionaries in Python
Dictionaries are unordered collections of key-value pairs. They are mutable, which means they can be changed after
creation. Keys in a dictionary must be unique and immutable
(e.g., strings, numbers, tuples), while values can be of any data type and can be duplicated.

Creating Dictionaries:
You can create dictionaries using curly braces {} or the dict() function.
'''


# Using curly braces
my_dict = {'name': 'Anish', 'age': 30, 'is_student': False}

# Using the dict() function
your_dict = dict(name='Nirja', age=12, is_student=True)

# Creating an empty dictionary
empty_dict = {}



'''Accessing Dictionary Values:

You can access/get values in a dictionary by using their corresponding keys.
'''


my_dict = {'name': 'Anish', 'age': 30, 'is_student': False}

# Accessing values
print(my_dict['name'])       # Output: Anish
print(my_dict['age'])        # Output: 30
print(my_dict['is_student']) # Output: False

# Using the get() method
print(my_dict.get('name'))   # Output: Anish
print(my_dict.get('gender')) # Output: None
print(my_dict.get('gender', 'Not specified')) # Output: Not specified

'''Modifying Dictionaries:
You can add new key-value pairs, update existing ones, or delete pairs.
'''


my_dict = {'name': 'Nirja', 'age': 25, 'is_student': True}

# Adding a new key-value pair
my_dict['gender'] = 'Female'

# Updating an existing value
my_dict['age'] = 26

# Deleting a key-value pair
del my_dict['is_student']

'''Iterating Through Dictionaries:
You can iterate through keys, values, or key-value pairs.Iterating means you can 
use for loop to go through each element of dictionary
'''


my_dict = {'name': 'Nirja', 'age': 25, 'is_student': True}

# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)








'''
Dictionary Methods:Built in methods which could be used to perform operations on dictionary.
'''

my_dict = {'name': 'Nirja', 'age': 25, 'is_student': True}

# Using pop() method
age = my_dict.pop('age')  # Removes and returns the value associated with 'age'
print(age)                # Output: 26

my_dict = {'name': 'Nirja', 'age': 25, 'is_student': True,'gender': 'Female'}

# Using popitem() method
# Removes and returns the last inserted key-value pair
last_item = my_dict.popitem()
print(last_item)          # Output: ('gender', 'Female')

#clear(): Removes all items from the dictionary.
my_dict.clear()
print(my_dict)            # Output: {}


#copy(): Returns a shallow copy of the dictionary.

my_dict = {'name': 'Nirja', 'age': 25, 'is_student': True}

# copy()
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'Nirja', 'age': 25, 'is_student': True}


'''fromkeys(iterable, value): Creates a new dictionary from the given iterable with
all keys having the specified value.'''

# fromkeys()
new_dict = dict.fromkeys(['name', 'age', 'is_student'], 'Unknown')
print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'is_student': 'Unknown'}


#get(key, default): Returns the value for the specified key, or default if the key is not found.

# get()
my_dict = {'name': 'Nirja', 'age': 25, 'is_student': True}
print(my_dict.get('name'))  # Output: Nirja
print(my_dict.get('gender'))  # Output: None
print(my_dict.get('gender', 'Not specified'))  # Output: Not specified

#items(): Returns a view object with a list of key-value pairs.

# items()
print(my_dict.items())  # Output: dict_items([('name', 'Nirja'), ('age', 25), ('is_student', True)])


#keys(): Returns a view object with a list of keys.

# keys()
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'is_student'])

'''setdefault(key, default): Returns the value for the specified key,
or sets it to default if the key is not found.
'''

# setdefault()
my_dict = {'name': 'Nirja', 'age': 25}
value = my_dict.setdefault('age', 26)
print(value)  # Output: 25
value = my_dict.setdefault('gender', 'female')
print(value)  # Output: 25
print(my_dict)  # Output: {'name': 'Nirja', 'age': 25, 'gender': 'female'}

'''update(other_dict): Updates the dictionary with key-value pairs
from another dictionary or iterable.
'''

# update()
my_dict = {'name': 'Nirja', 'age': 25}
my_dict.update({'age': 26, 'is_student': True})
print(my_dict)  # Output: {'name': 'Nirja', 'age': 26, 'is_student': True}

#values(): Returns a view object with a list of values.
# values()
print(my_dict.values())  # Output: dict_values(['Nirja', 26, True])


'''Nested Dictionaries:
Dictionaries can contain other dictionaries, which allows you to represent 
complex data structures.
'''


students = {
    'student1': {'name': 'Sula', 'age': 25, 'courses': ['Math', 'Physics']},
    'student2': {'name': 'Michel', 'age': 22, 'courses': ['English', 'History']},
}

print(students)

# Accessing nested dictionary values
print(students['student1']['name'])      # Output: Sula
print(students['student2']['courses'])   # Output: ['English', 'History']

# Adding a new entry to a nested dictionary
students['student3'] = {'name': 'Charlie', 'age': 23, 'courses': ['Biology', 'Chemistry']}
print(students)

# Modifying an existing entry in a nested dictionary
students['student1']['age'] = 26
print(students['student1'])


'''Dictionary Comprehensions:
Dictionary comprehensions provide a concise way to create dictionaries.'''


# Creating a dictionary with dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Using dictionary comprehension with condition
odd_squares = {x: x**2 for x in range(1, 11) if x % 2 != 0}
print(odd_squares)  # Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}


