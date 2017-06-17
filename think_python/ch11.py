## Chapter 11  Dictionaries


## 11.1  A dictionary is a mapping


# A dictionary is like a list, but more general. 

# In a list, the indices have to be integers; in a dictionary they can be (almost) any type.

# A dictionary contains a collection of indices, which are called keys, and a collection of values. 

# Each key is associated with a single value. 

# The association of a key and a value is called a key-value pair or sometimes an item.

# In mathematical language, a dictionary represents a mapping from keys to values, so you can also say that each key “maps to” a value.

d = dict()

d['b'] = 1
d['a'] = 2

print(d)

# The order of the key-value pairs might not be the same. 

# In general, the order of items in a dictionary is unpredictable.

d['a']

# If the key isn’t in the dictionary, you get an exception.

# d['c'] # KeyError: 'four'


# The len function works on dictionaries; it returns the number of key-value pairs.

len(d) # 2

# The in operator works on dictionaries, too; it tells you whether something appears as a key in the dictionary.

"a" in d # True
"c" in d # False

# To see whether something appears as a value in a dictionary, you can use the method values, which returns a collection of values, and then use the in operator.

d_vals = d.values()
print(1 in d_vals)

# The in operator uses different algorithms for lists and dictionaries. For lists, it searches the elements of the list in order, as in Section 8.6. As the list gets longer, the search time gets longer in direct proportion.

# For dictionaries, Python uses an algorithm called a hashtable that has a remarkable property: the in operator takes about the same amount of time no matter how many items are in the dictionary. 


# 11.2  Dictionary as a collection of counters

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

print(histogram("brontosaurus"))


