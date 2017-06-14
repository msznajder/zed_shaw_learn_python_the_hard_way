## Chapter 3  Functions

# A function is a named sequence of statements that performs a computation. 


## 3.1  Function calls

# We have already seen one example of a function call.

type(42)

# The name of the function is type. The expression in parentheses is called the argument of the function. The result, for this function, is the type of the argument.

# It is common to say that a function “takes” an argument and “returns” a result. The result is also called the return value.


## 3.2  Math functions

# A module is a file that contains a collection of related functions.

# Before we can use the functions in a module, we have to import it with an import statement.

import math

# This statement creates a module object named math.

# The module object contains the functions and variables defined in the module. To access one of the functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period). This format is called dot notation.
ration = 2 / 20
decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)

# The expression math.pi gets the variable pi from the math module. Its value is a floating-point approximation of π, accurate to about 15 digits.


## 3.3  Composition

# So far, we have looked at the elements of a program—variables, expressions, and statements—in isolation, without talking about how to combine them.

# One of the most useful features of programming languages is their ability to take small building blocks and compose them. For example, the argument of a function can be any kind of expression, including arithmetic operator.

x = math.sin(degrees / 360.0 * 2 * math.pi)

# Almost anywhere you can put a value, you can put an arbitrary expression, with one exception: the left side of an assignment statement has to be a variable name. 

minutes = hours * 60
# hours * 60 = minutes


## 3.4  Adding new functions

# A function definition specifies the name of a new function and the sequence of statements that run when the function is called.

def print_lirycs():
	print("Ha!")

# def is a keyword that indicates that this is a function definition. The name of the function is print_lyrics. The rules for function names are the same as for variable names: letters, numbers and underscore are legal, but the first character can’t be a number. You can’t use a keyword as the name of a function, and you should avoid having a variable and a function with the same name.

# The first line of the function definition is called the header; the rest is called the body. The header has to end with a colon and the body has to be indented. By convention, indentation is always four spaces. The body can contain any number of statements.

# Defining a function creates a function object, which has type function.
print(print_lirycs)
print(type(print_lirycs))

# The syntax for calling the new function is the same as for built-in functions:

print_lyrics()

# Once you have defined a function, you can use it inside another function.

def repeat_lirycs():
	print_lyrics()
	print_lyrics()

# And then call repeat_lyrics.

repeat_lyrics()

# This program contains two function definitions: print_lyrics and repeat_lyrics. Function definitions get executed just like other statements, but the effect is to create function objects. The statements inside the function do not run until the function is called, and the function definition generates no output.


## 3.6  Flow of execution

# To ensure that a function is defined before its first use, you have to know the order statements run in, which is called the flow of execution.

# Execution always begins at the first statement of the program. Statements are run one at a time, in order from top to bottom.

# Function definitions do not alter the flow of execution of the program, but remember that statements inside the function don’t run until the function is called.

# A function call is like a detour in the flow of execution. Instead of going to the next statement, the flow jumps to the body of the function, runs the statements there, and then comes back to pick up where it left off.


## 3.7  Parameters and arguments

# Some of the functions we have seen require arguments. 

# Inside the function, the arguments are assigned to variables called parameters. Here is a definition for a function that takes an argument.

def print_twice(bruce):
	print(bruce)
	print(bruce)

# This function assigns the argument to a parameter named bruce. When the function is called, it prints the value of the parameter (whatever it is) twice.

# The argument is evaluated before the function is called.
print_twice("Spam" * 4)

# You can also use a variable as an argument.
michael = "Eric, the half bee."
print_twice(michael)

# The name of the variable we pass as an argument (michael) has nothing to do with the name of the parameter (bruce)


## 3.8  Variables and parameters are local

# When you create a variable inside a function, it is local, which means that it only exists inside the function. 

def cat_twice(part1, part2):
	cat = part1 + part2
	print_twice(cat)

cat_twice("ko", "t")

# When cat_twice terminates, the variable cat is destroyed.

# Parameters are also local. 


## 3.10  Fruitful functions and void functions

# Fruitful functions return something. Void functions don't return anything.

# When you call a fruitful function, you almost always want to do something with the result; for example, you might assign it to a variable or use it as part of an expression.

x = math.cos(radians)

# Void functions might display something on the screen or have some other effect, but they don’t have a return value. If you assign the result to a variable, you get a special value called None.

result = print_twice("Bing")
print(result)

# The value None is not the same as the string 'None'. It is a special value that has its own type.
print(type(None))


## 3.11  Why functions?

# Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read and debug.

# Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place.

# Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.

# Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.


## 3.13  Glossary

# function:
# A named sequence of statements that performs some useful operation. Functions may or may not take arguments and may or may not produce a result.

# function definition:
# A statement that creates a new function, specifying its name, parameters, and the statements it contains.

# function object:
# A value created by a function definition. The name of the function is a variable that refers to a function object.

# header:
# The first line of a function definition.

# body:
# The sequence of statements inside a function definition.

# parameter:
# A name used inside a function to refer to the value passed as an argument.

# function call:
# A statement that runs a function. It consists of the function name followed by an argument list in parentheses.

# argument:
# A value provided to a function when the function is called. This value is assigned to the corresponding parameter in the function.

# local variable:
# A variable defined inside a function. A local variable can only be used inside its function.

# return value:
# The result of a function. If a function call is used as an expression, the return value is the value of the expression.

# fruitful function:
# A function that returns a value.

# void function:
# A function that always returns None.

# None:
# A special value returned by void functions.
 
# module:
# A file that contains a collection of related functions and other definitions.

# import statement:
# A statement that reads a module file and creates a module object.

# module object:
# A value created by an import statement that provides access to the values defined in a module.

# dot notation:
# The syntax for calling a function in another module by specifying the module name followed by a dot (period) and the function name.

# composition:
# Using an expression as part of a larger expression, or a statement as part of a larger statement.

# flow of execution:
# The order statements run in.

# stack diagram:
# A graphical representation of a stack of functions, their variables, and the values they refer to.

# frame:
# A box in a stack diagram that represents a function call. It contains the local variables and parameters of the function.

# traceback:
# A list of the functions that are executing, printed when an exception occurs.
