## Chapter 12  Tuples


## 12.1  Tuples are immutable

# A tuple is a sequence of values. 

# The values can be any type, and they are indexed by integers, so in that respect tuples are a lot like lists. 

# The important difference is that tuples are immutable.

t = 'a', 'b', 'c'

# Although it is not necessary, it is common to enclose tuples in parentheses.

t = ('a', 'b', 'c')

# To create a tuple with a single element, you have to include a final comma.

t1 = 'a',

# A value in parentheses is not a tuple.

t2 = ('a')
type(t2) # <class 'str'>


# Another way to create a tuple is the built-in function tuple. 

# With no argument, it creates an empty tuple.
t3 = tuple()


# If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of the sequence.
t = tuple("lupins")
t # ('l', 'u', 'p', 'i', 'n', 's')


# The bracket operator indexes an element.

t[0]

# The slice operator selects a range of elements.
t[1:3]


# If you try to modify one of the elements of the tuple, you get an error.
# t[0] = 1
# Traceback (most recent call last):
#   File "ch12.py", line 48, in <module>
#     t[0] = 1
# TypeError: 'tuple' object does not support item assignment

# Because tuples are immutable, you can’t modify the elements. 


# But you can replace one tuple with another.

t = ('A',) + t[1:]
t # ('A', 'b', 'c', 'd', 'e')

# This statement makes a new tuple and then makes t refer to it.


# The relational operators work with tuples and other sequences; Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next elements, and so on, until it finds elements that differ. Subsequent elements are not considered (even if they are really big).
(0, 1, 2) < (0, 3, 4) # True
(0, 1, 20000000) < (0, 3, 4) # True


## 12.2  Tuple assignment


a = 1
b = 2

a, b = b, a

a, b = 1, 2

# a, b = 1, 2, 3 # error


## 12.3  Tuples as return values

# Strictly speaking, a function can only return one value, but if the value is a tuple, the effect is the same as returning multiple values. 

def min_max(t):
	return min(t), max(t)


## 12.4  Variable-length argument tuples

# Functions can take a variable number of arguments. 

# A parameter name that begins with * gathers arguments into a tuple.

def print_all(*args):
	print(args)


# The complement of gather is scatter. 

# If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the * operator. 
t = (7, 9)

# divmod(t)

# Traceback (most recent call last):
#   File "ch12.py", line 105, in <module>
#     divmod(t)
# TypeError: divmod expected 2 arguments, got 1

divmod(*t)


# Many of the built-in functions use variable-length argument tuples. For example, max and min can take any number of arguments.

max(1, 2, 3)

# But sum does not.

# sum(1, 2, 3)

# Traceback (most recent call last):
#   File "ch12.py", line 122, in <module>
#     sum(1, 2, 3)
# TypeError: sum expected at most 2 arguments, got 3


## 12.5  Lists and tuples


# zip is a built-in function that takes two or more sequences and returns a list of tuples where each tuple contains one element from each sequence.

s = "abc"
l = [0, 1, 2]
z = zip(s, t)

# The result is a zip object that knows how to iterate through the pairs. 

# A zip object is a kind of iterator, which is any object that iterates through a sequence. Iterators are similar to lists in some ways, but unlike lists, you can’t use an index to select an element from an iterator.

list(z) # [('a', 0), ('b', 1), ('c', 2)]

# The result is a list of tuples; in this example, each tuple contains a character from the string and the corresponding element from the list.

# If the sequences are not the same length, the result has the length of the shorter one.

list(zip("Anne", "Elk")) # [('A', 'E'), ('n', 'l'), ('n', 'k')]

# You can use tuple assignment in a for loop to traverse a list of tuples.

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
	print(letter, number)


# You can traverse two sequences at the same time.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
for x, y in zip(l1, l2):
	print(x, y)


# Traverse the elements of a sequence and their indices, you can use the built-in function enumerate.

for idx, val in enumerate("abc"):
	print(idx, val)

# The result from enumerate is an enumerate object, which iterates a sequence of pairs. 
# Each pair contains an index (starting from 0) and an element from the given sequence. 


## 12.9  Glossary

# tuple:
# An immutable sequence of elements.

# tuple assignment:
# An assignment with a sequence on the right side and a tuple of variables on the left. The right side is evaluated and then its elements are assigned to the variables on the left.

# gather:
# The operation of assembling a variable-length argument tuple.

# scatter:
# The operation of treating a sequence as a list of arguments.

# zip object:
# The result of calling a built-in function zip; an object that iterates through a sequence of tuples.

# iterator:
# An object that can iterate through a sequence, but which does not provide list operators and methods.

# data structure:
# A collection of related values, often organized in lists, dictionaries, tuples, etc.

# shape error:
# An error caused because a value has the wrong shape; that is, the wrong type or size.