def histogram_get(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

print(histogram_get("brontosaurus"))


## 11.3  Looping and dictionaries


# If you use a dictionary in a for statement, it traverses the keys of the dictionary.

for key in d:
	print(key, d[key])

# To traverse the keys in sorted order, you can use the built-in function sorted.

for key in sorted(d):
	print(key, d[key])


## 11.4  Reverse lookup

# raise LookupError()

# Traceback (most recent call last):
#   File "ch11.py", line 94, in <module>
#     raise LookupError()
# LookupError

# The raise statement causes an exception; in this case it causes a LookupError, which is a built-in exception used to indicate that a lookup operation failed.

# The effect when you raise an exception is the same as when Python raises one: it prints a traceback and an error message.

# The raise statement can take a detailed error message as an optional argument.

# raise LookupError('value does not appear in the dictionary')

# Traceback (most recent call last):
#   File "ch11.py", line 107, in <module>
#     raise LookupError('value does not appear in the dictionary')
# LookupError: value does not appe


## 11.5  Dictionaries and lists


# Lists can appear as values in a dictionary.

# Lists can be values in a dictionary but they cannot be keys. 

# A dictionary is implemented using a hashtable and that means that the keys have to be hashable.

# A hash is a function that takes a value (of any kind) and returns an integer. 

# Dictionaries use these integers, called hash values, to store and look up key-value pairs.

# This system works fine if the keys are immutable. But if the keys are mutable, like lists, bad things happen. For example, when you create a key-value pair, Python hashes the key and stores it in the corresponding location. If you modify the key and then hash it again, it would go to a different location. In that case you might have two entries for the same key, or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.

# That’s why keys have to be hashable, and why mutable types like lists aren’t. The simplest way to get around this limitation is to use tuples, which we will see in the next chapter.

# Since dictionaries are mutable, they can’t be used as keys, but they can be used as values.


## 11.7  Global variables


# Variables in __main__ are sometimes called global because they can be accessed from any function. 

# Unlike local variables, which disappear when their function ends, global variables persist from one function call to the next.

verbose = True

def example1():
	if verbose:
		print("Running example1")


example1()


# If you try to reassign a global variable, you might be surprised. 

been_called = False

def example2():
	been_called = True # WRONG

example2()
print(been_called)

# But if you run it you will see that the value of been_called doesn’t change. The problem is that example2 creates a new local variable named been_called. The local variable goes away when the function ends, and has no effect on the global variable.

# To reassign a global variable inside a function you have to declare the global variable before you use it.

been_called = False

def example3():
	global been_called
	been_called = True

example3()
print(been_called)

# The global statement tells the interpreter something like, “In this function, when I say been_called, I mean the global variable; don’t create a local one.”


# Here’s an example that tries to update a global variable.

count = 0

def example4():
	count = count + 1

# example4()

# Traceback (most recent call last):
#   File "ch11.py", line 185, in <module>
#     example4()
#   File "ch11.py", line 183, in example4
#     count = count + 1
# UnboundLocalError: local variable 'count' referenced before assignment

# Python assumes that count is local, and under that assumption you are reading it before writing it. The solution, again, is to declare count global.

count = 0

def example5():
	global count
	count += 1

example5()
print(count)


# If a global variable refers to a mutable value, you can modify the value without declaring the variable.

known = {0: 0, 1: 1}


def example6():
	known[2] = 1


print(known)
example6()
print(known)

# So you can add, remove and replace elements of a global list or dictionary. 

# If you want to reassign the variable, you have to declare it.

known = {0: 0, 1: 1}


def example7():
	global known
	known = dict()

print(known)
example7()
print(known)


# Dictionaries have a method called items that returns a sequence of tuples, where each tuple is a key-value pair.

d = {'a':0, 'b':1, 'c':2}
print(d.items()) # dict_items([('c', 2), ('a', 0), ('b', 1)])

# The result is a dict_items object, which is an iterator that iterates the key-value pairs. 

# You can use it in a for loop like this.

for key, val in d.items():
	print(key, val)

# As you should expect from a dictionary, the items are in no particular order.


# You can use a list of tuples to initialize a new dictionary.
t = [('a', 0), ('b', 1)]
d = dict(t)
print(d) # {'a': 0, 'b': 1}


# Combining dict with zip yields a concise way to create a dictionary
d = dict(zip("abc", range(3)))
print(d) # {'a': 0, 'b': 1, 'c': 2}


# It is common to use tuples as keys in dictionaries (primarily because you can’t use lists).
directory = dict()
directory["michal", "sznajder"] = 111

# We could use tuple assignment to traverse this dictionary.

for first, last in directory:
	print(first, last)

## 11.9  Glossary

# mapping:
# A relationship in which each element of one set corresponds to an element of another set.

# dictionary:
# A mapping from keys to their corresponding values.

# key-value pair:
# The representation of the mapping from a key to a value.

# item:
# In a dictionary, another name for a key-value pair.

# key:
# An object that appears in a dictionary as the first part of a key-value pair.

# value:
# An object that appears in a dictionary as the second part of a key-value pair. This is more specific than our previous use of the word “value”.

# implementation:
# A way of performing a computation.

# hashtable:
# The algorithm used to implement Python dictionaries.

# hash function:
# A function used by a hashtable to compute the location for a key.

# hashable:
# A type that has a hash function. Immutable types like integers, floats and strings are hashable; mutable types like lists and dictionaries are not.

# lookup:
# A dictionary operation that takes a key and finds the corresponding value.

# reverse lookup:
# A dictionary operation that takes a value and finds one or more keys that map to it.

# raise statement:
# A statement that (deliberately) raises an exception.

# singleton:
# A list (or other sequence) with a single element.

# call graph:
# A diagram that shows every frame created during the execution of a program, with an arrow from each caller to each callee.

# memo:
# A computed value stored to avoid unnecessary future computation.

# global variable:
# A variable defined outside a function. Global variables can be accessed from any function.

# global statement:
# A statement that declares a variable name global.

# flag:
# A boolean variable used to indicate whether a condition is true.

# declaration:
# A statement like global that tells the interpreter something about a variable.
