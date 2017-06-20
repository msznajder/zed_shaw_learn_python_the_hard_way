## Chapter 14  Files


## 14.1  Persistence

# The idea of “persistent” programs that keep data in permanent storage, and shows how to use different kinds of permanent storage, like files and databases.

# Most of the programs we have seen so far are transient in the sense that they run for a short time and produce some output, but when they end, their data disappears.

# ther programs are persistent: they run for a long time (or all the time); they keep at least some of their data in permanent storage (a hard drive, for example); and if they shut down and restart, they pick up where they left off.

# Examples of persistent programs are operating systems, which run pretty much whenever a computer is on, and web servers, which run all the time, waiting for requests to come in on the network.

# One of the simplest ways for programs to maintain their data is by reading and writing text files. We have already seen programs that read text files; in this chapter we will see programs that write them.

# n alternative is to store the state of the program in a database.


## 14.4  Filenames and paths

# Files are organized into directories (also called “folders”). 

# Every running program has a “current directory”, which is the default directory for most operations. 

# The os module provides functions for working with files and directories (“os” stands for “operating system”).

# os.getcwd returns the name of the current directory.

import os
cwd = os.getcwd()
cwd

# cwd stands for “current working directory”.

# A string like '/home/dinsdale' that identifies a file or directory is called a path.

# A simple filename, like memo.txt is also considered a path, but it is a relative path because it relates to the current directory. 

# If the current directory is /home/dinsdale, the filename memo.txt would refer to /home/dinsdale/memo.txt.

# A path that begins with / does not depend on the current directory; it is called an absolute path. 

# To find the absolute path to a file, you can use os.path.abspath.

os.path.abspath("memo.txt")


# os.path provides other functions for working with filenames and paths.

# os.path.exists checks whether a file or directory exists

os.path.exists("memo.txt")


# os.path.isdir checks whether it’s a directory.
os.path.isdir("memo.txt") # False
os.path.isdir("/home/dinsdale") # True


# os.path.isfile checks whether it’s a file.

os.path.isfile("memo.txt") # True


# os.listdir returns a list of the files (and other directories) in the given directory.
print(os.listdir(cwd))


# To demonstrate these functions, the following example “walks” through a directory, prints the names of all the files, and calls itself recursively on all the directories.
def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)

		if os.path.isfile(path):
			print(path)
		else:
			walk(path)

# os.path.join takes a directory and a file name and joins them into a complete path.


## 14.5  Catching exceptions

try:
	fin = open("bad_file")
except:
	print("Error")

# Handling an exception with a try statement is called catching an exception. 


## 14.6  Databases

# A database is a file that is organized for storing data. 

# Many databases are organized like a dictionary in the sense that they map from keys to values. 

# The biggest difference between a database and a dictionary is that the database is on disk (or other permanent storage), so it persists after the program ends.


# The module dbm provides an interface for creating and updating database files. 

# Opening a database is similar to opening other files.

import dbm
db = dbm.open("captions", "c")

# The mode 'c' means that the database should be created if it doesn’t already exist. 

# The result is a database object that can be used (for most operations) like a dictionary.

# When you create a new item, dbm updates the database file.

db['cleese.png'] = "Photo of John Cleese."

# When you access one of the items, dbm reads the file.

db['cleese.png']

# If you make another assignment to an existing key, dbm replaces the old value.

db['cleese.png'] = "Photo 2"

# As with other files, you should close the database when you are done.

db.close()


## 14.7  Pickling

# A limitation of dbm is that the keys and values have to be strings or bytes.

# The pickle module translates almost any type of object into a string suitable for storage in a database, and then translates strings back into objects.

# ickle.dumps takes an object as a parameter and returns a string representation (dumps is short for “dump string”).

import pickle
 
t1 = [1, 2, 3]
s = pickle.dumps(t1)
print(s)

# The format isn’t obvious to human readers; it is meant to be easy for pickle to interpret. pickle.loads (“load string”) reconstitutes the object.

t2 = pickle.loads(s)
print(t1 == t2)
print(t1 is t2)

# In other words, pickling and then unpickling has the same effect as copying the object.

# You can use pickle to store non-strings in a database. In fact, this combination is so common that it has been encapsulated in a module called shelve.


## 14.9  Writing modules

# Any file that contains Python code can be imported as a module.

# The only problem with this example is that when you import the module it runs the test code at the bottom. 

# Normally when you import a module, it defines new functions but it doesn’t run them.

# Programs that will be imported as modules often use the following idiom.

if __name__ == "__main__":
	print("something")

# __name__ is a built-in variable that is set when the program starts. 

# If the program is running as a script, __name__ has the value '__main__'; in that case, the test code runs. Otherwise, if the module is being imported, the test code is skipped.


## 14.11  Glossary

# persistent:
# Pertaining to a program that runs indefinitely and keeps at least some of its data in permanent storage.

# format operator:
# An operator, %, that takes a format string and a tuple and generates a string that includes the elements of the tuple formatted as specified by the format string.

# format string:
# A string, used with the format operator, that contains format sequences.

# format sequence:
# A sequence of characters in a format string, like %d, that specifies how a value should be formatted.

# text file:
# A sequence of characters stored in permanent storage like a hard drive.

# directory:
# A named collection of files, also called a folder.

# path:
# A string that identifies a file.

# relative path:
# A path that starts from the current directory.

# absolute path:
# A path that starts from the topmost directory in the file system.

# catch:
# To prevent an exception from terminating a program using the try and except statements.

# database:
# A file whose contents are organized like a dictionary with keys that correspond to values.

# bytes object:
# An object similar to a string.

# shell:
# A program that allows users to type commands and then executes them by starting other programs.

# pipe object:
# An object that represents a running program, allowing a Python program to run commands and read the results.
