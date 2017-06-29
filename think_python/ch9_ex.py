"""
Exercise 1   
Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).
"""
WORDS_FILE_PATH = "words.txt"


def load_words():
	words = []
	with open(WORDS_FILE_PATH) as fin:
		for line in fin:
			words.append(line.strip())
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
# print_abecedarian_words()


"""
Exercise 7  
This question is based on a Puzzler that was broadcast on the radio program Car Talk (http://www.cartalk.com/content/puzzlers):
Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it. Solution: http://thinkpython2.com/code/cartalk1.py.
"""
def find_doubles_indexes(word):
	indexes = []
	for idx in range(1, len(word)):
		if word[idx] == word[idx-1]:
			indexes.append(idx)
	return indexes


def check_for_tripple_double_letters(word):
	doubles_indexes = find_doubles_indexes(word)
	if len(doubles_indexes) < 3:
		return False
	counter = 0
	for idx in range(1, len(doubles_indexes)):
		if counter == 2:
			return True
		if doubles_indexes[idx] - doubles_indexes[idx-1] == 2:
			counter += 1
		else:
			counter = 0
	return counter == 2


def print_tripple_double_words():
	words = load_words()
	for word in words:
		if check_for_tripple_double_letters(word):
			print(word)


# print(check_for_tripple_double_letters("peppa"))
# print_tripple_double_words()


"""
Exercise 8   Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
“I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic!

“The question is, what was on the odometer when I first looked?”

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements. Solution: http://thinkpython2.com/code/cartalk2.py.
"""
def generate_all_six_digit_numbers():
	return range(100000, 999996)


def is_palindrome(s):
	return s == s[::-1]


def print_all_palindromic_numbers():
	for number in generate_all_six_digit_numbers():
		if is_palindrome(str(number)[-4:]) and is_palindrome(str(number+1)[-5:]) and is_palindrome(str(number+2)[1:-1]) and is_palindrome(str(number+3)):
			print(number)


# print_all_palindromic_numbers()


"""
Exercise 9   Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):
“Recently I had a visit with my mom and we realized that the two digits that make up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often this has happened over the years but we got sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times so far. I also figured out that if we’re lucky it would happen again in a few years, and if we’re really lucky it would happen one more time after that. In other words, it would have happened 8 times over all. So the question is, how old am I now?”
Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string method zfill useful.
Solution: http://thinkpython2.com/code/cartalk3.py.
"""
def generate_reverse_ages_pairs(difference):
	ages = range(18, 100)
	reverse_ages_pairs = [(x, int(str(x)[::-1])) for x in ages if x > int(str(x)[::-1]) and x - int(str(x)[::-1]) == difference]
	return reverse_ages_pairs


print(generate_reverse_ages_pairs(18))
