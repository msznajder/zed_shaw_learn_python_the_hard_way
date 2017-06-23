## Chapter 6  Fruitful functions


## 6.1  Return values

# We have seen the return statement before, but in a fruitful function the return statement includes an expression. This statement means: “Return immediately from this function and use the following expression as a return value.”

def area(radius):
	a = math.pi * radius**2
	return a

# The expression can be arbitrarily complicated, so we could have written this function more concisely.

def area(radius):
	return math.pi * radius**2

# On the other hand, temporary variables like a can make debugging easier.

# Sometimes it is useful to have multiple return statements, one in each branch of a conditional.

def absolute_value(x):
	if x < 0:
		return -x
	else:
		return x

# Since these return statements are in an alternative conditional, only one runs.

# Code that appears after a return statement, or any other place the flow of execution can never reach, is called dead code.
# It is a good idea to ensure that every possible path through the program hits a return statement.


## 6.2  Incremental development

# To deal with increasingly complex programs, you might want to try a process called incremental development.

# Suppose you want to find the distance between two points, given by the coordinates (x1, y1) and (x2, y2).

# The first step is to consider what a distance function should look like in Python.

# Immediately you can write an outline of the function.

def distance(x1, y1, x2, y2):
	return 0.0

# To test the new function, call it with sample arguments.

distance(1, 2, 4, 5)

# I chose these values so that the horizontal distance is 3 and the vertical distance is 4; that way, the result is 5, the hypotenuse of a 3-4-5 triangle. When testing a function, it is useful to know the right answer.

# At this point we have confirmed that the function is syntactically correct, and we can start adding code to the body. A reasonable next step is to find the differences x2 − x1 and y2 − y1. The next version stores those values in temporary variables and prints them.

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	print("dx is", dx)
	print("dy is", dy)
	return 0.0

# Next we compute the sum of squares of dx and dy.

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	print("dsquared is:", dsquared)
	return 0.0

# Finally, you can use math.sqrt to compute and return the result.

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result

# The print statements we wrote are useful for debugging, but once you get the function working, you should remove them. Code like that is called scaffolding because it is helpful for building the program but is not part of the final product.

# When you start out, you should add only a line or two of code at a time. As you gain more experience, you might find yourself writing and debugging bigger chunks. Either way, incremental development can save you a lot of debugging time.

# The key aspects of the process are:
# Start with a working program and make small incremental changes. At any point, if there is an error, you should have a good idea where it is.
# Use variables to hold intermediate values so you can display and check them.
# Once the program is working, you might want to remove some of the scaffolding or consolidate multiple statements into compound expressions, but only if it does not make the program difficult to read.


## 6.4  Boolean functions

# Functions can return booleans, which is often convenient for hiding complicated tests inside functions.

def is_divisible(x, y):
	if x % y == 0:
		return True
	else:
		return False

# It is common to give boolean functions names that sound like yes/no questions; is_divisible returns either True or False to indicate whether x is divisible by y.

is_divisible(6, 4) # False


## 6.5  More recursion - study it!!!!!!!!!!!!!

# Definition of the factorial function:
# 0! = 1 
# n! = n (n−1)!

# This definition says that the factorial of 0 is 1, and the factorial of any other value, n, is n multiplied by the factorial of n−1.

# This is an recursive definition.

# If you can write a recursive definition of something, you can write a Python program to evaluate it. 

# The first step is to decide what the parameters should be. In this case it should be clear that factorial takes an integer:

# def factorial(n):

# If the argument happens to be 0, all we have to do is return 1.

def factorial(n):
	if n == 0:
		return 1

# Otherwise, and this is the interesting part, we have to make a recursive call to find the factorial of n−1 and then multiply it by n.

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

# The flow of execution for this program is similar to the flow of countdown.

factorial(3)

# Since 3 is not 0, we take the second branch and calculate the factorial of n-1...
# 	Since 2 is not 0, we take the second branch and calculate the factorial of n-1...
# 		Since 1 is not 0, we take the second branch and calculate the factorial of n-1...
# 			Since 0 equals 0, we take the first branch and return 1 without making any more recursive calls.
# 		The return value, 1, is multiplied by n, which is 1, and the result is returned.
# The return value, 1, is multiplied by n, which is 2, and the result is returned.

# The return value (2) is multiplied by n, which is 3, and the result, 6, becomes the return value of the function call that started the whole process.


# After factorial, the most common example of a recursively defined mathematical function is fibonacci, which has the following definition.

# fibonacci(0) = 0 
# fibonacci(1) = 1 
# fibonacci(n) = fibonacci(n−1) + fibonacci(n−2)

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


## 6.8  Checking types

# We can use the built-in function isinstance to verify the type of the argument. 

n = 1

if isinstance(n, int):
	print("n is an integer")

# This program demonstrates a pattern sometimes called a guardian. 


## 6.10  Glossary

# temporary variable:
# A variable used to store an intermediate value in a complex calculation.

# dead code:
# Part of a program that can never run, often because it appears after a return statement.

# incremental development:
# A program development plan intended to avoid debugging by adding and testing only a small amount of code at a time.

# scaffolding:
# Code that is used during program development but is not part of the final version.

# guardian:
# A programming pattern that uses a conditional statement to check for and handle circumstances that might cause an error.
