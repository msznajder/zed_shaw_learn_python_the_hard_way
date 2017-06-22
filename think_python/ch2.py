## Chapter 2  Variables, expressions and statements

# A variable is a name that refers to a value.


## 2.1  Assignment statements

# An assignment statement creates a new variable and gives it a value

n = 17


## 2.2  Variable names

# 76trombones is illegal because it begins with a number. more@ is illegal because it contains an illegal character, @.

# Python 3 keywords:
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise


## 2.3  Expressions and statements

# An expression is a combination of values, variables, and operators. 
# A value all by itself is considered an expression, and so is a variable
# so the following are all legal expressions:
42
n
n + 25

# When you type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression.


# A statement is a unit of code that has an effect, like creating a variable or displaying a value.

n = 17
print(n)

# The first line is an assignment statement that gives a value to n. The second line is a print statement that displays the value of n.

# When you type a statement, the interpreter executes it, which means that it does whatever the statement says. In general, statements don’t have values.


## 2.4  Script mode

# Interactive mode, which means that you interact directly with the interpreter. 

# The alternative is to save code in a file called a script and then run the interpreter in script mode to execute the script. By convention, Python scripts have names that end with .py.

miles = 26.2
print(miles * 1.61)

# A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

print(1)
x = 2
print(x)

# The assignment statement produces no output.


## 2.8  Debugging

# Three kinds of errors can occur in a program: syntax errors, runtime errors, and semantic errors.

# Syntax error:
# “Syntax” refers to the structure of a program and the rules about that structure. For example, parentheses have to come in matching pairs, so (1 + 2) is legal, but 8) is a syntax error.
# If there is a syntax error anywhere in your program, Python displays an error message and quits, and you will not be able to run the program. During the first few weeks of your programming career, you might spend a lot of time tracking down syntax errors. As you gain experience, you will make fewer errors and find them faster.

# Runtime error:
# The second type of error is a runtime error, so called because the error does not appear until after the program has started running. These errors are also called exceptions because they usually indicate that something exceptional (and bad) has happened.
# Runtime errors are rare in the simple programs you will see in the first few chapters, so it might be a while before you encounter one.

# Semantic error:
# The third type of error is “semantic”, which means related to meaning. If there is a semantic error in your program, it will run without generating error messages, but it will not do the right thing. It will do something else. Specifically, it will do what you told it to do.
# Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.


## 2.9  Glossary

# variable:
# A name that refers to a value.

# assignment:
# A statement that assigns a value to a variable.

# state diagram:
# A graphical representation of a set of variables and the values they refer to.

# keyword:
# A reserved word that is used to parse a program; you cannot use keywords like if, def, and while as variable names.

# operand:
# One of the values on which an operator operates.

# expression:
# A combination of variables, operators, and values that represents a single result.

# evaluate:
# To simplify an expression by performing the operations in order to yield a single value.

# statement:
# A section of code that represents a command or action. So far, the statements we have seen are assignments and print statements.

# execute:
# To run a statement and do what it says.

# interactive mode:
# A way of using the Python interpreter by typing code at the prompt.

# script mode:
# A way of using the Python interpreter to read code from a script and run it.

# script:
# A program stored in a file.

# order of operations:
# Rules governing the order in which expressions involving multiple operators and operands are evaluated.

# concatenate:
# To join two operands end-to-end.

# comment:
# Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.

# syntax error:
# An error in a program that makes it impossible to parse (and therefore impossible to interpret).

# exception:
# An error that is detected while the program is running.

# semantics:
# The meaning of a program.

# semantic error:
# An error in a program that makes it do something other than what the programmer intended.
