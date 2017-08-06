## 19.1  Conditional expressions

import math

x = 5

y = math.log(x) if x > 0 else float('nan')

# Recursive functions can sometimes be rewritten using conditional expressions. 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial(n):
	return 1 if n == 0 else n * factorial(n-1)

# In general, you can replace a conditional statement with a conditional expression if both branches contain simple expressions that are either returned or assigned to the same variable.


## 19.2  List comprehensions

t = "abba"

# mapping
res = []
for s in t:
    res.append(s.capitalize())

# shorter
[s.capitalize() for s in t]


# filtering
res = []
for s in t:
    if s.isupper():
        res.append(s)

[s for s in t if s.isupper()]

# List comprehensions are concise and easy to read, at least for simple expressions. And they are usually faster than the equivalent for loops, sometimes much faster. 

# List comprehensions are harder to debug because you can’t put a print statement inside the loop. I suggest that you use them only if the computation is simple enough that you are likely to get it right the first time. And for beginners that means never.

## 19.3  Generator expressions

# Generator expressions are similar to list comprehensions, but with parentheses instead of square brackets
g = (x**2 for x in range(5))
g
# <generator object <genexpr> at 0x7f4c45a786c0>

# The result is a generator object that knows how to iterate through a sequence of values. But unlike a list comprehension, it does not compute the values all at once; it waits to be asked. The built-in function next gets the next value from the generator.
next(g) # 0
next(g) # 1

# When you get to the end of the sequence, next raises a StopIteration exception. 


# You can also use a for loop to iterate through the values.
for val in g:
	print(val)

# The generator object keeps track of where it is in the sequence, so the for loop picks up where next left off.


# Once the generator is exhausted, it continues to raise StopException:
# next(g) # StopIteration


# Generator expressions are often used with functions like sum, max, and min.
sum(x**2 for x in range(5)) # 30


# Set comprehensions.
g = {x**2 for x in range(5)}


## 19.4  any and all

# Python provides a built-in function, any, that takes a sequence of boolean values and returns True if any of the values are True.
any([False, False, True]) # True

# It is often used with generator expressions.
any(letter == "t" for letter in "monty") # True

# We could write avoids.
def avoids(word, forbidden):
	return not any(letter in forbidden for letter in word)

# The function almost reads like English, “word avoids forbidden if there are not any forbidden letters in word.”

# Using any with a generator expression is efficient because it stops immediately if it finds a True value, so it doesn’t have to evaluate the whole sequence.


# Python provides another built-in function, all, that returns True if every element of the sequence is True.


## 19.5  Sets

 # A set, that behaves like a collection of dictionary keys with no values.
 # Adding elements to a set is fast; so is checking membership. And sets provide methods and operators to compute common set operations.

 # Set subtraction is available as a method called difference or as an operator, -.
print(set("abba") - set("afv"))


## 19.6  Counters

# A Counter is like a set, except that if an element appears more than once, the Counter keeps track of how many times it appears.

# Counter is defined in a standard module called collections, so you have to import it. You can initialize a Counter with a string, list, or anything else that supports iteration.
from collections import Counter
count = Counter("parrot")
count # Counter({'r': 2, 't': 1, 'o': 1, 'p': 1, 'a': 1})

# Counters behave like dictionaries in many ways; they map from each key to the number of times it appears. As in dictionaries, the keys have to be hashable.
# Unlike dictionaries, Counters don’t raise an exception if you access an element that doesn’t appear. Instead, they return 0.

count["d"] # 0

# Counters provide methods and operators to perform set-like operations, including addition, subtraction, union and intersection. 

# And they provide an often-useful method, most_common, which returns a list of value-frequency pairs, sorted from most common to least

count = Counter("parrot")
for val, freq in count.most_common(3):
	print(val, freq)

# r 2
# p 1
# a 1


## 19.7  defaultdict

# The collections module also provides defaultdict, which is like a dictionary except that if you access a key that doesn’t exist, it can generate a new value on the fly.
# When you create a defaultdict, you provide a function that’s used to create new values. A function used to create objects is sometimes called a factory. The built-in functions that create lists, sets, and other types can be used as factories.
from collections import defaultdict
d = defaultdict(list)
# Notice that the argument is list, which is a class object, not list(), which is a new list. 

# The function you provide doesn’t get called unless you access a key that doesn’t exist.
t = d["new key"]
t # []

# The new list, which we’re calling t, is also added to the dictionary. So if we modify t, the change appears in d.

t.append("new value")
d # defaultdict(<class 'list'>, {'new key': ['new value']})

# If you are making a dictionary of lists, you can often write simpler code using defaultdict.


## 19.8  Named tuples

# Many simple objects are basically collections of related values. 

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

# The first argument is the name of the class you want to create. The second is a list of the attributes Point objects should have, as strings. The return value from namedtuple is a class object.
Point # <class '__main__.Point'>

# Point automatically provides methods like __init__ and __str__ so you don’t have to write them.

# To create a Point object, you use the Point class as a function:

p = Point(1, 2)
p # Point(x=1, y=2)

# The init method assigns the arguments to attributes using the names you provided. The str method prints a representation of the Point object and its attributes.


# You can access the elements of the named tuple by name.
p.x, p.y # (1, 2)

# But you can also treat a named tuple as a tuple.
p[0], p[1] # (1, 2)

x, y = p
x, y # (1, 2)


## 19.9  Gathering keyword args

# Standard gather.
def printall(*args):
    print(args)

printall(1, 2.0, '3') # (1, 2.0, '3')

# The * operator doesn’t gather keyword arguments.
# printall(1, 2.0, third='3') # TypeError: printall() got an unexpected keyword argument 'third'


# To gather keyword arguments, you can use the ** operator.

def printall(*args, **kwargs):
	print(args, kwargs)

# You can call the keyword gathering parameter anything you want, but kwargs is a common choice. The result is a dictionary that maps keywords to values.

printall(1, 2.0, third='3') # (1, 2.0) {'third': '3'}


# You can use the scatter operator with a dictionary of keywords and values.

d = dict(x=1, y=2)
# **d # x=1, y=2


## 19.10  Glossary:

# conditional expression:
# An expression that has one of two values, depending on a condition.

# list comprehension:
# An expression with a for loop in square brackets that yields a new list.

# generator expression:
# An expression with a for loop in parentheses that yields a generator object.

# multiset:
# A mathematical entity that represents a mapping between the elements of a set and the number of times they appear.

# factory:
# A function, usually passed as a parameter, used to create objects.
