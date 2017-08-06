"""
Exercise 1  
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
Hint: The string module provides a string named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters. Let’s see if we can make Python swear:

>>> import string
>>> string.punctuation
'!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
Also, you might consider using the string methods strip, replace and translate.
"""
import string

def load_words(filepath):
	all_words = []
	translator = str.maketrans('', '', string.punctuation+'”'+'“'+'’')
	with open(filepath) as fin:
		for line in fin:
			line = line.translate(translator)
			# word = word.strip(string.punctuation + string.whitespace)
			words = line.split()
			for word in words:
				word = word.strip()
				all_words.append(word.lower())
				# all_words.append(word)
	return all_words


"""
Exercise 2  
Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times each word is used.

Print the number of different words used in the book. Compare different books by different authors, written in different eras. Which author uses the most extensive vocabulary?
"""
import time

JUNGLE_BOOK = "jungle_book.txt"
PRIDE_AND_PREJUDICE = "a_pride_and_prejudice.txt"
TALE_OF_TWO_CITIES = "a_tale_of_two_cities.txt"
ULYSSES = "ulysses.txt"


def histogram(words):
	hist = {}
	for word in words:
		hist[word] = hist.get(word, 0) + 1
	return hist


def get_book_stats(filepath):
	words = load_words(filepath)
	print("Book:", filepath)
	print("Total number words in the book: ", len(words))
	print("Number of unique words in the book: ", len(set(words)))
	print("Words histogram")
	words_hist = histogram(words)
	for word, count in words_hist.items():
		print(word, count)


# get_book_stats(JUNGLE_BOOK)
# get_book_stats(PRIDE_AND_PREJUDICE)
# get_book_stats(TALE_OF_TWO_CITIES)
# get_book_stats(ULYSSES)

"""
Exercise 3  
Modify the program from the previous exercise to print the 20 most frequently used words in the book.
"""

def get_top_n_from_hist(hist, n=10):
	return sorted(hist.items(), key=lambda x: x[1], reverse=True)[:n]


def get_book_stats(filepath):
	words = load_words(filepath)
	print("Book:", filepath)
	print("Total number words in the book: ", len(words))
	print("Number of unique words in the book: ", len(set(words)))
	print("Most common words")
	words_hist = histogram(words)
	top_words = get_top_n_from_hist(words_hist, 100)
	for word, count in top_words:
		print(word, count)


# h = histogram(["a", "a", "b", "c", "c", "d", "r", "f", "f", "w", "f"])
# print(get_top_n_from_hist(h, 3))

# get_book_stats(JUNGLE_BOOK)
# get_book_stats(PRIDE_AND_PREJUDICE)
# get_book_stats(TALE_OF_TWO_CITIES)
# get_book_stats(ULYSSES)


"""
Exercise 4  
Modify the previous program to read a word list (see Section 9.1) and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that should be in the word list, and how many of them are really obscure?
"""
import ch10_ex
import ch11_ex

def get_strange_words(filepath):
	words_list = ch10_ex.load_words()
	words_dict = ch11_ex.dict_from_list(words_list)
	book_words = load_words(filepath)
	strange_list = []
	for word in book_words:
		if word not in words_dict:
			strange_list.append(word)
	print(set(strange_list))


# get_strange_words(JUNGLE_BOOK)
# get_strange_words(PRIDE_AND_PREJUDICE)
# get_strange_words(TALE_OF_TWO_CITIES)
# get_strange_words(ULYSSES)


"""
Exercise 5  
Write a function named choose_from_hist that takes a histogram as defined in Section 11.2 and returns a random value from the histogram, chosen with probability in proportion to frequency. For example, for this histogram:
>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
"""
import random

t = ['a', 'a', 'b', 'b']
hist = histogram(t)

def get_list_from_hist(hist):
	res = []
	for val, count in hist.items():
		res.extend([val] * count)
	return(res)

def choose_from_hist(hist):
	list_from_hist = get_list_from_hist(hist)
	return random.choice(list_from_hist)

# print(choose_from_hist(hist))


"""
Exercise 6  
Python provides a data structure called set that provides many common set operations. You can read about them in Section 19.5, or read the documentation at http://docs.python.org/3/library/stdtypes.html#types-set.
Write a program that uses set subtraction to find words in the book that are not in the word list. Solution: http://thinkpython2.com/code/analyze_book2.py.
"""
def subtract(d1, d2):
	return set(d1) - set(d2)

def get_strange_words_set(filepath):
	words_list = ch10_ex.load_words()
	book_words = load_words(filepath)
	return subtract(book_words, words_list)

# print(get_strange_words_set(JUNGLE_BOOK))


"""
Exercise 8  
Markov analysis:
Write a program to read a text from a file and perform Markov analysis. The result should be a dictionary that maps from prefixes to a collection of possible suffixes. The collection might be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your program with prefix length two, but you should write the program in a way that makes it easy to try other lengths.
Add a function to the previous program to generate random text based on the Markov analysis. Here is an example from Emma with prefix length 2:
He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?" "I cannot make speeches, Emma:" he soon cut it all himself.
For this example, I left the punctuation attached to the words. The result is almost syntactically correct, but not quite. Semantically, it almost makes sense, but not quite.
What happens if you increase the prefix length? Does the random text make more sense?

Once your program is working, you might want to try a mash-up: if you combine text from two or more books, the random text you generate will blend the vocabulary and phrases from the sources in interesting ways.
Credit: This case study is based on an example from Kernighan and Pike, The Practice of Programming, Addison-Wesley, 1999.
"""
from collections import defaultdict
import random

EMMA = "emma.txt"


def perform_markov_analysis(filepath, prefix_length=2):
	words = load_words(filepath)
	markov_analysis = defaultdict(list)
	for idx, word in enumerate(words):
		if idx + prefix_length == len(words):
			break
		markov_analysis[" ".join(words[idx:idx+prefix_length])].append(words[idx+prefix_length])
	return markov_analysis


def generate_text_from_markov(markov, prefixes_num=10):
	prefixes = random.sample(markov.keys(), prefixes_num)
	text = ""
	for prefix in prefixes:
		text += prefix + " " + random.choice(markov[prefix]) + " "
	return text


# markov_analysis = perform_markov_analysis(EMMA, 3)
# generated_text = generate_text_from_markov(markov_analysis, 10)
# print(generated_text)


"""
Exercise 9  
The “rank” of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common has rank 2, etc.
"""

def generate_words_sorted_by_rank(filepath):
	words = load_words(filepath)
	words_hist = histogram(words)
	words_with_counts = list(words_hist.items())
	sorted_words_with_counts = sorted(words_with_counts, key=lambda x: x[1], reverse=True)
	words_with_ranks = []
	for idx, word_with_count in enumerate(sorted_words_with_counts):
		words_with_ranks.append((word_with_count[0], idx+1))
	return words_with_ranks


words_by_ranks = generate_words_sorted_by_rank(EMMA)
print(words_by_ranks)
