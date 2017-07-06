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
# print(get_all_rotate_pairs())


"""
Exercise 6  
Here’s another Puzzler from Car Talk (http://www.cartalk.com/content/puzzlers):
This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable, five-letter word recently that has the following unique property. When you remove the first letter, the remaining letters form a homophone of the original word, that is a word that sounds exactly the same. Replace the first letter, that is, put it back and remove the second letter and the result is yet another homophone of the original word. And the question is, what’s the word?
Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is a real word, it’s just not a homophone of the other two words.
But there is, however, at least one word that Dan and we know of, which will yield two homophones if you remove either of the first two letters to make two, new four-letter words. The question is, what’s the word?

You can use the dictionary from Exercise 1 to check whether a string is in the word list.

To check whether two words are homophones, you can use the CMU Pronouncing Dictionary. You can download it from http://www.speech.cs.cmu.edu/cgi-bin/cmudict or from http://thinkpython2.com/code/c06d and you can also download http://thinkpython2.com/code/pronounce.py, which provides a function named read_dictionary that reads the pronouncing dictionary and returns a Python dictionary that maps from each word to a string that describes its primary pronunciation.

Write a program that lists all the words that solve the Puzzler. Solution: http://thinkpython2.com/code/homophone.py.
"""
def generate_pronounciation_dict():
	pronounciation_dict = dict()
	with open("c06d.txt") as fin:
		for line in fin:
			if not line.startswith("##"):
				split_line = line.strip().lower().split()
				word = split_line[0]
				pron = " ".join(split_line[1:])
				pronounciation_dict[word] = pron
	return pronounciation_dict


def look_for_word_homophones():
	words = ch10_ex.load_words()
	words_dict = dict_from_list(words)
	words_pronounciation_dict = generate_pronounciation_dict()
	for word in words:
		word_no_first_letter = word[1:]
		word_no_second_letter = word[0] + word[2:]
		if word_no_first_letter not in words_dict or word_no_second_letter not in words_dict:	
			continue
		if word not in words_pronounciation_dict or word_no_first_letter not in words_pronounciation_dict or word_no_second_letter not in words_pronounciation_dict:	
			continue
		if words_pronounciation_dict[word] == words_pronounciation_dict[word_no_first_letter] == words_pronounciation_dict[word_no_second_letter]:
			print(word, word_no_first_letter, word_no_second_letter)

# print(generate_pronounciation_dict())
# look_for_word_homophones()
