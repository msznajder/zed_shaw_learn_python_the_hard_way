## Chapter 10  Lists


## 10.1  A list is a sequence


# Like a string, a list is a sequence of values. 

# In a string, the values are characters; in a list, they can be any type. 

# The values in a list are called elements or sometimes items.

# There are several ways to create a list.

l1 = [10, 20, 30, 40]
l2 = ["s1", "s2", "s3"]
l3 = ["spam", 2, 3.0, [10, 20]]

# A list within another list is nested.

# A list that contains no elements is called an empty list.
[]


## 10.2  Lists are mutable

# The syntax for accessing the elements of a list is the same as for accessing the characters of a string—the bracket operator.

l1[0] # 10

# Unlike strings, lists are mutable.

numbers = [42, 123]
numbers[1] == 5
numbers # [42, 5]

# Check list for membership.

cheeses = ["Cheddar", "Edam", "Gouda"]
"Edam" in cheeses # True
"Brie" in cheeses # False


## 10.3  Traversing a list

# The most common way to traverse the elements of a list is with a for loop. 

for cheese in cheeses:
	print(cheese)

# If you want to write or update the elements, you need the indices. 

for idx, val in enumerate(numbers):
	numbers[idx] = numbers[idx] * 2
print(numbers) # [84, 246]

# A for loop over an empty list never runs the body.

for x in []:
	print("Never executes.")

# Although a list can contain another list, the nested list still counts as a single element.
nested_list = ["spam", 1, ["Brie", "Gouda"], [1, 2, 3]]
len(nested_list) # 4


## 10.4  List operations

# The + operator concatenates lists.

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c # [1, 2, 3, 4, 5, 6]

# The * operator repeats a list a given number of times.
[0] * 4 # [0, 0, 0, 0]
[1, 2, 3] * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Since lists are mutable, it is often useful to make a copy before performing operations that modify lists.
a[:] # [1, 2, 3]

# A slice operator on the left side of an assignment can update multiple elements.
t = ["a", "b", "c", "d", "e", "f"]
t[1:3] = ["x", "y"]
t # ["a", "x", "y", "d", "e", "f"]


## 10.6  List methods

t = ['a', 'b', 'c']
t.append('d')
t # 'a', 'b', 'c', 'd']

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
t1 # ['a', 'b', 'c', 'd', 'e']

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
t # ['a', 'b', 'c', 'd', 'e']

# Most list methods are void; they modify the list and return None. 


## 10.7  Map, filter and reduce


# To add up all the numbers in a list, you can use a loop like this.

def add_all(t):
	total = 0
	for x in t:
		total += x
	return total

t = [1, 2, 3]
print(add_all(t)) # 6

# An operation like this that combines a sequence of elements into a single value is sometimes called reduce.


# Sometimes you want to traverse one list while building another. For example, the following function takes a list of strings and returns a new list that contains capitalized strings.

def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

t = ['a', 'b', 'c']
print(capitalize_all(t)) # ['A', 'B', 'C']

# An operation like capitalize_all is sometimes called a map because it “maps” a function (in this case the method capitalize) onto each of the elements in a sequence.


# Another common operation is to select some of the elements from a list and return a sublist. For example, the following function takes a list of strings and returns a list that contains only the uppercase strings.

