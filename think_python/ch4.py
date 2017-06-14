## Chapter 4  Case study: interface design


import turtle
import math


def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)


def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360 / n)


def circle(t, r):
	circumference = 2 * math.pi * r
	n = 1000
	length = circumference / n 
	polygon(t, length, n)


def arc(t, r, angle):
	angle_proportion = angle / 360
	circumference = 2 * math.pi * r * angle_proportion
	n = int(1000 * angle_proportion)
	print(n)
	length = circumference / n
	for i in range(n):
		t.fd(length)
		t.lt(angle / n)


bob = turtle.Turtle()
arc(bob, 100, 360)
turtle.mainloop()


# A development plan:

# Start by writing a small program with no function definitions.

# Once you get the program working, identify a coherent piece of it, encapsulate the piece in a function and give it a name.

# Generalize the function by adding appropriate parameters.

# Repeat steps 1–3 until you have a set of working functions. Copy and paste working code to avoid retyping (and re-debugging).

# Look for opportunities to improve the program by refactoring. For example, if you have similar code in several places, consider factoring it into an appropriately general function.


# This process has some drawbacks—we will see alternatives later—but it can be useful if you don’t know ahead of time how to divide the program into functions. This approach lets you design as you go along.


def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# A docstring is a string at the beginning of a function that explains the interface (“doc” is short for “documentation”)

# It is terse, but it contains the essential information someone would need to use this function. It explains concisely what the function does (without getting into the details of how it does it). It explains what effect each parameter has on the behavior of the function and what type each parameter should be (if it is not obvious).

# Writing this kind of documentation is an important part of interface design. A well-designed interface should be simple to explain.

# An interface is like a contract between a function and a caller. The caller agrees to provide certain parameters and the function agrees to do certain work.

# These requirements are called preconditions because they are supposed to be true before the function starts executing. Conversely, conditions at the end of the function are postconditions. Postconditions include the intended effect of the function (like drawing line segments) and any side effects (like moving the Turtle or making other changes).

# Preconditions are the responsibility of the caller. If the caller violates a (properly documented!) precondition and the function doesn’t work correctly, the bug is in the caller, not the function.

# If the preconditions are satisfied and the postconditions are not, the bug is in the function. If your pre- and postconditions are clear, they can help with debugging.


## Glosary

# method:
# A function that is associated with an object and called using dot notation.

# loop:
# A part of a program that can run repeatedly.

# encapsulation:
# The process of transforming a sequence of statements into a function definition.

# generalization:
# The process of replacing something unnecessarily specific (like a number) with something appropriately general (like a variable or parameter).

# keyword argument:
# An argument that includes the name of the parameter as a “keyword”.

# interface:
# A description of how to use a function, including the name and descriptions of the arguments and return value.

# refactoring:
# The process of modifying a working program to improve function interfaces and other qualities of the code.

# development plan:
# A process for writing programs.

# docstring:
# A string that appears at the top of a function definition to document the function’s interface.

# precondition:
# A requirement that should be satisfied by the caller before a function starts.

# postcondition:
# A requirement that should be satisfied by the function before it ends.
