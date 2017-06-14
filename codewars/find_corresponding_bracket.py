def find_corresponding_opening_bracket_idx(s):

	did_find_other_closing_counter = 0
	for idx, ch in enumerate(s[::-1]):
		if ch == ']':
			did_find_other_closing_counter += 1
		elif ch == '[' and did_find_other_closing_counter != 0:
			did_find_other_closing_counter -= 1
		elif ch == '[' and did_find_other_closing_counter == 0:
			return (len(s) - 1) - idx


print(find_corresponding_opening_bracket_idx(',[.[-],')) # 1
print(find_corresponding_opening_bracket_idx(',[.[-')) # 3
print(find_corresponding_opening_bracket_idx(',>,<[>[->+>+<<]>>[-<<+>>')) # 17
print(find_corresponding_opening_bracket_idx(',>,<[>[->+>+<<]>>[-<<+>>]')) # 4
print(find_corresponding_opening_bracket_idx('[,>,<[>[->+>+<<]>>[-<<+>>]]')) # 0


def find_corresponding_closing_bracket_idx(s):
	did_find_other_opening_counter = 0
	for idx, ch in enumerate(s):
		if ch == '[':
			did_find_other_opening_counter += 1 
		elif ch == ']' and did_find_other_opening_counter != 0:
			did_find_other_opening_counter -= 1
		elif ch == ']' and did_find_other_opening_counter == 0:
			return idx


print(find_corresponding_closing_bracket_idx('-.,+]')) # 4 
print(find_corresponding_closing_bracket_idx('.[-],]')) # 5
print(find_corresponding_closing_bracket_idx('>[->+>+<<]>>[-<<+>>]]')) # 20
print(find_corresponding_closing_bracket_idx('->+>+<<]>>[-<<+>>]')) # 7
print(find_corresponding_closing_bracket_idx(',>,<[>[->+>+<<]>>[-<<+>>]]]')) # 26
