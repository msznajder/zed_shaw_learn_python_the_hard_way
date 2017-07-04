"""
Exercise 0
Create hist function generating sequence values histogram.
"""
def hist(seq):
	h = {}
	for val in seq:
		h[val] = h.get(val, 0) + 1
	return h


# print(hist("abbba"))

"""
Exercise 0
Create reverse_lookup function loking dictionary key for given value.
"""
def reverse_lookup(d, target):
	res = []
	for key, val in d.items():
		if val == target:
			res.append(key)
	return res


# print(reverse_lookup({"a": 1, "b": 2, "c": 2, "d": 3}, 2))

"""
Exercise 0
Write invert_dict function.
Values as key and list of keys that occured in dict with given value.
"""
def invert_dict(d):
	inv = dict()
	for key, val in d.items():
		inv[val] = inv.get(val, []) + [key]
	return inv


# print(invert_dict({"a": 1, "b": 2, "c": 2, "d": 3}))

"""
Exercise 1
Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
If you did Exercise 10, you can compare the speed of this implementation with the list in operator and the bisection search.
"""
def dict_from_list(l):
	return {val : 0 for val in l}


# print(4 in dict_from_list([1, 2, 3]))


"""
Exercise 2  
Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict. Solution: http://thinkpython2.com/code/invert_dict.py.
"""
def invert_dict(d):
	inv = dict()
	for key, val in d.items():
		inv.setdefault(val, []).append(key)
	return inv


# print(invert_dict({"a": 1, "b": 2, "c": 2, "d": 3}))

"""
Exercise 4  
If you did Exercise 7, you already have a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.
Use a dictionary to write a faster, simpler version of has_duplicates. Solution: http://thinkpython2.com/code/has_duplicates.py.
"""
def has_duplicates(l):
	return len(l) != len(set(l))


# print(has_duplicates([1, 2, 2, 3]))


"""
Exercise 5  
Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 5).
Write a program that reads a wordlist and finds all the rotate pairs. Solution: http://thinkpython2.com/code/rotate_pairs.py.
"""
import ch8_ex
import ch10_ex

def generate_all_rotations(word):
	return [ch8_ex.rotate_word(word, i) for i in range(1, 26)]


def get_all_rotate_pairs():
	rotate_pairs = []
	words = ch10_ex.load_words()
	words_dict = dict_from_list(words)
	for word in words_dict:
		word_rotations = generate_all_rotations(word)
		for word_rotation in word_rotations:
			if word_rotation in words_dict:
				rotate_pairs.append((word, word_rotation))
	return rotate_pairs



# print(ch8_ex.rotate_word("abcd", 26))
# print(generate_all_rotations("abcd"))
print(get_all_rotate_pairs())



















