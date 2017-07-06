"""
Exercise 1  
Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. Solution: http://thinkpython2.com/code/most_frequent.py.
"""
def most_frequent(s):
	hist = letters_hist(s)
	hist_list = [(key, val) for key, val in hist.items()]
	hist_list.sort(key=lambda x: x[1], reverse=True)
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
import ch11_ex
from collections import defaultdict

def find_anagram_lists():
	words = ch10_ex.load_words()
	anagrams_sets = defaultdict(list)
	for word in words:
		key = tuple(sorted(list(word)))
		anagrams_sets[key].append(word)
	return sorted([val for key, val in anagrams_sets.items() if len(val) > 1], key=lambda val: len(val), reverse=True)

for val in find_anagram_lists():
	print(val)







