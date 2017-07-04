"""
Exercise 1  
Read the documentation of the string methods at http://docs.python.org/3/library/stdtypes.html#string-methods. You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
"""

s = "Abc\n"

# Return a copy of the string with its first character capitalized and the rest lowercased.
# print(s.capitalize())

# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# print(s.casefold())

# Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). 
# print(s.center(100))

# Return an encoded version of the string as a bytes object.
# print(s.encode(encoding="utf-8", errors="strict"))

# Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. 
# print("\tabc".expandtabs(tabsize=8))

# Perform a string formatting operation.
# print("{} and {}".format(1, 2))

# Return true if all characters in the string are decimal characters and there is at least one character, false otherwise. 
# print("0001".isdecimal())

# Return true if all characters in the string are digits and there is at least one character, false otherwise. 
# print(s.isdigit())

# Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise.
# print(s.isnumeric())

# Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones.
# print(s.istitle())

# Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
# print("203.022".partition("."))

# Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. 
# print("203.022.000".rpartition("."))

# Whole list:
# https://docs.python.org/3/library/stdtypes.html#string-methods


"""
Exercise 2  
There is a string method called count that is similar to the function in Section 8.7. Read the documentation of this method and write an invocation that counts the number of a’s in 'banana'.
"""
# print("banana".count("a"))


"""
Exercise 3  
A string slice can take a third index that specifies the “step size”; that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 3.
"""
def is_palindrome(s):
	return s == s[::-1]

# print(is_palindrome("abba"))

"""
Exercise 4  
The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
"""

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase3(s):
    flag = False
    for c in s:
    	if c.islower():
        	flag = True
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if c.islower():
            return True
    return False


# print(any_lowercase5("tesT"))
# print(any_lowercase5("TEST"))


"""
Exercise 5  
A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer is called HAL, which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer as parameters, and returns a new string that contains the letters from the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a character to a numeric code, and chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical order, so for example:

>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar cypher with rotation 13. If you are not easily offended, find and decode some of them. Solution: http://thinkpython2.com/code/rotate.py.
"""
import string


def rotate_word(s, shift):
	alphabet = string.ascii_lowercase
	res = ""
	for letter in s:
		letter_idx = alphabet.find(letter)
		shifted_ch_idx = (letter_idx + shift) % len(alphabet)
		shifted_ch = alphabet[shifted_ch_idx]
		res += shifted_ch
	return res


# print(rotate_word("hal", 1))
