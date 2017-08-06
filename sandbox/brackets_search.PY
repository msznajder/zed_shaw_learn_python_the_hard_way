o1 = ">[*>*>*>]>]"
o2 = "*>[>[*]>]>]"
o3 = "[]*>*>*>]"


def find_closing_bracket_idx(s):
	counter = 0
	for idx, ch in enumerate(s):
		if ch == "[":
			counter += 1
		elif ch == "]" and counter > 0:
			counter -= 1
		elif ch == "]" and counter <= 0:
			return idx
	
# print(find_closing_bracket_idx(o1))




def find_opening_bracket_idx(s):
	counter = 0
	for idx, ch in enumerate(s[::-1]):
		print(idx, ch)
		if ch == "]":
			counter += 1
		elif ch == "[" and counter > 0:
			counter -= 1
		elif ch == "[" and counter <= 0:
			return len(s) - idx - 1


c1 = "[>[*>*>*>]>"
c2 = "[*>[>[*]>>"
c3 = "[[]*>*>*>"

print(find_opening_bracket_idx(c3))
# index od przodu nie od tylu