def only_upper(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
	return res

t = ['a', 'B', 'C']
print(only_upper(t))

# An operation like only_upper is called a filter because it selects some of the elements and filters out the others.

# Most common list operations can be expressed as a combination of map, filter and reduce.


## 10.8  Deleting elements

# There are several ways to delete elements from a list. 

# If you know the index of the element you want, you can use pop.

t = ['a', 'b', 'c']
x = t.pop(1)
t # ['a', 'c']
x # 'b'

# pop modifies the list and returns the element that was removed. 

# If you don’t provide an index, it deletes and returns the last element.

# If you don’t need the removed value, you can use the del operator.

t = ['a', 'b', 'c']
del t[1]
t # ['a', 'c']

# If you know the element you want to remove (but not the index), you can use remove.

t = ['a', 'b', 'c']
t.remove('b')
t # ['a', 'c']

# The return value from remove is None.

# To remove more than one element, you can use del with a slice index.

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
t # ['a', 'f']


## 10.9  Lists and strings

# A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string.

# To convert from a string to a list of characters, you can use list.

s = 'spam'
t = list(s)
t # ['s', 'p', 'a', 'm']

# Because list is the name of a built-in function, you should avoid using it as a variable name. I also avoid l because it looks too much like 1. So that’s why I use t.

# The list function breaks a string into individual letters. If you want to break a string into words, you can use the split method.

s = 'pining for the fjords'
t = s.split()
t # ['pining'. 'for', 'the', 'fjords']

# An optional argument called a delimiter specifies which characters to use as word boundaries. 

s = "spam-spam-spam"
delimeter = '-'
t = s.split(delimeter)
t # ["spam", "spam", "spam"]

# join is the inverse of split. 

# It takes a list of strings and concatenates the elements. 

# join is a string method, so you have to invoke it on the delimiter and pass the list as a parameter.

t = ['pining', 'for', 'the', 'fjords']
delimeter = ' '
s = delimeter.join(t)
s # 'pining for the fjords'

# In this case the delimiter is a space character, so join puts a space between words. 

# To concatenate strings without spaces, you can use the empty string, '', as a delimiter.


# 10.10  Objects and values

a = "banana"
b = "banana"
a is b # True

# Python only created one string object, and both a and b refer to it. 

a = [1, 2, 3]
b = [1, 2, 3]
a is b # False

# When you create two lists, you get two objects.

# In this case we would say that the two lists are equivalent, because they have the same elements, but not identical, because they are not the same object. If two objects are identical, they are also equivalent, but if they are equivalent, they are not necessarily identical.


# Until now, we have been using “object” and “value” interchangeably, but it is more precise to say that an object has a value. 

# If you evaluate [1, 2, 3], you get a list object whose value is a sequence of integers. 

# If another list has the same elements, we say it has the same value, but it is not the same object.


## 10.11  Aliasing


# If a refers to an object and you assign b = a, then both variables refer to the same object.

a = [1, 2, 3]
b = a
b is a # True

# The association of a variable with an object is called a reference. 

# In this example, there are two references to the same object.

# An object with more than one reference has more than one name, so we say that the object is aliased.

# If the aliased object is mutable, changes made with one alias affect the other.

b[0] = 42
a # [42, 2, 3]

# Although this behavior can be useful, it is error-prone. 

# In general, it is safer to avoid aliasing when you are working with mutable objects.

# For immutable objects like strings, aliasing is not as much of a problem.

a = "banana"
b = "banana"

# It almost never makes a difference whether a and b refer to the same string or not.


## 10.12  List arguments


# When you pass a list to a function, the function gets a reference to the list. 

# If the function modifies the list, the caller sees the change

def delete_head(t):
	del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
letters # ['b', 'c']


# It is important to distinguish between operations that modify lists and operations that create new lists. 

# For example, the append method modifies a list, but the + operator creates a new list.

t1 = [1, 2]
t2 = t1.append(3)
t1 # [1, 2, 3]
t2 # None

# The return value from append is None.


# Here’s an example using the + operator.

t3 = t1 + [4]
t1 # [1, 2, 3]
t3 # [1, 2, 3, 4]

# The result of the operator is a new list, and the original list is unchanged.



# This difference is important when you write functions that are supposed to modify lists. 

# For example, this function does not delete the head of a list.

def bad_delete_head(t):
	t = t[1:] # WRONG

# The slice operator creates a new list and the assignment makes t refer to it, but that doesn’t affect the caller.

t4 = [1, 2, 3]
bad_delete_head(t4)
t4 # [1, 2, 3]

# At the beginning of bad_delete_head, t and t4 refer to the same list. At the end, t refers to a new list, but t4 still refers to the original, unmodified list.

# An alternative is to write a function that creates and returns a new list. For example, tail returns all but the first element of a list.

def tail(t):
	return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
rest # ['b', 'c']


## 10.13  Debugging

# Most list methods modify the argument and return None. This is the opposite of the string methods, which return a new string and leave the original alone.
word = "word\n"

word = word.strip()

t = [2, 1, 3]
t = t.sort() # WRONG

# Because sort returns None, the next operation you perform with t is likely to fail.


# Pick an idiom and stick with it.

# Part of the problem with lists is that there are too many ways to do things. 

# For example, to remove an element from a list, you can use pop, remove, del, or even a slice assignment.

# To add an element, you can use the append method or the + operator. Assuming that t is a list and x is a list element, these are correct

t = [1, 2, 3]

t.append(1)
t = t + [1]
t += [1]

# And these are wrong:

# t.append([1])
# t = append(1)
# t + [1]
# t = t + 1


# Make copies to avoid aliasing.

# If you want to use a method like sort that modifies the argument, but you need to keep the original list as well, you can make a copy.

t = [3, 1, 2]
t2 = t[:]
t2.sort()
t # [3, 1, 2]
t2 # [1, 2, 3]

# In this example you could also use the built-in function sorted, which returns a new, sorted list and leaves the original alone.

t2 = sorted(t)
t # [3, 2, 1]
t2 # [1, 2, 3]


## 10.14  Glossary


# list:
# A sequence of values.

# element:
# One of the values in a list (or other sequence), also called items.

# nested list:
# A list that is an element of another list.

# accumulator:
# A variable used in a loop to add up or accumulate a result.

# augmented assignment:
# A statement that updates the value of a variable using an operator like +=.

# reduce:
# A processing pattern that traverses a sequence and accumulates the elements into a single result.

# map:
# A processing pattern that traverses a sequence and performs an operation on each element.

# filter:
# A processing pattern that traverses a list and selects the elements that satisfy some criterion.

# object:
# Something a variable can refer to. An object has a type and a value.

# equivalent:
# Having the same value.

# identical:
# Being the same object (which implies equivalence).

# reference:
# The association between a variable and its value.

# aliasing:
# A circumstance where two or more variables refer to the same object.

# delimiter:
# A character or string used to indicate where a string should be split.
