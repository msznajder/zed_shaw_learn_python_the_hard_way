"""
Exercise 1

Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
"""

def right_justify(s):
	print((70 - len(s)) * " " + s)


right_justify("abba")


"""
Exercise 2

A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
    f()
    f()
Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
    print('spam')

do_twice(print_spam)
Type this example into a script and test it.
Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
Copy the definition of print_twice from earlier in this chapter to your script.
Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
"""


def print_spam():
	print("spam")


def print_anything(val):
	print(val)


def do_twice(f, val):
	f(val)
	f(val)


def do_four(f, val):
	do_twice(f, val)
	do_twice(f, val)


do_twice(print_anything, "ha!")

do_four(print_anything, "hi!")


"""
Exercise 3

Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -'.
A print statement with no argument ends the current line and goes to the next line.
"""


def print_square():
	print("+" + " -" * 4 + " +" + " -" * 4 + " +")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("+" + " -" * 4 + " +" + " -" * 4 + " +")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("/" + " " * 9 + "/" + " " * 9 + "/")
	print("+" + " -" * 4 + " +" + " -" * 4 + " +")


print_square()
