## Chapter 1  The way of the program

# The single most important skill for a computer scientist 
# is problem solving. Problem solving means the ability to formulate problems, 
# think creatively about solutions, and express a solution clearly and accurately.


## 1.1  What is a program?

# A program is a sequence of instructions that specifies how to perform 
# a computation.


## 1.3  The first program

print("Hello, World!")


## 1.4  Arithmetic operators

print(40 + 2)
print(40 - 1)
print(6 * 7)
print(84 / 2)
print(6**2 + 6)


## 1.5  Values and types

# A value is one of the basic things a program works with, like a letter or a number. 

# These values belong to different types.

print(type(2))
print(type(42.0))
print('Hello, World!')
print(type('2'))
print('42.0')


## 1.6  Formal and natural languages

# Natural languages are the languages people speak, such as English, Spanish, 
# and French. They were not designed by people (although people try to impose 
# some order on them); they evolved naturally.

# Formal languages are languages that are designed by people for specific applications. 
# For example, the notation that mathematicians use is a formal language that is particularly 
# good at denoting relationships among numbers and symbols. 

# Programming languages are formal languages that have been designed to express computations.

# Formal languages tend to have strict syntax rules that govern the structure of statements.

# Syntax rules come in two flavors, pertaining to tokens and structure. Tokens are the basic 
# elements of the language, such as words, numbers, and chemical elements. 
# One of the problems with 3 += 3 $ 6 is that $ is not a legal token in mathematics (at least as 
# 	far as I know). Similarly, 2Zz is not legal because there is no element with the abbreviation Zz.

# The second type of syntax rule pertains to the way tokens are combined. The equation 3 += 3 is illegal 
# because even though + and = are legal tokens, you can’t have one right after the other. Similarly, 
# in a chemical formula the subscript comes after the element name, not before.

# When you read a sentence in English or a statement in a formal language, you have to figure 
# out the structure (although in a natural language you do this subconsciously). 
# This process is called parsing.

# Although formal and natural languages have many features in common—tokens, structure, 
# and syntax—there are some differences.
# ambiguity: Natural languages are full of ambiguity, which people deal with by using 
# contextual clues and other information. Formal languages are designed to be nearly 
# or completely unambiguous, which means that any statement has exactly one meaning, regardless of context.
# redundancy: In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots 
# of redundancy. As a result, they are often verbose. Formal languages are less redundant and more concise.
# literalness: Natural languages are full of idiom and metaphor. If I say, “The penny dropped”, there is 
# probably no penny and nothing dropping (this idiom means that someone understood something after a period 
# of confusion). Formal languages mean exactly what they say.


## 1.8  Glossary

# problem solving:
# The process of formulating a problem, finding a solution, and expressing it.

# high-level language:
# A programming language like Python that is designed to be easy for humans to read and write.

# low-level language:
# A programming language that is designed to be easy for a computer to run; also called “machine language” or “assembly language”.

# portability:
# A property of a program that can run on more than one kind of computer.

# interpreter:
# A program that reads another program and executes it

# prompt:
# Characters displayed by the interpreter to indicate that it is ready to take input from the user.

# program:
# A set of instructions that specifies a computation.

# print statement:
# An instruction that causes the Python interpreter to display a value on the screen.

# operator:
# A special symbol that represents a simple computation like addition, multiplication, or string concatenation.

# value:
# One of the basic units of data, like a number or string, that a program manipulates.

# type:
# A category of values. The types we have seen so far are integers (type int), floating-point numbers (type float), and strings (type str).

# integer:
# A type that represents whole numbers.

# floating-point:
# A type that represents numbers with fractional parts.

# string:
# A type that represents sequences of characters.

# natural language:
# Any one of the languages that people speak that evolved naturally.

# formal language:
# Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs; all programming languages are formal languages.

# token:
# One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.

# syntax:
# The rules that govern the structure of a program.

# parse:
# To examine a program and analyze the syntactic structure.

# bug:
# An error in a program.

# debugging:
# The process of finding and correcting bugs.
