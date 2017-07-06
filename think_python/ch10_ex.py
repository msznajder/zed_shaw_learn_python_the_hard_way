"""
Exercise 1  
Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""
def flatten_list(l):
	return [x for sublist in l for x in sublist]


def nested_sum(l):
	return sum(flatten_list(l))


# t = [[1, 2], [3], [4, 5, 6]]
# print(flatten_list(t))
# print(nested_sum(t))


"""
Exercise 2  
Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""

def cumsum(t):
	return [sum(t[:idx+1]) for idx in range(len(t))]

# t = [1, 2, 3, 4, 5]
# print(cumsum(t))

"""
Exercise 3  
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
"""
def middle(t):
	return t[1:-1]

# t = [1, 2, 3, 4]
# print(middle(t))


"""
Exercise 4  
Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
"""
def chop(t):
	del t[0]
	del t[-1]


# t = [1, 2, 3, 4]
# chop(t)
# print(t)


"""
Exercise 5   Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""
def is_sorted(t):
	for idx in range(1, len((t))):
		if t[idx] < t[idx-1]:
			return False
	return True


# print(is_sorted([1, 2, 2]))
# print(is_sorted(['b', 'a']))


"""
Exercise 6  
Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""
def is_anagram(s1, s2):
	if len(s1) != len(s2):
		return False
	for ch in set(s1):
		if s1.count(ch) != s2.count(ch):
			return False
	return True

# print(is_anagram("abba", "abbb"))
# print(is_anagram("sarka", "raska"))

"""
Exercise 7  
Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
"""
def has_duplicates(t):
	return len(t) != len(set(t))


# print(has_duplicates("abc"))
# print(has_duplicates("abba"))


"""
Exercise 8  
This exercise pertains to the so-called Birthday Paradox, which you can read about at http://en.wikipedia.org/wiki/Birthday_paradox.
If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.

You can download my solution from http://thinkpython2.com/code/birthday.py.
"""
import random


def generate_birthday_paradox_simulations(simulations_number, population_size):
	population_samples = [generate_birthday_paradox_sample(population_size) for _ in range(simulations_number)]
	return sum(population_samples) / simulations_number


def generate_birthday_paradox_sample(population_size):
	birthdays = generate_n_random_ints_in_range(population_size, 1, 365)
	return len(birthdays) != len(set(birthdays))


def generate_n_random_ints_in_range(population_size, start, stop):
	return [random.randint(start, stop) for _ in range(population_size)]


# print(generate_birthday_paradox_simulations(1000, 23))


"""
Exercise 9  
Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?
Solution: http://thinkpython2.com/code/wordlist.py.
"""
import time
FILE_PATH = "words.txt"

def load_words():
	words = []
	with open(FILE_PATH) as fin:
		for line in fin:
			words.append(line.strip())
	return words


def load_words2():
	words = []
	with open(FILE_PATH) as fin:
		for line in fin:
			words = words + [line.strip()]
	return words

# start_time = time.time()
# load_words()
# print("load_words1 time: ", time.time() - start_time)

# start_time = time.time()
# load_words2()
# print("load_words2 time: ", time.time() - start_time)


"""
Exercise 10  
To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary. You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, you search the first half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there.

Write a function called in_bisect that takes a sorted list and a target value and returns the index of the value in the list if it’s there, or None if it’s not.

Or you could read the documentation of the bisect module and use that! Solution: http://thinkpython2.com/code/inlist.py.
"""
import time
import ch11_ex

def bisection_search(l, target):
	low = 0
	high = len(l) - 1
	while True:
		if low > high:
			return -1
		m = int((low + high) / 2)
		if target > l[m]:
			low = m + 1
		elif target < l[m]:
			high = m - 1
		if l[m] == target:
			return m


def in_bisect(l, value):
	return bisection_search(l, value) != -1


def time_checking_membership_methods():
	words = load_words()

	start_time = time.time()
	"bawdinesses" in words
	print("in_regular", time.time() - start_time)
	print("bawdinesses" in words)

	start_time = time.time()
	in_bisect(words, "bawdinesses")
	print("in_bisect", time.time() - start_time)
	print(in_bisect(words, "bawdinesses"))

	words_dict = ch11_ex.dict_from_list(words)
	start_time = time.time()
	"bawdinesses" in words_dict
	print("in_dict", time.time() - start_time)
	print("bawdinesses" in words_dict)
	

