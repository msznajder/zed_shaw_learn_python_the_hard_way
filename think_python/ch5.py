## Chapter 5  Conditionals and recursion

## 5.1 Floor division and modulus

# The floor division operator, //, divides two numbers and rounds down to an integer. 

minutes = 105 / 60 # 1.75

minutes = 105 // 60 # 1

# To get the remainder use modulus operator.

remainder = 105 % 60 # 45

# The modulus operator is more useful than it seems. 
# For example, you can check whether one number is divisible by another.

if 20 % 5:
	print("Is divisible by 5.")

# You can extract the right-most digit or digits from a number. 

152 % 10 # 2
152 % 100 # 52


## 5.2  Boolean expressions

# A boolean expression is an expression that is either true or false. 

# True and False are special values that belong to the type bool; they are not strings.

type(True) # <class 'bool'>


## 5.3  Logical operators

# The operands of the logical operators should be boolean expressions, but Python is not very strict. Any nonzero number is interpreted as True.

42 and True # True

# This flexibility can be useful, but there are some subtleties to it that might be confusing. You might want to avoid it (unless you know what you are doing).


## 5.4  Conditional execution

# Conditional statements give us the ability to check conditions and change the behavior of the program accordingly.

if 2 > 0:
	print("2 is bigger than zero")

# The boolean expression after if is called the condition.

# There is no limit on the number of statements that can appear in the body, but there has to be at least one. Occasionally, it is useful to have a body with no statements (usually as a place keeper for code you haven’t written yet). 

if 2 < 0:
	pass


## 5.5  Alternative execution

if 2 % 2 == 0:
	print("x is even")
else:
	print("x is odd")

# The alternatives are called branches, because they are branches in the flow of execution.


## 5.6  Chained conditionals

# Sometimes there are more than two possibilities and we need more than two branches. One way to express a computation like that is a chained conditional.

if 2 < 3:
	print("2 is smaller than 3")
elif 3 < 2:
	print("3 is smaller than 2")
else:
	print("2 and 3 are equal")

# elif is an abbreviation of “else if”. 

# Again, exactly one branch will run. 

# There is no limit on the number of elif statements. 

# If there is an else clause, it has to be at the end, but there doesn’t have to be one.

choice = "a"

if choice == "a":
	print("a")
elif choice == "b":
	print("b")
elif choice == "c":
	print("c")

# Each condition is checked in order. 

# If the first is false, the next is checked, and so on. If one of them is true, the corresponding branch runs and the statement ends. Even if more than one condition is true, only the first true branch runs.


## 5.7  Nested conditionals

if 2 == 3:
	print("2 and 3 are equal.")
else:
	if 2 < 3:
		print("2 is less than 3")
	else:
		print("x is greater than y")

# Nested conditionals become difficult to read very quickly. It is a good idea to avoid them when you can.

# We can rewrite the following code using a single conditional.

x = 2

if 0 < x and x < 10:
	print("x is a positive and single-digit number.")

# For this kind of condition, Python provides a more concise option.

if 0 < x < 10:
	print("x is a positive single-digit number.")


## 5.8  Recursion

# It is legal for one function to call another; it is also legal for a function to call itself. It may not be obvious why that is a good thing, but it turns out to be one of the most magical things a program can do.

def countdown(n):
	if n <= 0:
		print("Blastoff")
	else:
		print(n)
		countdown(n-1)

# What happens if we call this function like this?

countdown(3)

# The execution of countdown begins with n=3, and since n is greater than 0, it outputs the value 3, and then calls itself...
# 	The execution of countdown begins with n=2, and since n is greater than 0, it outputs the value 2, and then calls itself...
# 		The execution of countdown begins with n=1, and since n is greater than 0, it outputs the value 1, and then calls itself...
# 			The execution of countdown begins with n=0, and since n is not greater than 0, it outputs the word, “Blastoff!” and then returns.
# 		The countdown that got n=1 returns.
# 	The countdown that got n=2 returns.
# The countdown that got n=3 returns.

# 3
# 2
# 1
# Balstoff!

# A function that calls itself is recursive. 

# The process of executing it is called recursion.

def print_n(s, n):
	if n <= 0:
		return
	else:
		print(s)
		print_n(s, n-1)

# If n <= 0 the return statement exits the function. The flow of execution immediately returns to the caller, and the remaining lines of the function don’t run.

# The bottom of the stack, where n=0, is called the base case. It does not make a recursive call, so there are no more frames.

print_n(s="Hello", n=2)

def do_n(f, n):
	if n <= 0:
		return
	else:
		f()
		do_n(f, n-1)


## 5.10  Infinite recursion

# If a recursion never reaches a base case, it goes on making recursive calls forever, and the program never terminates. This is known as infinite recursion.

def recurse():
	recurse()


# n most programming environments, a program with infinite recursion does not really run forever. Python reports an error message when the maximum recursion depth is reached.

# 	File "<stdin>", line 2, in recurse
#   File "<stdin>", line 2, in recurse
#   File "<stdin>", line 2, in recurse
#                   .   
#                   .
#                   .
#   File "<stdin>", line 2, in recurse
# RuntimeError: Maximum recursion depth exceeded

# If you encounter an infinite recursion by accident, review your function to confirm that there is a base case that does not make a recursive call. And if there is a base case, check whether you are guaranteed to reach it.


# 5.13  Glossary

# floor division:
# An operator, denoted //, that divides two numbers and rounds down (toward negative infinity) to an integer.

# modulus operator:
# An operator, denoted with a percent sign (%), that works on integers and returns the remainder when one number is divided by another.

# boolean expression:
# An expression whose value is either True or False.

# relational operator:
# One of the operators that compares its operands: ==, !=, >, <, >=, and <=.

# logical operator:
# One of the operators that combines boolean expressions: and, or, and not.

# conditional statement:
# A statement that controls the flow of execution depending on some condition.

# condition:
# The boolean expression in a conditional statement that determines which branch runs.

# compound statement:
# A statement that consists of a header and a body. The header ends with a colon (:). The body is indented relative to the header.

# branch:
# One of the alternative sequences of statements in a conditional statement.

# chained conditional:
# A conditional statement with a series of alternative branches.

# nested conditional:
# A conditional statement that appears in one of the branches of another conditional statement.

# return statement:
# A statement that causes a function to end immediately and return to the caller.
# The process of calling the function that is currently executing.

# base case:
# A conditional branch in a recursive function that does not make a recursive call.

# infinite recursion:
# A recursion that doesn’t have a base case, or never reaches it. Eventually, an infinite recursion causes a runtime error.
