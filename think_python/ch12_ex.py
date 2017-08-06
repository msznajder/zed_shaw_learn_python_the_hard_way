"""
Exercise 1  
Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. Solution: http://thinkpython2.com/code/most_frequent.py.
"""
def most_frequent(s):
	hist = letters_hist(s)
	hist_list = [(key, val) for key, val in hist.items()]
	hist_list.sort(key=lambda x: x[1], reverse=True) # !!
	print(list(zip(*hist_list))[0])


def letters_hist(s):
	hist = {}
	for ch in s:
		hist[ch] = hist.get(ch, 0) + 1
	return hist


# most_frequent("abcdee")


"""
Exercise 2  
More anagrams!
Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters. The question is, how can you represent the collection of letters in a way that can be used as a key?
Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest, and so on.
In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What collection of 8 letters forms the most possible bingos? Hint: there are seven.
Solution: http://thinkpython2.com/code/anagram_sets.py.
"""
import ch10_ex
from collections import defaultdict

def find_anagram_lists():
	words = ch10_ex.load_words()
	anagrams_sets = defaultdict(list)
	for word in words:
		key = tuple(sorted(list(word)))
		anagrams_sets[key].append(word)
	return sorted([val for key, val in anagrams_sets.items() if len(val) > 1], key=lambda val: len(val), reverse=True) # !!

for val in find_anagram_lists():
	print(val)

"""
Exercise 3  
Two words form a “metathesis pair” if you can transform one into the other by swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible swaps. Solution: http://thinkpython2.com/code/metathesis.py. Credit: This exercise is inspired by an example at http://puzzlers.org.
"""
import ch11_ex

def find_metathesis_pairs():
	words = ch10_ex.load_words()
	words_dict = ch11_ex.dict_from_list(words)
	metathesis_pairs = []
	for word in words:
		swaps = generate_all_characters_swaps(word)
		for swap in swaps:
			if swap in words_dict:
				metathesis_pairs.append((word, swap))
	return metathesis_pairs


def generate_all_characters_swaps(s):
	swaps = []
	for i in range(len(s)):
		for j in range(len(s)):
			if i != j:
				s_list = list(s)
				s_list[i], s_list[j] = s_list[j], s_list[i] # !!
				swap = "".join(s_list)
				if s != swap:
					swaps.append(swap)
	return list(set(swaps))


# print(generate_all_characters_swaps("0123"))
# print(find_metathesis_pairs())


"""
Exercise 4  
Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
What is the longest English word, that remains a valid English word, as you remove its letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t rearrange any of the letters. Every time you drop a letter, you wind up with another English word. If you do that, you’re eventually going to wind up with one letter and that too is going to be an English word—one that’s found in the dictionary. I want to know what’s the longest word and how many letters does it have?
I’m going to give you a little modest example: Sprite. Ok? You start off with sprite, you take a letter off, one from the interior of the word, take the r away, and we’re left with the word spite, then we take the e off the end, we’re left with spit, we take the s off, we’re left with pit, it, and I.

Write a program to find all words that can be reduced in this way, and then find the longest one.
"""

## Version 1.0

import itertools

def get_removed_letters_words2():
	words = ch10_ex.load_words()
	words_dict = ch11_ex.dict_from_list(words)
	removed_letters_words = []
	# words = ["abcd", "sprite"]
	for word in words:
		# print(word)
		for n in range(1, len(word)):
			# print(n)
			removal_idices_combinations = get_n_chars_removal_combinations_idices(word, n)
			any_combination_is_word = False
			for removal_idices_combination in removal_idices_combinations:
				# print(removal_idices_combination)
				removed_letters_word = get_word_after_index_char_removal(word, removal_idices_combination)
				# print(removed_letters_word)
				if removed_letters_word in words_dict:
					# print("in!!!")
					any_combination_is_word = True
			# print("!!!", any_combination_is_word)
			if not any_combination_is_word:
				break
		# print("end", any_combination_is_word)
		if any_combination_is_word:
			removed_letters_words.append(word)
	return sorted(removed_letters_words, key=lambda val: len(val), reverse=True)


def get_n_chars_removal_combinations_idices(s, n):
	indices = range(0, len(s))
	indices_removal_combinations = itertools.combinations(indices, n)
	return indices_removal_combinations


def get_word_after_index_char_removal(s, removal_idices):
	return "".join([ch for idx, ch in enumerate(s) if idx not in removal_idices])

# print(get_removed_letters_words2())



## Version 2.0

import itertools

def get_word_stripping_patterns_tree(word):
	val_ranges = []
	for n in range(len(word) - 1):
		val_ranges.append(list(range(0, len(word) - n)))	
	return list(itertools.product(*val_ranges))

def get_word_for_stripping_pattern(word, stripping_pattern):
	word_list = list(word)
	for idx in stripping_pattern:
		del word_list[idx]
	return "".join(word_list)

def check_words_for_stripping_sequence(word, stripping_sequence, words_dict):
	stripped_words = []
	all_stripped_are_words = True
	for idx in range(len(stripping_sequence)):
		stripped_word = get_word_for_stripping_pattern(word, stripping_sequence[:idx+1])
		if stripped_word not in words_dict:
			all_stripped_are_words = False
		stripped_words.append(stripped_word)
	return all_stripped_are_words, stripped_words

def get_all_correct_word_strippings(word, words_dict):
	correct_word_strippings = []
	stripping_patterns = get_word_stripping_patterns_tree(word)
	for stripping_pattern in stripping_patterns:
		correct, sequence = check_words_for_stripping_sequence(word, stripping_pattern, words_dict)
		if correct:
			correct_word_strippings.append([word] + sequence)
	return correct_word_strippings

def get_all_words_correct_word_strippings():
	words = ch10_ex.load_words()
	words_dict = ch11_ex.dict_from_list(words)
	all_words_stripping_patterns = []
	for word in words:
		print(word)
		all_correct_word_strippings = get_all_correct_word_strippings(word, words_dict)
		if len(all_correct_word_strippings) > 0:
			all_words_stripping_patterns.extend(all_correct_word_strippings)
	return all_words_stripping_patterns


print(get_all_words_correct_word_strippings())

# w = "word"
# [w] 
# ['word']

# list(w)
# ['w', 'o', 'r', 'd']
	