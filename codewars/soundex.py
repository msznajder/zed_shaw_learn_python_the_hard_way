"""
http://www.codewars.com/kata/soundex
"""


def soundex(name):
    processed_name_list = []

    for split_name in name.split(" "):
        processed_name_list.append(process_word(split_name))
    return " ".join(processed_name_list)


def process_word(word):
    ones    = ["b", "f", "p", "v"]
    twos    = ["c", "g", "j", "k", "q", "s", "x", "z"]
    threes  = ["d", "t"]
    fours   = ["l"]
    fives   = ["m", "n"]
    sixes   = ["r"]
    vovels  = ["a", "e", "i", "o", "u", "y"]

    res = []

    first_letter = word[0]
    
    word = word.lower()
    
    for idx, ch in enumerate(word):
        if (ch == "h" or ch == "w") and idx != 0:
            pass
        elif (ch == "h" or ch == "w") and idx == 0:
            res.append(ch)
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
        else:
            res.append(ch)
    
    res = get_unique_list(res)

    res = "".join(res)
    for vovel in vovels:
        res = res[0] + res[1:].replace(vovel, "")

    if res[0].isdigit():
        res = first_letter + res[1:]
    
    if len(res) < 4:
        res = res + "000"

    return res[0:4].upper()


def get_unique_list(l):
    last_element = None
    unique_list = []
    for element in l:
        if last_element != element:
            unique_list.append(element)
        last_element = element
    return unique_list


print(soundex("Ashcraft"))

# Ashcraft
# A613
# 'A261'


