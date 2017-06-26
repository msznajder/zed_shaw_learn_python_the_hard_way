"""
Exercise 1   
Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).
"""
WORDS_FILE_PATH = "words.txt"


def load_words():
	words = []
	with open(WORDS_FILE_PATH) as fin:
		for line in fin:
			word = line.strip()
			words.append(word)
	return words


def print_only_long_words():
	for word in load_words():
		if len(word) > 20:
			print(word)


# print_only_long_words()

"""
Exercise 2  
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.
In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.

All right, I’ll stop now.

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list that have no “e”.
"""
def has_no_e(s):
	if "e" in s:
		return False
	else:
		return True


def print_only_no_e_words():
	for word in load_words():
		if has_no_e(word):
			print(word)


def compute_e_no_e_words_percentage():
	no_e_words = []
	all_words = []
	for word in load_words():
		if has_no_e(word):
			no_e_words.append(word)
		all_words.append(word)
	return (len(no_e_words) / len(all_words)) * 100


# print(has_no_e("abeba"))

# print_only_no_e_words()

# print(compute_e_no_e_words_percentage())


"""
Exercise 3  
Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
"""
def avoid(word, forbidden):
	for letter in forbidden:
		if letter in word:
			return False
	return True


def print_user_avoid_letters_words():
	forbidden = input()
	for word in load_words():
		if avoid(word, forbidden):
			print(word)

# print(avoid("anagram", "bcd"))
# print_user_avoid_letters_words()


"""
Exercise 4  
Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
"""
def uses_only(word, used):
	for letter in word:
		if letter not in used:
			return False
	return True


def print_user_use_letters_words():
	used = input()
	for word in load_words():
		if uses_only(word, used):
			print(word)


# print(uses_only("abba", "b"))
# print_user_use_letters_words()


"""
Exercise 5  
Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeiouy?
"""

def uses_all(word, used):
	for letter in used:
		if letter not in word:
			return False
	return True


def print_user_use_all_letters_words():
	used = input()
	for word in load_words():
		if uses_all(word, used):
			print(word)


# print(uses_all("abba", "ab"))
# print_user_use_all_letters_words()


"""
Exercise 6  
Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?
"""
def is_abecedarian(word):
	for idx in range(1, len(word)):
		if word[idx] < word[idx-1]:
			return False
	return True


def print_abecedarian_words():
	for word in load_words():
		if is_abecedarian(word):
			print(word)


# print(is_abecedarian("deeeefa"))
print_abecedarian_words()