# time_checking_membership_methods()

"""
Exercise 11  
Two words are a “reverse pair” if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list. Solution: http://thinkpython2.com/code/reverse_pair.py.
"""
## enumerate all pairs
def find_all_reverse_pairs_enumerate_all_pairs():
	reverse_pairs = []
	words = load_words()
	for idx1, word1 in enumerate(words):
		for idx2, word2 in enumerate(words):
			if word1 == word2[::-1] and idx1 != idx2:
				reverse_pairs.append((word1, word2))
	return reverse_pairs

## check for list membership with in
def find_all_reverse_pairs_list_membership():
	reverse_pairs = []
	words = load_words()
	for word in words:
		if word[::-1] in words and word != word[::-1]:
			reverse_pairs.append((word, word[::-1]))
	return reverse_pairs


## check for list membership with bisect_in
def find_all_reverse_pairs_bisect_membership():
	reverse_pairs = []
	words = load_words()
	for word in words:
		if in_bisect(words, word[::-1]) and word != word[::-1]:
			reverse_pairs.append((word, word[::-1]))
	return reverse_pairs

## check for dict membership
def find_all_reverse_pairs_dict_membership():
	reverse_pairs = []
	words = load_words()
	words_dict = ch11_ex.dict_from_list(words)
	for word in words:
		if word[::-1] in words_dict and word != word[::-1]:
			reverse_pairs.append((word, word[::-1]))
	return reverse_pairs


# print(find_all_reverse_pairs_enumerate_all_pairs())

# start_time = time.time()
# print(find_all_reverse_pairs_list_membership())
# print("find_all_reverse_pairs_list_membership time", time.time() - start_time)

# start_time = time.time()
# print(find_all_reverse_pairs_bisect_membership())
# print("find_all_reverse_pairs_bisect_membership time", time.time() - start_time)

# start_time = time.time()
# print(find_all_reverse_pairs_dict_membership())
# print("find_all_reverse_pairs_dict_membership time", time.time() - start_time)


"""
Exercise 12  
Two words “interlock” if taking alternating letters from each forms a new word. For example, “shoe” and “cold” interlock to form “schooled”. Solution: http://thinkpython2.com/code/interlock.py. Credit: This exercise is inspired by an example at http://puzzlers.org.
Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?
"""
def un_interlock(s):
	return s[0::2], s[1::2]


## check for list membership with in
def find_interlock_words_list_membership():
	words = load_words()
	interlocking_pairs = []
	for word in words:
		un_interlocked_word1, un_interlocked_word2 = un_interlock(word)
		if un_interlocked_word1 in words and un_interlocked_word2 in words:
			interlocking_pairs.append((un_interlocked_word1, un_interlocked_word2, word))
	return interlocking_pairs


## check for list membership with bisect_in
def find_interlock_words_bisect_membership():
	words = load_words()
	interlocking_pairs = []
	for word in words:
		un_interlocked_word1, un_interlocked_word2 = un_interlock(word)
		if in_bisect(words, un_interlocked_word1) and in_bisect(words, un_interlocked_word2):
			interlocking_pairs.append((un_interlocked_word1, un_interlocked_word2, word))
	return interlocking_pairs

## check for dict membership
def find_interlock_words_dict_membership():
	words = load_words()
	words_dict = ch11_ex.dict_from_list(words)
	interlocking_pairs = []
	for word in words:
		un_interlocked_word1, un_interlocked_word2 = un_interlock(word)
		if un_interlocked_word1 in words_dict and un_interlocked_word2 in words_dict:
			interlocking_pairs.append((un_interlocked_word1, un_interlocked_word2, word))
	return interlocking_pairs


# start_time = time.time()
# print(find_interlock_words_list_membership())
# print("find_interlock_words_list_membership time", time.time() - start_time)

# start_time = time.time()
# print(find_interlock_words_bisect_membership())
# print("find_interlock_words_bisect_membership time", time.time() - start_time)

# start_time = time.time()
# print(find_interlock_words_dict_membership())
# print("find_interlock_words_dict_membership time", time.time() - start_time)
