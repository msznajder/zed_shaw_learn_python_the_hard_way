2e2

# Can also do roots this way
4**0.5

# Can use parenthesis to specify orders
(2+10) * (10+3)

# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 3. It's considered best practice (PEP8) that the names are lowercase.

# Grab everything but the last letter
s[:-1]

# We can use this to print a string backwards
s[::-1]

# Let's try to change the first letter to 'x' - STRINGS ARE IMMUTABLE
s[0] = 'x'

# Concatenate strings!
s + ' concatenate me!'

# Print Formatting
'Insert another string with curly brackets: {}'.format('The inserted string')
'Insert another string with curly brackets: The inserted string'

# We can also use + to concatenate lists, just like we did for strings.
my_list + ['new item']
['one', 'two', 'three', 4, 5, 'new item']
# Note: This doesn't actually change the original list!

# Make the list double
my_list * 2
['one',
 'two',
 'three',
 4,
 5,
 'add new item permanently',
 'one',
 'two',
 'three',
 4,
 5,
 'add new item permanently']
 # not permanent

 # Assign the popped element, remember default popped index is -1
popped_item = l.pop()

# Matrix.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# So what are mappings? 
# Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

# Its important to note that dictionaries are very flexible in the data types they can hold.
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
# Keep calling the keys
d['key1']['nestkey']['subnestkey']
'value'

# iPython Writing a File - make a new text file with some iPython Magic.
%%writefile test.txt
Hello, this is a quick test file
# Overwriting test.txt

# Create set.
x = set()

# We add to sets with the add() method
x.add(1)



Introduction to Python Statements

# Semicolons are used to denote statement endings in many other languages, but in Python, the end of a line is the same as the end of a statement.

# Note how Python is so heavily driven by code indentation and whitespace. This means that code readability is a core part of the design of the Python language.

# Python 3 range generators
# This means a generator would not create a list to generate like range() does, but instead provide a one time generation of the numbers in that range. Python 2 has a built-in range generator called xrange(). It is recommended to use xrange() for for loops in Python 2.

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in Celsius ]

# We can also perform nested list comprehensions
[ x**2 for x in [x**2 for x in range(11)]]
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

# You can always use Shift+Tab in the Jupyter Notebook to get more help about the method. In general Python you can use the help() function:
help(l.count)
