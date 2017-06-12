from collections import defaultdict

"""
https://www.codewars.com/kata/526156943dfe7ce06200063e
https://fatiherikli.github.io/brainfuck-visualizer/#LD4sPFs+Wy0+Kz4rPDxdPj5bLTw8Kz4+XTw8PC1dPj4u
"""


def brain_luck(code, input):

	input_bytes_array = [ord(ch) for ch in input]
	
	inpt_pointer_idx = 0
	inst_pointer_idx = 0
	data_pointer_idx = 0
	data_pointer_val = defaultdict(int)
	res_array = [] 

	counter = 0

	while True:
		instruction = code[inst_pointer_idx]
		if instruction == '>':
			data_pointer_idx += 1
			inst_pointer_idx += 1
		elif instruction == '<':
			data_pointer_idx -= 1
			inst_pointer_idx += 1
		elif instruction == '+':
			data_pointer_val[data_pointer_idx] = (data_pointer_val[data_pointer_idx] + 1) % 256
			inst_pointer_idx += 1
		elif instruction == '-':
			data_pointer_val[data_pointer_idx] = (data_pointer_val[data_pointer_idx] - 1) % 256
			inst_pointer_idx += 1
		elif instruction == '.':
			res_array.append(chr(data_pointer_val[data_pointer_idx]))
			inst_pointer_idx += 1
		elif instruction == ',':
			data_pointer_val[data_pointer_idx] = input_bytes_array[inpt_pointer_idx]
			inst_pointer_idx += 1
			inpt_pointer_idx += 1
		elif  instruction == '[':
			if data_pointer_val[data_pointer_idx] == 0:
				inst_pointer_idx = inst_pointer_idx + find_corresponding_closing_bracket_idx(code[inst_pointer_idx+1:]) + 1
			else:
				inst_pointer_idx += 1
		elif instruction == ']':
			if data_pointer_val[data_pointer_idx] != 0:
				inst_pointer_idx = find_corresponding_opening_bracket_idx(code[:inst_pointer_idx]) + 1
			else:
				inst_pointer_idx += 1

		if inst_pointer_idx >= len(code):
			break

	return "".join(res_array)


def find_corresponding_closing_bracket_idx(s):
	did_find_other_opening_counter = 0
	for idx, ch in enumerate(s):
		if ch == '[':
			did_find_other_opening_counter += 1 
		elif ch == ']' and did_find_other_opening_counter != 0:
			did_find_other_opening_counter -= 1
		elif ch == ']' and did_find_other_opening_counter == 0:
			return idx


def find_corresponding_opening_bracket_idx(s):

	did_find_other_closing_counter = 0
	for idx, ch in enumerate(s[::-1]):
		if ch == ']':
			did_find_other_closing_counter += 1
		elif ch == '[' and did_find_other_closing_counter != 0:
			did_find_other_closing_counter -= 1
		elif ch == '[' and did_find_other_closing_counter == 0:
			return (len(s) - 1) - idx


print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))
print(brain_luck(',[.[-],]', 'Codewars' + chr(0)))
print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))
