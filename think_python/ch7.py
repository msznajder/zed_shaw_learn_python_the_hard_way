## Chapter 7  Iteration


## 7.1  Reassignment

a = 5
b = a # a and b are now equal
a = 3 # a and b are no longer equal
a     # 3
b 	  # 5

# The third line changes the value of a but does not change the value of b, so they are no longer equal.

# Reassigning variables is often useful, but you should use it with caution. If the values of variables change frequently, it can make the code difficult to read and debug. 


## 7.3  The while statement

# Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly. 

# In a computer program, repetition is also called iteration.

def countdown(n):
	while n > 0:
		print(n)
		n -= 1
	print("Blastoff!")

# More formally, here is the flow of execution for a while statement:
# - Determine whether the condition is true or false.
# - If false, exit the while statement and continue execution at the next statement.
# - If the condition is true, run the body and then go back to step 1.

# The body of the loop should change the value of one or more variables so that the condition becomes false eventually and the loop terminates. 

# Otherwise the loop will repeat forever, which is called an infinite loop. 

# An endless source of amusement for computer scientists is the observation that the directions on shampoo, “Lather, rinse, repeat”, are an infinite loop.

def print_n(s, n):
	while n > 0:
		print(s)
		n -= 1

print_n("!", 5)

n = 4
while True:
	print(n)
	n -= 1
	if n == 1:
		break


## 7.5  Square roots

# One way of computing square roots is Newton’s method. 

# Suppose that you want to know the square root of a. If you start with almost any estimate, x, you can compute a better estimate with the following formula.

# y = (x + a / x) / 2

# For example, if a is 4 and x is 3:

a = 4
x = 3 # this is our first guess - rather random
y = (x + a/x) / 2
y # 2.16666666667

# The result is closer to the correct answer (√4 = 2). If we repeat the process with the new estimate, it gets even closer.

x = y
y = (x + a/x) / 2
y # 2.00641025641

# After a few more updates, the estimate is almost exact.

x = y
y = (x + a/x) / 2
y # 2.00001024003

x = y
y = (x + a/x) / 2
y # 2.00000000003

# In general we don’t know ahead of time how many steps it takes to get to the right answer, but we know when we get there because the estimate stops changing.

x = y
y = (x + a/x) / 2
y # 2.0

x = y
y = (x + a/x) / 2
y # 2.0

# When y == x, we can stop. Here is a loop that starts with an initial estimate, x, and improves it until it stops changing.

while True:
	print(x)
	y = (x + a/x) / 2
	if y == x:
		break
	x = y
print(y)

# For most values of a this works fine, but in general it is dangerous to test float equality. Floating-point values are only approximately right: most rational numbers, like 1/3, and irrational numbers, like √2, can’t be represented exactly with a float.


# Rather than checking whether x and y are exactly equal, it is safer to use the built-in function abs to compute the absolute value, or magnitude, of the difference between them.

epsilon = 0.0000001
while True:
	print(x)
	y = (x + a/x) / 2
	if abs(x-y) < epsilon:
		break
	x = y
print(y)


## 7.8  Glossary

# reassignment:
# Assigning a new value to a variable that already exists.

# update:
# An assignment where the new value of the variable depends on the old.

# initialization:
# An assignment that gives an initial value to a variable that will be updated.

# increment:
# An update that increases the value of a variable (often by one).

# decrement:
# An update that decreases the value of a variable.

# iteration:
# Repeated execution of a set of statements using either a recursive function call or a loop.

# infinite loop:
# A loop in which the terminating condition is never satisfied.

# algorithm:
# A general process for solving a category of problems.
