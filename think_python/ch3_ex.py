"""
Exercise 1
"""

def right_justify(s):
	print((70 - len(s)) * " " + s)


right_justify("abba")


"""
Exercise 2
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
