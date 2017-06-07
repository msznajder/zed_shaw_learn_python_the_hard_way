"""
http://www.codewars.com/kata/soundex
"""


def soundex(name):
	processed_name_list = []

	for split_name in name.split(" "):
		processed_name_list.append(process_word(split_name))
	return " ".join(processed_name_list)


def process_word(word):
    ones 	= ["b", "f", "p", "v"]
    twos 	= ["c", "g", "j", "k", "q", "s", "x", "z"]
    threes 	= ["d", "t"]
    fours 	= ["l"]
    fives 	= ["m", "n"]
    sixes 	= ["r"]
    vovels  = ["a", "e", "i", "o", "u", "y"]

    res = []

    first_letter = word[0]
    word = word.lower()
   
    for idx, ch in enumerate(word):
    	if (ch == "h" or ch == "w") and idx != 0:
    		pass
    	elif ch in vovels and idx != 0:
    		pass
    	elif ch in ones:
    		res.append("1")
    	elif ch in twos:
    		res.append("2")
    	elif ch in threes:
    		res.append("3")
    	elif ch in fours:
    		res.append("4")
    	elif ch in fives:
    		res.append("5")
    	elif ch in sixes:
    		res.append("6")

    res = get_unique_list(res)
    if len(res) < 4:
    	res.extend(["0", "0", "0"])
    res[0] = first_letter

    return "".join(res[0:4])


def get_unique_list(l):
	last_element = None
	unique_list = []
	for element in l:
		if last_element != element:
			unique_list.append(element)
		last_element = element
	return unique_list


soundex("Sarah Connor")