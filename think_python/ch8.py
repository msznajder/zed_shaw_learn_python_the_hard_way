## Chapter 8  Strings

# Strings are not like integers, floats, and booleans. 

# A string is a sequence, which means it is an ordered collection of other values. 


## 8.1  A string is a sequence

# A string is a sequence of characters. 

# You can access the characters one at a time with the bracket operator.

fruit = "banana"
letter = fruit[1]

# The expression in brackets is called an index. 

# The index indicates which character in the sequence you want (hence the name).

# As an index you can use an expression that contains variables and operators.

i = 1
fruit[i] # "a"
fruit[i+1] # "n"

# But the value of the index has to be an integer - therwise you get an error.

# letter = fruit[1.5] # TypeError: string indices must be integers


## 8.3  Traversal with a for loop

s = "Abba"
for letter in s:
	print(letter)


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	if letter == "O" or letter == "Q":
		print(letter + "u" + suffix)
	else:
		print(letter + suffix)

fruit = "banana"
print(fruit[3:3])

# An empty string contains no characters and has length 0, but other than that, it is the same as any other string.


## 8.5  Strings are immutable

greeting = "Hello, world!"
# greeting[0] = "J" # TypeError: 'str' object does not support item assignment

# The reason for the error is that strings are immutable, which means you can’t change an existing string. 

# The best you can do is create a new string that is a variation on the original.

greeting = "Hello, world!"
new_greeting = "J" + greeting[1:]
print(new_greeting) # "Jello, world!"

# This example concatenates a new first letter onto a slice of greeting. It has no effect on the original string.


## 8.8  String methods

# Strings provide methods that perform a variety of useful operations.

# A method is similar to a function—it takes arguments and returns a value—but the syntax is different. 

# For example, the method upper takes a string and returns a new string with all uppercase letters.

# Instead of the function syntax upper(word), it uses the method syntax word.upper().

word = "banana"
new_word = word.upper()
print(new_word) # "BANANA"

# This form of dot notation specifies the name of the method, upper, and the name of the string to apply the method to, word. 
# The empty parentheses indicate that this method takes no arguments.

# A method call is called an invocation; in this case, we would say that we are invoking upper on word.

word = "banana"
index = word.find("a")
print(index) # 1

# In this example, we invoke find on word and pass the letter we are looking for as a parameter.

# Actually, the find method is more general than our function; it can find substrings, not just characters.

word.find("na") # 2

# By default, find starts at the beginning of the string, but it can take a second argument, the index where it should start.

word.find("na", 3) # 4

# This is an example of an optional argument; find can also take a third argument, the index where it should stop.
# Searching up to, but not including.
word.find("na", 2, 5) # 2

# It returns -1 when nothing is found.
word.find("na", 0, 2) # -1


## 8.10  String comparison

# The relational operators work on strings. To see if two strings are equal.
print(word == "banana") # True
print(word == "Banana") # False


## 8.12  Glossary

# object:
# Something a variable can refer to. For now, you can use “object” and “value” interchangeably.

# sequence:
# An ordered collection of values where each value is identified by an integer index.

# item:
# One of the values in a sequence.

# index:
# An integer value used to select an item in a sequence, such as a character in a string. In Python indices start from 0.

# slice:
# A part of a string specified by a range of indices.

# empty string:
# A string with no characters and length 0, represented by two quotation marks.

# immutable:
# The property of a sequence whose items cannot be changed.

# traverse:
# To iterate through the items in a sequence, performing a similar operation on each.

# search:
# A pattern of traversal that stops when it finds what it is looking for.

# counter:
# A variable used to count something, usually initialized to zero and then incremented.

# invocation:
# A statement that calls a method.

# optional argument:
# A function or method argument that is not required.
