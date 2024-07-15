'''Tuples:

Tuples are ordered collections of items, similar to lists.
Unlike lists, tuples are immutable, meaning their elements cannot be changed after they are created.
Tuples are defined using parentheses ()
'''

numbers = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)

'''
Creating Tuples:
You can create tuples by enclosing the items in parentheses and separating them with commas.
'''

fruits = ("apple", "banana", "cherry")

'''
Tuples can also be created without parentheses by simply separating the items with commas.
'''

fruits = "apple", "banana", "cherry"

'''
To create a tuple with a single element, you need to include a trailing comma.
'''

single_element_tuple = ("apple",)

'''
Accessing Elements:
You can access elements by their index. Indexing starts at 0
'''
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Outputs: apple
print(fruits[2])  # Outputs: cherry


'''
Slicing Tuples:
Slicing allows you to access a subset of the tuple.
'''

fruits = ("apple", "banana", "cherry", "date", "fig")
print(fruits[1:4])  # Outputs: ('banana', 'cherry', 'date')
print(fruits[:3])   # Outputs: ('apple', 'banana', 'cherry')
print(fruits[2:])   # Outputs: ('cherry', 'date', 'fig')
print(fruits[-3:])  # Outputs: ('cherry', 'date', 'fig')

'''
Unpacking Tuples:
You can unpack tuples into individual variables.
'''

fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)  # Outputs: apple
print(b)  # Outputs: banana
print(c)  # Outputs: cherry

for (a,b,c) in fruits:
    print(a)
    print(b)
    print(c)
