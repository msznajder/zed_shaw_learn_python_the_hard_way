"""
Exercise 1   
Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).
"""

def print_only_long_words():
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
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
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
			if has_no_e(word):
				print(word)


def compute_e_no_e_words_percentage():
	no_e_words = []
	all_words = []
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
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
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
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
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
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
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
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
	with open("words.txt") as fin:
		for line in fin:
			word = line.strip()
			if is_abecedarian(word):
				print(word)

print(is_abecedarian("deeeefa"))
print_abecedarian_words()


"""
Exercise 7  
This question is based on a Puzzler that was broadcast on the radio program Car Talk (http://www.cartalk.com/content/puzzlers):
Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it. Solution: http://thinkpython2.com/code/cartalk1.py.
"""



















